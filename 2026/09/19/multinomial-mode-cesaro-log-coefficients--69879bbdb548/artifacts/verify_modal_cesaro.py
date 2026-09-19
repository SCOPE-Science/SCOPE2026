#!/usr/bin/env python3
"""Verify Cesaro means of logarithmic multinomial-mode coefficients.

The script uses only Python's standard library.  It generates the unique
Jefferson/D'Hondt allocation sequentially for a fixed generic probability
vector, evaluates the Bernoulli-polynomial coefficient formula at each mode,
and compares empirical Cesaro means with the closed Stirling-number formula.
"""

from fractions import Fraction
from math import comb, factorial, pi, sqrt
import sys


def bernoulli_numbers(mmax):
    B = [Fraction(1)]
    for m in range(1, mmax + 1):
        s = sum(Fraction(comb(m + 1, j)) * B[j] for j in range(m))
        B.append(-s / Fraction(m + 1))
    return B


def bernoulli_poly(m, x, B):
    return sum(comb(m, j) * float(B[j]) * x ** (m - j) for j in range(m + 1))


def stirling2(n, r):
    row = [0] * (r + 1)
    row[0] = 1
    for i in range(1, n + 1):
        new = [0] * (r + 1)
        for j in range(1, min(i, r) + 1):
            new[j] = row[j - 1] + j * row[j]
        row = new
    return row[r]


def A(m, n):
    return Fraction(
        factorial(m) * factorial(n - 2) * stirling2(m + n - 1, n - 1),
        factorial(m + n - 2),
    )


def theory_cbar(k, n, B):
    m = k + 1
    return Fraction((-1) ** (k + 1), k * (k + 1)) * (B[m] - A(m, n))


def coefficient(k, t, p, B):
    m = k + 1
    s = sum((p[i] ** (-k)) * bernoulli_poly(m, t[i] + 1.0, B) for i in range(len(p)))
    return ((-1) ** (k + 1)) * (float(B[m]) - s) / (k * (k + 1))


def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 300000
    p = [sqrt(2.0) / 4.0, pi / 12.0]
    p.append(1.0 - p[0] - p[1])
    n = len(p)
    K = 4
    B = bernoulli_numbers(K + 1)
    seats = [0] * n
    sums = [0.0] * K

    for N in range(1, M + 1):
        j = max(range(n), key=lambda i: p[i] / (seats[i] + 1))
        seats[j] += 1
        t = [seats[i] - N * p[i] for i in range(n)]
        for k in range(1, K + 1):
            sums[k - 1] += coefficient(k, t, p, B)

    print(f"Nmax={M}")
    print("p=" + repr(p))
    for k in range(1, K + 1):
        th = theory_cbar(k, n, B)
        emp = sums[k - 1] / M
        print(
            f"k={k} theory={float(th): .12f} exact={th} "
            f"empirical={emp: .12f} error={emp-float(th): .3e}"
        )


if __name__ == "__main__":
    main()
