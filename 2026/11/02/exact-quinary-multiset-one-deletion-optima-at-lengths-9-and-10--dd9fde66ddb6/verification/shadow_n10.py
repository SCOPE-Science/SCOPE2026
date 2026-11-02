import sys,time
from itertools import combinations
from math import comb
import numpy as np
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix

def comps(n,q):
    for bars in combinations(range(n+q-1),q-1):
        b=(-1,)+bars+(n+q-1,)
        yield tuple(b[i+1]-b[i]-1 for i in range(q))

n,q=10,5
X=list(comps(n,q));Y=list(comps(n-1,q)); ix={x:i for i,x in enumerate(X)}
A=lil_matrix((len(Y),len(X)),dtype=float)
for j,y in enumerate(Y):
    for i in range(q):
       x=list(y);x[i]+=1
       A[j,ix[tuple(x)]]=1
A=A.tocsr()
assert len(X)==1001 and len(Y)==715 and A.nnz==3575
# witness size 143, code syndromes uniform
syn=[sum(i*x[i] for i in range(q))%q for x in X]
W=[j for j,v in enumerate(syn) if v==0]
assert len(W)==201
assert np.max(np.asarray(A[:,W].sum(axis=1)).ravel())<=1
print('WITNESS 201 VALID 1001 words 715 shadows',flush=True)
t0=time.monotonic()
r=milp(c=-np.ones(len(X)),integrality=np.ones(len(X)),bounds=Bounds(0,1),constraints=LinearConstraint(A,lb=np.zeros(len(Y)),ub=np.ones(len(Y))),options={'time_limit':180,'mip_rel_gap':0.0})
print('MILP elapsed',time.monotonic()-t0,'status',r.status,'message',r.message,'max',None if r.fun is None else -r.fun,'upper',None if r.mip_dual_bound is None else -r.mip_dual_bound,'gap',r.mip_gap,flush=True)
assert r.status==0 and r.mip_gap<1e-7 and -r.mip_dual_bound<202-1e-5 and -r.fun>200.999999
assert np.max(np.abs(r.x-np.rint(r.x)))<1e-7
assert np.max((A @ np.rint(r.x))-1)<1e-7
print('Q5N10_MILP_VERIFIED',flush=True)
sys.stdout.flush();import os;os._exit(0)
