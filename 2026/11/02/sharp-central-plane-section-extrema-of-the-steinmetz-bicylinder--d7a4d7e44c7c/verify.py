#!/usr/bin/env python3
"""Deterministic numerical cross-check of the central bicylinder section formula.

No external dependencies. This checks finite instances only; the theorem is proven
analytically in RESULT.md.
"""
import math
import random

PI = math.pi


def formula(n):
    length = math.sqrt(sum(x*x for x in n))
    a, b, c = sorted((abs(n[0]/length), abs(n[1]/length)), reverse=True) + [abs(n[2]/length)]
    if a < 1e-13:
        return 4.0
    if b < 1e-13:
        if c < 1e-13:
            return PI
        return 2.0/a * (math.atan2(a, c) + a*c/(a*a+c*c))
    if c < 1e-13:
        return PI/a
    return ((a+b)*math.atan2(a+b, c)-(a-b)*math.atan2(a-b, c))/(a*b)


def independent_radial_integral(n, samples=16384):
    length = math.sqrt(sum(x*x for x in n))
    x,y,z=(s/length for s in n)
    p=math.hypot(x,y)
    if p < 1e-13:
        e=(1.0,0.0,0.0)
        f=(0.0,1.0,0.0)
    else:
        e=(-y/p,x/p,0.0)
        f=(-z*x/p,-z*y/p,p)
    s=0.0
    for j in range(samples):
        theta=2.0*PI*(j+0.5)/samples
        co,si=math.cos(theta),math.sin(theta)
        dx=e[0]*co+f[0]*si
        dy=e[1]*co+f[1]*si
        dz=e[2]*co+f[2]*si
        radius_squared=1.0/max(dx*dx+dz*dz,dy*dy+dz*dz)
        s+=radius_squared
    return PI*s/samples


def g(k):
    return k*(k*k+4.0)*math.atan2(2.0,k)-2.0*(k*k+2.0)


def test():
    random.seed(211620)
    cases=[(1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,-1,0),
           (1,1,1),(0.1,0.8,0.4),(1,1,1.320136713376677),
           (0.00001,0.4,1),(1,0.00001,0.003)]
    cases += [(random.gauss(0,1), random.gauss(0,1), random.gauss(0,1)) for _ in range(144)]
    err=0
    lower=PI;upper=PI*math.sqrt(2)
    for i,n in enumerate(cases):
        expected=formula(n)
        measured=independent_radial_integral(n)
        d=abs(expected-measured)
        err=max(err,d)
        assert d < 1.4e-5, (i, n,expected,measured,d)
        assert lower-1e-12<=expected<=upper+1e-12,(i,n,expected)
    lo,hi=1.0,2.0
    for _ in range(65):
        mid=(lo+hi)/2
        if g(mid)<0: lo=mid
        else: hi=mid
    k=(lo+hi)/2
    area=2*math.sqrt(k*k+2)*math.atan2(2,k)
    assert abs(k-1.320136713376677)<2e-12
    assert abs(area-3.8203968413887655)<2e-12
    print('PASS: %d independent radial-vs-analytic section areas' % len(cases))
    print('max absolute quadrature discrepancy: %.12g'%err)
    print('sharp endpoints: pi=%.12g, pi sqrt(2)=%.12g'%(lower,upper))
    print('diagonal profile: unique stationary k=%.14g, area=%.14g'%(k,area))

if __name__=='__main__':
    test()
