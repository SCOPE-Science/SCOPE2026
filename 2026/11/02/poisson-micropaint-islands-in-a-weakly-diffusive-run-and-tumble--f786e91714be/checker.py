#!/usr/bin/env python3
"""Numerical cross-checks for a two-state diffusion's first-passage paint field.

Requires only Python 3 standard library. Numerical checks support the analytic proof;
they are not substitutes for its infinite-dimensional or weak-limit arguments.
"""
import math
import random


def rates(diffusivity, speed, flip_rate):
    root = math.sqrt(speed*speed + 2.0*diffusivity*flip_rate)
    return flip_rate/(root + speed), (root + speed)/(2.0*diffusivity)


def laplace_exact(diffusivity, speed, flip_rate, length, theta):
    a, b = rates(diffusivity, speed, flip_rate)
    h = theta/diffusivity
    z = a+b+h
    det = a*h
    gap = math.sqrt(z*z-4.0*det)
    lam_slow = -2.0*det/(z+gap)
    lam_fast = -z-lam_slow
    return ((-lam_fast)*math.exp(lam_slow*length) +
            lam_slow*math.exp(lam_fast*length))/(lam_slow-lam_fast)


def laplace_limit(speed, flip_rate, length, theta):
    return math.exp(-flip_rate*length*theta/(2.0*speed*(speed+theta)))


def simulated_paint(diffusivity, speed, flip_rate, length, rng):
    a, b = rates(diffusivity, speed, flip_rate)
    x=0.0
    blue_length=0.0
    islands=0
    while True:
        x += rng.expovariate(a)
        if x >= length:
            break
        islands += 1
        width = rng.expovariate(b)
        blue_length += min(width,length-x)
        x += width
        if x >= length:
            break
    return blue_length/diffusivity, islands


def check():
    checks=0
    for v in (0.3, 0.8, 1.0, 2.1):
        for q in (0.2, 1.0, 3.0):
            for d in (0.0001, 0.01, 0.4):
                a,b=rates(d,v,q)
                k=a+b
                # Riccati D K^2 - diag(v,-v) K + Q = 0, using K=[[-a,a],[b,-b]].
                residual_plus = -d*a*k-v*a+q
                residual_minus = -d*b*k+v*b+q
                assert abs(residual_plus) < 1e-9*(1+q)
                assert abs(residual_minus) < 1e-9*(1+q)
                checks += 2
                assert a>0 and b>0
                checks += 1
                pi_minus=a/k
                pe=v*v/(2.0*q*d)
                paper_fraction=(math.sqrt(1.0+pe)-math.sqrt(pe))/(2.0*math.sqrt(1.0+pe))
                assert abs(pi_minus-paper_fraction) < 1e-12
                checks += 1
    for v,q,length in ((1.0,2.0,5.0),(0.7,1.6,2.0),(2.1,0.4,8.0)):
        for theta in (0.25,1.0,2.0):
            target=laplace_limit(v,q,length,theta)
            errors=[]
            for d in (0.1,0.01,0.001,0.00001):
                f=laplace_exact(d,v,q,length,theta)
                assert 0.0 < f <= 1.0
                errors.append(abs(f-target))
                checks += 1
            assert errors[-1] < 2.5e-4
            assert errors[-1] < errors[0]
            checks += 2
    # Independent simulation of the alternating-exponential spatial chain
    # versus a matrix-exponential Feynman-Kac calculation.
    rng=random.Random(46572026)
    for v,q,d,L,theta in ((1.0,2.0,0.02,3.0,1.0),(1.4,0.7,0.01,5.0,0.7)):
        n=25000
        vals=[]
        counts=[]
        for _ in range(n):
            area,count=simulated_paint(d,v,q,L,rng)
            vals.append(math.exp(-theta*area))
            counts.append(count)
        mean=sum(vals)/n
        exact=laplace_exact(d,v,q,L,theta)
        assert abs(mean-exact)<0.014, (mean, exact)
        checks+=1
        expected_count_limit=q*L/(2*v)
        assert abs(sum(counts)/n-expected_count_limit)<0.13
        checks+=1
    return checks


if __name__ == '__main__':
    print('Verified',check(),'deterministic analytic/numerical assertions plus 50,000 simulated finite-window samples.')
