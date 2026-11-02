#!/usr/bin/env python3
"""Supplementary exact and numerical tests for a Bergman-kernel Cesaro family."""
from fractions import Fraction
from math import gamma,log,exp,sqrt,lgamma

def harmonic(n): return sum((Fraction(1,j) for j in range(1,n+1)),Fraction(0))

def exact_s2(n):
    q=Fraction(1,(n+1)*(n+2))
    S=sum((j+1)**2 for j in range(n+1))
    return q*q*S

for n in range(0,200):
    assert exact_s2(n)==Fraction(2*n+3,6*(n+1)*(n+2))
    assert sum((exact_s2(j) for j in range(n+1)),Fraction(0))==(harmonic(n+1)+harmonic(n+2)-1)/6
print('EXACT_ROWS_OK 200')

# Midpoint integration in logarithmic boundary coordinate y=-log(1-t).
# Only supplementary finite numerical checks, not a proof of asymptotics.
def moment(n,s,h,dy=0.006,cutoff=30.0):
    a=0.0
    N=int(cutoff/dy)
    for j in range(N):
        y=(j+.5)*dy
        logterm = 0.0 if n==0 else n*log(-__import__('math').expm1(-y))
        a+=exp(logterm-s*y)*((1+y)**(-h))
    return a*dy

for s in (2.0,2.5,4.0):
    for n in (0,1,3,11,50,200):
        mu=moment(n,s,0.0)
        exact=exp(lgamma(n+1)+lgamma(s)-lgamma(n+s+1))
        assert abs(mu-exact)<8e-6*max(1,exact),(s,n,mu,exact)
print('BETA_MOMENTS_OK 18')

for s,g in ((2.0,.25),(2.0,.75),(3.0,.5)):
    b=1.0; S=0.0
    for n in range(0,601):
        if n: b *= (s+n-1)/n
        S += b*b
        if n in (100,300,600):
            m=moment(n,s,g)
            empirical=m*m*S*n*log(n)**(2*g)
            expected=1/(2*s-1)
            assert abs(empirical/expected-1)<.35,(s,g,n,empirical,expected)
print('LOG_ROW_SCALE_OK 9')
print('ALL_CHECKS_OK')
