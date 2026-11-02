"""Standalone small-prime numerical rank and character-nullity cross-checks.
Only the proof in RESULT.md establishes the all-prime assertion.
"""
from math import pi
import numpy as np

def primes(L):
    return [p for p in range(3,L+1,2) if all(p%d for d in range(2,int(p**0.5)+1))]

def primitive_root(p):
    for g in range(2,p):
        if len({pow(g,k,p) for k in range(p-1)})==p-1:return g
    raise ValueError(p)

cases=0
by_p=[]
for p in primes(31):
    n=p-1;g=primitive_root(p)
    units=[pow(g,j,p) for j in range(n)]
    by_p_counts={"nonsquare":0,"square":0,"degenerate":0}
    for a,b in [(0,0),(0,1),(1,0)]+[(1,c) for c in range(1,p)]:
        phases=np.empty((n,n),dtype=int)
        for i,s in enumerate(units):
            for j,t in enumerate(units):
                w=(s*t)%p
                phases[i,j]=(a*w+b*pow(w,-1,p))%p
        Z=np.exp(2j*pi*phases/p)
        sv=np.linalg.svd(Z,compute_uv=False)
        rank=int(np.sum(sv>1e-7))
        legendre=0 if a*b==0 else (1 if pow(a*b,(p-1)//2,p)==1 else -1)
        expected=1 if a==0 and b==0 else (p-2 if legendre==-1 else p-1)
        assert rank==expected,(p,a,b,rank,expected,sv)
        if (a,b)==(0,0) or a*b==0:by_p_counts['degenerate']+=1
        elif legendre==1:by_p_counts['square']+=1
        else:by_p_counts['nonsquare']+=1
        cases+=1
    by_p.append((p,by_p_counts))
print('PASS',cases,'numerical parameter/rank checks')
for p,counts in by_p:print(p,counts)
