"""Finite rational and analytic-asymptotic checks for the weighted-shift theorem.

Finite checks are diagnostics; the infinite-dimensional result uses the proof.
"""
from fractions import Fraction
from math import exp, log, isclose
from itertools import product


def g(j, n, d, q):
    u = q ** j
    return (1 + n * u) / (1 + d * u)


def prod_of(start, length, n, d, q):
    result = Fraction(1)
    for j in range(start, start + length):
        result *= g(j, n, d, q)
    return result


def neg_dilog(a):
    # -Li_2(-a)=sum_{k>=1} (-1)^(k+1) a^k/k^2 for |a|<1.
    result, term = 0.0, 1.0
    for k in range(1, 2000):
        term *= -a
        add = -term / (k * k)
        result += add
        if abs(add) < 1e-17:
            break
    return result


def log_kappa(n, d, h):
    q = exp(-h)
    # Absolute monotone log factor, rigorously bounded tail can be estimated
    # using geometric decay (not a proof of asymptotic).
    total, j = 0.0, 0
    while True:
        z = exp(-h * j)
        a = log((1 + n*z)/(1 + d*z))
        total += a
        j += 1
        if z < 1e-12:
            break
        assert j < 3000000
    return abs(total) / 2


def main():
    rational_tests = 0
    for q, n, d, length, start in product(
        [Fraction(1, 2), Fraction(2, 3), Fraction(4, 5)],
        [Fraction(-3, 5), Fraction(-1, 4), Fraction(0), Fraction(1, 4), Fraction(3, 5)],
        [Fraction(-3, 5), Fraction(-1, 4), Fraction(0), Fraction(1, 4), Fraction(3, 5)],
        range(1, 8), range(0, 14)
    ):
        prefix = prod_of(0, length, n, d, q)
        segment = prod_of(start, length, n, d, q)
        if n > d:
            assert segment <= prefix
        if n < d:
            assert segment >= prefix
        if n == d:
            assert segment == prefix == 1
        rational_tests += 1
    numeric_tests = 0
    for n, d in [(0.5, -0.3), (-0.4, 0.2), (0.0, 0.7)]:
        # integral of log(1+a exp(-x)) dx = -Li_2(-a)
        integral = neg_dilog(n) - neg_dilog(d)
        f0 = log((1+n)/(1+d))
        for h in [0.2, 0.1, 0.05, 0.025]:
            exact = log_kappa(n, d, h)
            prediction = abs(integral)/(2*h) + abs(f0)/4
            assert abs(exact - prediction) < 0.15*h
            numeric_tests += 1
    print('exact rational block comparisons:', rational_tests)
    print('high-precision asymptotic diagnostics:', numeric_tests)
    print('all diagnostics passed')

if __name__ == '__main__':
    main()
