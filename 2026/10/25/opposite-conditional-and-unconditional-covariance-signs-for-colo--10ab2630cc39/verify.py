"""Exact checks of fixed-composition singleton-run covariance identities.

Run with Python 3.9+; no external packages are required.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def run_data(bits):
    n = len(bits)
    ones = zeros = 0
    runs = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and bits[j] == bits[i]:
            j += 1
        runs += 1
        if j == i + 1:
            if bits[i] == 1:
                ones += 1
            else:
                zeros += 1
        i = j
    return ones, zeros, runs


def covariance(records):
    size = len(records)
    return (Fraction(sum(x * y for x, y in records), size)
            - Fraction(sum(x for x, y in records) * sum(y for x, y in records), size * size))


def formulas(a, b):
    n = a + b
    ex = Fraction(a * b * (b + 1), n * (n - 1))
    ey = Fraction(a * b * (a + 1), n * (n - 1))
    exy = Fraction(a * b * ((a*b)**2 + a*b*(n-7) + 4),
                   n * (n-1) * (n-2) * (n-3))
    cov = Fraction(2*a*b*(a-1)*(b-1)*(a*b*(2*n-3)-2*n),
                   n*n*(n-1)**2*(n-2)*(n-3))
    return ex, ey, exy, cov


def conditional(a, b, r):
    if r % 2 == 0:
        return Fraction(0)
    t = (r - 1) // 2
    if t < 1:
        return Fraction(0)
    w1 = comb(a-1, t) * comb(b-1, t-1) if t <= a-1 and t-1 <= b-1 else 0
    w0 = comb(a-1, t-1) * comb(b-1, t) if t-1 <= a-1 and t <= b-1 else 0
    return Fraction(-4*t*t*w1*w0, (a-1)*(b-1)*(w1+w0)**2) if w1+w0 else None


def verify():
    assertions = 0
    cases = 0
    for n in range(4, 14):
        for a in range(2, n-1):
            b = n-a
            records = []
            grouped = {}
            for positions in combinations(range(n), a):
                P = set(positions)
                bits = [int(i in P) for i in range(n)]
                x, y, r = run_data(bits)
                records.append((x, y))
                grouped.setdefault(r, []).append((x, y))
                cases += 1
            size = len(records)
            ex, ey, exy, cov = formulas(a, b)
            for actual, expected in [
                (Fraction(sum(x for x,y in records), size), ex),
                (Fraction(sum(y for x,y in records), size), ey),
                (Fraction(sum(x*y for x,y in records), size), exy),
                (covariance(records), cov),
            ]:
                assert actual == expected, (n, a, actual, expected)
                assertions += 1
            assert cov > 0
            assertions += 1
            for r, group in grouped.items():
                expected = conditional(a, b, r)
                actual = covariance(group)
                assert actual == expected, (n,a,r,actual,expected)
                assertions += 1
                assert actual <= 0
                assertions += 1
                if r == 3:
                    assert actual == Fraction(-4, (n-2)**2)
                    assertions += 1
    for a in range(2, 50):
        for b in range(2, 50):
            ex, ey, exy, cov = formulas(a,b)
            assert exy-ex*ey == cov
            assert cov > 0
            assertions += 2
    print(f"PASS: {assertions} exact rational and sign assertions; {cases} binary words enumerated")

if __name__ == '__main__':
    verify()
