#!/usr/bin/env python3
"""Exact standard-library verification for a cyclic Euler lattice."""
from math import gcd
from itertools import combinations

def product(A,B):
    return [[sum(A[i][h]*B[h][j] for h in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]

def power(A,k):
    out=identity(len(A))
    while k:
        if k&1: out=product(out,A)
        A=product(A,A); k//=2
    return out

def minus(A,B):
    return [[a-b for a,b in zip(x,y)] for x,y in zip(A,B)]

def rank(A):
    from fractions import Fraction
    B=[[Fraction(x) for x in row] for row in A]
    h=0
    for j in range(len(B[0])):
        p=next((i for i in range(h,len(B)) if B[i][j]),None)
        if p is None: continue
        B[h],B[p]=B[p],B[h]
        pivot=B[h][j]
        for i in range(h+1,len(B)):
            v=B[i][j]/pivot
            if v: B[i]=[x-v*y for x,y in zip(B[i],B[h])]
        h+=1
        if h==len(B):break
    return h

# The monic polynomial is t^6-t^5-t^4+2t^3-t^2-t+1.
coeff=[1,-1,-1,2,-1,-1]
C=[[0]*6 for _ in range(6)]
for j in range(5):C[j+1][j]=1
for i in range(6):C[i][5]=-coeff[i]
D=minus(power(C,6),identity(6))
expected=[[-2,-1,-2,-1,-2,-1],
          [ 1,-1, 1,-1, 1,-1],
          [ 1, 2, 1, 2, 1, 2]]*2
assert D==expected
assert product(D,D)==[[0]*6 for _ in range(6)]
assert rank(D)==2
all_two=[]
for ii in combinations(range(6),2):
    for jj in combinations(range(6),2):
        a,b=(D[i][jj[0]] for i in ii)
        c,d=(D[i][jj[1]] for i in ii)
        all_two.append(abs(a*d-b*c))
assert gcd(*[abs(v) for row in D for v in row])==1
assert gcd(*all_two)==3
for k in range(1,13):
    B=minus(power(C,6*k),identity(6))
    assert B==[[k*x for x in row] for row in D]
    assert rank(B)==2
    assert gcd(*[abs(v) for row in B for v in row])==k
    assert gcd(*[k*k*v for v in all_two])==3*k*k

for n in range(3,61):
    H=[[0]*n for _ in range(n)]
    for i in range(n):
        for off,c in ((0,2),(1,-1),(-1,-1),(2,-1),(-2,-1),(3,1),(-3,1)):
            H[i][(i+off)%n]+=c
    for i in range(n):
        for j in range(n):assert H[i][j]==H[j][i]
    null=n-rank(H)
    expected_null=4 if n%6==0 else 2 if n%2==0 else 1
    assert null==expected_null,(n,null,expected_null)
print('OK: companion presentation, exact Smith determinantal divisors and finite spectral cross-checks')
