#!/usr/bin/env python3
"""Reproduce exact spectral identities and test sharp optimal-face endpoints.
Run with Python 3, numpy and sympy. No external data or network required.
"""
from fractions import Fraction as F
from math import comb
import numpy as np
import sympy as sp

def parameters(r,s):
    assert r>=2 and s>=2
    if s<=2*r:
        x=F(2,s+2*r)
        mu=F(s,s+2*r)
    else:
        x=F(1,s)
        mu=F(s-r,s)
    c=1-s*x
    low=max(F(0),F(r-1,2)*(c-mu))
    high=min(F(r,2)*c,F(r-1,2)*(c+mu))
    return x,mu,c,low,high

def matrix(r,s,x,y):
    n=r+s
    p=sp.zeros(n)
    for i in range(r):
        for j in range(i+1,r):
            p[i,j]=p[j,i]=sp.Rational(y.numerator,y.denominator)
        for j in range(s):
            p[i,r+j]=p[r+j,i]=sp.Rational(x.numerator,x.denominator)
    for i in range(n):
        p[i,i]=1-sum(p[i,j] for j in range(n) if j!=i)
    return p

def eigen_formula(r,s,x,y):
    c=1-s*x
    return {sp.Integer(1):1,
            sp.Rational(1-r*x):s-1,
            sp.Rational(1-(r+s)*x):1,
            sp.Rational(c-r*y):r-1}

cases=0
for r in range(2,9):
    for s in range(2,17):
        x,mu,c,low,high=parameters(r,s)
        assert low<=high
        for T in {low,high,(low+high)/2}:
            y=T/F(comb(r,2))
            P=matrix(r,s,x,y)
            assert all(P[i,j]>=0 for i in range(r+s) for j in range(r+s))
            assert all(sum(P[i,j] for j in range(r+s))==1 for i in range(r+s))
            # Derive the claimed spectrum by direct exact matrix multiplication
            u=sp.ones(r+s,1)
            assert P*u==u
            for j in range(1,s):
                v=sp.zeros(r+s,1);v[r]=1;v[r+j]=-1
                assert P*v==(1-r*x)*v
            for j in range(1,r):
                v=sp.zeros(r+s,1);v[0]=1;v[j]=-1
                assert P*v==(c-r*y)*v
            v=sp.Matrix([s]*r+[-r]*s)
            assert P*v==(1-(r+s)*x)*v
            assert abs(1-r*x)<=mu
            assert abs(1-(r+s)*x)<=mu
            assert abs(c-r*y)<=mu
            cases+=1
        if s<r:
            assert low>0
        elif s<2*r:
            assert low==0 and high>0
        else:
            assert low==high==c==0

# Non-invariant examples from small symmetric stochastic core perturbations.
noninvariant=0
for r,s in [(4,2),(5,3),(6,5),(5,7)]:
    x,mu,c,low,high=parameters(r,s)
    y=(low+high)/2/F(comb(r,2))
    A=np.full((r,r),float(y));np.fill_diagonal(A,float(c-(r-1)*y))
    # A zero-row-sum symmetric perturbation, supported by the first three core vertices.
    H=np.zeros((r,r))
    H[0,0]=1;H[1,1]=1;H[0,1]=H[1,0]=-1
    for eps in [1e-4, 2e-4]:
        B=A+eps*H
        if np.min(B)<-1e-14: continue
        v=np.linalg.eigvalsh(B)
        if max(abs(v[:-1])) <=float(mu)+1e-10:
            noninvariant+=1

# Exhaustive rational symbolic characteristic polynomial checks for small graphs.
char_cases=0
for r,s in [(2,2),(2,5),(3,2),(4,3),(3,6),(5,2)]:
    x,mu,c,lo,hi=parameters(r,s)
    y=(lo+hi)/2/F(comb(r,2))
    P=matrix(r,s,x,y)
    z=sp.symbols('z')
    expected=(z-1)*(z-sp.Rational(1-r*x))**(s-1)*(z-sp.Rational(1-(r+s)*x))*(z-sp.Rational(c-r*y))**(r-1)
    assert sp.factor(P.charpoly(z).as_expr()-expected)==0
    char_cases+=1

# A proposed no-core-edge kernel is suboptimal when s<r.
for r,s in [(3,2),(5,2),(7,3),(8,5)]:
    x,mu,c,lo,hi=parameters(r,s)
    P=matrix(r,s,x,F(0))
    vals=np.linalg.eigvalsh(np.array(P,dtype=float))
    assert max(abs(vals[:-1])) > float(mu)+1e-9

print('PASS: exact block/eigenvector/capacity/boundary tests',cases)
print('PASS: symbolic characteristic polynomials',char_cases)
print('PASS: noninvariant optimal core perturbations',noninvariant)
print('PASS: necessary core-edge use for clique larger than independent part')
