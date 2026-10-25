"""Finite integer-programming corroboration; not used for infinite proofs."""
from itertools import combinations
from scipy.optimize import milp,Bounds,LinearConstraint
from scipy.sparse import lil_matrix
import numpy as np

def vectors(q,n):
    if q==1:
        yield (n,);return
    for v in range(n+1):
        for sub in vectors(q-1,n-v):yield (v,)+sub

def solve(q,n,L):
    msgs=list(vectors(q,n));pairs=list(combinations(range(q),2))
    targets=[(i,i) for i in range(q)]+pairs
    A=lil_matrix((len(targets),len(msgs)),dtype=float)
    for j,x in enumerate(msgs):
        for i,(a,b) in enumerate(targets):
            A[i,j]=int(x[a]>=2) if a==b else int(x[a]>=1 and x[b]>=1)
    c=-np.ones(len(msgs))
    res=milp(c,integrality=np.ones(len(msgs)),bounds=Bounds(0,1),constraints=[LinearConstraint(A.tocsr(),0,L)],options={'time_limit':30,'mip_rel_gap':0})
    return {'q':q,'n':n,'L':L,'sol':int(round(-res.fun)) if res.fun is not None else None,'dual_bound':-res.mip_dual_bound if getattr(res,'mip_dual_bound',None) is not None else None,'status':res.message}
if __name__=='__main__':
    for L in [12,13,14,15]:print(solve(4,5,L))
