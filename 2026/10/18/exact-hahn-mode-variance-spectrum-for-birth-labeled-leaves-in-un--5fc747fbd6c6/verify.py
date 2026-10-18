#!/usr/bin/env python3
"""Exact finite checks for a birth-label leaf covariance spectral identity.
The mathematical argument is in RESULT.md; this script checks finite instances.
Requires only the Python standard library.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial

checks=0
for n in range(3,9):
    N=n-1
    choices=(range(1,j) for j in range(2,n+1))
    trees=0
    count=[0]*n
    joint=[[0]*n for _ in range(n)]
    for parents in product(*choices):
        trees+=1
        child={p for p in parents}
        leaf=[int(j not in child) for j in range(1,n+1)]
        for i in range(1,n+1):
            if leaf[i-1]:
                count[i-1]+=1
                for j in range(1,n+1):
                    if leaf[j-1]:joint[i-1][j-1]+=1
    assert trees==factorial(n-1)
    for i in range(2,n):
        x=i-1
        mean=F(count[i-1],trees)
        assert mean==F(x,N)
        checks+=1
        for j in range(2,n):
            y=j-1
            cov=F(joint[i-1][j-1],trees)-F(count[i-1]*count[j-1],trees**2)
            expected=(F(x*(N-x),N*N) if i==j else -F(min(x,y)*(N-max(x,y)),N*N*(N-1)))
            assert cov==expected,(n,i,j,cov,expected)
            checks+=1
    assert count[n-1]==trees
    checks+=1

# Exact orthogonal-polynomial eigen-equations for the generalized covariance.
for N in range(2,16):
    xs=list(range(1,N))
    a={x:x*(N-x) for x in range(N+1)}
    polynomials=[]
    def inner(u,v): return sum(F(a[x])*u[x-1]*v[x-1] for x in xs)
    for d in range(N-1):
        p=[F(x**d) for x in xs]
        for q in polynomials:
            coeff=inner(p,q)/inner(q,q)
            p=[p[k]-coeff*q[k] for k in range(N-1)]
        assert inner(p,p)>0
        for q in polynomials:
            assert inner(p,q)==0
            checks+=1
        poly={x:p[x-1] for x in xs}
        poly[0]=poly[N]=F(0)
        r=d+1
        for x in xs:
            T=2*a[x]*poly[x]-a[x-1]*poly[x-1]-a[x+1]*poly[x+1]
            assert T==F(r*(r+1))*poly[x],(N,d,x,T)
            checks+=1
        # Direct kernel eigen-identity for G relative to D.
        mu=F(N,(N-1)*r*(r+1))
        for x in xs:
            left=sum(F(min(x,y)*(N-max(x,y)),N*N*(N-1))*poly[y] for y in xs)
            right=mu*F(a[x],N*N)*poly[x]
            assert left==right,(N,d,x)
            checks+=1
        polynomials.append(p)
    assert len(polynomials)==N-1
    checks+=1

print('VERIFY_OK', 'assertions=',checks,'recursive_trees_through_n=8','polynomial_spectra_through_N=15')
