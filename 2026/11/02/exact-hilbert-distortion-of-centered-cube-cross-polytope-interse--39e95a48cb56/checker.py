#!/usr/bin/env python3
"""Exact finite checks of the centered cube--cross-polytope radial theorem.

Run: python3 checker.py
No packages beyond the Python standard library are needed. The exhaustive
checks are finite consistency tests, not the proof of the all-dimensional theorem.
"""
from fractions import Fraction
from itertools import product
from math import floor


def predicted_outer_radius_squared(n, tau):
    """Maximum squared Euclidean length in the norm unit ball."""
    s = min(tau / 2, Fraction(n // 2))
    integer = s.numerator // s.denominator
    remainder = s - integer
    return 2 * (integer + remainder * remainder)


def predicted_numerator_squared(n, tau):
    """Maximum of N_tau(x)^2 over the Euclidean unit sphere."""
    a, b = n // 2, (n + 1) // 2
    return max(Fraction(n-1, n), Fraction(4*a*b, n) / tau**2)


def checker():
    tested = 0
    arithmetic_checks = 0
    for n in range(2, 8):
        scale = 4
        observed = {}
        for first in product(range(-scale, scale+1), repeat=n-1):
            last = -sum(first)
            if abs(last) > scale:
                continue
            coords = first + (last,)
            mass = sum(abs(x) for x in coords)
            square = sum(x*x for x in coords)
            best = observed.get(mass, -1)
            if square > best:
                observed[mass] = square
            tested += 1
        for h in range(1, 2*n+3):
            tau = Fraction(h, 2)
            possible = [v for mass, v in observed.items() if mass <= scale*tau]
            assert possible
            actual = Fraction(max(possible), scale**2)
            expected = predicted_outer_radius_squared(n,tau)
            assert actual == expected, (n, tau, actual, expected)
            numerator = predicted_numerator_squared(n,tau)
            assert numerator > 0
            # Numerator squared times outer-radius squared is the claimed
            # squared Banach--Mazur distance after permutation averaging.
            assert numerator * actual >= 1
            arithmetic_checks += 3
        # The largest zero-sum Euclidean dual norm of a sign vector is
        # obtained by the most balanced choice of positive and negative signs.
        sign_max = max(Fraction(n*n-sum(signs)**2, n)
                       for signs in product((-1, 1), repeat=n))
        a, b = n//2, (n+1)//2
        assert sign_max == Fraction(4*a*b,n)
        arithmetic_checks += 1
        # At small parameter the norm is a rescaled coordinate l1 norm;
        # past the maximum zero-mass l1 the cross-polytope cap is inactive.
        assert predicted_outer_radius_squared(n,Fraction(n+5)) == 2*(n//2)
        arithmetic_checks += 1
    print('CHECK_OK',tested,'grid points;',arithmetic_checks,'exact rational assertions')

if __name__ == '__main__':
    checker()
