#!/usr/bin/env python3
"""Standalone reproducibility checks for two overdamped Langevin SRK integrators.
Uses only the Python standard library; checks are not substituted for proof.
"""
import math
import random
from fractions import Fraction as F


def polynomial(x):
    return 1 - x + x*x/2


def qpoly(x):
    return 1 - x + x*x/3


def invariant_ratio(x):
    p=polynomial(x)
    return 2*x*qpoly(x)/(1-p*p)


def avg_factor(x):
    return qpoly(x)/(1-x/2)**2


def srk1(z, lam, h, db, j):
    stage=z-3*h*lam*z/4+3*math.sqrt(2)*j/(2*h)
    return z-h*lam*z/3-2*h*lam*stage/3+math.sqrt(2)*db


def srk2(z, lam, h, db, j):
    a=z-h*lam*z/2 + math.sqrt(2)*(1+1/math.sqrt(2))*j/h
    b=z-h*lam*z/2 + math.sqrt(2)*(1-1/math.sqrt(2))*j/h
    return z-h*lam*(a+b)/2+math.sqrt(2)*db


def reduced(z, lam, h, db, j):
    x=h*lam
    return polynomial(x)*z + math.sqrt(2)*(db-lam*j)


def run():
    checks=0
    xs=[F(1,100),F(1,3),F(1,2),F(1,1),F(4,3),F(3,2),F(7,4),F(199,100)]
    for x in xs:
        p=polynomial(x); q=qpoly(x)
        assert 0<p<1 and q>0; checks+=1
        assert 12*((1-p*p)-2*x*q)==x**3*(4-3*x); checks+=1
        assert invariant_ratio(x)-1 == x*x*(3*x-4)/(3*(2-x)*(x*x-2*x+4)); checks+=1
        assert avg_factor(x)-1 == x*x/(3*(2-x)**2); checks+=1
        assert (avg_factor(x)>1); checks+=1
        assert (invariant_ratio(x)>1)==(x>F(4,3)) if x!=F(4,3) else invariant_ratio(x)==1;checks+=1
    assert polynomial(F(4,3))==F(5,9); checks+=1
    assert avg_factor(F(4,3))==F(7,3); checks+=1
    assert invariant_ratio(F(4,3))==1; checks+=1
    for num in range(1,400):
        x=F(num,200)
        if x>=2: continue
        assert (0<polynomial(x)<1)
        assert avg_factor(x)>1
        checks+=2
    rng=random.Random(20261025)
    for i in range(5000):
        lam=math.exp(rng.uniform(-2,2));h=rng.uniform(0.0005,1.9)/lam
        z=rng.gauss(0,2);db=rng.gauss(0,math.sqrt(h));j=h*db/2+h**1.5*rng.gauss(0,1)/math.sqrt(12)
        val=reduced(z,lam,h,db,j)
        assert math.isclose(srk1(z,lam,h,db,j),val,rel_tol=3e-13,abs_tol=4e-13)
        assert math.isclose(srk2(z,lam,h,db,j),val,rel_tol=3e-13,abs_tol=4e-13)
        checks+=2
    # Independent covariance construction from correlated Brownian increments.
    for k in range(1,199):
        lam=F(k,100);h=F(2,3)
        var=2*(h-lam*h*h+lam*lam*h**3/3)
        assert var==2*h*qpoly(h*lam);checks+=1
    # Compare exact AR covariance series at finite N to large-N formula,
    # avoiding a Monte Carlo claim for a deterministic equality.
    for x in [0.13,0.5,1.0,1.3333333333333333,1.8]:
        p=polynomial(x);h=x;lam=1
        v=2*h*qpoly(x)/(1-p*p)
        n=60000
        series=v*(n+2*sum((n-j)*p**j for j in range(1,300)))*h/n
        predicted=2*avg_factor(x)
        assert abs(series-predicted) < 0.007
        checks+=1
    print('PASS',checks,'algebraic/deterministic checks')
    return checks

if __name__=='__main__':
    run()
