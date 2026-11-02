"""Reproduce the scalar squared-amplification coupling calculations.

Uses only the Python standard library. Finite tests supplement, not replace, the analytical proof.
"""
from fractions import Fraction
from itertools import permutations
from math import sqrt, log

def g(r,u):
    return (1-r/(1+r*u))**2

def pivot(r):
    m=min(r-1,1/(r+1))
    return 2*m/(1-m*m)

def q(r,p):
    if r <= 1:
        return g(r,p)
    b=pivot(r)
    if p <= b:
        t=p/(1+sqrt(1+p*p))
    elif r < sqrt(2):
        t=1-1/(p+1/r)
    else:
        t=1/(1+1/r-p)-1
    return t*t

def cdf(r,x):
    t=sqrt(x)
    lo=1-r; hi=1/(1+r)
    low=max(lo,-t); high=min(hi,t)
    if low>=high:return 0.
    return 1/(1-high)-1/(1-low)

def midpoint(fun,n):
    return sum(fun((i+0.5)/n) for i in range(n))/n

for r in (0.125, 0.5,1.,1.00001,1.1,1.4,1.5,2.,3.,10.):
    for j in range(1,1000):
        p=j/1000
        value=q(r,p)
        assert abs(cdf(r,value)-p)<5.e-9,(r,p,value,cdf(r,value))

for r in (Fraction(1,2),Fraction(1),Fraction(3,2),Fraction(2),Fraction(4)):
    vals=[g(r,Fraction(2*i+1,12)) for i in range(6)]
    best=min(sum(vals[i]*vals[k] for i,k in enumerate(perm)) for perm in permutations(range(6)))
    vals.sort()
    sorted_antithetic=sum(vals[i]*vals[5-i] for i in range(6))
    assert best==sorted_antithetic

r=2.
n=120000
best=midpoint(lambda p:q(r,p)*q(r,1-p),n)
antithetic=midpoint(lambda p:g(r,p)*g(r,1-p),n)
formula_antithetic=Fraction(5,3)-1.5*log(3.)
assert abs(antithetic-formula_antithetic)<1e-9
assert abs(best-0.0018799202751994874)<1e-8
assert antithetic>9*best
print('VERIFY_OK: quantile inversion across 10 step sizes, 5 exhaustive exact six-cell couplings, r=2 optimum %.12f vs antithetic %.12f' %(best, antithetic))
