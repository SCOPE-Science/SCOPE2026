#!/usr/bin/env python3
"""Independent exact and floating-point checks of the stated cycle-resolvent theorem."""
from fractions import Fraction as Q
from itertools import combinations
import numpy as np

def solve_exact(a,b):
    n=len(b)
    aug=[list(map(Q,a[i]))+[Q(b[i])] for i in range(n)]
    for j in range(n):
        p=next((k for k in range(j,n) if aug[k][j]),None)
        if p is None: raise AssertionError('singular')
        aug[j],aug[p]=aug[p],aug[j]
        s=aug[j][j]
        aug[j]=[v/s for v in aug[j]]
        for k in range(n):
            if k==j: continue
            c=aug[k][j]
            if c: aug[k]=[x-c*y for x,y in zip(aug[k],aug[j])]
    return [aug[i][-1] for i in range(n)]

def test():
    exact=0
    for n in (3,4,6,8,9):
        for r in range(1,n+1):
            if n%r: continue
            q=n//r
            for kappa in (Q(1,2),Q(3)):
                bound=Q(n,r)/kappa+Q((q*q)//4,2)
                for traps in combinations(range(n),r):
                    a=[[Q(2 if i==j else -1 if ((i-j)%n in (1,n-1)) else 0) for j in range(n)] for i in range(n)]
                    for z in traps: a[z][z]+=kappa
                    u=solve_exact(a,[1]*n)
                    assert max(u)>=bound,(n,r,kappa,traps,max(u),bound)
                    if traps==tuple(i*q for i in range(r)): assert max(u)==bound
                    exact+=1
    count=0
    for n in (3,4,6,8,9,10,12,15):
        lap=np.zeros((n,n))
        for i in range(n):
            j=(i+1)%n
            lap[i,i]+=1;lap[j,j]+=1;lap[i,j]-=1;lap[j,i]-=1
        for r in range(1,n+1):
            if n%r: continue
            q=n//r
            for kappa in (0.125,1.,5.):
                bound=n/(r*kappa)+(q*q//4)/2
                for traps in combinations(range(n),r):
                    a=lap.copy()
                    a[np.array(traps),np.array(traps)]+=kappa
                    u=np.linalg.solve(a,np.ones(n))
                    assert max(u)>=bound-2e-8*(1+bound)
                    if traps==tuple(i*q for i in range(r)):
                        assert abs(max(u)-bound)<1e-8*(1+bound)
                    count+=1
    print('VERIFY_OK exact_cases=',exact,'float_cases=',count)
if __name__=='__main__': test()
