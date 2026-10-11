#!/usr/bin/env python3
"""Reproducible numerical consistency checks for a rank-one Cesaro perturbation.

This checks resolvent representations, endpoint constants, and a local
bifurcation. It is NOT a substitute for the analytic infinite-dimensional proof.
Uses only the Python standard library.
"""
from math import cosh, exp, expm1, pi
from fractions import Fraction


def simpson(fun, a, b, n=24000):
    assert n % 2 == 0
    h = (b-a)/n
    total = fun(a)+fun(b)
    for k in range(1,n):
        total += (4 if k % 2 else 2)*fun(a+k*h)
    return total*h/3


def q(t):
    if t == 0:
        return 1.0
    return t/expm1(t)


def qprime(t):
    if abs(t) < 0.002:
        return -.5 + t/6 - t**3/180 + t**5/5040
    y=exp(-t)
    return y*(1-y-t)/(1-y)**2


def resolvent_scalar(lam):
    """Spectral-measure integral in the established multiplication picture."""
    def integrand(s):
        z=1/complex(.5,-s)
        return (pi/(2*cosh(pi*s)**2)/(lam-z)).real
    return simpson(integrand, -7.,7., 24000)


def g(lam):
    assert lam not in (0., 2.)
    if lam < 0:
        x=-1/lam
        return simpson(lambda u: exp(-u)*qprime(u/x), 0.,42.)
    if lam < 2:
        x=1/lam
        return -simpson(lambda u: exp(-u)*(1+qprime(u/x)),0.,42.)
    w=1/lam
    return w + w*w*simpson(lambda t: exp(w*t)*q(t),0.,85.)


def main():
    assert Fraction(1,1)+(-2)*Fraction(1,2)==0
    assert Fraction(1,1)+(-2)*Fraction(1,2)==0
    for lam in [-10.,-1.,-.1,.1,.5,1.,1.8,1.99,2.01,2.5,3.,10.]:
        lhs=resolvent_scalar(lam)
        rhs=g(lam)
        assert abs(lhs-rhs)<3e-6,(lam,lhs,rhs)
    assert abs(g(1.)-(1-pi*pi/6))<2e-9
    assert abs((.5+pi*pi/8)-(4+pi*pi)/8)<1e-14
    assert abs((.5-pi*pi/8)-(-(pi*pi-4)/8))<1e-14
    assert 0 < 8/(4+pi*pi) < 1
    assert -2 < -8/(pi*pi-4) < -1
    for ls in [[-10.,-5.,-1.,-.5,-.1],[.1,.5,1.,1.5,1.9],[2.01,2.1,3.,5.,10.]]:
        vals=[g(v) for v in ls]
        assert all(a>b for a,b in zip(vals,vals[1:])),(ls,vals)
    # For tau=-2+epsilon the real eigenvalue has slope 3/2.
    for eps in [0.001,-0.001]:
        tau=-2+eps
        target=1/tau
        lo,hi=(1e-6,.02) if eps>0 else (-.02,-1e-6)
        for _ in range(35):
            mid=(lo+hi)/2
            if g(mid)>target:
                lo=mid
            else:
                hi=mid
        lam=(lo+hi)/2
        assert abs(lam/eps-1.5)<.03,(eps,lam)
    print('RANK_ONE_REAL_CESARO_BIFURCATION_NUMERICAL_CHECKS_OK')


if __name__=='__main__':
    main()
