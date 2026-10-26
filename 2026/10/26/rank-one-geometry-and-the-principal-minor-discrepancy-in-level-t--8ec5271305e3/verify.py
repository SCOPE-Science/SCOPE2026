#!/usr/bin/env python3
"""Exact finite checks for signed rank-one symmetric-matrix components.

The exhaustive finite sign-pattern enumeration is a diagnostic, not a proof
of the all-d statement, which follows from vertex-sign gauge normalization.
"""
from itertools import product, combinations
from math import comb

for d in range(2, 8):
    edges=list(combinations(range(d),2))
    E=len(edges)
    assert E <= 21
    orbit_reps=set()
    for mask in range(1 << E):
        signs={e: -1 if mask>>k&1 else 1 for k,e in enumerate(edges)}
        # gauge to all +1 on star edges (0,j)
        gauge=[1]+[signs[(0,j)] for j in range(1,d)]
        repr_mask=0
        for k,(i,j) in enumerate(edges):
            if signs[(i,j)]*gauge[i]*gauge[j] == -1:
                repr_mask |= 1<<k
        orbit_reps.add(repr_mask)
    assert len(orbit_reps) == 2**(E-d+1)
    rank1_degree=2**(d-1)
    principal_degree=2**E
    assert len(orbit_reps)*rank1_degree==principal_degree
    h_nums=[comb(d,2*j) for j in range(d//2+1)]
    assert sum(h_nums)==rank1_degree
    f=2*d*d-d*(d+1)//2
    dimension=f+d
    assert dimension == d*(3*d+1)//2
    print(f'd={d} components={len(orbit_reps)} component_degree={rank1_degree} '
          f'principal_degree={principal_degree} ambient={2*d*d} '
          f'dimension={dimension} hilbert_numerator={h_nums}')
M=[[1,1,1],[1,1,-1],[1,-1,1]]
for i,j in combinations(range(3),2):
    assert M[i][i]*M[j][j] == M[i][j]**2
# a nonprincipal 2x2 minor
minor=M[0][0]*M[1][2]-M[0][1]*M[0][2]
assert minor==-2
# determinant, explicit expansion 3x3
det=(M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-
     M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+
     M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
assert det==-4
print('VERIFY_OK d=3 principal_equations=0 nonprincipal_minor=-2 determinant=-4')
