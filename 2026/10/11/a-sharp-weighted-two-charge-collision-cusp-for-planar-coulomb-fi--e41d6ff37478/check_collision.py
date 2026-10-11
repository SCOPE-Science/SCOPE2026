#!/usr/bin/env python3
"""Elementary checks for an exact Coulomb collision coefficient.

Pure Python 3 (standard library). Tests are diagnostic, not a substitute for
proof of an asymptotic limit or a proof of novelty.
"""
from fractions import Fraction
from math import comb, cos, cosh, pi, sin, sqrt


def b(m):
    return Fraction(comb(2*m, m), 4**m)


def equal_weight_coefficient(N=20000):
    # Positively summed convergent series, stable central-binomial recurrence.
    s = 0.0
    previous = 1.0
    current = 1.0
    for m in range(1, N + 1):
        current *= (2*m-1)/(2*m)
        s += current*current*previous/(2*m-1)
        previous = current
    return s*pi*pi


def elliptic_coefficient(alpha, beta, steps=320, umax=13.0):
    # Composite midpoint quadrature for a manifestly positive elliptic integral.
    # The missing u-tail is O(exp(-umax)) for fixed positive alpha, beta.
    h = umax / steps
    k = pi / steps
    A = alpha + beta
    q = (alpha-beta)/A
    acc = 0.0
    for j in range(steps):
        u = (j + .5)*h
        C = cosh(u)
        for m in range(steps):
            v = (m + .5)*k
            s2 = (1-q*q)*sin(v)**2
            B = C + q*cos(v)
            # Rationalized subtraction avoids floating-point cancellation.
            acc += A*s2/(B + sqrt(B*B-s2))
    return acc*h*k


def main():
    for m in range(1, 16):
        # Exact coefficients in 1-sqrt(1-x)=sum_{m>=1} b_m*x^m/(2m-1).
        ratio = b(m) / (2*m-1)
        if m == 1:
            assert ratio == Fraction(1, 2)
        else:
            prev = b(m-1)/(2*m-3)
            # c_m / c_{m-1} = (2m-3)/(2m), m>=2.
            assert ratio / prev == Fraction(2*m-3, 2*m)
    # Exact finite-prefix identity, independently of the floating recurrence.
    prefix = sum((b(m)**2*b(m-1)/ (2*m-1) for m in range(1, 30)), Fraction(0))
    assert abs(float(prefix)*pi*pi - equal_weight_coefficient(29)) < 1e-13
    c_series = equal_weight_coefficient(200)
    c_ellip = elliptic_coefficient(1, 1, 400)
    assert 2.870 < c_series < c_ellip + .002 < 2.874
    assert abs(c_ellip - equal_weight_coefficient(100000)) < .00015
    for alpha, beta in [(1., 2.), (.25, .75)]:
        c1 = elliptic_coefficient(alpha, beta, 250)
        c2 = elliptic_coefficient(beta, alpha, 250)
        assert c1 > 0
        assert abs(c1-c2)<1e-9
        print('weight_pair', alpha, beta, 'coefficient', format(c1, '.10f'))
    print('equal_series_200', format(c_series, '.10f'))
    print('equal_elliptic_400', format(c_ellip, '.10f'))
    print('equal_series_100000', format(equal_weight_coefficient(100000), '.10f'))
    print('Checks passed; numerical quadrature does not certify the limiting theorem.')


if __name__ == '__main__':
    main()
