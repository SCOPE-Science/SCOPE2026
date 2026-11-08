#!/usr/bin/env python3
"""Exact, self-contained finite checks for a three-category occupancy theorem."""
from math import comb, factorial
from fractions import Fraction

P = (Fraction(7, 10), Fraction(1, 5), Fraction(1, 10))
N = 16


def closed_cov(p, n, r):
    qsum = sum((1 - x) ** n for x in p)
    return comb(n, r) * sum(
        p[j] ** r * (
            (1 - p[j]) ** (n - r) * qsum
            - sum((1 - p[i] - p[j]) ** (n - r)
                  for i in range(len(p)) if i != j)
        ) for j in range(len(p))
    )


def independent_cov(p, n):
    k = len(p)
    vectors = []
    def visit(prefix, remaining):
        if len(prefix) == k - 1:
            tup = prefix + (remaining,)
            prob = Fraction(factorial(n), 1)
            for v, x in zip(tup, p):
                prob *= x ** v / factorial(v)
            vectors.append((prob, tup))
        else:
            for t in range(remaining + 1):
                visit(prefix + (t,), remaining - t)
    visit((), n)
    assert sum(prob for prob, _ in vectors) == 1
    ek = sum(prob * sum(v > 0 for v in x) for prob, x in vectors)
    ans = []
    for r in range(1, n + 1):
        ef = sum(prob * sum(v == r for v in x) for prob, x in vectors)
        ekf = sum(prob * sum(v > 0 for v in x) * sum(v == r for v in x)
                  for prob, x in vectors)
        ans.append(ekf - ek * ef)
    return ans, len(vectors)


def test():
    a, num = independent_cov(P, N)
    assert num == 153
    assert all(a[r - 1] == closed_cov(P, N, r) for r in range(1, N + 1))
    signs = ''.join('+' if x > 0 else '-' if x < 0 else '0' for x in a)
    assert signs == '+++++-++++++----', signs
    expected = {
        5: Fraction(491477014571896186404867387,1562500000000000000000000000000),
        6: Fraction(-3969577919885613399780795379,3125000000000000000000000000000),
        7: Fraction(565425373537234919456753577,312500000000000000000000000000),
        12:Fraction(909901009394535995895709651,1250000000000000000000000000000),
        13:Fraction(-5488321470389007696069451107,312500000000000000000000000000),
    }
    for r, v in expected.items():
        assert a[r - 1] == v, r
    # All two-category index covariances are positive until the terminal count.
    for n in range(2, 11):
        for t in range(1, 10):
            p = (Fraction(t, 10), Fraction(10 - t, 10))
            b, cnt = independent_cov(p, n)
            assert cnt == n + 1
            assert all(x > 0 for x in b[:-1]), (n, p)
            assert b[-1] < 0, (n, p)
            assert all(b[r - 1] == closed_cov(p, n, r) for r in range(1, n + 1))
    print('VERIFY_OK: 153 three-category outcomes, 16 covariances, 5 boundary fractions, two-category exact checks')

if __name__ == '__main__':
    test()
