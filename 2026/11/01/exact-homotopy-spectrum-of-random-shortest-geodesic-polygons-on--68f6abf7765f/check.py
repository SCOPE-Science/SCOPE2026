#!/usr/bin/env python3
"""Standalone finite diagnostics for random shortest-geodesic loops on RP^2.

Finite numerical checks are not proofs of the universal theorem.
Requires only Python's standard library.
"""
import math
import random


def legendre(n, t):
    if n == 0:
        return 1.0
    p0, p1 = 1.0, t
    for j in range(1, n):
        p0, p1 = p1, ((2 * j + 1) * t * p1 - j * p0) / (j + 1)
    return p1


def integrate_odd_legendre(n, N=10000):
    # Simpson's rule on [0,1], independent of the Catalan recurrence.
    h = 1.0 / N
    s = legendre(n, 0) + legendre(n, 1)
    for j in range(1, N):
        s += (4 if j % 2 else 2) * legendre(n, j*h)
    return s*h/3


def coefficients(K):
    a = .5
    for k in range(K):
        yield k, (-1)**k*a
        a *= (2*k+1)/(2*(k+2))


def parity_bias(n, K=400):
    return sum((4*k+3)*v**n for k,v in coefficients(K))


def sample_sphere(rng):
    x,y,z = rng.gauss(0,1), rng.gauss(0,1), rng.gauss(0,1)
    m = math.sqrt(x*x+y*y+z*z)
    return x/m,y/m,z/m


def is_nontrivial(vertices):
    product = 1
    for i, a in enumerate(vertices):
        b=vertices[(i+1)%len(vertices)]
        if a[0]*b[0]+a[1]*b[1]+a[2]*b[2] < 0:
            product *= -1
    return product == -1


def main():
    for k,v in list(coefficients(8)):
        n=2*k+1
        numerical=integrate_odd_legendre(n)
        assert abs(numerical-v)<1.e-6,(k,n,numerical,v)
    print('DIRECT_FUNK_HECKE_LEGENDRE_INTEGRALS_PASSED',8)

    b3=parity_bias(3)
    b4=parity_bias(4)
    assert abs(b3-(1-2/math.pi))<2.e-10
    assert abs(b4-(1-8/math.pi**2))<2.e-10
    assert abs((1-b3)/2-1/math.pi)<2.e-10
    assert abs((1-b4)/2-4/math.pi**2)<2.e-10
    print('SEPARATE_TRIANGLE_QUADRILATERAL_BENCHMARKS_PASSED')

    vals=[(1-parity_bias(n))/2 for n in range(3,16)]
    assert all(0<v<.5 for v in vals)
    assert all(vals[i+1]>vals[i] for i in range(len(vals)-1))
    for n in range(3,16):
        b=parity_bias(n)
        expansion=3/2**n+7*(-1/8)**n
        assert abs(b-expansion)<=36/16**n+1.e-14
    print('EXPLICIT_SPECTRAL_ERROR_BOUNDS_AND_FINITE_MONOTONIC_DIAGNOSTICS_PASSED',13)

    # Independent Monte Carlo: generate actual random spherical lifts of
    # projective vertices, and inspect the end-point of the lifted loop.
    rng=random.Random(20261029)
    count=25000
    for n in (3,4,5,6,8):
        hits=sum(is_nontrivial([sample_sphere(rng) for _ in range(n)]) for _ in range(count))
        estimate=hits/count
        target=(1-parity_bias(n))/2
        assert abs(estimate-target)<.016,(n,estimate,target)
    print('DIRECT_GEODESIC_LOOP_MONTE_CARLO_PASSED',5,'x',count)
    print('ALL_CHECKS_PASSED')


if __name__=='__main__':
    main()
