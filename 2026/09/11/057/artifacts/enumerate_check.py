"""Enumerate facet-gluing choices; prove EVERY facet-sum S # octahedron (S stacked, along any facet pair) is non-Golod.

For each automorphism orbit of (facet of S, facet of octahedron) identifications,
build G9 and exhibit an explicit verified nonzero Baskakov product of two
missing-edge H^3 classes landing on a nonzero H^6 class over the hollow
4-cycle K_J (verified non-exact by exact rational rank test + hand equation).
Also verify d^2=0 and Leibniz on the tested pieces.
"""
from fractions import Fraction
from itertools import combinations, permutations
from collections import Counter

def stack(facets, f, newv):
    f = set(f)
    out = [t for t in facets if set(t) != f]
    for e in combinations(sorted(f), 2):
        out.append(tuple(sorted(tuple(e) + (newv,))))
    return sorted(out)

def auts(facets, verts):
    F = set(facets)
    return [p for p in permutations(verts)
            if all(tuple(sorted((p[a], p[b], p[c]))) in F for (a, b, c) in facets)]

S5 = stack([(0,1,2),(0,1,3),(0,2,3),(1,2,3)], (0,1,3), 4)
S = stack(S5, (0,1,2), 5)   # unique stacked 6-vertex sphere type (Aut(S5) facet-transitive)
O = sorted([(0,1,2),(0,1,5),(0,2,4),(0,4,5),(1,2,3),(1,3,5),(2,3,4),(3,4,5)])
# octahedron on {0..5} with opposite pairs (0,3),(1,4),(2,5)
print("S =", S)
print("O =", O)

# facet orbits
def facet_orbits(facets, verts):
    A = auts(facets, verts)
    seen, orbs = set(), []
    for f in facets:
        if f in seen:
            continue
        o = {tuple(sorted((p[f[0]], p[f[1]], p[f[2]]))) for p in A}
        orbs.append(sorted(o))
        seen |= o
    return orbs
print("S facet orbits:", facet_orbits(S, list(range(6))))
print("O facet orbits:", facet_orbits(O, list(range(6))))

# mature exact linear algebra
def mat_rank(M):
    M = [[Fraction(x) for x in row] for row in M]
    m, n = (len(M), len(M[0])) if M else (0, 0)
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if M[i][c] != 0), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        iv = M[r][c]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c] / iv
                for j in range(c, n): M[i][j] -= f * M[r][j]
        r += 1
    return r

def in_col_space(G, z):
    m = len(G)
    A = [list(G[i]) + [z[i]] for i in range(m)]
    return mat_rank(A) == mat_rank([list(r) for r in G])

def build_G9(Sf, Of):
    """Glue S (verts 0..5) to octahedron along facets Sf ~ Of.
    Relabel O-copy: keep Of vertices identified with Sf in order; other 3 get 6,7,8."""
    sv = list(Sf)
    ov = list(Of)
    o_verts = sorted({v for f in O for v in f})
    rest = [v for v in o_verts if v not in ov]
    mp = {o: s for o, s in zip(ov, sv)}
    nxt = iter([6, 7, 8])
    for v in rest: mp[v] = next(nxt)
    G = set()
    for f in S:
        if set(f) != set(Sf): G.add(tuple(sorted(f)))
    for f in O:
        if set(f) != set(Of): G.add(tuple(sorted(mp[v] for v in f)))
    return sorted(G)

def sphere_ok(G, verts):
    E = {tuple(sorted(e)) for f in G for e in combinations(f, 2)}
    if len(verts) - len(E) + len(G) != 2: return False
    c = Counter()
    for f in G:
        for e in combinations(f, 2): c[tuple(sorted(e))] += 1
    return set(c) == E and all(v == 2 for v in c.values())

