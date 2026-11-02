"""Exact finite checks and numerical diagnostics for the stated recursive-tree theorem.

Run: python verify.py
No third-party packages are required. Exhaustive checks are finite only; the
all-order stochastic and asymptotic claims rely on the written proofs.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product
from math import factorial, log, exp, pi


def mu(n, p):
    v = Q(1)
    for t in range(1, n):
        v *= 1 + p / t
    return v


def covariance(n, p):
    t_sum = sum((Q(1) / ((t + 1) * (t + p)) for t in range(1, n)), Q(0))
    return mu(n, p) * (Q(1, n) + (1 - p) * t_sum) - 1


def exact_distribution(n, p):
    a, b = p.numerator, p.denominator
    counts = defaultdict(int)
    total = factorial(n - 1) * b ** (n - 1)
    for parents in product(*(range(1, j) for j in range(2, n + 1))):
        d = sum(u == 1 for u in parents)
        for kept in product((0, 1), repeat=n - 1):
            connected = [False] * (n + 1)
            connected[1] = True
            s = 1
            w = 1
            for j, (u, bit) in enumerate(zip(parents, kept), start=2):
                w *= a if bit else (b - a)
                connected[j] = bool(bit and connected[u])
                s += int(connected[j])
            counts[d, s] += w
    assert sum(counts.values()) == total
    return counts, total


def test(n, p):
    cnt, total = exact_distribution(n, p)
    E_D = sum(Q(d * w, total) for (d, s), w in cnt.items())
    E_S = sum(Q(s * w, total) for (d, s), w in cnt.items())
    E_DS = sum(Q(d * s * w, total) for (d, s), w in cnt.items())
    E_S2 = sum(Q(s * s * w, total) for (d, s), w in cnt.items())
    h = sum((Q(1, t) for t in range(1, n)), Q(0))
    assert E_D == h
    assert E_S == mu(n, p)
    assert E_DS - E_D * E_S == covariance(n, p)
    assert E_S2 == 2 * mu(n, 2 * p) - mu(n, p)
    # Every conditional upper tail is weakly increasing with the original
    # root degree; the tail at 2 is strictly increasing for 0 < p < 1.
    for d in range(1, n - 1):
        z0 = sum(w for (dd, s), w in cnt.items() if dd == d)
        z1 = sum(w for (dd, s), w in cnt.items() if dd == d + 1)
        for threshold in range(1, n + 1):
            tail0 = Q(sum(w for (dd, s), w in cnt.items()
                          if dd == d and s >= threshold), z0)
            tail1 = Q(sum(w for (dd, s), w in cnt.items()
                          if dd == d + 1 and s >= threshold), z1)
            assert tail0 <= tail1, (n, p, d, threshold, tail0, tail1)
            if threshold == 2:
                assert tail0 < tail1
    return len(cnt), total


def test_local_cov(n, p):
    # Independent moment recursion checks every local covariance contribution.
    m = [Q(1)]
    for t in range(1, n):
        m.append(m[-1] * (1 + p / t))
    pieces = []
    for j in range(2, n + 1):
        t = j - 1
        pieces.append(p * m[-1] / (t * m[j - 1]) * (1 - m[j - 2] / t))
    assert sum(pieces) == covariance(n, p)
    assert pieces[0] == 0
    if Q(0) < p < Q(1):
        assert all(v > 0 for v in pieces[1:])


def test_recurrence(n, p):
    # Independent exact recurrence for E[D*S] with the filtration.
    m = Q(1)
    D = Q(0)
    mixed = Q(0)
    for t in range(1, n):
        mixed = (1 + p / t) * mixed + m / t + p / t
        D += Q(1, t)
        m *= (1 + p / t)
    assert mixed - D * m == covariance(n, p)


def diagnostics():
    # Only numerical asymptotic illustrations, not proofs of an infinite claim.
    c = pi * pi / 6 - 1
    for n in (100, 1000, 10000):
        L = log(n)
        p = 1 - 1 / L
        acc_mu = exp(sum(log(1 + p / t) for t in range(1, n)))
        t_sum = sum(1 / ((t + 1) * (t + p)) for t in range(1, n))
        actual = (acc_mu * (1 / n + (1 - p) * t_sum) - 1) * L / n
        print('critical-window diagnostic', n, round(actual, 7),
              'limiting value', round(c / exp(1), 7))


def main():
    completed = 0
    for n in range(3, 8):
        for p in (Q(1, 3), Q(1, 2), Q(2, 3)):
            test(n, p)
            test_local_cov(n, p)
            test_recurrence(n, p)
            completed += 1
    test(8, Q(1, 2))
    test_local_cov(8, Q(1, 2))
    test_recurrence(8, Q(1, 2))
    completed += 1
    for n in range(3, 101):
        for p in (Q(1, 3), Q(1, 2), Q(2, 3)):
            test_local_cov(n, p)
            test_recurrence(n, p)
    diagnostics()
    print('PASS:', completed, 'exhaustive rational models,',
          98 * 3, 'additional exact recursion comparisons')

if __name__ == '__main__':
    main()
