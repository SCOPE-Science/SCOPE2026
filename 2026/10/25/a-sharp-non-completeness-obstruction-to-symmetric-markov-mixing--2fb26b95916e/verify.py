#!/usr/bin/env python3
"""Exact rational replay of the deleted-matching fastest mixing formulas."""
from fractions import Fraction as F
from itertools import combinations

def mat(n,k):
    m=n-2*k
    pairs={(2*j,2*j+1) for j in range(k)}
    z=F(m-1,m*(n-1)) if m else None
    a=F(1,n-1)
    P=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if tuple(sorted((i,j))) in pairs: row.append(F(0))
            elif i<2*k or j<2*k: row.append(a)
            else: row.append(z)
        P.append(row)
    return P

def vectors(n,k):
    m=n-2*k
    u=lambda a: [F(x) for x in a]
    v=[]
    for j in range(k):
        z=[0]*n;z[2*j]=1;z[2*j+1]=-1;v.append((u(z),F(1,n-1)))
    for j in range(1,k):
        z=[0]*n;z[0]=1;z[1]=1;z[2*j]=-1;z[2*j+1]=-1;v.append((u(z),-F(1,n-1)))
    for j in range(1,m):
        z=[0]*n;z[2*k]=1;z[2*k+j]=-1;v.append((u(z),F(0)))
    if m:
        z=[m]* (2*k)+[-2*k]*m
        v.append((u(z),-F(1,n-1)))
    v.append(([F(1)]*n,F(1)))
    return v

def run():
    cases=0
    for n in range(3,31):
        for k in range(1,n//2+1):
            P=mat(n,k)
            assert all(sum(row)==1 for row in P)
            assert all(P[i][j]==P[j][i] and P[i][j]>=0 for i in range(n) for j in range(n))
            spec=vectors(n,k)
            assert len(spec)==n
            for v,lam in spec:
                assert all(sum(P[i][j]*v[j] for j in range(n))==lam*v[i] for i in range(n))
            cases+=1
    print('EXACT_REPLAY_OK',cases)
if __name__=='__main__':run()
