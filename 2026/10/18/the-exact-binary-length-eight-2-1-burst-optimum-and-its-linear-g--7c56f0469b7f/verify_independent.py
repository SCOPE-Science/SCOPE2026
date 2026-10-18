"""Independent direct channel checks and integer set-packing optimization.

The exhaustive upper-bound certificate is proof_checker.cpp, not a solver log.
This script independently checks channel sets, witnesses and an MILP optimum.
Requires Python 3, scipy and numpy.
"""
from itertools import combinations, product
import numpy as np
from scipy.sparse import coo_matrix
from scipy.optimize import milp, Bounds, LinearConstraint

N=8
words=[''.join(bits) for bits in product('01',repeat=N)]
received=[''.join(bits) for bits in product('01',repeat=N-1)]
pos={w:i for i,w in enumerate(received)}
ball=[]
rows=[]
cols=[]
for j,w in enumerate(words):
    b={w[:i]+bit+w[i+2:] for i in range(N-1) for bit in '01'}
    assert len(b)==N
    ball.append(b)
    for y in b:
        rows.append(pos[y]);cols.append(j)
A=coo_matrix((np.ones(len(rows)),(rows,cols)),
             shape=(len(received),len(words))).tocsr()
nonlinear=[12,21,34,51,72,87,126,129,178,187,207,212,237,240]
basis=[21,79,164]
linear=[int(bool(mask&1))*basis[0] ^ int(bool(mask&2))*basis[1] ^
        int(bool(mask&4))*basis[2] for mask in range(8)]
assert len(set(linear))==8
for candidate in (nonlinear,linear):
    assert all(not(ball[x]&ball[y]) for x,y in combinations(candidate,2))
res=milp(-np.ones(len(words)),integrality=np.ones(len(words)),
    bounds=Bounds(0,1),constraints=LinearConstraint(A,0,1),
    options={'mip_rel_gap':0.0,'time_limit':60.0})
assert res.success and round(-res.fun)==14 and abs(res.fun+14)<1e-5
print('INDEPENDENT_CHECK_OK',len(nonlinear),len(linear),round(-res.fun))
