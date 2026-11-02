#!/usr/bin/env python3
"""Reproducible finite checks for flat quotient geodesic-distance formulas.
The proof in RESULT.md, rather than numerical tests, handles arbitrary dimensions.
"""
from fractions import Fraction
from math import log, sqrt
from random import Random


def analytic_gain_2d(a,b):
    if a<=0 or b<=0: raise ValueError('periods must be positive')
    c=2*b/a
    base=a**4/(360*b*b)
    if c>=1:return base
    z=sqrt(1-c*c)
    integral=(z*(8-26*c*c+33*c**4)-15*c**6*log((1+z)/c))/48
    return base-a**4/(60*b*b)*integral


def independent_quadrature_2d(a,b,N=30000):
    # Formula for the pair-sum correction with a new 1D integral.
    A=a/2; v=4*A**4/45
    if b>=A:return v/(2*b*b)
    step=(A-b)/N
    integ=sum(((b+(j+.5)*step)**2-b*b)**2.5 for j in range(N))*step
    correction=(8/(15*A*A))*integ
    return (v-correction)/(2*b*b)


def cutoff_gain_fraction(periods,b):
    periods=[Fraction(x) for x in periods]; b=Fraction(b)
    assert b*b >= sum((a/2)**2 for a in periods)
    return sum(a**4 for a in periods)/(360*b*b)


def experiment(periods,b,N=50000,seed=1947):
    r=Random(seed)
    p=list(map(float,periods)); b=float(b)
    differences=[]
    violation=0
    for _ in range(N):
        # Independently uniformly sampled quotient representatives; direct deck minima.
        x=[r.random()*a for a in p]; xp=[r.random()*a for a in p]
        y=r.random()*b; yp=r.random()*b
        t=abs(y-yp)
        h_even=sum((min((xx-zz)%a,(zz-xx)%a))**2 for xx,zz,a in zip(x,xp,p))
        h_odd=sum((min((xx+zz)%a,(-xx-zz)%a))**2 for xx,zz,a in zip(x,xp,p))
        dK2=min(h_even+t*t,h_odd+(b-t)**2)
        # Coupled torus squared-distance with preferred route (even or odd).
        dT2=(h_even if t<=b/2 else h_odd)+min(t,b-t)**2
        # This coupled torus distance has the right distribution by Haar invariance.
        gap=dT2-dK2
        if gap < -1e-10:violation+=1
        differences.append(gap)
    sample=sum(differences)/N
    err=(sum((x-sample)**2 for x in differences)/(N-1)/N)**.5
    return sample,err,violation


def main():
    assert cutoff_gain_fraction([1],1)==Fraction(1,360)
    assert cutoff_gain_fraction([1,2],2)==Fraction(17,1440)
    assert cutoff_gain_fraction([1,2,3],3)==Fraction(49,1620)
    print('EXACT_CUTOFF_RATIONAL_MOMENTS_PASSED')
    for a,b in [(1.,1.),(1.,.5),(1.,.4),(1.,.25),(4.,1.),(1.,.1),(1.,2.)]:
        v=analytic_gain_2d(a,b);q=independent_quadrature_2d(a,b)
        assert abs(v-q)<5e-8*max(1,v)
        assert v>0
    print('INDEPENDENT_QUADRATURE_AND_BRANCH_MATCH_PASSED')
    # Exact normalization for the square torus / square Klein pair.
    assert Fraction(1,6)-cutoff_gain_fraction([1],1)==Fraction(59,360)
    print('UNIT_SQUARE_EXACT_SECOND_MOMENT_PASSED')
    for periods,b in [([1],1),([4],1),([1,2],3),([1,2,3],4),([1],.1)]:
        sample,err,viol=experiment(periods,b)
        if b*b>=sum((a/2)**2 for a in periods):
            expected=float(cutoff_gain_fraction(periods,b))
        elif len(periods)==1:expected=analytic_gain_2d(periods[0],b)
        else:raise AssertionError('no exact reference for trial')
        assert viol==0
        assert abs(sample-expected)<7*err+2e-5,(periods,b,sample,expected,err)
    print('DIRECT_DECK_MINIMUM_AND_STOCHASTIC_COUPLING_PASSED')
    # The nonanalyticity exponent is obtained analytically from the boundary integral.
    k=2**3.5/7
    for h in [0.01,0.005,0.002]:
        Jind=sum((((1-h)+(j+.5)*h/30000)**2-(1-h)**2)**2.5 for j in range(30000))*h/30000
        ratio=Jind/h**3.5
        assert abs(ratio/k-1)<.05
    print('SEVEN_HALVES_CUTOFF_ASYMPTOTIC_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':main()
