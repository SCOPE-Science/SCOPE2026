"""Exact-rational finite tests for five-cross-polytope vertex averages.
Proof for arbitrary resolution is in RESULT.md; tests are not substituted for it.
"""
from fractions import Fraction as F
from itertools import product

def reduced_error_sq(f, t):
    ff=sorted(f,reverse=True)
    s=sum(x*x for x in ff)
    return min(s+r-2*sum(ff[:r]) for r in range(t%2,min(5,t)+1,2))

count=0
for f0 in product([F(0),F(1,4),F(1,2),F(3,4),F(1)], repeat=5):
    for t in range(1,7):
        if sum(f0)>t: continue
        bound = F(1) if t<=2 else F(5,4)
        assert reduced_error_sq(f0,t)<=bound,(f0,t)
        count+=1

for k in range(1,7):
    grid=[]
    for z in product(range(-k,k+1), repeat=5):
        mass=sum(map(abs,z))
        if mass<=k and (k-mass)%2==0:
            grid.append(z)
    y=([F(0)]*5 if k==1 else [F(1)]+[F(0)]*4 if k==2 else [F(1,2)]*5)
    ds=min(sum((a-b)**2 for a,b in zip(y,z)) for z in grid)
    assert ds == (F(1) if k<=2 else F(5,4)), (k,ds)
print('FIVE_CROSSPOLYTOPE_HAUSDORFF_OK grid_checks=',count,' witness_resolutions=6')
