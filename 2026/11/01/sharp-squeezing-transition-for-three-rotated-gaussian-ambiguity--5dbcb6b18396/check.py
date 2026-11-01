#!/usr/bin/env python3
"""Finite diagnostics for the three-rotated-Gaussian ambiguity formula.

The analytical argument, not these sampled tests, proves the global assertion.
"""
import math
from scipy.optimize import minimize_scalar, brentq


def ambiguity_sum(tau, a, theta):
    angles = (0.0, math.pi/3, 2*math.pi/3)
    return sum(math.exp(-tau*(a*math.cos(theta-p)**2 + math.sin(theta-p)**2/a)) for p in angles)


def closed_min(tau, a):
    u = (a+1/a)/2
    v = (a-1/a)/2
    y = tau*v
    return math.exp(-tau*u) * (math.exp(-y) + 2*math.exp(y/2))


def h(y):
    w = math.exp(-1.5*y)
    return (1-w)/(2+w)


def transition(y):
    return y*math.sqrt(1-h(y)**2)/h(y)


def optimal_a(tau):
    if tau <= 2:
        return 1.0
    y = brentq(lambda z: transition(z)-tau,1.e-9, max(3*tau,10),xtol=1.e-13)
    return math.hypot(1.,y/tau)+y/tau


def run():
    checks=0
    for tau in (0.2,0.8,1.5,2.,2.01,2.3,3.,5.,12.):
        for a in (1.,1.05,1.3,1.7,2.,3.,7.):
            m=closed_min(tau,a)
            # Angle zero is an exact analytic minimizer for a>1.
            assert math.isclose(ambiguity_sum(tau,a,0),m,rel_tol=2.e-14,abs_tol=1.e-14)
            checks+=1
            for k in range(121):
                theta=math.pi*k/120
                assert ambiguity_sum(tau,a,theta) >= m-3.e-13
                checks+=1
    for tau in (0.3,1,1.9,2,2.02,2.4,3,5,10,30):
        a=optimal_a(tau)
        m=closed_min(tau,a)
        assert a >= 1
        checks+=1
        if tau <= 2:
            assert a == 1.
        else:
            assert a>1.
            # Check optimality against neighboring and coarse alternative squeezes.
            for factor in (0.85,0.95,0.999,1.001,1.05,1.2):
                b= max(1,a*factor)
                assert closed_min(tau,b)<=m+1.e-13
                checks+=1
        for b in (1.,1.01,1.1,1.3,1.5,2.,3.,5.,10.):
            assert closed_min(tau,b)<=m+1.e-12
            checks+=1
    prev=2.
    for k in range(1,1001):
        y=.01*k
        now=transition(y)
        assert now>prev
        prev=now
        checks+=1
    assert abs(optimal_a(1000)-math.sqrt(3))<1.e-6
    checks+=1
    print('Passed',checks,'finite assertions')

if __name__=='__main__':run()
