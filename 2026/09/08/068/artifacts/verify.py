"""Independent verifier: different code path from compute.py."""
import json, itertools, random

def agree(p, q):
    return any(p[i] == q[i] for i in range(8))

def compose(p, q):
    return tuple(p[q[i]] for i in range(8))

def load():
    with open('output/artifacts/groups.json') as f:
        G = {m: [tuple(g) for g in v] for m, v in json.load(f).items()}
    return G

def stars_of(G):
    idx = {g: i for i, g in enumerate(G)}
    idt = tuple(range(8))
    S = set()
    per_point = {}
    for x in range(8):
        st = [g for g in G if g[x] == x]
        cos = set()
        for a in G:
            cos.add(frozenset(idx[compose(a, s)] for s in st))
        per_point[x] = (len(st), len(cos))
        S |= cos
    return S, per_point

def is_clique(G, C):
    for a in range(len(C)):
        for b in range(a + 1, len(C)):
            if not agree(G[C[a]], G[C[b]]):
                return False
    return True

def brute_omega_and_count(G, k):
    """Brute force: count k-cliques and certify no (k+1)-clique via bounded search."""
    n = len(G)
    cnt = 0
    for C in itertools.combinations(range(n), k):
        if is_clique(G, C):
            cnt += 1
    # upper bound: greedy coloring of agreement graph gives omega <= num colors
    order = sorted(range(n), key=lambda v: -sum(1 for u in range(n) if u != v and agree(G[v], G[u])))
    colors = {}
    for v in order:
        used = set()
        for u in range(n):
            if u != v and agree(G[v], G[u]) and u in colors:
                used.add(colors[u])
        c = 0
        while c in used:
            c += 1
        colors[v] = c
    return cnt, max(colors.values()) + 1

def simple_bb_omega(G):
    """Independent max-clique via degeneracy-order branch and bound."""
    n = len(G)
    N = [{u for u in range(n) if u != v and agree(G[v], G[u])} for v in range(n)]
    best = [0]
    # degeneracy order
    deg = sorted(range(n), key=lambda v: len(N[v]))
    def bound(C):
        # greedy coloring bound on set C
        cols = 0
        rem = set(C)
        while rem:
            cols += 1
            ind = set()
            for v in list(rem):
                if not (N[v] & ind):
                    ind.add(v)
                    rem.discard(v)
        return cols
    def expand(R, P):
        if not P:
            if len(R) > best[0]:
                best[0] = len(R)
            return
        while P:
            if len(R) + bound(P) <= best[0]:
                return
            v = P.pop()
            expand(R + [v], [u for u in P if u in N[v]])
            if len(R) + (1 if not P else bound(P)) <= best[0]:
                return
        if len(R) > best[0]:
            best[0] = len(R)
    expand([], deg)
    return best[0]

if __name__ == '__main__':
    G = load()
    with open('output/artifacts/results.json') as f:
        R = json.load(f)
    print("== G24 brute force ==")
    g = G['G24']
    S, pp = stars_of(g)
    print("per-point (stabsize, numcosets):", pp)
    print("total distinct stars:", len(S))
    cnt, ub = brute_omega_and_count(g, 3)
    print(f"brute #3-cliques={cnt} greedy-color-UB={ub} enum-said={R['G24']['num_max_cliques']}")
    assert cnt == R['G24']['num_max_cliques'], "enum mismatch!"
    bb = simple_bb_omega(g)
    print("independent BB omega:", bb)
    assert bb == 3
    non = [c for c in R['G24']['noncanonical'][:1]]
    print("witness idx:", non[0], "is_clique:", is_clique(g, non[0]),
          "in_stars:", frozenset(non[0]) in S)
    assert is_clique(g, non[0]) and frozenset(non[0]) not in S

    print("== G32 ==")
    g = G['G32']
    S, pp = stars_of(g)
    print("per-point:", pp, "distinct stars:", len(S))
    bb = simple_bb_omega(g)
    print("independent BB omega:", bb, " k=4 enum-said:", R['G32']['num_max_cliques'])
    assert bb == 4

    print("== G48 ==")
    g = G['G48']
    S, pp = stars_of(g)
    print("per-point:", pp, "distinct stars:", len(S))
    bb = simple_bb_omega(g)
    print("independent BB omega:", bb, " k=6 enum-said:", R['G48']['num_max_cliques'])
    assert bb == 6

    print("== GW64 ==")
    g = G['GW64']
    S, pp = stars_of(g)
    print("per-point:", pp, "distinct stars:", len(S))
    bb = simple_bb_omega(g)
    print("independent BB omega:", bb, " k=8 enum-said:", R['GW64']['num_max_cliques'])
    assert bb == 8
    w = R['GW64']['noncanonical'][0]
    print("witness idx:", w, "is_clique:", is_clique(g, w), "in_stars:", frozenset(w) in S)
    assert is_clique(g, w) and frozenset(w) not in S

    print("== AGL18 ==")
    g = G['AGL18']
    S, pp = stars_of(g)
    print("per-point:", pp, "distinct stars:", len(S))
    bb = simple_bb_omega(g)
    print("independent BB omega:", bb, " k=7")
    assert bb == 7
    w = R['AGL18']['noncanonical'][0]
    print("witness idx:", w, "is_clique:", is_clique(g, w), "in_stars:", frozenset(w) in S)
    assert is_clique(g, w) and frozenset(w) not in S
    print("ALL VERIFY CHECKS PASSED")
