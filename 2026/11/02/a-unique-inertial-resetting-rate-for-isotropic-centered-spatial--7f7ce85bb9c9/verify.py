#!/usr/bin/env python3
"""Independent stationary-moment and threshold checks for a resetting inertial ABP.

Uses only Python's standard library. All algebraic identities are tested with
exact rational arithmetic; numerical root checks are consistency tests, not
proofs of uniqueness or asymptotic limits.
"""
from fractions import Fraction as F
from math import sqrt


def closed_mean(r, g, d, speed):
    return speed * g / ((r + d) * (r + g))


def polynomial(r, g, d):
    return 5*r**3 + (5*d + 7*g)*r*r + 2*g*g*r - 4*d*g*(d+g)


def closed_q(r, g, d, speed):
    return (speed**2 * g*g * polynomial(r,g,d)
            / ((r+d)**2*(r+4*d)*(r+g)**2*(r+2*g)*(r+d+g)))


def closed_raw_complex_second(r, g, d, speed):
    return (2*g*g*speed**2*(3*r+2*d+2*g)
            / ((r+d)*(r+4*d)*(r+g)*(r+2*g)*(r+d+g)))


def recurrence_complex_moments(r, g, d, speed):
    # Independently solve the stationary generator's upper-triangular moment system.
    mean_n = r / (r+d)
    mean_n2 = r / (r+4*d)
    mean_u = g*speed*mean_n/(r+g)
    mean_z = mean_u/r
    mean_u_n = g*speed*mean_n2/(r+g+d)
    mean_u2 = 2*g*speed*mean_u_n/(r+2*g)
    mean_z_n = mean_u_n/(r+d)
    mean_z_u = (mean_u2 + g*speed*mean_z_n)/(r+g)
    mean_z2 = 2*mean_z_u/r
    return mean_z,mean_z2,mean_z2-mean_z**2


def trace_by_generator(r,g,d,speed,kappa):
    # Isotropic thermal velocity diffusion contributes 4*kappa to E|U|^2.
    mean_n = r/(r+d)
    mean_u = g*speed*mean_n/(r+g)
    mean_z = mean_u/r
    mean_ubar_n = g*speed/(r+g+d)
    mean_uabs2 = (2*g*speed*mean_ubar_n+4*kappa)/(r+2*g)
    mean_zbar_n = mean_ubar_n/(r+d)
    mean_zbar_u = (mean_uabs2+g*speed*mean_zbar_n)/(r+g)
    mean_zabs2 = 2*mean_zbar_u/r
    return mean_zabs2 - mean_z**2


def trace_closed(r,g,d,speed,kappa):
    active = (2*g*g*speed**2*(2*d+2*g+3*r)
              / (r*(r+d)*(r+g)*(r+2*g)*(r+d+g)))
    passive = 8*kappa/(r*(r+g)*(r+2*g))
    return active+passive - closed_mean(r,g,d,speed)**2


def zero_by_bisection(g,d):
    lo,hi = 0.0,2*d
    for _ in range(100):
        mid=(lo+hi)/2
        if polynomial(mid,g,d)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2


def run():
    checked = 0
    rates=[F(1,8),F(3,4),F(7,5),F(17,3)]
    damping=[F(1,7),F(1,2),F(3),F(20)]
    rotations=[F(1,3),F(1),F(5,2)]
    for r in rates:
        for g in damping:
            for d in rotations:
                v=F(7,3)
                m,s,q=recurrence_complex_moments(r,g,d,v)
                assert m==closed_mean(r,g,d,v); checked+=1
                assert s==closed_raw_complex_second(r,g,d,v); checked+=1
                assert q==closed_q(r,g,d,v); checked+=1
                assert q==s-m*m; checked+=1
                for kappa in (F(0),F(3,11)):
                    assert trace_by_generator(r,g,d,v,kappa)==trace_closed(r,g,d,v,kappa)
                    checked+=1
                # The centered covariance eigenvalues (trace +/- anisotropy)/2 must be nonnegative.
                for kappa in (F(0),F(3,11)):
                    t=trace_closed(r,g,d,v,kappa)
                    assert t+q>0 and t-q>0
                    checked+=2
                # Polarity of anisotropy follows the cubic exactly.
                assert (q>0)==(polynomial(r,g,d)>0); checked+=1
    prev = 0.0
    for g in (0.0001,0.001,0.01,0.1,1,10,100,10000):
        c=zero_by_bisection(g,1.0)
        assert 0<c<2 and c>prev
        prev=c
        assert abs(polynomial(c,g,1.0))<1e-5*max(1,g*g)
        checked+=2
    # Verify the predicted asymptotic scales, without treating them as proofs.
    slow=zero_by_bisection(1e-8,1.0)
    fast=zero_by_bisection(1e6,1.0)
    assert abs(slow/(2/sqrt(5)*sqrt(1e-8))-1)<0.001; checked+=1
    assert abs((2-fast)/(12/1e6)-1)<0.0001; checked+=1
    # For finite damping the overdamped threshold is not the root.
    for g in (0.2,1.,5.,50.):
        assert polynomial(2.,g,1.)>0 and zero_by_bisection(g,1.)<2
        checked+=1
    print(f"PASS: {checked} exact-rational and numerical consistency checks")


if __name__=='__main__':
    run()
