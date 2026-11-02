#!/usr/bin/env python3
"""Numerical checks for affine-Crofton sections of spherical latitude zones.

No external dependencies. Finite diagnostics corroborate the separate analytic proof.
"""
import math
import random

PI = math.pi


def law(a, b):
    if not (0 <= a <= 1 and 0 <= b <= 1 and a+b > 0):
        raise ValueError('Require 0<=a,b<=1 and a+b>0')
    f = math.acos
    g = lambda x: math.sqrt(max(0., 1.-x*x))
    H = lambda x: f(x)*g(x)
    p0 = 1.-(a+b)/2.-(H(a)+H(b))/4.
    p2 = (f(a)*g(b)+f(b)*g(a))/4.
    return (p0, 1.-p0-p2, p2)


def direct_counts(u, s, a, b):
    c = u*s
    r = math.sqrt(max(0., 1.-u*u))*math.sqrt(max(0., 1.-s*s))
    lo, hi = c-r, c+r
    if lo > b or hi < -a:
        return 0
    if lo < -a and hi > b:
        return 2
    return 1


def deterministic_grid(a, b, steps=560):
    counts = [0, 0, 0]
    # Midpoint integration directly on plane-normal height and signed offset.
    for i in range(steps):
        u = -1.+(2*i+1)/steps
        for j in range(steps):
            s = -1.+(2*j+1)/steps
            counts[direct_counts(u,s,a,b)] += 1
    return [x/(steps*steps) for x in counts]


def check():
    shapes = [(0.1, 0.1),(0.2, 0.7),(0.4, 0.4),(0.1, 0.9),
              (0.3, 0.8),(0.7, 0.95),(0., 0.6),(0.2, 1.),(1., 1.)]
    for a, b in shapes:
        target = law(a,b)
        counts = deterministic_grid(a,b,560)
        assert abs(sum(target)-1)<1.e-12
        assert min(target)>-1.e-12
        assert max(abs(x-y) for x,y in zip(target, counts)) < .004, (a,b,target,counts)
    print('INDEPENDENT_KINEMATIC_MIDPOINT_INTEGRALS_PASSED',len(shapes),'x',560*560)
    rng = random.Random(20261029)
    for a,b in [(0.13,0.47),(0.35,0.9),(0.01,0.99),(0.5,0.5)]:
        tally=[0,0,0]
        for _ in range(170000):
            tally[direct_counts(rng.uniform(-1,1),rng.uniform(-1,1),a,b)]+=1
        target=law(a,b)
        assert all(abs(t/170000-p)<.009 for t,p in zip(tally,target))
    print('INDEPENDENT_RAW_HAAR_AFFINE_PLANE_SIMULATIONS_PASSED',4,'x',170000)
    for h in (.05,.2,.49,.5,.51,.74,.95):
        offset=min(h,1-h)
        pcenter=law(h,h)
        assert pcenter[2] == max(pcenter[2],law(h-offset,h+offset)[2])
        assert pcenter[0] <= law(h-offset,h+offset)[0]+1.e-12
        for j in range(1,100):
            m=offset*j/100
            p=law(h-m,h+m)
            q=law(h-(m-offset/1000),h+(m-offset/1000))
            assert p[2] < q[2]+1.e-13, (h,m,p,q)
            assert p[0] > q[0]-1.e-13, (h,m,p,q)
        if h>=.5:
            assert abs(law(h-offset,h+offset)[2])<1.e-12
        else:
            assert law(h-offset,h+offset)[2]>0
    for h in (.05,.2,.5,.77,.99):
        assert abs(law(h,h)[1]-h)<1.e-12
        for frac in (.1,.3,.7,.99):
            m=frac*min(h,1-h)
            assert law(h-m,h+m)[1]>h
    print('RIGID_AREA_FRACTION_IDENTITY_AND_SHARP_SHAPE_ORDER_PASSED')
    print('FIXED_AREA_STRICT_SHAPE_ORDER_AND_HALF_AREA_THRESHOLD_DIAGNOSTICS_PASSED')
    for eps in (1.e-3,1.e-4,1.e-5):
        h=(1-eps)/2
        p=law(0,2*h)[2]
        predicted=(math.pi/2+1)*math.sqrt(2*eps)/4
        assert abs(p/predicted-1)<.025
    print('SHARP_ONE_SIDED_SQUARE_ROOT_ONSET_DIAGNOSTICS_PASSED')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    check()