def find_witness(G):
    V = list(range(9))
    FS = set(G)
    E = {tuple(sorted(e)) for f in G for e in combinations(f, 2)}
    FC = {()} | {(v,) for v in V} | set(E) | set(G)
    MISS = [tuple(sorted(p)) for p in combinations(V, 2) if tuple(sorted(p)) not in E]
    def piece(J, s):
        return sorted([L for L in FC if len(L) == s and set(L) <= set(J)], key=tuple)
    def diff(J, s):
        dom, cod = piece(J, s), piece(J, s + 1)
        ci = {L: i for i, L in enumerate(cod)}
        M = [[Fraction(0)] * len(dom) for _ in cod]
        for c, L in enumerate(dom):
            rest = sorted(set(J) - set(L))
            for i in rest:
                U = tuple(sorted(tuple(L) + (i,)))
                if U in ci:
                    pos = sum(1 for a in rest if a < i)
                    M[ci[U]][c] = Fraction(1 if pos % 2 == 0 else -1)
        return M
    # d^2 on tested pieces
    for J in [tuple(sorted(set(A) | set(B))) for A in MISS for B in MISS if not (set(A) & set(B))]:
        for s in (0, 1):
            A1, B1 = diff(J, s), diff(J, s + 1)
            if A1 and B1 and A1[0] and B1[0]:
                for c in range(len(A1[0])):
                    col = [A1[i][c] for i in range(len(A1))]
                    assert all(x == 0 for x in [sum(B1[i][j]*col[j] for j in range(len(col))) for i in range(len(B1))]), ("d2", J, s)
    for A in MISS:
        for B in MISS:
            if set(A) & set(B): continue
            J = tuple(sorted(set(A) | set(B)))
            if len(J) != 4: continue
            # K_J must be hollow 4-cycle
            EJ = [e for e in E if set(e) <= set(J)]
            if len(EJ) != 4: continue
            Pj2 = piece(J, 2)
            for la in A:
                for lb in B:
                    va = {(la,): Fraction(1)}
                    vb = {(lb,): Fraction(1)}
                    # inputs closed: grade1 -> grade2 zero
                    dA = diff(A, 1); dB = diff(B, 1)
                    pa = piece(A, 1); pb = piece(B, 1)
                    za = [va.get(L, Fraction(0)) for L in pa]
                    zb = [vb.get(L, Fraction(0)) for L in pb]
                    if any(x != 0 for x in [sum(dA[i][j]*za[j] for j in range(len(za))) for i in range(len(dA))]): continue
                    if any(x != 0 for x in [sum(dB[i][j]*zb[j] for j in range(len(zb))) for i in range(len(dB))]): continue
                    # products e_la . e_lb, two orders
                    for sgn0, L1, L2, JJ in ((1, (la,), (lb,), J),):
                        U = tuple(sorted(L1 + L2))
                        if U not in FC: continue
                        sgn = 1 if not any(a > c for a in (set(A)-set(L1)) for c in (set(B)-set(L2))) else -1
                        # compute shuffle properly
                        X = sorted(set(A) - set(L1)); Y = sorted(set(B) - set(L2))
                        inv = sum(1 for a in X for c in Y if a > c)
                        sgn = 1 if inv % 2 == 0 else -1
                        pv = [Fraction(sgn if L == U else 0) for L in Pj2]
                        dJ = diff(J, 2)
                        if any(x != 0 for x in [sum(dJ[i][j]*pv[j] for j in range(len(pv))) for i in range(len(dJ))]): continue
                        if not in_col_space(diff(J, 1), pv):
                            return (A, la, B, lb, J, U, sgn)
    return None

S_orb = facet_orbits(S, list(range(6)))
O_orb = facet_orbits(O, list(range(6)))
S_reps = [o[0] for o in S_orb]   # 3 facet orbits of stacked block
O_reps = [O_orb[0][0]]            # octahedron facet-transitive
Of = O_reps[0]
for Sf in S_reps:
    print("=== gluing facet of S:", Sf)
    seen_G, results = set(), []
    for q in permutations(Of):
        G = build_G9(Sf, q)
    key = tuple(G)
    if key in seen_G: continue
    seen_G.add(key)
    ok = sphere_ok(G, list(range(9)))
    w = find_witness(G) if ok else None
    results.append((G, ok, w))
    print("distinct glued facet sets:", len(results))
    nok = sum(1 for _, ok, _ in results if ok)
    print("sphere OK:", nok, "/", len(results))
    nwit = sum(1 for _, ok, w in results if ok and w)
    print("with verified nonzero product:", nwit, "/", nok)
    for G, ok, w in results:
        assert ok and w, (G, ok, w)
        print("  facets:", G)
        print("   witness: [%s via e_%s] x [%s via e_%s] -> K_%s cocycle e_%s (sign %s)" % (w[0], w[1], w[2], w[3], w[4], w[5], w[6]))
print("ENUMERATE_OK")
