#!/usr/bin/env python3
"""Exact rational checks for the fourth spectral moment formula."""
from fractions import Fraction
from itertools import product

def tuple_sum(p):
    d = p + 1
    total = Fraction(0)
    for i, j, k, ell in product(range(p), repeat=4):
        # A has zero diagonal, so any adjacent repeated index contributes zero.
        if i == j or j == k or k == ell or ell == i:
            continue
        if len({i, j, k, ell}) == 4:
            moment = Fraction(1, d**3)
        elif i == k and j == ell:
            moment = Fraction(3, d * (d + 2))
        elif i == k or j == ell:
            moment = Fraction(1, d**2)
        else:
            raise AssertionError((i, j, k, ell))
        total += moment
    return total

def closed_form(p):
    d = p + 1
    return (Fraction(p*(p-1)*(p-2)*(p-3), d**3)
            + Fraction(2*p*(p-1)*(p-2), d**2)
            + Fraction(3*p*(p-1), d*(d+2)))

def simplified(p):
    return Fraction(p*(p-1)*(3*p**3 + 5*p**2 - 13*p + 9),
                    (p+1)**3 * (p+3))

def main():
    for p in range(2, 13):
        assert tuple_sum(p) == closed_form(p) == simplified(p), p
    for p in range(2, 41):
        assert closed_form(p) == simplified(p), p
    print("PASS: exact tuple-pattern sums for p=2..12; rational simplification for p=2..40")

if __name__ == "__main__":
    main()
