#!/usr/bin/env python3
"""Standalone exact-coefficient and numerical corroboration; no external dependencies."""
from fractions import Fraction as Q
import math

def derivative6(n,t):
    return ((16*n**3+48*n**2+32*n+9)*t**3
            -(36*n**2+72*n+27)*t*t+(36*n+27)*t-9)

def root(n):
    lo,hi=0.,1.
    for _ in range(140):
        md=(lo+hi)/2
        if derivative6(n,md)>0:hi=md
        else:lo=md
    return (lo+hi)/2

def direct(n,t):
    s=(1-t)/2
    r=[s]+[-t]*n+[s]
    corr=[sum(r[j]*r[j+d] for j in range(len(r)-d)) for d in range(len(r))]
    return corr[0]**2+2*sum(x*x for x in corr[1:]),corr

def closed(n,t):
    s=(1-t)/2
    return 6*s**4+12*n*s*s*t*t-4*n*(n-1)*s*t**3+n*(2*n*n+1)*t**4/3

nchecks=0
for n in [1,2,3,4,5,10,20,50,100,1000]:
    t=root(n)
    assert 0<t<1
    assert abs(derivative6(n,t))<1e-7*(1+n)
    for trial in [0., .1, .25, t, .5, 1.]:
        value,corr=direct(n,trial)
        assert abs(value-closed(n,trial))<1e-7*(1+abs(value))
        ss=(1-trial)/2
        assert abs(corr[0]-(2*ss*ss+n*trial*trial))<1e-10
        assert abs(corr[-1]-ss*ss)<1e-10
        nchecks+=3
    for h in [-0.0005,-0.0001,0.0001,0.0005]:
        assert closed(n,t+h)>closed(n,t)-1e-11
        nchecks+=1
assert abs(1000*root(1000)-0.357498368378205)<0.0002
nchecks+=1
print('PASS:',nchecks,'deterministic assertions; exact formula and sharp root limits corroborated.')
