#!/usr/bin/env python3
"""Reproduce finite checks for a dyadic Franel convolution valuation theorem.

Only the mathematical proof establishes the infinite range.
"""
from fractions import Fraction
from math import comb, factorial


def v2(a):
    if a == 0:
        raise ValueError("valuation of zero is not finite")
    a = abs(a)
    return (a & -a).bit_length() - 1


def weight(a):
    return a.bit_count()


def franel_by_recurrence(N):
    f = [1, 2]
    for m in range(1, N - 1):
        z = (7 * m * m + 7 * m + 2) * f[m] + 8 * m * m * f[m - 1]
        assert z % (m + 1) ** 2 == 0
        f.append(z // (m + 1) ** 2)
    return f[:N]


def direct_sum(n, f):
    a = 0
    for k in range(n):
        a = -16 * a + (3 * k + 1) * comb(2 * k, k) * f[k]
    return a


def guo_quotient(n):
    q = Fraction(0)
    for j in range(1, n + 1):
        k = n - j
        B = factorial(3 * n - 2 * j) // (factorial(j) * factorial(k) ** 3)
        q += Fraction((-1) ** (j + 1) * j * (4 ** j) * B, 8 * (2 * k + 1))
    return q


def term_via_legendre(n, j):
    k = n - j
    vb = weight(j) + 3 * weight(k) - weight(3 * n - 2 * j)
    return vb + v2(j) + 2 * j - 3


# Distinct exact Franel formula and recurrence, including the small boundary.
f = franel_by_recurrence(1024)
for n in range(0, 24):
    assert f[n] == sum(comb(n, k) ** 3 for k in range(n + 1))
assert direct_sum(2, f) == 0

# Published identity, checked by two independent finite expressions.
for n in range(2, 27):
    S = direct_sum(n, f)
    denom = n * comb(2 * n, n)
    assert S % denom == 0
    assert guo_quotient(n) == Fraction(S, denom)

# Inspect the exact valuation of each transformed summand (no cancellation
# used except the explicitly excluded n=2 case).
for r in range(2, 13):
    n = 1 << r
    low = []
    for j in range(1, n + 1):
        v = term_via_legendre(n, j)
        if j <= n // 2:
            assert v == 2 * r + 2 * j - 2 - weight(j - 1)
        if v == 2 * r:
            low.append(j)
        if j > 1:
            assert v >= 2 * r + 1
    assert low == [1]

# Exact direct convolution at several dyadic heights, independent of the
# transformed-summand calculation above.
for r in range(2, 11):
    n = 1 << r
    S = direct_sum(n, f)
    assert v2(S) == 3 * r + 1
    assert S % (1 << (3 * r + 2)) == (1 << (3 * r + 1))
    assert v2(S // (n * comb(2 * n, n))) == 2 * r

print('VERIFY_OK')
