#!/usr/bin/env python3
"""Reproduce finite checks for Poisson thresholds of rook-graph total domination.

Python 3 standard library only. The exact tests check the original open-neighbor
rule, while randomized tests are diagnostics, not a proof of any limit.
"""
from math import exp, factorial, log
from random import Random


def original_rule(n, occupied, k):
    for i in range(n):
        for j in range(n):
            defenders = sum((i == x or j == y) and (i, j) != (x, y)
                            for x, y in occupied)
            if defenders < k:
                return False
    return True


def row_column_rule(n, occupied, k):
    drow = [0] * n
    dcol = [0] * n
    for i, j in occupied:
        drow[i] += 1
        dcol[j] += 1
    return all(drow[i] + dcol[j] - 2 * ((i, j) in occupied) >= k
               for i in range(n) for j in range(n))


def finite_exact():
    tests = 0
    for n in (2, 3):
        for mask in range(1 << (n * n)):
            occupied = {(i, j) for i in range(n) for j in range(n)
                        if (mask >> (i * n + j)) & 1}
            for k in range(1, 2 * n):
                assert original_rule(n, occupied, k) == row_column_rule(n, occupied, k)
                tests += 1
    return tests


def sampled(n, r, trials, seed):
    rng = Random(seed + 100 * n + r)
    p = (log(n) + (r - 1) * log(log(n))) / n
    counts = [0, 0, 0, 0]
    for _ in range(trials):
        row = [0] * n
        col = [0] * n
        occupied = set()
        for i in range(n):
            for j in range(n):
                if rng.random() < p:
                    row[i] += 1
                    col[j] += 1
                    occupied.add((i, j))
        odd = even = True
        for i in range(n):
            for j in range(n):
                # Calculate defenders directly from coordinate degrees.
                v = row[i] + col[j]
                if (i, j) in occupied:
                    v -= 2
                if v < 2 * r - 1:
                    odd = False
                if v < 2 * r:
                    even = False
        low_rows = sum(d == r - 1 for d in row)
        low_cols = sum(d == r - 1 for d in col)
        pred_odd = (low_rows == 0 or low_cols == 0)
        pred_even = (low_rows == 0 and low_cols == 0)
        counts[0] += odd
        counts[1] += even
        counts[2] += odd != pred_odd
        counts[3] += even != pred_even
    lam = 1 / factorial(r - 1)
    pred_odd = 2 * exp(-lam) - exp(-2 * lam)
    pred_even = exp(-2 * lam)
    return {'n': n, 'r': r, 'trials': trials,
            'odd_frequency': round(counts[0] / trials, 4),
            'even_frequency': round(counts[1] / trials, 4),
            'limiting_odd': round(pred_odd, 4),
            'limiting_even': round(pred_even, 4),
            'odd_surrogate_disagreements': counts[2],
            'even_surrogate_disagreements': counts[3]}


if __name__ == '__main__':
    print('Exact adjacency comparisons:', finite_exact())
    # A modest diagnostic simulation. No finite sample is used to infer a limit.
    for n, trials in ((80, 200), (180, 120)):
        for r in (1, 2):
            print(sampled(n, r, trials, 20261025))
