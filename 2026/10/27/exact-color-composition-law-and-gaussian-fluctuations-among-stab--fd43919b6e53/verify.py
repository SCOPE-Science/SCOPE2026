#!/usr/bin/env python3
"""Exact enumeration for binary majority fixed points on cycles."""
from fractions import Fraction
from math import comb
from itertools import product

def brute(n):
    ans=[0]*(n+1)
    for bits in product((0,1),repeat=n):
        if all(bits[(i-1)%n]==bits[i] or bits[(i+1)%n]==bits[i] for i in range(n)):
            ans[sum(bits)]+=1
    return ans

def coefficient(n,k):
    if k in (0,n):return 1
    return sum(Fraction(n,r)*comb(k-r-1,r-1)*comb(n-k-r-1,r-1)
        for r in range(1,min(k//2,(n-k)//2)+1))

def matmul(A,B):
    s=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(s)) for j in range(s)] for i in range(s)]

def mulpoly(a,b):
    ans=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):ans[i+j]+=x*y
    return ans

def polytrace(n):
    a=[(0,0),(0,1),(1,0),(1,1)]
    T=[[[0] for j in range(4)] for i in range(4)]
    for i,(x,y) in enumerate(a):
        for j,(u,v) in enumerate(a):
            if u==y and not(x==v and x!=y):T[i][j]=[0,1] if v else [1]
    P=[[[int(i==j)] for j in range(4)]for i in range(4)]
    for _ in range(n):
        P=[[sum_poly([mulpoly(P[i][k],T[k][j]) for k in range(4)]) for j in range(4)]for i in range(4)]
    return sum_poly([P[i][i] for i in range(4)])

def sum_poly(q):
    o=[0]*max(map(len,q))
    for p in q:
        for j,v in enumerate(p):o[j]+=v
    return o

if __name__=='__main__':
    for n in range(3,17):
        b=brute(n)
        f=[int(coefficient(n,k)) for k in range(n+1)]
        m=polytrace(n)
        m+= [0]*(n+1-len(m))
        assert b==f==m,(n,b,f,m)
        print('n',n,'fixed',sum(b),'mean',float(Fraction(sum(k*v for k,v in enumerate(b)),sum(b))))
    print('VERIFIED n=3..16: exhaustive states, run coefficients, transfer traces')
