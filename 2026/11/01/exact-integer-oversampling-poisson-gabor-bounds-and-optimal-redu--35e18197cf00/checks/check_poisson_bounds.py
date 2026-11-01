#!/usr/bin/env python3
"""Supplementary tests of exact Poisson-window Gabor-frame formulas.

Run with: python3 checks/check_poisson_bounds.py
The infinite-dimensional theorem is proved analytically in RESULT.md.
"""
import cmath
import math
import random

PI = math.pi


def zak_closed(w, x, omega):
    assert w > 0
    c = 2 * PI * w
    r = math.exp(-c)
    v = omega % 1.0
    theta = 2 * PI * x
    a = math.sinh(c * (1 - v))
    b = math.sinh(c * v)
    numerator = a + b * cmath.exp(-1j * theta)
    denominator = 1 - 2 * r * math.cos(theta) + r*r
    return (2*PI*r/w) * cmath.exp(1j * v * theta) * numerator / denominator


def frame_density(w, q, x, omega):
    return sum(abs(zak_closed(w, x, omega + j/q))**2 for j in range(q))


def frame_bounds(w, q):
    assert w > 0 and q >= 2 and isinstance(q, int)
    c = 2*PI*w
    ratio = math.sinh(c)/math.sinh(c/q)
    prefactor = (PI/w)**2
    lower = prefactor*(ratio-q)/(2*math.cosh(c/2)**2)
    upper = prefactor*(ratio*math.cosh(c/q)+q)/(2*math.sinh(c/2)**2)
    return lower, upper


def zak_direct(w, x, omega, half_range=6000):
    return sum(cmath.exp(-2j*PI*k*omega)/((x+k)**2+w*w)
               for k in range(-half_range, half_range+1))


def polynomial(y):
    return 4*y**4-10*y**3+4*y*y+y-1


def optimal_width_q2():
    lo,hi=1.,3.
    for _ in range(80):
        mid=(lo+hi)/2
        if polynomial(mid)>0: hi=mid
        else: lo=mid
    y=(lo+hi)/2
    w=2/PI*math.acosh(math.sqrt(y))
    return y,w


def run():
    rng=random.Random(20261021)
    count=0
    for w in (0.2, 0.57, 1.15):
        for q in (2, 3, 4, 7):
            A,B=frame_bounds(w,q)
            assert 0 < A < B
            assert abs(frame_density(w,q,0.5,0.5/q)-A) < 1e-9 * max(1,A)
            assert abs(frame_density(w,q,0,0)-B) < 1e-9 * max(1,B)
            count+=3
            for _ in range(75):
                x=rng.random()
                omega=rng.random()
                val=frame_density(w,q,x,omega)
                assert A-1e-9 * max(1,A) <= val <= B+1e-9 * max(1,B)
                count+=1
    for w in (0.2,0.57,1.15):
        for x,omega in ((0.2,0.37),(0.5,0.25),(0.,0.)):
            z0=zak_closed(w,x,omega)
            z1=zak_direct(w,x,omega)
            assert abs(z0-z1) < 5e-4
            count+=1
    y,w=optimal_width_q2()
    assert abs(polynomial(y))<1e-12
    assert 0.55<w<0.56
    A,B=frame_bounds(w,2)
    k=B/A
    assert abs(k-5.620882374215344)<1e-10
    for factor in (0.5,0.75,0.95,1.05,1.25,2.0):
        a,b=frame_bounds(w*factor,2)
        assert b/a > k
        count+=1
    print("POISSON_FRAME_CHECKS_OK", count)
    print("unique_width", format(w,".15g"), "condition_number", format(k,".15g"))

if __name__ == "__main__":
    run()
