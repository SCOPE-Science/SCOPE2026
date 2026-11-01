#!/usr/bin/env python3
"""Deterministic numerical cross-checks for the octahedral conditional brightness law.

This verifies sampled instances only; the continuum result is proved analytically.
"""
from math import acos, cos, pi, sin, sqrt


def law(a):
    assert 1 / sqrt(3) < a < 1
    r = sqrt(1 - a*a)
    phi0 = 0.0 if a >= 1 / sqrt(2) else acos(a / r)
    q = pi/4 - phi0
    tmax = sqrt(2)*r
    cutoff = 0.0 if a >= sqrt(2/3) else min(q, acos(a/tmax))
    atom = 1 - cutoff/q
    min_area = 2*a if a >= 1 / sqrt(2) else 2*a+sqrt(1-2*a*a)
    max_area = 2*a if a >= sqrt(2/3) else a+tmax
    mean = 2*a + (tmax*sin(cutoff)-a*cutoff)/q
    return r,q,cutoff,atom,min_area,max_area,mean


def actual_brightness(a,b,c):
    return sum(abs(i*a+j*b+k*c) for i in (-1,1)
               for j in (-1,1) for k in (-1,1))/4


def verify():
    for a in (0.58,0.6,0.62,0.65,0.7,1/sqrt(2),0.75,0.79,0.81,0.83,0.91,0.97):
        r,q,cutoff,atom,amin,amax,mean = law(a)
        n = 30000
        total=0.0
        atomic=0
        for i in range(n):
            psi = q*(i+0.5)/n
            theta = pi/4-psi
            b,c = r*cos(theta),r*sin(theta)
            assert a>=b>=c>=0
            direct=actual_brightness(a,b,c)
            formula=2*a+max(0.0,sqrt(2)*r*cos(psi)-a)
            assert abs(direct-formula) < 4e-14, (a,i,direct,formula)
            assert amin-1e-12 <= direct <= amax+1e-12
            total+=direct
            atomic+=(abs(direct-2*a)<1e-13)
        assert abs(total/n-mean) < 2e-5, (a,total/n,mean)
        assert abs(atomic/n-atom)< 1.1/n, (a,atomic/n,atom)
        assert 0<=atom<=1+1e-12
    print('VERIFY_OK: 360000 azimuth/facet checks; conditional means and atom fractions match')

if __name__=='__main__':
    verify()
