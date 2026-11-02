#!/usr/bin/env python3
"""Reproduce exact finite checks and the formal second-order coefficient.
Python 3.9+ standard library only.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb, factorial


def count_by_inclusion_exclusion(m):
    """Number of perfect matchings avoiding a prescribed matching."""
    total = 0
    for i in range(m + 1):
        for j in range(m + 1):
            for k in range(m + 1):
                v = (comb(m, i) * comb(m, j) * comb(m, k) *
                     comb(2*m-i-j, m-i) * comb(2*m-j-k, m-j) *
                     comb(2*m-k-i, m-k) *
                     factorial(m-i) * factorial(m-j) * factorial(m-k))
                total += (-1)**(i+j+k) * v
    return total


def total_matchings(m):
    return comb(2*m, m)**3 * factorial(m)**3


def direct_count(m, exclude):
    """Completely independent vertex-mask recurrence on K_{2m,2m,2m}."""
    n = 6 * m
    blocked = set()
    # Split each part into two groups of m for the three types of pairs.
    for t in range(m):
        blocked.add(frozenset((t, 2*m+t)))
        blocked.add(frozenset((m+t, 4*m+t)))
        blocked.add(frozenset((3*m+t, 5*m+t)))
    permitted = [0] * n
    for a in range(n):
        for b in range(n):
            if a//(2*m) != b//(2*m) and (not exclude or frozenset((a, b)) not in blocked):
                permitted[a] |= 1 << b

    @lru_cache(None)
    def count(mask):
        if mask == 0:
            return 1
        b = mask & -mask
        a = b.bit_length() - 1
        partners = (mask ^ b) & permitted[a]
        result = 0
        while partners:
            pick = partners & -partners
            result += count(mask ^ b ^ pick)
            partners ^= pick
        return result
    return count((1 << n) - 1)

# Sparse polynomials with monomial degrees in (i,j,k), rational coefficients.
ZERO = (0, 0, 0)
ONE = {ZERO: F(1)}

def const(c):
    return {ZERO: F(c)} if c else {}

def var(t):
    exps = [0, 0, 0]; exps[t] = 1
    return {tuple(exps): F(1)}

def add(*args):
    d = defaultdict(F)
    for p in args:
        for mon, coeff in p.items(): d[mon] += coeff
    return {mon: coeff for mon, coeff in d.items() if coeff}

def scale(p, c):
    return {mon: coeff * F(c) for mon, coeff in p.items() if coeff * F(c)}

def neg(p):
    return scale(p, -1)

def mul(a, b):
    d = defaultdict(F)
    for ea, ca in a.items():
        for eb, cb in b.items():
            d[tuple(ea[t] + eb[t] for t in range(3))] += ca * cb
    return {mon: v for mon, v in d.items() if v}

def power(p, n):
    result = ONE
    for _ in range(n): result = mul(result, p)
    return result

def pair_a(x, y):
    return scale(add(x, y, neg(power(add(x, neg(y)), 2))), F(1, 4))

def falling2(x):
    return mul(x, add(x, const(-1)))

def falling_cubic_sum(x):
    return mul(falling2(x), add(scale(x, 2), const(-1)))

def pair_b(x, y):
    v = add(x, y)
    return add(scale(add(falling_cubic_sum(x), falling_cubic_sum(y)), F(-1, 12)),
               scale(falling_cubic_sum(v), F(1, 48)))

def stirling2(n, k):
    if n == 0: return int(k == 0)
    if k == 0: return 0
    return k * stirling2(n - 1, k) + stirling2(n - 1, k - 1)

def touchard(n, lam):
    return sum(stirling2(n, r) * lam**r for r in range(n + 1))

def formal_expect(p, lam):
    return sum(coef * touchard(e[0], lam) * touchard(e[1], lam) * touchard(e[2], lam)
               for e, coef in p.items())


def check_formal_asymptotics():
    x, y, z = var(0), var(1), var(2)
    A = add(pair_a(x, y), pair_a(y, z), pair_a(z, x))
    B = add(pair_b(x, y), pair_b(y, z), pair_b(z, x))
    Q = add(B, scale(power(A, 2), F(1, 2)))
    for lam in [F(-1, 4), F(0), F(1, 3), F(5, 7)]:
        assert formal_expect(A, lam) == 0
        assert formal_expect(B, lam) == -F(3, 4) * lam**2
        assert formal_expect(scale(power(A, 2), F(1, 2)), lam) == F(9, 8) * lam**2
        assert formal_expect(Q, lam) == F(3, 8) * lam**2
    assert formal_expect(Q, F(-1, 4)) == F(3, 128)
    print('FORMAL_MOMENTS_OK: first coefficient 0; second coefficient 3/128')


def main():
    for m in range(1, 4):
        numerator = count_by_inclusion_exclusion(m)
        denom = total_matchings(m)
        counted = direct_count(m, True)
        all_counted = direct_count(m, False)
        assert numerator == counted and denom == all_counted
        print('DIRECT_ENUM_OK', m, numerator, denom, F(numerator, denom))
    for m in range(4, 13):
        num = count_by_inclusion_exclusion(m)
        den = total_matchings(m)
        assert 0 < num < den
        if m in (4, 6, 8, 12):
            print('EXACT_IE_OK', m, str(F(num, den))[:80])
    check_formal_asymptotics()
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
