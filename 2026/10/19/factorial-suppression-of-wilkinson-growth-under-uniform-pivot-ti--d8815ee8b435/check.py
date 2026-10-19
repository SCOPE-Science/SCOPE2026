#!/usr/bin/env python3
"""Exact finite-size verification of uniformly tie-broken Wilkinson pivoting."""
from collections import defaultdict
from fractions import Fraction
from math import factorial


def wilkinson(n):
    return tuple(tuple(Fraction(1 if j == n - 1 or i == j else
                                -1 if i > j else 0)
                       for j in range(n)) for i in range(n))


def advance(a, pivot):
    b = list(a)
    b[0], b[pivot] = b[pivot], b[0]
    if len(b) == 1:
        return (), max(abs(x) for row in b for x in row)
    c = tuple(tuple(b[i][j] - b[i][0] * b[0][j] / b[0][0]
                    for j in range(1, len(b)))
              for i in range(1, len(b)))
    return c, max(abs(x) for row in b for x in row)


def exact_pmf(n):
    # States retain their own growth maxima: merging differently grown
    # histories by Schur matrix alone would be an unsound enumeration.
    states = {(wilkinson(n), Fraction(1)): Fraction(1)}
    checks = 0
    for step in range(n - 1):
        nxt = defaultdict(Fraction)
        for (a, peak), mass in states.items():
            candidate_max = max(abs(row[0]) for row in a)
            ties = [i for i, row in enumerate(a)
                    if abs(row[0]) == candidate_max]
            assert len(ties) > 0 and candidate_max != 0
            for i in ties:
                sub, upper_max = advance(a, i)
                new_peak = max(peak, upper_max,
                               *(abs(x) for row in sub for x in row))
                nxt[(sub, new_peak)] += mass / len(ties)
                checks += 1
        states = nxt
        assert sum(states.values()) == 1
    pmf = defaultdict(Fraction)
    for (a, peak), mass in states.items():
        assert len(a) == 1
        pmf[peak] += mass
    return dict(pmf), checks


def falling(n, t):
    x = 1
    for k in range(t):
        x *= n - k
    return x


def law(n):
    p = {Fraction(2 ** j): Fraction(n - j, falling(n, j))
         for j in range(1, n - 1)}
    p[Fraction(2 ** (n - 1))] = Fraction(2, factorial(n))
    return p


def run():
    total = 0
    for n in range(2, 10):
        calculated, checks = exact_pmf(n)
        expected = law(n)
        assert calculated == expected, (n, calculated, expected)
        assert sum(calculated.values()) == 1
        mean = sum(x * weight for x, weight in calculated.items())
        expected_mean = Fraction(2) + sum(
            Fraction(2 ** t, falling(n, t)) for t in range(1, n - 1))
        assert mean == expected_mean
        for j in range(1, n):
            survival = sum(v for x, v in calculated.items()
                           if x >= 2 ** j)
            assert survival == Fraction(1, falling(n, j - 1))
        total += checks
        print('n =', n, 'branches =', checks,
              'E(growth) =', str(mean), 'max-event =',
              str(expected[Fraction(2 ** (n - 1))]))
    print('EXACT_CHECKS_OK', total)

if __name__ == '__main__':
    run()
