"""Independent verifier: checks every certificate from scratch (stdlib only).

Inputs: certs.json (per graph: n, edges, c1, dual p per pair-orbit with orbit def via
  generators? INDEPENDENT: verifier recomputes Aut itself? That duplicates code. Compromise:
  certs.json contains: edges, pair-orbit adjacency-independent description? Pair orbits
  must be trusted... To be safe, verifier recomputes: APSP, pair orbits from EXPLICIT
  generator list stored in certs (verifier checks each generator is an automorphism by
  edge-image check — O(|gens|*m)), then orbit BFS, then:
  DUAL check: for EVERY cut S (2^(n-1)): sum_o sep_o(S) p_o <= cutsize(S)/m. Exact.
  PRIMAL check: expand orbit family (reps + full group generated from gens? expansion
  needs full Aut: BFS closure from gens — verifier does it) with weights lam_O/|O| per
    cut... store per-cut weights directly? Store orbit reps + lambda; verifier expands
    via group closure, builds z on all pairs, checks d <= z <= C*d (+ edge check).
  Checks group order too (closure size == claimed |Aut|).
"""
import sys, json
sys.path.insert(0, '.')
from fractions import Fraction
from collections import deque


def load():
    with open('output/artifacts/certs.json') as f:
        return json.load(f)


def check_graph(g):
    name = g['name']
    n = g['n']
    E = [tuple(e) for e in g['edges']]
    m = len(E)
    eset = set((min(a, b), max(a, b)) for a, b in E)
    # 1. generators are automorphisms
    gens = [tuple(x) for x in g['gens']]
    for h in gens:
        assert sorted(h) == list(range(n)), f'{name}: gen not a permutation'
        im = set()
        for (a, b) in E:
            im.add((min(h[a], h[b]), max(h[a], h[b])))
        assert im == eset, f'{name}: gen not automorphism'
    # 2. group closure + order
    G = {tuple(range(n))}
    stack = list(G)
    inv = lambda p: tuple(sorted(range(n), key=lambda i: p[i]))
    def comp(p, q):
        return tuple(p[q[i]] for i in range(n))
    allg = [tuple(range(n))] + list(gens)
    invs = [inv(h) for h in allg]
    while stack:
        a = stack.pop()
        for h in allg + invs:
            c = comp(a, h)
            if c not in G:
                G.add(c)
                stack.append(c)
    assert len(G) == g['aut_order'], f"{name}: |Aut| {len(G)} != {g['aut_order']}"
    G = sorted(G)
    # 3. APSP
    A = [[] for _ in range(n)]
    for (a, b) in E:
        A[a].append(b)
        A[b].append(a)
    D = [[0]*n for _ in range(n)]
    for s in range(n):
        d = [-1]*n
        d[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for w in A[u]:
                if d[w] < 0:
                    d[w] = d[u] + 1
                    q.append(w)
        D[s] = d
    # 4. pair orbits from G
    po = {}
    for u in range(n):
        for v in range(u+1, n):
            po[(u, v)] = None
    norb = 0
    for s in list(po):
        if po[s] is not None:
            continue
        mem = set()
        st = [s]
        mem.add(s)
        while st:
            (a, b) = st.pop()
            for h in gens + invs[1:]:
                c = (min(h[a], h[b]), max(h[a], h[b]))
                if c not in mem:
                    mem.add(c)
                    st.append(c)
        for t in mem:
            po[t] = norb
        norb += 1
    assert norb == g['norb'], f"{name}: norb {norb} != {g['norb']}"
    assert sorted(po) == sorted((u, v) for u in range(n) for v in range(u+1, n))
    # 5. DUAL check over all cuts
    p = [Fraction(x) for x in g['dual_p']]
    D_orb = [0]*norb
    for (u, v), o in po.items():
        D_orb[o] += D[u][v]
    LB = sum(D_orb[o] * p[o] for o in range(norb))
    assert LB == Fraction(g['c1']), f"{name}: dual obj {LB} != c1 {g['c1']}"
    for mask in range(1, 1 << (n - 1)):
        S = {b + 1 for b in range(n - 1) if (mask >> b) & 1}
        lhs = Fraction(0)
        for u in range(n):
            for v in range(u+1, n):
                if (u in S) != (v in S):
                    lhs += p[po[(u, v)]]
        cs = sum(1 for (a, b) in E if (a in S) != (b in S))
        assert lhs <= Fraction(cs, m), f'{name}: dual violated at {sorted(S)}: {lhs} > {cs}/{m}'
    # 6. PRIMAL check: expand orbit family
    fams = g['primal_fam']  # [{rep:[...], lambda:'a/b'}]
    z = {}
    for u in range(n):
        for v in range(u+1, n):
            z[(u, v)] = Fraction(0)
    for fam in fams:
        rep = frozenset(fam['rep'])
        lam = Fraction(fam['lambda'])
        O = set()
        for h in G:
            O.add(frozenset(h[v] for v in rep))
        w = lam / len(O)
        for T in O:
            for u in range(n):
                for v in range(u+1, n):
                    if (u in T) != (v in T):
                        z[(u, v)] += w
    C = Fraction(g['c1'])
    for u in range(n):
        for v in range(u+1, n):
            assert z[(u, v)] >= D[u][v], f"{name}: domination fails {(u,v)}: {z[(u,v)]} < {D[u][v]}"
            assert z[(u, v)] <= C * D[u][v], f"{name}: Lipschitz fails {(u,v)}: {z[(u,v)]} > {C}*{D[u][v]}"
    print(f'{name}: VERIFY_OK  c1={C}  (|Aut|={len(G)}, norb={norb}, cuts-checked={2**(n-1)-1})')
    return True


if __name__ == '__main__':
    allc = load()
    ok = True
    for g in allc['graphs']:
        try:
            check_graph(g)
        except AssertionError as e:
            print('FAIL:', e)
            ok = False
    print('ALL VERIFY_OK' if ok else 'FAILURES')
    sys.exit(0 if ok else 1)
