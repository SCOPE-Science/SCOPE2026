#!/usr/bin/env python3
"""Reproduce numerical checks of a flat Möbius band's intrinsic eccentricity and diameter.

Requires Python 3 standard library only. Analytical proof is in RESULT.md.
"""
import math
import random


def sqdist(L,u,t,v):
    return min(t*t+(u-v)**2, (L-t)**2+(u+v)**2)


def eccentricity(L,w,u):
    assert L>0 and w>0 and -1e-14<=u<=w+1e-14
    if u*w<=L*L/4:
        return math.sqrt(L*L/4+w*w+u*u+4*u*u*w*w/(L*L))
    return max(u+L*L/(4*u),math.hypot(L,w-u))


def diam(L,w):
    r=2*w/L
    return L*(1+r*r)/(2*max(1,r))


def off_center(L,w):
    return (w+math.sqrt(w*w+2*L*L))/4


def radius(L,w):
    core=math.hypot(L/2,w)
    wcrit=7*math.sqrt(15)*L/30
    if w<=wcrit:
        return core
    return (3*math.sqrt(w*w+2*L*L)-w)/4


def farthest_witness(L,w,u):
    if u*w<=L*L/4:
        return (L/2+2*u*w/L, w)
    a=u+L*L/(4*u)
    b=math.hypot(L,w-u)
    if a>=b:
        return (0.0,-L*L/(4*u))
    return (0.0,-w)


def self_check():
    rng=random.Random(220731)
    n=0
    worst=0
    for L in (.3,1.0,2.6):
        for ratio in (.02,.1,.4,.5,.51,.73,.9,7*math.sqrt(15)/30-.00001,
                      7*math.sqrt(15)/30+.00001,1,3,10):
            w=L*ratio
            for k in range(51):
                u=w*k/50
                e=eccentricity(L,w,u)
                t,v=farthest_witness(L,w,u)
                assert -1e-13<=t<=L+1e-13 and -w-1e-13<=v<=w+1e-13
                witness=math.sqrt(sqdist(L,u,t,v))
                assert math.isclose(e,witness,rel_tol=3e-13,abs_tol=1e-12),(L,w,u,e,witness)
                for j in range(45):
                    x=rng.random()*L
                    y=(2*rng.random()-1)*w
                    sample=math.sqrt(sqdist(L,u,x,y))
                    worst=max(worst,max(0,sample-e))
                    assert sample<=e+1e-11
                    n+=1
            D=diam(L,w)
            samples=[eccentricity(L,w,w*k/2000) for k in range(2001)]
            assert all(v<=D+2e-12 for v in samples)
            assert math.isclose(max(samples),D,rel_tol=2e-12,abs_tol=1e-12)
            u0=0.0
            ustar=off_center(L,w)
            if w<7*math.sqrt(15)*L/30:
                assert math.isclose(radius(L,w),eccentricity(L,w,0),rel_tol=2e-12)
            else:
                assert math.isclose(radius(L,w),eccentricity(L,w,ustar),rel_tol=2e-12)
            assert all(v>=radius(L,w)-2e-12 for v in samples)
    for i in range(10000):
        r=10**rng.uniform(-3,3)
        g=lambda x:(1+x*x)**2/(4*x*max(1,x)**2)
        assert math.isclose(g(r),g(1/r),rel_tol=4e-13)
        assert g(r)>=4*math.sqrt(3)/9-1e-13
    for r in (1/math.sqrt(3),math.sqrt(3)):
        g=(1+r*r)**2/(4*r*max(1,r)**2)
        assert math.isclose(g,4*math.sqrt(3)/9,rel_tol=1e-14)
    print('PASS:',n,'random point distances bounded by exact eccentricities;',
          1836,'analytical farthest-point witnesses;',
          36,'diameter/radius cross-sections;',
          10000,'dual isodiametric checks. Largest sampled overshoot',worst)

if __name__=='__main__':
    self_check()
