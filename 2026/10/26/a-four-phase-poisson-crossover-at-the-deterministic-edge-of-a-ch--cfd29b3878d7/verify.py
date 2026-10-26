#!/usr/bin/env python3
"""Reproduce finite-step and critical-window checks for a cyclic four-direction lattice walk."""
import cmath
import math
from collections import defaultdict

DIRECTIONS = ((1,0),(-1,0),(0,1),(0,-1))
ROTATE = (3,2,0,1)


def direct_probabilities(steps, p):
    state = {(0,0,d):1/4 for d in range(4)}
    for _ in range(steps):
        future = defaultdict(float)
        for (x,y,d),weight in state.items():
            for new_d in range(4):
                prob = (1-p)/4 + (p if new_d==ROTATE[d] else 0)
                dx,dy=DIRECTIONS[new_d]
                future[(x+dx,y+dy,new_d)] += weight*prob
        state=future
    return state


def msd_exact(n,p):
    return n + 2*sum((n-k)*p**k*math.cos(math.pi*k/2) for k in range(1,n))


def limit_msd(lam,r):
    return lam+1-math.exp(-lam)*math.cos(math.pi*r/2)


def limit_cf(kx,ky,lam,r):
    x,y=math.cos(kx),math.cos(ky)
    g0=(1+x)*(1+y)/4
    g1=(1-x*y)/4
    g2=(1-x)*(1-y)/4
    return ((1+x)*(1+y)*math.exp(lam*(g0-1)) +
      (-1)**r*(1-x)*(1-y)*math.exp(lam*(g2-1))+
      2*math.cos(math.pi*r/2)*(1-x*y)*math.exp(lam*(g1-1)))/4


def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def matpower(A,n):
    m=len(A)
    Z=[[complex(i==j) for j in range(m)] for i in range(m)]
    while n:
        if n&1:Z=matmul(Z,A)
        A=matmul(A,A);n//=2
    return Z


def cf_finite(n,p,kx,ky):
    weights=[cmath.exp(1j*(kx*dx+ky*dy)) for dx,dy in DIRECTIONS]
    M=[[weights[i]*((1-p)/4+(p if i==ROTATE[j] else 0)) for j in range(4)] for i in range(4)]
    T=matpower(M,n)
    return sum(sum(row)/4 for row in T)


def check():
    count=0
    for n in range(1,13):
      for p in (0.,.25,.65,.9,1.):
        s=direct_probabilities(n,p)
        assert abs(sum(s.values())-1)<1e-12
        val=sum((x*x+y*y)*w for (x,y,d),w in s.items())
        assert abs(val-msd_exact(n,p))<1e-9,(n,p,val,msd_exact(n,p))
        count+=1
    for r in range(4):
      for lam in (0.,.3,1.2,4.0):
        for kx,ky in ((.2,.5),(1.4,2.0),(math.pi/2,.7)):
            n=6000+r
            val=cf_finite(n,1-lam/n,kx,ky)
            target=limit_cf(kx,ky,lam,r)
            assert abs(val-target)<.004,(n,lam,kx,ky,val,target)
            count+=1
        n=20000+r
        assert abs(msd_exact(n,1-lam/n)-limit_msd(lam,r))<.006,(n,r,lam)
        count+=1
    print(f'PASS: {count} finite-step exact/MSD and critical-window comparisons')

if __name__=='__main__':
    check()
