"""Direct exact-matrix and numerical checks of the paired-clique spectral-gap formulas.
Run with Python 3, numpy, and sympy: python verify_matching.py
The analytic all-size theorem is established in RESULT.md, not by these tests.
"""
from fractions import Fraction as F
from random import Random
import numpy as np
import sympy as sp

checks = 0

def check(cond, explanation=''):
    global checks
    if not cond:
        raise AssertionError(explanation)
    checks += 1

def matrix(m, pair_prices, cross):
    """Laplacian for 2m vertices: 2i and 2i+1 are paired."""
    n = 2 * m
    L = sp.zeros(n)
    for i in range(m):
        a, b = 2 * i, 2 * i + 1
        w = sp.Rational(pair_prices[i])
        L[a,a] += w; L[b,b] += w
        L[a,b] -= w; L[b,a] -= w
    for i in range(m):
        for j in range(i+1, m):
            for a in [2*i, 2*i+1]:
                for b in [2*j, 2*j+1]:
                    w = sp.Rational(cross[i,j])
                    L[a,a] += w; L[b,b] += w
                    L[a,b] -= w; L[b,a] -= w
    return L

def anti(m, i):
    v = sp.zeros(2*m, 1)
    v[2*i] = 1
    v[2*i+1] = -1
    return v

def quotient(m, cross):
    L = sp.zeros(m)
    for i in range(m):
        for j in range(i+1, m):
            w = sp.Rational(cross[i,j])
            L[i,i] += w; L[j,j] += w
            L[i,j] -= w; L[j,i] -= w
    return L

def eiggap(L):
    vals=np.linalg.eigvalsh(np.asarray(L, dtype=float))
    return vals[1]

def budget(m,t,match,cross):
    return t*sum(match)+4*sum(cross[i,j] for i in range(m) for j in range(i+1,m))

rng=Random(168107)
for m in range(2,7):
    n=2*m
    for B in [F(1)]:
        for t in [F(1,2),F(2),F(5,2)]:
            if t<2:
                a=F(B,m*(n-2+t))
                match=[a]*m
                cross=sp.zeros(m)
                for i in range(m):
                    for j in range(i+1,m):cross[i,j]=a
                L=matrix(m,match,cross)
                P=sp.eye(n)-sp.ones(n)/n
                check(L==n*a*P, f'uniform form m={m},t={t}')
                check(budget(m,t,match,cross)==B)
                check(abs(eiggap(L)-float(n*a))<1e-8)
            else:
                a=F(B,m*(n-2))
                match=[F(0)]*m
                cross=sp.zeros(m)
                for i in range(m):
                    for j in range(i+1,m):cross[i,j]=a
                L=matrix(m,match,cross)
                check(budget(m,t,match,cross)==B)
                for i in range(m):
                    check(L*anti(m,i)==F(B,m)*anti(m,i))
                check(abs(eiggap(L)-float(F(B,m)))<1e-8)
            for z in range(2):
                pairs=[F(rng.randint(0,20)) for _ in range(m)]
                raw=sp.zeros(m)
                for i in range(m):
                    for j in range(i+1,m):raw[i,j]=rng.randint(0,20)
                cost=budget(m,t,pairs,raw)
                if cost==0:continue
                pairs=[B*x/cost for x in pairs]
                raw=raw*sp.Rational(B,cost)
                check(abs(float(budget(m,t,pairs,raw))-float(B))<1e-9)
                Ln=matrix(m,pairs,raw)
                optimum=float(n*B/(m*(n-2+t))) if t<2 else float(B/m)
                check(eiggap(Ln)<=optimum+1e-8, f'upper bound m={m},t={t}')

for m in range(2,7):
    B=F(1)
    c0=F(B,2*m*(m-1))
    cross=sp.zeros(m)
    for i in range(m):
        for j in range(i+1,m): cross[i,j]=c0
    if m>=4:
        eps=c0/F(100)
        for i,j,sign in [(0,1,1),(2,3,1),(0,2,-1),(1,3,-1)]:
            cross[i,j]+=sign*eps
    pair=[F(0)]*m
    L=matrix(m,pair,cross)
    check(budget(m,F(5,2),pair,cross)==B)
    for i in range(m):check(L*anti(m,i)==F(B,m)*anti(m,i))
    check(abs(eiggap(L)-float(B/m))<1e-8)
    check(eiggap(2*quotient(m,cross))>=float(B/m)-1e-8)
    if m>=4:check(any(cross[i,j]!=c0 for i in range(m) for j in range(i+1,m)))
    # At the critical price, matched edges can remain positive.
    cc=F(B,2*m*(m-1))*F(2*m-1,2*m)
    cross2=sp.zeros(m)
    for i in range(m):
        for j in range(i+1,m):cross2[i,j]=cc
    pair2=[F(B,4*m*m)]*m
    L2=matrix(m,pair2,cross2)
    check(budget(m,F(2),pair2,cross2)==B)
    for i in range(m):check(L2*anti(m,i)==F(B,m)*anti(m,i))
    check(abs(eiggap(L2)-float(B/m))<1e-8)

print(f'PASS: {checks} exact symbolic/rational identities and numerical spectral/budget/upper-bound checks')
