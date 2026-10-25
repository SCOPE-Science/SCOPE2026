#!/usr/bin/env python3
"""Numerical constant checks for post-contact first intrinsic-volume metric.

Uses only Python's standard library. The proof is analytical; these checks
validate formulas for Euclidean balls in dimensions 2 and 3 and ellipses in 2D.
"""
import math


def simpson(f, low, high, n=30000):
    assert n % 2 == 0
    dx=(high-low)/n
    total=f(low)+f(high)
    for k in range(1,n):
        total += (4 if k%2 else 2)*f(low+k*dx)
    return total*dx/3


def deficit_ball_2d(eps, r):
    t=2*r+eps
    # Noncancelling integral on a small angular cap, derived from (2).
    alpha=math.acos(2*r/t)
    # Spherical normalization: F=2 integral_0^alpha (t cos theta-2r) dtheta.
    return 2*(t*math.sin(alpha)-2*r*alpha)


def deficit_ball_3d(eps, r):
    return 2*eps*eps/(2*r+eps)


def deficit_ellipse_2d(eps,a,b):
    # K={x^2/a^2+y^2/b^2<=1}, v=e1, D has semi-axes 2a,2b.
    t=2*a+eps
    alpha=math.atan(math.sqrt((t*t-4*a*a)/(4*b*b)))
    return 2*simpson(lambda th: t*math.cos(th)-2*math.sqrt(a*a*math.cos(th)**2 + b*b*math.sin(th)**2),0,alpha)


def verify():
    for r in (0.5,1.,2.):
        expected=4/(3*math.sqrt(r))
        for eps in (1.e-2*r,1.e-3*r):
            measured=deficit_ball_2d(eps,r)/eps**1.5
            assert abs(measured/expected-1)<0.005,(r,eps,measured,expected)
    for r in (0.5,1.,2.):
        for eps in (1.e-2*r,1.e-3*r):
            actual=deficit_ball_3d(eps,r)/eps**2
            assert abs(actual*r-1)<0.006,(r,eps,actual)
    for a,b in ((1.,1.),(2.,1.),(1.,2.),(3.,0.5)):
        eps=1.e-5*a
        coeff=4*math.sqrt(a)/(3*b)
        observed=deficit_ellipse_2d(eps,a,b)/eps**1.5
        assert abs(observed/coeff-1)<0.005,(a,b,observed,coeff)
    print('PASS: planar balls, three-dimensional balls, and anisotropic planar ellipses')
    print('Limits: numerical tests do not prove the arbitrary-dimensional theorem')

if __name__=='__main__':
    verify()
