#!/usr/bin/env python3
"""Exact and numerical supplemental checks for the anisotropic-cube positivity theorem.

Standard-library only. This script is not an infinite-dimensional proof.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, sqrt
from random import Random

checks = 0

def verify(test, why):
    global checks
    if not test:
        raise AssertionError(why)
    checks += 1

def expectation(weights, s):
    d = len(weights)
    return sum((F(1, 1) / (1 + 2 * s * sum(weights[i] for i in range(d) if (mask >> i) & 1))
                for mask in range(1 << d)), F(0, 1)) / (1 << d)

def inverse(A):
    n = len(A)
    aug = [list(A[i]) + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next((i for i in range(k, n) if aug[i][k]), None)
        assert pivot is not None
        aug[k], aug[pivot] = aug[pivot], aug[k]
        t = aug[k][k]
        aug[k] = [x / t for x in aug[k]]
        for i in range(n):
            if i != k and aug[i][k]:
                t = aug[i][k]
                aug[i] = [x - t*y for x, y in zip(aug[i], aug[k])]
    return [row[n:] for row in aug]

def resolvent(weights,s):
    d = len(weights)
    n=1<<d
    S=sum(weights)
    A = [[F(int(x==y)) * (1+s*S) for y in range(n)] for x in range(n)]
    for x in range(n):
        for i,w in enumerate(weights):
            A[x][x^(1<<i)] = -s*w
    return inverse(A)

rng=Random(137)
for d in range(2,5):
    for r in range(5):
        w=[F(rng.randint(1,7),rng.randint(1,5)) for i in range(d)]
        s=F(rng.randint(1,13),rng.randint(1,7))
        R=resolvent(w,s)
        n=1<<d
        target=expectation(w,s)
        for x in range(n):
            verify(R[x][x]==target, ('Walsh diagonal',d,r,x))
            verify(sum(R[x])==1,('stochastic resolvent',d,r,x))
            verify(all(R[x][y]>0 for y in range(n)),('positive resolvent',d,r,x))
            Cdiag=2*R[x][x]-1
            verify((Cdiag>=0)==(target>=F(1,2)),('positivity criterion',d,r,x))
        for x in range(n):
            for y in range(n):
                if x!=y:
                    verify(2*R[x][y]>0,('positive CN offdiagonal',d,r,x,y))

for d in range(2,9):
    for r in range(40):
        w=[F(rng.randint(1,12),rng.randint(1,5)) for i in range(d)]
        i,j=rng.sample(range(d),2)
        avg=(w[i]+w[j])/2
        v=w.copy()
        v[i]=avg
        v[j]=avg
        if w[i]!=w[j]:
            for s in [F(1,10),F(1,2),F(2,1),F(7,1)]:
                verify(expectation(w,s)>expectation(v,s),('strict pair averaging',d,r,s))

# Every isotropic root is the unique crossing of a rational binomial resolvent.
def Fiso(d,theta):
    return sum(comb(d,k) / (2.0**d) / (1+2*theta*k/d) for k in range(d+1))

def bisect(f,a,b,iterations=85):
    assert f(a)>0 and f(b)<0
    for _ in range(iterations):
        m=(a+b)/2
        if f(m)>0:a=m
        else:b=m
    return (a+b)/2

prev=None
for d in range(2,129):
    theta=bisect(lambda y:Fiso(d,y)-0.5,0.99999,2.01)
    verify(1<theta<2,('isotropic bounds',d))
    if prev is not None:
        verify(theta<prev,('dimension ordering',d))
    prev=theta
    if d in (2,3,4,8,16,32,64,128):
        approx=1+0.5/d+0.625/d**2
        verify(abs(theta-approx)<(2/d**3),('third-order remainder consistency',d,theta,approx))
verify(abs(bisect(lambda y:Fiso(2,y)-.5,1,2)-(1+sqrt(5))/2)<1e-12,'golden ratio dimension two')

# The d=2 cubic for all rational a,b is checked at exactly computed resolvents.
for a,b in [(F(1),F(1)),(F(1,3),F(4,7)),(F(7,9),F(1,2)),(F(1,100),F(99,100))]:
    for s in [F(1,2), F(2),F(5,3)]:
        gap=expectation([a,b],s)-F(1,2)
        cub=4*a*b*(a+b)*s**3-2*(a+b)*s-1
        verify((gap>0)==(cub<0),('cubic sign',a,b,s))
        verify((gap==0)==(cub==0),('cubic zero',a,b,s))

# Severe-anisotropy prefactor, numerical check (not proof).
for d in [2,3,5,8]:
    for eps in [1e-4,1e-5,1e-6]:
        w=[1-(d-1)*eps]+[eps]*(d-1)
        terms=[2*sum(w[i] for i in range(d) if (k>>i)&1) for k in range(1<<d)]
        root=bisect(lambda s:sum(1/(1+s*t) for t in terms)/(1<<d)-.5,1e-4,1e5)
        pred=1/sqrt(2*(d-1)*eps)
        verify(abs(root/pred-1)<0.005,('singular prefactor',d,eps,root,pred))

print('VERIFIED', checks, 'supplementary checks (exact rational + numerical); theorem requires the analytic proof')
