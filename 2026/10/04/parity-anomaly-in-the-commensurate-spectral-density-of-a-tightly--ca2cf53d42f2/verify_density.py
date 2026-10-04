#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, pi, sin, cos


def sign_sin_pi_rational(m, x):
    # x is t/pi and is never a zero in the uses below.
    y = x * m
    n = y.numerator // y.denominator
    return 1 if n % 2 == 0 else -1


def exact_positive_fraction(p, q):
    zeros = {Fraction(j, p) for j in range(2*p + 1)}
    zeros |= {Fraction(j, q) for j in range(2*q + 1)}
    z = sorted(zeros)
    good = Fraction(0, 1)
    for a, b in zip(z, z[1:]):
        mid = (a + b) / 2
        if sign_sin_pi_rational(p, mid) * sign_sin_pi_rational(q, mid) > 0:
            good += b - a
    return good / 2  # interval x in [0,2]


def predicted(p, q):
    if p % 2 == 1 and q % 2 == 1:
        return Fraction(1, 2) + Fraction(1, 2*p*q)
    return Fraction(1, 2)


def exact_band_F(k, p, q, a=1.0):
    L3 = 2*pi*q/(p+q)
    z = a*a*k*k
    return 4*z - (z+1)**2*cos(2*pi*k) + (z-1)**2*cos(2*k*(pi-L3))


def sampled_energy_density(p, q, R, steps_per_unit=500):
    # Midpoint quadrature for a finite numerical sanity check only.
    n = int(R*steps_per_unit)
    h = R/n
    s = 0.0
    for i in range(n):
        k = (i + 0.5)*h
        if exact_band_F(k, p, q) >= 0.0:
            s += 2*k*h
    return s/(R*R)


def main():
    checked = 0
    for p in range(1, 26):
        for q in range(1, 26):
            if gcd(p, q) != 1:
                continue
            got = exact_positive_fraction(p, q)
            want = predicted(p, q)
            if got != want:
                raise AssertionError((p, q, got, want))
            checked += 1

    cases = [
        (1, 3, Fraction(2, 3)),
        (3, 5, Fraction(8, 15)),
        (1, 2, Fraction(1, 2)),
        (2, 3, Fraction(1, 2)),
    ]
    numerical = []
    for p, q, want in cases:
        val = sampled_energy_density(p, q, 240.0)
        numerical.append((p, q, val, float(want)))
        if abs(val - float(want)) > 0.012:
            raise AssertionError((p, q, val, float(want)))

    print('exact_coprime_pairs_checked=', checked)
    for row in numerical:
        print('sample', row)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
