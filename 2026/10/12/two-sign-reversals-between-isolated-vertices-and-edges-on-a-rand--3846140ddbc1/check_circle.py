#!/usr/bin/env python3
"""Finite precision checks for isolated-vertex / edge-count dependence on a circle."""
from fractions import Fraction
from math import isclose, sqrt
import numpy as np

def analytic(n,r):
    r=Fraction(r); ell=1-2*r
    if n < 2 or not (0 < r < Fraction(1,2)):
        return Fraction(0)
    qc=2*r/ell-(r/ell)**2 if r<=ell else Fraction(1)
    return n*(n-1)*ell**(n-1)*(Fraction(n-2,2)*(qc-2*r)-2*r)

def roots(n):
    assert n>=6
    return ((3*n+10)-sqrt(9*n*n-68*n+100))/(16*n), (n-2)/(2*n)

def check_exact():
    tests=0
    for n in range(2,81):
        for d in range(3,72):
            r=Fraction(1,d) if d>2 else Fraction(1,3)
            a=analytic(n,r)
            ell=1-2*r
            if r<=ell:
                b=Fraction(n*(n-1),2)*ell**(n-3)*r*(-4+(3*n+10)*r-8*n*r*r)
            else:
                b=Fraction(n*(n-1),2)*ell**(n-1)*((n-2)*ell-4*r)
            assert a==b,(n,r,a,b)
            tests+=1
    for n in range(2,101):
        for j in range(1,100):
            r=Fraction(j,200)
            c=analytic(n,r)
            if n<=5: assert c<0
            else:
                lo,hi=roots(n)
                if float(r)<lo-1e-11 or float(r)>hi+1e-11: assert c<0 or c==0
                if lo+1e-11 <float(r)<hi-1e-11: assert c>0
            tests+=1
    assert analytic(6,Fraction(1,4))==0
    assert analytic(6,Fraction(1,3))==0
    assert analytic(10,Fraction(2,5))==0
    return tests

def check_simulation():
    rng=np.random.default_rng(271828)
    result=[]
    for n,r,m in [(6,.10,220000),(6,.30,220000),(6,.40,220000),(9,.25,220000),(9,.40,220000)]:
        x=rng.random((m,n))
        e=np.zeros(m,dtype=np.float64)
        iso=np.ones((m,n),dtype=bool)
        for i in range(n):
            for j in range(i+1,n):
                d=np.abs(x[:,i]-x[:,j]); adj=np.minimum(d,1-d)<r
                e+=adj
                iso[:,i]&=~adj;iso[:,j]&=~adj
        z=iso.sum(axis=1)
        est=(z*e).mean()-z.mean()*e.mean()
        theory=float(analytic(n,Fraction(str(r))))
        # Conservative small absolute tolerance appropriate for dependent sample means.
        assert abs(est-theory)<.028,(n,r,est,theory)
        result.append((n,r,m,est,theory))
    return result

if __name__=='__main__':
    print('EXACT_TESTS',check_exact())
    for item in check_simulation(): print('SIMULATION',*item)
    print('ALL_CHECKS_PASS')
