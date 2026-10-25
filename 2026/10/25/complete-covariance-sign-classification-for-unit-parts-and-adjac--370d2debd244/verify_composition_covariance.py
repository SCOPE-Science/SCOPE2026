"""Exact checks for the covariance between unit parts and adjacent equalities.

Usage: python verify_composition_covariance.py
No external packages or network access are required.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def coefficients(s, m):
    """Coefficient of z^m in (1-z)^(-s)/(1-z^2), for s >= 0."""
    if m < 0:
        return 0
    if s == 0:
        return int(m % 2 == 0)
    return sum(choose(m - 2 * j + s - 1, s - 1)
               for j in range(m // 2 + 1))


def h(k, j):
    """Coefficient of z^j in (1-z)^(-(k-3))/(1-z^2)^2."""
    if j < 0:
        return 0
    if k == 3:
        return (j // 2 + 1) if j % 2 == 0 else 0
    return sum((t + 1) * choose(j - 2 * t + k - 4, k - 4)
               for t in range(j // 2 + 1))


def analytic_cov(n, k):
    assert 1 <= k <= n
    m = n - k
    if k == 1:
        return Fraction(0)
    if k == 2:
        return Fraction(-2, (n - 1)**2) if n >= 4 and n % 2 == 0 else Fraction(0)
    d = choose(n - 1, k - 1)
    return Fraction(2 * (k - 1) * ((k - 3) * h(k, m - 2) - h(k, m - 3)),
                    d * (n - 1))


def counted_cov(n, k):
    """Second derivation, from ordinary generating functions for mixed moments."""
    m, d = n - k, choose(n - 1, k - 1)
    if k == 1:
        return Fraction(0)
    u = k * choose(m + k - 2, k - 2)
    if k == 2:
        a = coefficients(0, m)
        au = 2 if m == 0 else 0
    else:
        a = (k - 1) * coefficients(k - 2, m)
        au = (k - 1) * (2 * choose(m + k - 3, k - 3)
                        + (k - 2) * coefficients(k - 3, m))
    return Fraction(au, d) - Fraction(u * a, d*d)


def brute_cov(n, k):
    """Direct exact enumeration of every ordered positive composition."""
    su = sa = sua = count = 0
    for bars in combinations(range(1, n), k - 1):
        prev = 0
        parts = []
        for b in (*bars, n):
            parts.append(b - prev)
            prev = b
        u = sum(p == 1 for p in parts)
        a = sum(parts[i] == parts[i + 1] for i in range(k - 1))
        su += u
        sa += a
        sua += u*a
        count += 1
    return Fraction(sua, count) - Fraction(su*sa, count*count)


def expected_sign(n, k):
    if k in (2, 3) and n % 2 == 0 and n >= (4 if k == 2 else 6):
        return -1
    if k == 4 and n % 2 == 0 and n >= 6:
        return 1
    if k >= 5 and n >= k + 2:
        return 1
    return 0


def run():
    checks = 0
    for n in range(1, 19):
        for k in range(1, n + 1):
            a, b, c = analytic_cov(n,k), counted_cov(n,k), brute_cov(n,k)
            assert a == b == c, (n, k, a, b, c)
            sign = (a > 0) - (a < 0)
            assert sign == expected_sign(n,k), (n,k,a)
            checks += 2
    for n in range(19, 141):
        for k in range(1, n + 1):
            a,b = analytic_cov(n,k), counted_cov(n,k)
            assert a == b, (n,k,a,b)
            assert (a>0)-(a<0) == expected_sign(n,k), (n,k,a)
            checks += 2
    assert analytic_cov(4,2) == Fraction(-2,9)
    assert analytic_cov(6,3) == Fraction(-2,25)
    assert analytic_cov(6,4) == Fraction(3,25)
    assert analytic_cov(7,4) == 0
    assert analytic_cov(7,5) == Fraction(8,45)
    checks += 5
    print(f"PASS: {checks} exact assertions; full composition enumeration n<=18; independent GF moment checks n<=140.")


if __name__ == "__main__":
    run()
