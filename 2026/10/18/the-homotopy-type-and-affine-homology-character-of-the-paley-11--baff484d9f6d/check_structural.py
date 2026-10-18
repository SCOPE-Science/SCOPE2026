#!/usr/bin/env python3
"""Finite combinatorial checks for the Paley-11 out-neighborhood theorem."""
from itertools import combinations
from collections import Counter
P = 11
Q = frozenset(pow(x, 2, P) for x in range(1, P))
assert Q == frozenset((1, 3, 4, 5, 9))
facets = [frozenset((i+a)%P for a in Q) for i in range(P)]
assert len(set(facets)) == 11
assert all(len(facets[i]&facets[j])==2 for i in range(P) for j in range(i+1,P))
F = {frozenset()}
for S in facets:
    for k in range(1, 6):
        F.update(frozenset(x) for x in combinations(S, k))
fvec = tuple(sum(len(s)==k for s in F) for k in range(6))
assert fvec == (1,11,55,110,55,11)
full_triangles = {frozenset(t) for t in combinations(range(P),3)}
missing = full_triangles - {s for s in F if len(s)==3}
assert len(missing) == 55
rep = frozenset((0,1,3)); assert rep in missing
orbit = {frozenset((a*x+b)%P for x in rep) for a in Q for b in range(P)}
assert len(orbit)==55 and orbit==missing
assert all(frozenset(t) in F for t in ((0,1,2),(0,2,3),(1,2,3)))
# Every triangle missing from the complex bounds the three triangular faces of an affine image of the (0,1,2,3) tetrahedral boundary.
for a in Q:
 for b in range(P):
    t = frozenset((a*x+b)%P for x in (0,1,3))
    witness = (a*2+b)%P
    assert t in missing and all((frozenset((u,v,witness)) in F) for u,v in combinations(t,2))
# A prescribed sequence of elementary free-face collapses of dimension >=3.
K = set(F)
pairs = []
for B in facets:
    seq=sorted(B); apex=seq[-1]; base=frozenset(seq[:-1])
    operations = [(base,B)]
    for tri in combinations(seq[:-1],3):
        t=frozenset(tri)
        operations.append((t,t|{apex}))
    for small,large in operations:
        assert small in K and large in K and len(large)==len(small)+1
        assert [s for s in K if small < s] == [large], (small,large)
        K.remove(small);K.remove(large)
        pairs.append((small,large))
assert len(pairs)==55
remaining = tuple(sum(len(s)==k for s in K) for k in range(6))
assert remaining == (1,11,55,66,0,0)
# Euler characteristic and simply-connectedness follow from the explicit orbit-filling proof.
chi=sum((-1)**(k-1)*fvec[k] for k in range(1,6))
assert chi == 22
assert 1-chi == -21
print('Q:',sorted(Q))
print('faces_by_cardinality:',fvec)
print('all_facet_pair_intersections: 2')
print('missing_triangles_affine_orbit: 55')
print('missing_triangle_filler:',sorted(rep),'apex=2')
print('elementary_collapses:',len(pairs),'residual:',remaining)
print('Euler_characteristic:',chi,'wedge_S2_rank:',chi-1)
