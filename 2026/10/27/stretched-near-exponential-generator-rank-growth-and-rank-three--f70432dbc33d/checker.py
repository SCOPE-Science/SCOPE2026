#!/usr/bin/env python3
"""Independent exact integer orbit-series arithmetic and lower-bound construction checks."""
import math

def colored_partitions(N, mode):
    p=[0]*(N+1);p[0]=1
    for j in range(1,N+1):
        exp=1 if mode=='partitions' else j//2 if mode=='cycles' else j if mode=='plane' else 0
        for _ in range(exp):
            for i in range(j,N+1):p[i]+=p[i-j]
    return p

def multiset(coeff):
    N=len(coeff)-1
    b=[0]*(N+1)
    for j in range(1,N+1):
        for i in range(j,N+1,j):b[i]+=j*coeff[j]
    a=[0]*(N+1);a[0]=1
    for n in range(1,N+1):
        s=sum(b[j]*a[n-j] for j in range(1,n+1))
        assert s%n==0
        a[n]=s//n
    return a

def series(N=40):
    P=colored_partitions(N,'partitions')
    Q=colored_partitions(N,'cycles')
    pq=[sum(P[j]*Q[k-j] for j in range(k+1)) for k in range(N+1)]
    F=[0]+[sum(pq[:j]) for j in range(1,N+1)]
    F0=[0]+[sum(P[:j]) for j in range(1,N+1)]
    Fe=[0]+list(range(1,N+1))
    G=multiset(F);G0=multiset(F0);Ge=multiset(Fe)
    print('n r3 r2 m r3/m log(m)/(n/sqrt(log n))')
    for n in [5,6,7,8,10,12,15,20,25,30,35,40]:
        if n>N:continue
        r3=G[n]-G0[n];r2=Ge[n]-P[n];m=3+r3+r2
        assert r3>0 and r2>=0 and m>=3
        print(n,r3,r2,m,round(r3/m,6),round(math.log(m)*math.sqrt(math.log(n))/n,6))
    for n in range(1,N+1):
        assert G[n]>=G0[n] and G[n]>=Ge[n]
    print('VERIFY_OK formal Euler factors and rank3 dominance, n<=',N)

if __name__=='__main__':series()
