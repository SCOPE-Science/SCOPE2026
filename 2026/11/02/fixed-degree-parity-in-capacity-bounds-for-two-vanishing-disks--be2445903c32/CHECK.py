#!/usr/bin/env python3
"""Exact rational checks of fixed-degree two-disk planar moments (a=1)."""
from fractions import Fraction as F
from math import comb

def moment(i,j,r):
    return sum(F(comb(i,h)*comb(j,h)*c**(i+j-2*h)) * r**(2*h+2) / F(h+1)
               for c in (-1,1) for h in range(min(i,j)+1))

def solve(a,b):
    n=len(b)
    if n==0: return []
    aug=[list(map(F,row))+[F(b[i])] for i,row in enumerate(a)]
    for j in range(n):
        h=next(i for i in range(j,n) if aug[i][j]!=0)
        aug[j],aug[h]=aug[h],aug[j]
        p=aug[j][j]
        aug[j]=[x/p for x in aug[j]]
        for i in range(n):
            if i!=j:
                m=aug[i][j]
                aug[i]=[aug[i][t]-m*aug[j][t] for t in range(n+1)]
    return [aug[i][-1] for i in range(n)]

def bound_square(n,r):
    d=n-1
    mat=[[moment(i,j,r) for j in range(d)] for i in range(d)]
    v=[moment(i,d,r) for i in range(d)]
    coeff=solve(mat,v)
    return n*(moment(d,d,r)-sum(v[i]*coeff[i] for i in range(d)))

def leading_square(n,r):
    if n%2==0:
        return (2*r)**n
    k=(n-1)//2
    return F(2*n,k+1)*2**(2*k)*r**(2*k+2)

for r in (F(1,10),F(1,100)):
    assert bound_square(1,r)==2*r*r
    assert bound_square(2,r)==4*r*r+2*r**4
    assert bound_square(3,r)==12*r**4+2*r**6
    for n in range(1,7):
        ratio=bound_square(n,r)/leading_square(n,r)
        assert abs(ratio-F(1))<F(1,2)
        if r==F(1,100):
            assert abs(ratio-F(1))<F(1,50)
for n in range(1,7):
    err_big=abs(bound_square(n,F(1,10))/leading_square(n,F(1,10))-1)
    err_small=abs(bound_square(n,F(1,100))/leading_square(n,F(1,100))-1)
    assert err_small<=err_big
print('CHECK_OK: exact low-degree Gram identities and six fixed-degree small-radius leading constants')
