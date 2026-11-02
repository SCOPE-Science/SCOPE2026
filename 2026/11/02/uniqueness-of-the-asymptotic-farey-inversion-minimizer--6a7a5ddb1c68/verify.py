#!/usr/bin/env python3
"""Finite reproducibility tests for the Farey minimizer rigidity theorem.
All comparisons of Farey fractions use exact rational arithmetic.
The unbounded theorem requires the published analytic exclusion bound.
"""
from fractions import Fraction
from math import gcd, isqrt
from decimal import Decimal, localcontext


def farey(n):
    return sorted((Fraction(a, b), a, b)
                  for b in range(1, n + 1)
                  for a in range(b + 1) if gcd(a, b) == 1)


def min_pairs(n):
    terms = farey(n)
    best = n + 1
    pairs = []
    for i, (_, a, b) in enumerate(terms):
        if a == 0 or b - a < 2:
            continue
        # A later qualifying endpoint cannot improve on the first one.
        for j in range(i + 1, min(len(terms), i + best + 3)):
            _, c, d = terms[j]
            if c > a and d < b:
                k = j - i - 1
                if k < best:
                    best, pairs = k, []
                if k == best:
                    pairs.append((a, b, c, d))
                break
    return best, pairs


def count_interval(terms, u, v):
    lo, hi = Fraction(*u), Fraction(*v)
    return sum(lo < z < hi for z, _, _ in terms)


def verify():
    tested_intervals = 0
    for m in range(6, 26):
        for r in range(4):
            n = 4 * m + r
            seq = farey(n)
            I = count_interval(seq, (2*m-1, 4*m), (2*m, 4*m-1))
            assert I == (m+1 if r == 0 else m+3 if r in (1,2) else m+5)
            K = count_interval(seq, (2*m-1, 4*m-1), (m, 2*m-1))
            assert K == (m+2 if r == 0 else m+4 if r in (1,2) else m+6)
            tested_intervals += 2
            if r:
                J = count_interval(seq, (2*m, 4*m+1), (2*m+1, 4*m))
                assert J == (m+2 if r in (1,2) else m+4)
                tested_intervals += 1
    tested_orders = 0
    for n in list(range(120, 149)) + [160, 180, 200]:
        m, r = divmod(n, 4)
        expected = ((2*m-1, 4*m, 2*m, 4*m-1) if r == 0
                    else (2*m, 4*m+1, 2*m+1, 4*m))
        expected_gap = m+1 if r == 0 else m+2 if r in (1,2) else m+4
        gap, pairs = min_pairs(n)
        assert gap == expected_gap and pairs == [expected], (n, gap, pairs)
        tested_orders += 1
    N = 5504798
    with localcontext() as ctx:
        ctx.prec = 42
        z = Decimal(9*isqrt(N)+3)
        error = z * (Decimal(61)*z.ln()/100 + Decimal(7)/6)
        margin = Decimal(N)/36 - 4 - error
        assert margin > 0, margin
    print(f'VERIFY_OK exact_interval_cells={tested_intervals} '
          f'brute_order_cells={tested_orders} analytic_bound_margin={margin:.8f} '
          'rational_arithmetic=PASS finite_samples_only=YES')


if __name__ == '__main__':
    verify()
