#!/usr/bin/env python3
"""Finite-level consistency checks for the dyadic Riesz-product carry law.

Only the Python standard library is required. This script does not certify
infinite-dimensional asymptotic conclusions; those follow from the proof.
"""
from fractions import Fraction
from itertools import product
from math import cos, pi, log, sqrt


def matrix_second_moment(a, n):
    a = Fraction(a)
    v0, v1 = Fraction(1), Fraction(0)
    for _ in range(n):
        v0, v1 = (1 + a*a/2)*v0 + 2*a*v1, (a*a/4)*v0 + a*v1
    return v0 + 2*v1


def independent_fourier_sum(a, n):
    a = Fraction(a)
    weights = {0: 1 + a*a/2, -1: a, 1: a, -2: a*a/4, 2: a*a/4}
    total = Fraction(0)
    for digits in product(range(-2, 3), repeat=n):
        if sum(d * (1 << (n-j-1)) for j, d in enumerate(digits)) % (1 << n) == 0:
            w = Fraction(1)
            for d in digits:
                w *= weights[d]
            total += w
    return total


def direct_second_moment(a, n):
    total = 0.0
    for x in range(1 << n):
        v = 1.0
        for j in range(1, n+1):
            v *= 1 + float(a)*cos(2*pi*x/(1 << j))
        total += v*v
    return total/(1 << n)


def spectral_data(a):
    a = float(a)
    theta = 1+a+a*a/2
    disc = sqrt(theta*theta-4*a)
    lp = (theta+disc)/2
    lm = (theta-disc)/2
    A = (1+a*a-lm)/(lp-lm)
    return lp,lm,A,1-log(lp,2)


def exact_energy_formula(a,s):
    aa = float(a)
    z = 2**(s-1)
    theta = 1+aa+aa*aa/2
    F = (1+(aa*aa/2-aa)*z)/(1-theta*z+aa*z*z)
    return 1+(1-2**(-s))*(F-1)


def truncated_energy(a,s,N):
    aa = float(a)
    v0,v1=1.0,0.0
    total=0.0
    z = 2**(s-1)
    for n in range(1,N+1):
        v0,v1=(1+aa*aa/2)*v0+2*aa*v1, (aa*aa/4)*v0+aa*v1
        total += z**n*(v0+2*v1)
    return 1+(1-2**(-s))*total


def run():
    rational_tests = 0
    for a in (Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)):
        for n in range(1,6):
            x = matrix_second_moment(a,n)
            y = independent_fourier_sum(a,n)
            assert x==y, (a,n,x,y)
            rational_tests += 1

    sample_tests = 0
    for a in (0.0,0.125,0.5,0.75,1.0):
        for n in range(1,8):
            x = float(matrix_second_moment(Fraction(str(a)),n))
            y = direct_second_moment(a,n)
            assert abs(x-y) <= 1e-10*max(1.0,x), (a,n,x,y)
            sample_tests += 1

    energy_tests = 0
    for a in (0.125,0.25,0.5,0.75):
        lp,lm,A,sc=spectral_data(a)
        assert 1 < lp < 2 and 0 < lm < 1 and 0 < sc < 1 and A>0
        s=0.35*sc
        direct=truncated_energy(a,s,240)
        expected=exact_energy_formula(a,s)
        assert abs(direct-expected)<2e-11*max(1.0,expected),(a,direct,expected)
        n=300
        moment=0.0
        v0,v1=1.0,0.0
        for _ in range(n):
            v0,v1=(1+a*a/2)*v0+2*a*v1,(a*a/4)*v0+a*v1
        moment=v0+2*v1
        assert abs(moment/(lp**n)-A)<1e-10,(a,moment/(lp**n),A)
        energy_tests += 1

    assert all(matrix_second_moment(Fraction(0),n)==1 for n in range(12))
    assert all(matrix_second_moment(Fraction(1),n)==2**n for n in range(12))
    print(f'PASS: {rational_tests} exact rational Fourier-carry sums; '
          f'{sample_tests} direct cyclic trigonometric sums; '
          f'{energy_tests} finite-energy/spectral checks; two endpoints.')
    print('At a=1/2: lambda, critical energy exponent:',
          spectral_data(.5)[0],spectral_data(.5)[3])


if __name__ == '__main__':
    run()
