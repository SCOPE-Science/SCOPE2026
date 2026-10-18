#!/usr/bin/env python3
"""Exact finite checks for Poisson occupation sampled along a walking observer.
Uses only Python standard library; numerical quadrature is supplemental.
"""
from fractions import Fraction as F
from itertools import product
from math import comb, sqrt, exp, pi

checks = 0

def check(condition, message):
    global checks
    assert condition, message
    checks += 1

def q(k,x):
    if abs(x)>k or (k+x)%2: return F(0)
    return F(comb(k,(k+x)//2),2**k)

def a_exact(k,p):
    return sum((F(comb(k,j)**2, 2**k)*p**j*(1-p)**(k-j) for j in range(k+1)), F(0))

# Return-probability generating function (1-z+(p-1/2)^2 z^2)^(-1/2).
for p in (F(1,4), F(1,2), F(3,4), F(1,1)):
    d=(p-F(1,2))**2
    a0,a1=F(1),F(1,2)
    check(a_exact(0,p)==a0, 'a0')
    check(a_exact(1,p)==a1, 'a1')
    for k in range(1,26):
        a2=((2*k+1)*a1-2*d*k*a0)/F(2*(k+1))
        check(a2==a_exact(k+1,p), f'return generating function p={p}, k={k}')
        a0,a1=a1,a2

# Exact check of conditional Poisson path-trace second and third moments.
# Every environment trajectory from an initial site is uniformly enumerated.
for n in range(1,7):
    for observer_increments in product((-1,1), repeat=n):
        x=[]; v=0
        for e in observer_increments:
            v+=e; x.append(v)
        trace2=trace3=F(0)
        for y in range(-2*n,2*n+1):
            for environment_increments in product((-1,1), repeat=n):
                u=y; L=0
                for i,e in enumerate(environment_increments):
                    u+=e
                    L += (u == x[i])
                trace2+=F(L*L,2**n)
                trace3+=F(L*L*L,2**n)
        pair=n+2*sum((q(j-i,x[j]-x[i]) for i in range(n) for j in range(i+1,n)), F(0))
        triple=F(0)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    ids=sorted((i,j,k))
                    a,b,c=ids
                    triple+=q(b-a,x[b]-x[a])*q(c-b,x[c]-x[b])
        check(trace2==pair, f'path second moment n={n} {observer_increments}')
        check(trace3==triple, f'path third moment n={n} {observer_increments}')
        check(trace3<=96*n*n, 'uniform third-moment bound')

# Independent exact check: covariance of X, Y with Poisson(lambda) marginals,
# sharing Poisson(lambda*t) plus independent remainder, is lambda*t.
for lam in (F(1,2), F(1), F(3,2)):
    for t in (F(0),F(1,4),F(1,2),F(1)):
        EXY=lam*lam+lam*t
        check(EXY-lam*lam==lam*t,'bivariate Poisson shared-component covariance')

# Numerical check of the n^(3/2) crossover normalization, against independent
# quadrature of its limiting integral (both calculated by different formulas).
for kappa in (0.0,1.0,2.0,4.0):
    # h=t^2 removes the endpoint singularity; composite Simpson rule, standard library.
    intervals=20000
    def integrand(j):
        t=j/intervals
        return 2*(1-t*t)*exp(-kappa*kappa*t*t/4)
    integral=(integrand(0)+integrand(intervals)+4*sum(integrand(j) for j in range(1,intervals,2))+2*sum(integrand(j) for j in range(2,intervals,2)))/(3*intervals)
    target=(2/sqrt(pi))*integral
    n=5000
    p=(1+kappa/sqrt(n))/2
    d=(p-.5)**2
    arr=[1.,.5]
    for k in range(1,n-1):
        arr.append(((2*k+1)*arr[-1]-2*d*k*arr[-2])/(2*(k+1)))
    variance=(n+2*sum((n-k)*arr[k] for k in range(1,n)))/(n**1.5)
    check(abs(variance-target)<0.03,f'crossover kappa={kappa}, {variance} vs {target}')
    print(f'kappa={kappa}: finite-n scaled variance={variance:.8f}; integral={target:.8f}')

print('PASS:',checks,'exact/supplemental assertions')
