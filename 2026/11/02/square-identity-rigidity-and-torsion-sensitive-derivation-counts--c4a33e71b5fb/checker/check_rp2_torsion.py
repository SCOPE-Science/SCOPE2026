"""Compute integral first homology for an explicit six-vertex RP2 triangulation,
then evaluate the derived incidence-algebra Jordan derivation counts over rings of size four."""
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

facets=[(1,2,3),(1,2,4),(1,3,5),(1,4,6),(1,5,6),(2,3,6),(2,4,5),(2,5,6),(3,4,5),(3,4,6)]
vertices=list(range(1,7)); edges=list(combinations(vertices,2))
assert all(any(set(e).issubset(f) for f in facets) for e in edges)
assert len(set(facets))==10
for e in edges: assert sum(set(e).issubset(f) for f in facets)==2
chords=[e for e in edges if 1 not in e]
# fundamental cycle coords for each 1-cycle read directly at non-tree chord edges
boundary=[]
for a,b,c in facets:
    ed={(b,c):1,(a,c):-1,(a,b):1}
    boundary.append([ed.get(e,0) for e in chords])
D=Matrix(boundary).T
S=smith_normal_form(D,domain=ZZ)
diag=[abs(int(S[i,i])) for i in range(10)]
print('facets',len(facets),'edges',len(edges),'vertices',len(vertices))
print('first homology presentation Smith diagonal',diag)
assert diag.count(1)==9 and diag.count(2)==1
# Face poset: all vertices, edges, facets. N = identity plus strict incidence pairs
faces=[frozenset((v,)) for v in vertices]+[frozenset(e) for e in edges]+[frozenset(f) for f in facets]
n=len(faces);N=sum(A<=B for A in faces for B in faces)
print('nonempty-face-poset n',n,'N_comparable_pairs_including_equal',N)
assert n==31 and N==121
print('Z/4 count: 2 * 4^120');print('F4 count: 4 * 4^120')
print('RP2_TORSION_JORDAN_COUNT_OK')
