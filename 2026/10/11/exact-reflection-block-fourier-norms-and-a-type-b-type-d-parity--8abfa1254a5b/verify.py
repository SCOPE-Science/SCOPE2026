#!/usr/bin/env python3
"""Exact finite checks for natural reflection-block Fourier projection norms.

The all-rank statements are proved analytically; this script only checks samples.
"""
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial


def a(j):
    return Fraction(comb(2*j, j), 2**j*factorial(j+1))


def norm_B_formula(n):
    return n*sum(((-1)**j*a(j) for j in range(n)), Fraction())


def parity_correction(n):
    if n % 2:
        return Fraction()
    return Fraction(n*(-1)**(n//2-1)*comb(n-2, n//2-1),
                    factorial(n)*2**(n-2))


def enumerate_character_moments(n):
    total_B = total_D = sq_B = sq_D = 0
    group_size = 2**n*factorial(n)
    for p in permutations(range(n)):
        fixed = tuple(i for i, pi in enumerate(p) if i == pi)
        for signs in product((-1, 1), repeat=n):
            trace = sum(signs[i] for i in fixed)
            total_B += abs(trace)
            sq_B += trace*trace
            if signs.count(-1) % 2 == 0:
                total_D += abs(trace)
                sq_D += trace*trace
    result_B = Fraction(n*total_B, group_size)
    result_D = Fraction(n*total_D, group_size//2)
    assert Fraction(sq_B, group_size) == 1
    if n >= 3:
        assert Fraction(sq_D, group_size//2) == 1
    return result_B, result_D


def check():
    direct = 0
    for n in range(1, 8):
        actual_B, actual_D = enumerate_character_moments(n)
        assert actual_B == norm_B_formula(n), (n, actual_B, norm_B_formula(n))
        if n >= 3:
            assert actual_D == actual_B + parity_correction(n), (n, actual_D)
        direct += 1
    sign_checks = 0
    # Check identity for the parity-conditioned absolute Rademacher sum.
    for n in range(1, 101):
        signed = sum(((-1)**j*comb(n,j)*abs(n-2*j) for j in range(n+1)), 0)
        exact = Fraction(signed, 2**n)
        expected = (Fraction() if n%2 else
                    Fraction((-1)**(n//2-1)*comb(n-2,n//2-1), 2**(n-2)))
        assert exact == expected, n
        sign_checks += 1
    # Bessel-generating coefficient recurrence and alternating tail monotonicity.
    coef_checks=0
    for j in range(1, 250):
        assert a(j) == a(j-1)*Fraction(2*j-1, j*(j+1))
        assert a(j) < a(j-1)
        coef_checks += 1
    print('VERIFY_OK direct_signed_group_ranks=1..7 checked=' + str(direct)
          + ' parity_moments_n=1..100 checked=' + str(sign_checks)
          + ' bessel_coefficients_checked=' + str(coef_checks))
    for n in (3,4,5,6,7):
        print('NORM',n,'B',norm_B_formula(n),'D',norm_B_formula(n)+parity_correction(n))

if __name__ == '__main__':
    check()
