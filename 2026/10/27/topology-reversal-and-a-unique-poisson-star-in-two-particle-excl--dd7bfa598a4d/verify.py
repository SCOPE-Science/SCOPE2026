"""Independent full-configuration checks for two-particle exclusion activity."""
import itertools
from fractions import Fraction
from math import comb

import numpy as np
import sympy as sp


def closed_form(m, n):
    N = m + n
    difference = m - n
    f = Fraction(N * N + difference * difference * (N * N - 6 * N + 4), N * N * (N - 1) ** 2) + 1
    rate = Fraction(4 * m * n * (N - 2), N * (N - 1))
    return rate, f


def independent_full_configuration(m, n):
    N = m + n
    states = list(itertools.combinations(range(N), 2))
    look = {s: k for k, s in enumerate(states)}
    Q = np.zeros((len(states), len(states)), dtype=float)
    for i, state in enumerate(states):
        occupied = set(state)
        for old in state:
            destinations = range(m, N) if old < m else range(m)
            for new in destinations:
                if new in occupied:
                    continue
                target = tuple(sorted((occupied - {old}) | {new}))
                Q[i, look[target]] += 1.0
        Q[i, i] = -sum(Q[i])
    pi = np.full(len(states), 1 / len(states))
    rates = -np.diag(Q)
    mu = pi @ rates
    A = np.vstack((Q[:-1, :], pi))
    rhs = np.r_[np.full(len(states) - 1, mu) - rates[:-1], 0]
    h = np.linalg.solve(A, rhs)
    W = Q + np.diag(rates)
    f = 1 + (2 / mu) * (pi @ W @ h)
    return mu, f


def check():
    total = 0
    for m in range(1, 7):
        for n in range(1, 7):
            if m + n < 3:
                continue
            expect_mu, expect_f = closed_form(m, n)
            actual_mu, actual_f = independent_full_configuration(m, n)
            assert abs(actual_mu - float(expect_mu)) < 1e-10, (m, n, actual_mu, expect_mu)
            assert abs(actual_f - float(expect_f)) < 1e-10, (m, n, actual_f, expect_f)
            total += 1

    m, n = sp.symbols('m n', positive=True)
    N = m + n
    rate = 4 * m * n * (N - 2) / (N * (N - 1))
    pi0 = n * (n - 1) / (N * (N - 1))
    pi2 = m * (m - 1) / (N * (N - 1))
    dirichlet = (2 / rate) * (
        2 * m * pi0 * (1 - rate / (2 * m)) ** 2
        + 2 * n * pi2 * (1 - rate / (2 * n)) ** 2
    )
    expected_excess = (N**2 + (m - n) ** 2 * (N**2 - 6 * N + 4)) / (N**2 * (N - 1) ** 2)
    assert sp.simplify(dirichlet - expected_excess) == 0
    assert sp.simplify(expected_excess.subs(m, 1) - (n - 3) ** 2 / (n + 1) ** 2) == 0

    topology_count = 0
    for N0 in range(3, 31):
        table = [(m0, closed_form(m0, N0 - m0)[1]) for m0 in range(1, N0 // 2 + 1)]
        star = table[0][1]
        balanced = table[-1][1]
        if N0 in (4, 5):
            assert star == min(f for _, f in table)
            assert balanced == max(f for _, f in table)
        elif N0 >= 6:
            assert star == max(f for _, f in table)
            assert balanced == min(f for _, f in table)
        if N0 == 4:
            assert star == 1
        topology_count += 1
    print(f'PASS: {total} full-generator comparisons, 2 exact symbolic checks, {topology_count} finite topology tests.')


if __name__ == '__main__':
    check()
