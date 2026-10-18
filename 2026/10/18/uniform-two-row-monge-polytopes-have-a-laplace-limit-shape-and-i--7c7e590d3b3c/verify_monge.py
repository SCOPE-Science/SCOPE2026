#!/usr/bin/env python3
"""Reproducible finite checks for the limit-shape identities of two-row Monge matrices.

Requires Python 3 standard library only. Analytical asymptotics are established in
RESULT.md; finite experiments are numerical corroboration, not proofs.
"""
import itertools
import math
import random
from fractions import Fraction


def sample(n, rng):
    pairs = [(rng.expovariate(1), rng.expovariate(1)) for _ in range(n)]
    pairs.sort(key=lambda z: z[0] - z[1])
    total = sum(u + v for u, v in pairs)
    return [u / total for u, v in pairs], [v / total for u, v in pairs]


def profile_a(t):
    if t <= .5:
        return t / 4
    if t >= 1:
        return .5
    return (3 * t - 1) / 4 + (1 - t) * math.log(2 * (1 - t)) / 2


def profile_b(t):
    if t <= 0:
        return 0.
    if t <= .5:
        return 3 * t / 4 - t * math.log(2 * t) / 2
    return (t + 1) / 4


def exact_max_laplace_mean(n):
    return sum((Fraction((-1) ** (j + 1) * math.comb(n, j), j * 2 ** j)
                for j in range(1, n + 1)), Fraction(0)) - Fraction(1, n * 2 ** n)


def run():
    rng = random.Random(104729)
    # The strict ordering regions partition the open simplex into n! equal-volume pieces.
    for n in range(2, 8):
        x = [rng.random() for _ in range(n)]
        unique = sum(all(x[p[j]] < x[p[j + 1]] for j in range(n - 1))
                     for p in itertools.permutations(range(n)))
        assert unique == 1
    print('EXACT order-region partition: n=2,...,7 PASS')

    for n in (2, 3, 5, 11):
        reps = 20000
        row1 = []
        lastdiff = []
        for _ in range(reps):
            a, b = sample(n, rng)
            assert abs(sum(a) + sum(b) - 1) < 1e-12
            assert all(a[i] - b[i] <= a[i + 1] - b[i + 1] + 1e-14
                       for i in range(n - 1))
            row1.append(sum(a))
            lastdiff.append(a[-1] - b[-1])
        mean_r = sum(row1) / reps
        variance_r = sum((r - mean_r) ** 2 for r in row1) / reps
        expected_var = 1 / (4 * (2 * n + 1))
        expected_last = float(exact_max_laplace_mean(n)) / (2 * n)
        est_last = sum(lastdiff) / reps
        se_last = math.sqrt(sum((x - est_last) ** 2 for x in lastdiff) / reps / reps)
        assert abs(mean_r - .5) < .016
        assert abs(variance_r - expected_var) < .006
        assert abs(est_last - expected_last) < 7 * se_last
        print('n=%d beta variance %.7f (exact %.7f), last contrast %.7f (exact %.7f): PASS' %
              (n, variance_r, expected_var, est_last, expected_last))

    n = 40000
    a, b = sample(n, rng)
    cumul_a = cumul_b = 0.
    maxerr = 0.
    for j in range(n + 1):
        t = j / n
        maxerr = max(maxerr, abs(cumul_a - profile_a(t)),
                     abs(cumul_b - profile_b(t)))
        if j < n:
            cumul_a += a[j]
            cumul_b += b[j]
    assert maxerr < .025
    print('n=%d full two-row limit-shape error %.7f: PASS' % (n, maxerr))

    # A numerical check of the two independent extreme-coordinate Gumbel laws.
    n, reps = 240, 3000
    both_nonpositive = 0
    right_nonpositive = 0
    for _ in range(reps):
        a, b = sample(n, rng)
        x = 2 * n * (a[-1] - b[-1]) - math.log(n / 2)
        y = -2 * n * (a[0] - b[0]) - math.log(n / 2)
        right_nonpositive += (x <= 0)
        both_nonpositive += (x <= 0 and y <= 0)
    g1 = math.exp(-1)
    g2 = math.exp(-2)
    assert abs(right_nonpositive / reps - g1) < .055
    assert abs(both_nonpositive / reps - g2) < .055
    print('joint Gumbel CDF at zero %.5f (limit %.5f): PASS' %
          (both_nonpositive / reps, g2))
    print('All finite reproducible checks PASS')


if __name__ == '__main__':
    run()
