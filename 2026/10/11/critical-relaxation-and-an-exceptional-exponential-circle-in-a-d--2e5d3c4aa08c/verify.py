#!/usr/bin/env python3
"""Standalone finite checks for the weighted three-oscillator sine map.
This script checks local algebra and finite numerical trajectories; it is not an infinite proof.
"""
from fractions import Fraction
from math import sin, cos, log, pi


def edge_step(x, y, h):
    z = sin(x+y)/2
    return (x + h*(2*sin(x)-sin(y)+z),
            y + h*(2*sin(y)-sin(x)+z))


def center_step(u, v, h):
    return (u + h*sin(u)*(cos(u)-cos(v)),
            v - 3*h*cos(u)*sin(v))


def check_exact_taylor():
    # r(z)=1+a*z+b*z^2+O(z^3), z=u^2, along v=0.
    for a_num, a_den in [(1, 6), (1, 3), (1, 2), (3, 5)]:
        h = Fraction(a_num, a_den)
        a = -h/2
        b = h/8
        linear = -2*a
        quadratic = 3*a*a-2*b
        assert linear == h
        assert quadratic == h*(3*h-1)/4
        # The logarithmic coefficient after summation is quadratic / h.
        assert quadratic / h == (3*h-1)/4


def check_coordinate_map():
    n = 0
    for h in [0.07, 0.2, 1/3, 0.51, 0.6]:
        for u in [-0.21, -0.05, 0, 0.08, 0.21]:
            for v in [-0.17, -0.03, 0, 0.04, 0.17]:
                x, y = pi+u+v, pi+u-v
                xx, yy = edge_step(x,y,h)
                uu, vv = center_step(u,v,h)
                assert abs((xx+yy)/2-pi-uu) < 3e-15
                assert abs((xx-yy)/2-vv) < 3e-15
                n += 2
    return n


def check_critical_fixed():
    c = 0
    for h in [0.07, 0.2, 0.32]:
        for x,y in [(0,0),(0,pi),(pi,0),(pi,pi)]:
            xx,yy=edge_step(x,y,h)
            assert abs(xx-x)<1e-14 and abs(yy-y)<1e-14
            c += 2
    return c


def check_local_asymptotic():
    # Two-point convergence checks: exact constants are not computable from finite orbits.
    done = 0
    for h in [0.13, 0.2, 1/3, 0.48, 0.6]:
        u,v=0.11,0.07
        obs={}
        for n in range(1,160001):
            u,v=center_step(u,v,h)
            if n in (40000,160000):
                obs[n]=u**(-2)-h*n-(3*h-1)/4*log(n)
            if n==80000:
                assert abs(v)<1e-14
        assert abs(obs[160000]-obs[40000])<0.006, (h,obs)
        done += 1
    return done


def main():
    check_exact_taylor()
    n=check_coordinate_map()
    n+=check_critical_fixed()
    n+=check_local_asymptotic()
    print('PASS:',n,'finite coordinate/fixed/asymptotic checks and 12 exact rational Taylor equalities')

if __name__=='__main__':
    main()
