#!/usr/bin/env python3
"""Reproduce exact Bernoulli order-statistic identities and Poisson limit."""
from fractions import Fraction
from itertools import product
from math import exp, log1p

def exact_squared_correlation(n, q):
    p = 1 - q
    a = p ** n
    b = a + n * q * p ** (n - 1)
    return a * (1-b) / (b * (1-a))

def exact_independent_enumeration(n, q):
    p = 1-q
    E0=E1=E01=Fraction(0)
    for zeros in product((0,1), repeat=n):
        k=sum(zeros)
        mass=q**k*p**(n-k)
        l=int(k==0); u=int(k<=1)
        E0+=mass*l; E1+=mass*u; E01+=mass*l*u
    return (E01-E0*E1)**2/(E0*(1-E0)*E1*(1-E1))

checks=0
for n in range(2,9):
    for q in (Fraction(1,7), Fraction(1,3), Fraction(2,5), Fraction(5,8)):
        assert exact_squared_correlation(n,q)==exact_independent_enumeration(n,q)
        checks+=1
print('exact independent finite enumeration checks:',checks)

def f(c):
    e=exp(c)
    return (e-1-c)/((1+c)*(e-1))

def h(c):
    return 1+c+c*c-exp(c)
lo,hi=1.0,3.0
assert h(lo)>0>h(hi)
for _ in range(70):
    mid=(lo+hi)/2
    if h(mid)>0:lo=mid
    else:hi=mid
c=(lo+hi)/2
limit=f(c)
print('positive root:',format(c,'.13f'))
print('limiting squared correlation:',format(limit,'.13f'))
print('limiting correlation:',format(limit**.5,'.13f'))
for n in (20,100,1000,10000):
    q=c/n
    actual=float(exact_squared_correlation(n,q))
    print('n',n,'squared correlation at q=c/n:',format(actual,'.11f'))
    assert abs(actual-limit)<5/n
print('all verifier checks passed')
