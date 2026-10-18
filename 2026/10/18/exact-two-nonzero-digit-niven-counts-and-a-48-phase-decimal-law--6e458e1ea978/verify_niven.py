#!/usr/bin/env python3
"""Exact arithmetic checks for two-nonzero-digit Niven counts."""
from collections import Counter
from fractions import Fraction
from math import gcd, lcm


def valuations(n, p):
    ans = 0
    while n % p == 0:
        ans += 1
        n //= p
    return ans


def primes(n):
    out = []
    trial = 2
    while trial * trial <= n:
        if n % trial == 0:
            out.append(trial)
            while n % trial == 0:
                n //= trial
        trial += 1
    if n > 1:
        out.append(n)
    return out


def invariants(b, a, c):
    m = a + c
    i_min = 0
    smooth = 1
    for p in primes(b):
        e = valuations(m, p)
        smooth *= p ** e
        r = valuations(a, p)
        if e > r:
            i_min = max(i_min, (e - r + valuations(b, p) - 1) // valuations(b, p))
    coprime_part = m // smooth
    h = coprime_part // gcd(coprime_part, c)
    order = 1
    if h > 1:
        state = b % h
        while state != 1:
            state = state * b % h
            order += 1
    return i_min, order


def F(period, N):
    q = max(0, (N - 1) // period)
    return q * N - period * q * (q + 1) // 2


def exact_count(b, L):
    return formula_count(b, L)


def formula_count(b, L):
    total = 0
    for a in range(1, b):
        for c in range(1, b):
            I, period = invariants(b, a, c)
            total += F(period, L - I)
    return total


def direct_count(b, L):
    total = 0
    for i in range(L):
        for j in range(i + 1, L):
            for a in range(1, b):
                for c in range(1, b):
                    total += (a * (b ** i) + c * (b ** j)) % (a + c) == 0
    return total


def coefficients(b):
    records = Counter(invariants(b, a, c) for a in range(1, b) for c in range(1, b))
    lead = sum((Fraction(n, 2 * period) for (I, period), n in records.items()), Fraction(0))
    linear = sum((n * (Fraction(I, period) + Fraction(1, 2)) for (I, period), n in records.items()), Fraction(0))
    return records, lead, linear


def main():
    expected = {(0, 1): 14, (0, 2): 8, (0, 6): 14, (0, 16): 2,
                (1, 1): 27, (1, 6): 2, (2, 1): 8,
                (3, 1): 4, (4, 1): 2}
    records, gamma, delta = coefficients(10)
    assert dict(records) == expected
    assert gamma == Fraction(1483, 48) and delta == Fraction(623, 6)
    assert sum(records.values()) == 81
    assert all(sum(n * F(period, L - I) for (I, period), n in records.items()) == formula_count(10, L) for L in range(1, 300))
    assert Fraction(2 * gamma, 81) == Fraction(1483, 1944)
    observed = [Fraction(formula_count(10, L)) - gamma * L * L + delta * L
                for L in range(4, 52)]
    assert all(observed[z] == Fraction(formula_count(10, z + 52)) - gamma * (z + 52)**2 + delta * (z + 52) for z in range(48))
    for d in (1, 2, 3, 4, 6, 8, 12, 16, 24):
        assert any(observed[z] != observed[z % d] for z in range(48)), d
    for L, expected_count in ((2, 14), (5, 362), (20, 10391), (100, 298685)):
        assert formula_count(10, L) == expected_count
    checks = 0
    for b in range(2, 15):
        for L in range(1, 12):
            a = direct_count(b, L)
            s = formula_count(b, L)
            assert a == s, (b, L, a, s)
            checks += 1
    for b in (2, 3, 4, 5, 6, 8, 10, 12):
        for a in range(1, b):
            for c in range(1, b):
                I, period = invariants(b, a, c)
                for i in range(9):
                    for j in range(i + 1, 15):
                        actual = (a * pow(b, i, a + c) + c * pow(b, j, a + c)) % (a + c) == 0
                        model = i >= I and (j - i) % period == 0
                        assert actual == model, (b, a, c, i, j)
    print('SPARSE_NIVEN_EXACT_REGRESSION_OK bases=2..14 lengths=1..11 comparisons=%d decimal_period=48' % checks)


if __name__ == '__main__':
    main()
