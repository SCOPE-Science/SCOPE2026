"""Independent homology-engine cross-check (target stress-test, stdlib only).

A second, separately written simplicial-homology routine builds face sets
DOWNWARD from explicit facet lists (vs verify_target_obstruction.py, which
builds them UPWARD from the minimal-nonface rule), then compares:
 (1) synthetic unit cases with known answers (filled/hollow triangle,
     2 points, square boundary, tetrahedron boundary, point, void);
 (2) K0 full complex and selected induced subcomplexes vs the primary engine.
Repro: python3 verify_homology_engine.py. Stdlib only.
"""
from fractions import Fraction
from itertools import combinations

def rank_frac(rows):
    M = [[Fraction(x) for x in r] for r in rows]
    m = len(M)
    n = len(M[0]) if m else 0
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = 1 / M[r][c]
        M[r] = [x * inv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r

def faces_from_facets(facets):
    F = set()
    for f in facets:
        fs = sorted(f)
        for r in range(len(fs) + 1):
            for c in combinations(fs, r):
                F.add(tuple(c))
    return F

def betti_from_faces(F):
    """Reduced Betti over Q. F: set of sorted tuples; () present iff the
    complex is nonempty-as-complex (has the empty simplex)."""
    if () not in F:
        return {} if F == set() else (_ for _ in ()).throw(ValueError("bad face set"))
    bydim = {}
    for f in F:
        bydim.setdefault(len(f) - 1, []).append(f)
    maxd = max(bydim)
    idx = {d: {s: j for j, s in enumerate(bydim[d])} for d in bydim}
    drank = {0: 1}  # augmentation rank (vertex present since () in F and F has vertices... careful)
    # drank[0]=1 iff C_0 nonempty; if complex is just {()} then C_0 empty -> rank 0
    if -1 in bydim and 0 not in bydim:
        drank[0] = 0
    for n in range(1, maxd + 1):
        dom, cod = bydim.get(n, []), bydim.get(n - 1, [])
        if not dom or not cod:
            drank[n] = 0
            continue
        mat = [[Fraction(0)] * len(dom) for _ in range(len(cod))]
        for j, s in enumerate(dom):
            for t in range(n + 1):
                f = tuple(v for u, v in enumerate(s) if u != t)
                mat[idx[n - 1][f]][j] += Fraction((-1) ** t)
        drank[n] = rank_frac(mat)
    out = {}
    if -1 in bydim and (1 - drank[0]):
        out[-1] = 1 - drank[0]
    for n in range(0, maxd + 1):
        if n not in bydim:
            continue
        b = len(bydim[n]) - drank.get(n, 0) - drank.get(n + 1, 0)
        if b:
            out[n] = b
    return out

def check(name, facets, want):
    got = betti_from_faces(faces_from_facets(facets))
    assert got == want, f"{name}: got {got}, want {want}"
    print(f"UNIT {name}: {got} OK")

check("filled-triangle", [(0, 1, 2)], {})
check("hollow-triangle", [(0, 1), (1, 2), (0, 2)], {1: 1})
check("two-points", [(0,), (1,)], {0: 1})
check("square-boundary", [(0, 1), (1, 2), (2, 3), (0, 3)], {1: 1})
check("tetrahedron-boundary", [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)], {2: 1})
check("point", [(0,)], {})
check("three-edges-path", [(0, 1), (1, 2)], {})

import verify_target_obstruction as V

# K0 facets: maximal faces under the non-face rule
allfaces = [c for r in range(10) for c in combinations(range(9), r) if V.is_face(c)]
facet = [set(f) for f in allfaces]
facets = []
for f in facet:
    if not any(f < g for g in facet):
        facets.append(tuple(sorted(f)))
print(f"K0 facets: {len(facets)} (sizes {sorted(len(f) for f in facets)})")
F0 = faces_from_facets(facets)
indep_full = betti_from_faces(F0)
primary_full = V.reduced_betti(tuple(range(9)))
print("independent full:", indep_full, " primary full:", primary_full)
assert indep_full == primary_full == {4: 8}
print("FULL_COMPLEX_CROSSCHECK_OK")

for S in [(0, 1, 2), (0, 3, 6), (0, 1, 2, 3, 4, 5), (1, 2, 4, 5, 7, 8)]:
    sub = [tuple(sorted(set(f) & set(S))) for f in facets]
    sub = [f for f in sub if f]
    got = betti_from_faces(faces_from_facets(sub))
    want = V.reduced_betti(tuple(sorted(S)))
    assert got == want, (S, got, want)
    print(f"SUBCOMPLEX {[x+1 for x in S]}: {got} OK")
print("ENGINE_CROSSCHECK_PASS")
