"""Reproduce minimum-support mod-3 H2 carriers of a Paley neighborhood complex.

Python 3.9+; standard library only. All ranks use exact finite-field arithmetic.
"""
from itertools import combinations
from collections import Counter

P = 17
SQUARES = {x*x % P for x in range(1, P)}
FACETS = [frozenset((a+d) % P for d in SQUARES) for a in range(P)]
faces = {k: sorted({f for facet in FACETS
                    for f in combinations(sorted(facet), k)})
         for k in range(1, 9)}
ids = {k: {f: i for i, f in enumerate(faces[k])} for k in faces}
assert [len(faces[k]) for k in range(1, 9)] == [17,136,612,1122,952,476,136,17]

def boundary_columns(k):
    return [{ids[k-1][f[:j]+f[j+1:]]: (-1)**j
             for j in range(k)} for f in faces[k]]

B2 = boundary_columns(3)
B3 = boundary_columns(4)

def reduce_vec(v, pivots, p):
    v = {r: a % p for r, a in v.items() if a % p}
    while v:
        lead = min(v)
        if lead not in pivots:
            return v
        coef = v[lead]
        for r, a in pivots[lead].items():
            new = (v.get(r, 0) - coef*a) % p
            if new: v[r] = new
            else: v.pop(r, None)
    return {}

def add_vec(v, pivots, p):
    rem = reduce_vec(v, pivots, p)
    if not rem:
        return False
    lead = min(rem)
    inv = pow(rem[lead], -1, p)
    pivots[lead] = {r: (a*inv) % p for r, a in rem.items()}
    return True

def basis(cols, p):
    pivots = {}
    for c in cols: add_vec(c, pivots, p)
    return pivots

for col in B3:
    # The simplicial boundary really composes to zero, over the integers.
    residue = {}
    for t, coeff in col.items():
        for e, val in B2[t].items():
            residue[e] = residue.get(e, 0) + coeff*val
    assert all(x == 0 for x in residue.values())

ranks = {}
for p in (3, 101):
    ranks[p] = (len(basis(B2,p)), len(basis(B3,p)))
assert ranks == {3:(120,491), 101:(120,492)}, ranks
# All 136 edges appear, so the complete 1-skeleton has boundary-one rank 16.
# Consequently H1(F3)=0, H2(F3)=1, H2(Q)=0.

G = [tuple((a*x+b) % P for x in range(P))
     for a in sorted(SQUARES) for b in range(P)]
assert len(G) == 136 and len(set(G)) == 136
assert all({perm[x] for x in FACETS[0]} in FACETS
           for perm in G)

def orbit(W):
    return {tuple(sorted(perm[x] for x in W)) for perm in G}

piv3 = basis(B3, 3)
assert len(piv3) == 491

def sphere(W):
    return all(t in ids[3] for t in combinations(W,3)) and W not in ids[4]

def sphere_chain(W):
    return {ids[3][W[:i]+W[i+1:]]: (-1)**i for i in range(4)}

classified = []
seen = set()
for W in combinations(range(P),4):
    if W in seen: continue
    orb = orbit(W)
    seen.update(orb)
    if not sphere(W): continue
    c = sphere_chain(W)
    assert all(sum(c.get(t, 0)*B2[t].get(e,0) for t in c) == 0
               for e in range(len(faces[2])))
    survives = bool(reduce_vec(c, piv3, 3))
    assert all(sphere(w) and bool(reduce_vec(sphere_chain(w), piv3, 3)) == survives
               for w in orb)
    classified.append((W,len(orb),survives))

assert len(seen) == 2380
expected = [
 ((0,1,3,13),136,True),
 ((0,1,4,7),136,True),
 ((0,1,4,14),68,True),
 ((0,1,6,7),68,True),
 ((0,1,6,12),68,True),
 ((0,1,4,5),34,False),
]
assert set(classified) == set(expected), classified
assert sum(n for _,n,_ in classified) == 510
assert sum(n for _,n,v in classified if v) == 476
assert sum(n for _,n,v in classified if not v) == 34
# For three or fewer vertices, there is no nonzero simplicial H2;
# with four vertices, the only possible nonzero 2-cycle is a missing
# tetrahedral boundary, which the exhaustive classification covers.
print('FACE_COUNTS',tuple(len(faces[k]) for k in range(1,9)))
print('RANKS_MOD3_MOD101',ranks)
print('FOUR_VERTEX_MISSING_TETRAHEDRA',510)
print('NONZERO_H2_F3_SUPPORTS',476)
print('NULL_H2_F3_SUPPORTS',34)
print('AFFINE_ORBITS',sorted(classified))
print('MINIMAL_SUPPORT',4)
print('VERIFY_OK_PALEY17_NEIGHBORHOOD_TORSION_CARRIERS')
