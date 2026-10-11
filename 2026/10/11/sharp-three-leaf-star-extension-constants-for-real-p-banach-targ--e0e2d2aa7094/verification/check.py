#!/usr/bin/env python3
"""Deterministic finite checks of the three-leaf star formula.

The infinite-parameter statement and global minimizer classification require
(and are supplied by) the analytic proof; finite sampling is not a proof.
"""
from fractions import Fraction
from itertools import product
from math import log


def norm_p(s, t, p):
    triples = ((abs(s), abs(t)), (abs(s + t), abs(s)), (abs(s + t), abs(t)))
    return 2.0 * min((a**p + b**p)**(1 / p) for a, b in triples)


def radius(lam, p):
    a, b, c = lam
    return max(norm_p(b, c, p), norm_p(b - 1, c, p), norm_p(b, c - 1, p))


def exact_p1_check():
    tests = 0
    for ia in range(-6, 13):
        for ib in range(-6, 13):
            a = Fraction(ia, 6)
            b = Fraction(ib, 6)
            c = 1 - a - b
            for s, t in ((b, c), (b - 1, c), (b, c - 1)):
                val = 2 * min(abs(s) + abs(t), abs(s + t) + abs(s), abs(s + t) + abs(t))
                assert val >= 0
                tests += 1
            rad = 2 * max(
                min(abs(b) + abs(c), abs(b + c) + abs(b), abs(b + c) + abs(c)),
                min(abs(b - 1) + abs(c), abs(b - 1 + c) + abs(b - 1), abs(b - 1 + c) + abs(c)),
                min(abs(b) + abs(c - 1), abs(b + c - 1) + abs(b), abs(b + c - 1) + abs(c - 1)),
            )
            assert rad >= Fraction(4, 3), (a, b, rad)
    assert radius((Fraction(1, 3),) * 3, 1) == 4 / 3
    return tests


def sampled_minimizers():
    # Samples compare against the analytic formula without being used as proof.
    tested = 0
    p0 = log(2) / log(3)
    for p in [0.25, 0.5, 0.6, 0.62, 0.63, p0, 0.65, 0.75, 0.9, 1.0]:
        theorem = min(2.0, 2.0**(1.0 + 1.0/p) / 3.0)
        assert abs(radius((1/3, 1/3, 1/3), p) - 2.0**(1.0 + 1.0/p)/3) < 2e-12
        assert abs(radius((1,0,0), p) - 2.0) < 2e-12
        for i in range(31):
            for j in range(31 - i):
                lam = (i/30, j/30, (30-i-j)/30)
                got = radius(lam, p)
                assert got + 3e-12 >= theorem, (p, lam, got, theorem)
                tested += 1
    return tested


def main():
    n1 = exact_p1_check()
    n2 = sampled_minimizers()
    print(f"VERIFY_OK p1_exact_pairs={n1} simplex_grid_points={n2} phase_p0={log(2)/log(3):.12f} analytic_global_proof_required=True")

if __name__ == '__main__':
    main()
