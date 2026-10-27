#!/usr/bin/env python3
"""Numerical tests for the two-spectral-zero critical merger theorem.

Uses only the Python standard library. The analytic proof is in RESULT.md.
"""
import cmath
import math


def exact_expected_count(r, epsilon):
    c = math.cos(epsilon)
    delta = math.sqrt((1.0-r*r)/2.0)
    v = c + 1j*delta
    w = cmath.sqrt(v*v-r*r)
    assert w.real > 0
    return r*r/(1-r*r) + 1.0 - ((c+1j/(2*delta))/w).real


def angular_quadrature_count(r, epsilon, samples=16000):
    c = math.cos(epsilon)
    total = 0.0
    for j in range(samples):
        t = 2.0*math.pi*(j+0.5)/samples
        ct = math.cos(t)
        q = 4.0*(r*ct-c)**2 + 2.0*(1-r*r)
        qprime = 8.0*(r*ct-c)*ct-4.0*r
        total += qprime/q
    return r*r/(1-r*r) + r*total/(2.0*samples)


def limit_profile(lam):
    return 0.5*((lam*lam+2j)**(-0.5)).real


def exact_deficit(r, epsilon):
    c = math.cos(epsilon)
    delta = math.sqrt((1-r*r)/2.0)
    v = c+1j*delta
    return -1.0+((c+1j/(2*delta))/cmath.sqrt(v*v-r*r)).real


def run_checks():
    checks=0
    for epsilon in (0.0, 0.2, 0.6):
        for r in (0.45,0.65,0.85):
            actual=exact_expected_count(r,epsilon)
            independent=angular_quadrature_count(r,epsilon)
            assert abs(actual-independent)<1e-8, (r,epsilon,actual,independent)
            checks+=1
    optimal=math.sqrt(2.0/math.sqrt(3.0))
    assert abs(limit_profile(0.0)-0.25)<1e-13
    assert abs(limit_profile(optimal)-3**0.75/8)<1e-13
    assert limit_profile(0.0)<limit_profile(optimal)
    checks+=3
    for lam in (0.,0.5,1.,optimal,2.,3.):
        h=1e-7
        deficit=exact_deficit(1.0-h,lam*h**0.25)
        scaled=h**0.75*deficit
        assert abs(scaled-limit_profile(lam))<0.001,(lam,scaled,limit_profile(lam))
        checks+=1
    vals=[limit_profile(k*0.01) for k in range(401)]
    peak=max(range(len(vals)),key=lambda i: vals[i])*0.01
    assert abs(peak-optimal)<0.011
    checks+=1
    print(f'PASS {checks} deterministic quadrature, scaling, and profile checks')

if __name__=='__main__':
    run_checks()
