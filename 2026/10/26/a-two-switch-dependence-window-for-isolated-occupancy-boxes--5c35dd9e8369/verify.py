"""Exact small-case checks for uniform singleton-box covariance."""
from fractions import Fraction
from itertools import product
from math import exp, floor, sqrt, log1p


def formula(m, n):
    one = Fraction(n, m) * Fraction(m - 1, m) ** (n - 1)
    both = Fraction(n * (n - 1), m * m) * Fraction(m - 2, m) ** (n - 2)
    return both - one * one


def brute(m, n):
    c1 = c11 = 0
    for assign in product(range(m), repeat=n):
        u, v = assign.count(0) == 1, assign.count(1) == 1
        c1 += u
        c11 += u and v
    z = m ** n
    return Fraction(c11, z) - Fraction(c1, z) ** 2


def main():
    tested = 0
    for m in range(2, 6):
        for n in range(2, 7):
            assert formula(m, n) == brute(m, n), (m, n)
            tested += 1
    for m in range(2, 81):
        signs = [1 if formula(m, n) > 0 else (-1 if formula(m, n) < 0 else 0) for n in range(2, 3 * m + 11)]
        positive_indices = [i for i, sign in enumerate(signs) if sign == 1]
        assert positive_indices == list(range(positive_indices[0], positive_indices[-1] + 1)), m
        assert signs[-1] == -1, m
        if m >= 4:
            assert signs[0] == -1 and signs[m - 2] == 1, m
        elif m == 3:
            assert signs[:3] == [1, 1, -1]
        else:
            assert signs[:2] == [1, -1]
    for m in (1000, 10000, 100000):
        s = 0.4
        n = m + floor(s * sqrt(m))
        p1 = n / m * (1 - 1 / m) ** (n - 1)
        f = log1p(-1 / n) - 2 * log1p(-1 / m) + (n - 2) * log1p(-1 / (m - 1) ** 2)
        scaled = m * m * p1 * p1 * (exp(f) - 1)
        assert abs(scaled - exp(-2) * (0.5 - s * s)) < 0.016, (m, scaled)
    print(f"VERIFY_OK exact_enumerations={tested}, rational_sign_grid=79, asymptotic_checks=3")


if __name__ == "__main__":
    main()
