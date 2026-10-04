#!/usr/bin/env python3
from fractions import Fraction
from math import comb


def age(m, q, r, k):
    return Fraction(r * k + ((k * q) % m), m)


def cyclic_canonical(m, q, r):
    if m <= 1:
        return True
    q %= m
    return all(age(m, q, r, k) >= 1 for k in range(1, m))


def direct_canonical(r, a, b):
    return cyclic_canonical(a, b, r) and cyclic_canonical(b, a, r)


def formula_canonical(r, a, b):
    d = b - a
    return 0 <= d <= r and 1 <= a <= r + d


def rho(r, a, b):
    return Fraction(comb(r, 2) + r * (a + b) + a * b, (r + a + b) ** 2)


def main():
    for r in range(2, 26):
        # This box strictly contains the formula-predicted canonical region.
        for a in range(1, 3 * r + 3):
            for b in range(a, 4 * r + 4):
                d = direct_canonical(r, a, b)
                f = formula_canonical(r, a, b)
                assert d == f, ("canonical mismatch", r, a, b, d, f)

        lo = Fraction(23 * r - 1, 72 * r)
        hi = Fraction(r + 1, 2 * (r + 2))
        lo_eq = []
        hi_eq = []
        for d in range(0, r + 1):
            for a in range(1, r + d + 1):
                b = a + d
                x = rho(r, a, b)
                assert lo <= x <= hi, ("bound failure", r, a, b, x, lo, hi)
                if x == lo:
                    lo_eq.append((a, b))
                if x == hi:
                    hi_eq.append((a, b))
        assert lo_eq == [(2 * r, 3 * r)], (r, lo_eq)
        assert hi_eq == [(1, 1)], (r, hi_eq)

    for r in range(2, 501):
        assert rho(r, 1, 1) == Fraction(r + 1, 2 * (r + 2))
        assert rho(r, 2 * r, 3 * r) == Fraction(23 * r - 1, 72 * r)

    print("VERIFY_OK")


if __name__ == "__main__":
    main()
