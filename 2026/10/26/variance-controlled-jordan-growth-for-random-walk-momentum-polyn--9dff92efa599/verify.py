#!/usr/bin/env python3
"""Exact finite sanity checks for the random-walk polynomial derivative recurrence.
The asymptotic theorem is proved in RESULT.md; finite checks do not prove it.
"""
from fractions import Fraction
from math import factorial


def falling(n, k):
    if k > n:
        return Fraction(0)
    out = 1
    for r in range(k):
        out *= n - r
    return Fraction(out)


def jets(p, N, K):
    m = len(p) - 1
    rows = [[falling(n, k) for k in range(K + 1)] for n in range(m)]
    for n in range(m - 1, N):
        row = []
        for k in range(K + 1):
            rhs = rows[n][k] + (k * rows[n][k - 1] if k else 0)
            rhs -= sum(p[j] * rows[n + 1 - j][k] for j in range(1, m + 1))
            row.append(rhs / p[0])
        rows.append(row)
    return rows


def main():
    examples = [
        ("Chebyshev sanity case", [Fraction(1, 2), Fraction(0), Fraction(1, 2)]),
        ("endpoint order three", [Fraction(2, 3), Fraction(0), Fraction(0), Fraction(1, 3)]),
        ("interior order four", [Fraction(3, 5), Fraction(0), Fraction(1, 4), Fraction(1, 10), Fraction(1, 20)]),
    ]
    for label, p in examples:
        m = len(p) - 1
        assert sum(p) == 1
        assert p[0] > 0 and p[1] == 0
        assert sum(Fraction(j) * p[j] for j in range(m + 1)) == 1
        sigma2 = sum(p[j] * Fraction((1 - j) ** 2) for j in range(m + 1))
        assert sigma2 > 0 and sigma2 <= m - 1
        D = jets(p, 80, 3)
        for n in range(m - 1, 80):
            for k in range(4):
                rhs = D[n][k] + (k * D[n][k - 1] if k else 0)
                lhs = sum(p[j] * D[n + 1 - j][k] for j in range(m + 1))
                assert lhs == rhs
        ratio = float(D[80][1] / (Fraction(80 * 80) / sigma2))
        assert 0.75 < ratio < 1.25
        if p[0] == Fraction(m - 1, m) and p[m] == Fraction(1, m) and all(p[j] == 0 for j in range(1, m)):
            assert sigma2 == m - 1
        print(f"CHECK_OK: {label}; m={m}; sigma2={sigma2}; first-derivative leading ratio at n=80={ratio:.6f}")
    print("VERIFY_OK: exact recurrence checks passed; finite values are not the proof of the asymptotic.")


if __name__ == "__main__":
    main()
