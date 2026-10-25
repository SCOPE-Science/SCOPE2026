#!/usr/bin/env python3
"""Reproduce numeric and structural checks for a Poisson-abundance survey covariance theorem.

This checks finite values and derivative signs; it is not a proof of global uniqueness.
Python 3.9+ standard library only.
"""
import math
import random
from fractions import Fraction

def covariance(lam, q):
    if not lam > 0 or not 0 <= q <= 1:
        raise ValueError('lambda>0 and q in [0,1] required')
    return math.exp(-lam * (2*q-q*q)) * (-math.expm1(-lam*q*q))

def ratio(q):
    if not 0 < q < 1:
        raise ValueError('q must be interior')
    return -math.log1p(-q)/q**2

def aux(q):
    return q/(1-q)+2*math.log1p(-q)

def derivative(lam,q):
    return 2*lam*math.exp(-lam*(2*q-q*q))*(math.exp(-lam*q*q)-(1-q))

def bisect(f, left, right, iters=95):
    a,b=left,right
    fa=f(a)
    fb=f(b)
    assert fa*fb<0, (a,b,fa,fb)
    for _ in range(iters):
        c=(a+b)/2
        if c==a or c==b:
            break
        fc=f(c)
        if fc==0: return c
        if fa*fc<0:
            b=c;fb=fc
        else:
            a=c;fa=fc
    return (a+b)/2

qturn=bisect(aux,0.5,0.75)
lamturn=ratio(qturn)
assert 0.71533186<qturn<0.71533187
assert 2.45540748<lamturn<2.45540749

def qsmall(lam):
    assert lam > lamturn
    return bisect(lambda q: ratio(q)-lam, min(1e-12,1/(lam*lam)), qturn)

def qlarge(lam):
    assert lam > lamturn
    return bisect(lambda q: ratio(q)-lam, qturn,1-1e-12)

def gap(lam):
    return covariance(lam,qsmall(lam))-covariance(lam,1)

lamglobal=bisect(gap,2.5,3.0)
qglobal=qsmall(lamglobal)
assert 2.61022714<lamglobal<2.61022716
assert 0.56370836<qglobal<0.56370839
assert abs(gap(lamglobal))<1e-14

# Exact inequality proving high-abundance interior improvement at lambda=3,
# q=1/2: exp(3/4) > 1+3/4+(3/4)^2/2 = 65/32 > 2.
assert Fraction(1,1)+Fraction(3,4)+Fraction(3,4)**2/Fraction(2,1)==Fraction(65,32)
assert covariance(3,0.5)>covariance(3,1)

rng=random.Random(20261023)
for trial in range(3000):
    lam=0.1+10*rng.random()
    q=0.0001+0.9998*rng.random()
    deriv=derivative(lam,q)
    sign=ratio(q)-lam
    if abs(sign)>1e-7:
        assert deriv*sign>0, (lam,q,deriv,sign)
    # Differentiation verified independently by central finite differences.
    h=1e-5*min(q,1-q,0.5)
    finite=(covariance(lam,q+h)-covariance(lam,q-h))/(2*h)
    assert abs(finite-deriv)<1e-5

for lam in [0.1,1,2,lamturn,2.5,lamglobal,3,6,12,40]:
    points=[j/1000 for j in range(1001)]
    vals=[covariance(lam,q) for q in points]
    best=max(vals)
    actual=covariance(lam,1) if lam<=lamglobal else covariance(lam,qsmall(lam))
    assert abs(best-actual)<0.0002, (lam,best,actual)

for lam in [100,1000,10000]:
    q=qsmall(lam)
    assert abs(lam*q-1)<0.03
    assert abs(lam*covariance(lam,q)/math.exp(-2)-1)<0.03

# Poisson finite-sum check of Bernoulli visit correlation.
for lam,q in [(0.3,0.27),(1.5,0.61),(3,0.5),(5,0.9)]:
    prob=math.exp(-lam)
    e1=0.0
    e2=0.0
    for n in range(120):
        p=1-(1-q)**n
        e1+=prob*p
        e2+=prob*p*p
        prob=prob*lam/(n+1)
    assert abs(e2-e1*e1-covariance(lam,q))<1e-12

print('ALL CHECKS PASSED')
print(f'local-extrema onset q={qturn:.12f}, lambda={lamturn:.12f}')
print(f'global-max crossover lambda={lamglobal:.12f}, interior optimum q={qglobal:.12f}')
print(f'lambda=3: covariance(q=1/2)={covariance(3,.5):.12f}; covariance(q=1)={covariance(3,1):.12f}')
