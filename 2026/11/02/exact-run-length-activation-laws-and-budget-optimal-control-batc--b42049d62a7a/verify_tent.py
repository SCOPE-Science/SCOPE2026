#!/usr/bin/env python3
"""Exact, standalone sample verification of the finite-horizon control theorem."""
from fractions import Fraction
from itertools import combinations
from math import prod


def tent(x):
    return 1 - 2 * abs(x)


def runs_of(schedule):
    runs = []
    for t in sorted(schedule):
        if runs and runs[-1][-1] + 1 == t:
            runs[-1].append(t)
        else:
            runs.append([t])
    return runs


def predicted(schedule):
    return prod((Fraction(len(r)+2, 2**(len(r)+1)) for r in runs_of(schedule)),
                start=Fraction(1))


def direct_survival(schedule, horizon):
    """One exact rational interior sample per depth-(horizon+2) cylinder."""
    total = 2**(horizon+2)
    count = 0
    schedule = set(schedule)
    for j in range(total):
        x = Fraction(-1, 1) + Fraction(2*j+1, total)
        safe = True
        for n in range(horizon):
            if n in schedule and abs(x) < Fraction(1, 4):
                safe = False
                break
            x = tent(x)
        count += int(safe)
    return Fraction(count, total)


def bounds(n, k):
    r = min(k, n-k+1)
    a, b = divmod(k, r)
    minimum = Fraction(k+2, 2**(k+1))
    maximum = Fraction(a+2, 2**(a+1))**(r-b) * Fraction(a+3, 2**(a+2))**b
    return minimum, maximum


def main():
    patterns = 0
    checks = 0
    for n in range(1, 9):
        for mask in range(1 << n):
            schedule = [j for j in range(n) if (mask >> j) & 1]
            assert predicted(schedule) == direct_survival(schedule, n), (n, mask)
            patterns += 1
        for k in range(1, n+1):
            candidates = [predicted(seq) for seq in combinations(range(n), k)]
            lo, hi = bounds(n, k)
            assert min(candidates) == lo and max(candidates) == hi, (n, k)
            checks += 1
    assert predicted([0, 1, 2]) == Fraction(5, 16)
    assert predicted([0, 2, 4]) == Fraction(27, 64)
    print(f'PASS: {patterns} schedules (horizons 1..8), {checks} budget extremum comparisons, exact rational arithmetic')


if __name__ == '__main__':
    main()
