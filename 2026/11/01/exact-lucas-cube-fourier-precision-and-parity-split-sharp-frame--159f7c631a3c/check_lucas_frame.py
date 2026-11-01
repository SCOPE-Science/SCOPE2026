#!/usr/bin/env python3
"""Independent tests for centered coordinate sampling on cyclic hard-core strings.

Uses Python standard library only. The finite tests corroborate, but do not
replace, the all-n transfer-matrix and positivity arguments in RESULT.md.
"""
from fractions import Fraction
from math import cos, pi, sqrt


def fibs(n):
    f = [0, 1]
    for _ in range(n):
        f.append(f[-1] + f[-2])
    return f


def moment_row(n):
    f = fibs(n + 2)
    l = f[n - 1] + f[n + 1]
    p = Fraction(f[n - 1], l)
    row = [p - p * p]
    for d in range(1, n):
        joint = Fraction(0) if d in (1, n - 1) else Fraction(f[d - 1] * f[n - d - 1], l)
        row.append(joint - p * p)
    return row


def direct_row(n):
    accepted = [mask for mask in range(1 << n)
                if mask & (mask << 1) == 0
                and not (mask & 1 and mask & (1 << (n - 1)))]
    z = len(accepted)
    p = Fraction(sum(mask & 1 for mask in accepted), z)
    return z, [Fraction(sum((mask & 1) and (mask & (1 << d)) != 0
                             for mask in accepted), z) - p * p
               for d in range(n)]


def spectrum(n, k):
    r = (sqrt(5) - 3) / 2
    b = (1 - r * r) * (1 - r ** n) / (5 * (1 + r ** n))
    result = b / (1 - 2 * r * cos(2 * pi * k / n) + r * r)
    if k == 0:
        result += n * r ** n / (5 * (1 + r ** n) ** 2)
    return result


def precision(n, k, j):
    r = (sqrt(5) - 3) / 2
    s = -r
    b = (1 - s * s) * (1 - r ** n) / (5 * (1 + r ** n))
    base = (1 + s * s) * (k == j) + s * ((k - j) % n in (1, n - 1))
    delta = (1 / spectrum(n, 0) - (1 + s) ** 2 / b) / n
    return base / b + delta


def main():
    exact_comparisons = 0
    dft_comparisons = 0
    inverse_comparisons = 0
    extremum_comparisons = 0
    for n in range(5, 17):
        z, observed = direct_row(n)
        f = fibs(n + 2)
        assert z == f[n - 1] + f[n + 1]
        formula = moment_row(n)
        assert observed == formula, (n, observed, formula)
        exact_comparisons += n + 1
    for n in range(5, 51):
        row = moment_row(n)
        vals = []
        for k in range(n):
            observed = sum(float(row[d]) * cos(2 * pi * k * d / n) for d in range(n))
            target = spectrum(n, k)
            assert abs(observed - target) < 1e-10, (n, k, observed, target)
            dft_comparisons += 1
            vals.append(target)
        if n <= 34:
            assert vals[0] < vals[1]
            assert vals[n // 2] >= max(vals) - 1e-12
            assert vals[n // 2] / vals[0] < 5
            extremum_comparisons += 3
    for n in range(5, 19):
        cov = moment_row(n)
        q = [[precision(n, i, j) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                got = sum(float(cov[(i - k) % n]) * q[k][j] for k in range(n))
                assert abs(got - (i == j)) < 1e-8, (n, i, j, got)
                inverse_comparisons += 1
    # Exact inequalities supporting uniform finite-order strictness.
    assert 6**3 * Fraction(2, 5)**6 < 1
    assert 7**3 * Fraction(2, 5)**7 < Fraction(8, 7) * (1 - Fraction(2, 5)**7)**2
    # Leading asymptotics on the two parity subsequences.
    s = (3 - sqrt(5)) / 2
    for n in (15, 17, 19, 21, 23, 25):
        deficit = 5 - spectrum(n, n // 2) / spectrum(n, 0)
        assert 0 < deficit < 5
        assert abs(deficit / (5 * pi * pi / n**2) - 1) < 0.24
    for n in (6, 8, 10, 12, 14, 16, 18, 20):
        deficit = 5 - spectrum(n, n // 2) / spectrum(n, 0)
        assert 0 < deficit < 5
        assert abs(deficit / (5 * sqrt(5) * n * s**n) - 1) < 0.25
    print("PASS: exact independent-set moment comparisons", exact_comparisons)
    print("PASS: direct DFT versus closed spectra", dft_comparisons)
    print("PASS: inverse-covariance precision identity entries", inverse_comparisons)
    print("PASS: finite-mode eigenvalue extremum comparisons", extremum_comparisons)
    print("PASS: rational uniform-bound inequalities and parity asymptotic tests")


if __name__ == '__main__':
    main()
