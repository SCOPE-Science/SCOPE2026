#!/usr/bin/env python3
"""Exact-rational finite-dimensional checks of the utility-biased gossip limit constants.

Run with Python 3.10+ using only the standard library. These checks are
algebraic witnesses, not a substitute for the stochastic-limit proof.
"""
from fractions import Fraction as F
from itertools import combinations


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def add(a, b):
    return [[v + b[i][j] for j, v in enumerate(row)]
            for i, row in enumerate(a)]


def scale(c, a):
    return [[c * v for v in row] for row in a]


def check(n, mu):
    assert n >= 2 and F(0) < mu < F(1)
    I = [[F(i == j) for j in range(n)] for i in range(n)]
    P = [[F(i == j) - F(1, n) for j in range(n)] for i in range(n)]
    pairs = list(combinations(range(n), 2))
    cp = F(n - 1, 2 * n) / (mu * (1 - mu))
    C = scale(cp, P)
    avg = [[F(0) for _ in range(n)] for _ in range(n)]
    # Invariant covariance: C=E[A C A^T + P D_ij P].
    for i, j in pairs:
        v = [F(k == i) - F(k == j) for k in range(n)]
        A = [[I[k][l] - mu * v[k] * v[l] for l in range(n)] for k in range(n)]
        D = [[F(k == l and k in (i, j)) for l in range(n)] for k in range(n)]
        term = add(mm(mm(A, C), transpose(A)), mm(mm(P, D), P))
        avg = add(avg, term)
    assert scale(F(1, len(pairs)), avg) == C

    y = [F(k + 1) - F(n + 1, 2) for k in range(n)]
    s = sum(t*t for t in y)
    pair_second = sum((y[i]-y[j])**2 for i,j in pairs) / len(pairs)
    assert pair_second == 2*s/F(n-1)
    a = 1-4*mu*(1-mu)/F(n-1)
    assert 0 <= a < 1
    expected_s = F((n-1)**2, 2*n)/(mu*(1-mu))
    assert sum(C[k][k] for k in range(n)) == expected_s
    stationary_pair = 2*expected_s/F(n-1)
    assert stationary_pair == F(n-1,n)/(mu*(1-mu))
    # With micro-time k, mean drift = delta^2 * b * (log U)' + o(delta^2)
    b_micro = mu * stationary_pair/n
    assert b_micro == F(n-1, n*n)/(1-mu)
    # Physical time k/n accelerated by delta^2:
    b_physical = n*b_micro
    D_physical = F(1,n)
    inverse_temperature = b_physical / D_physical
    assert b_physical == F(n-1,n)/(1-mu)
    assert inverse_temperature == F(n-1)/(1-mu)
    # The limiting exponent is N-1 rather than N, divided by 1-mu.
    assert (F(n)/(1-mu)-inverse_temperature) == F(1)/(1-mu)
    return cp, inverse_temperature


if __name__ == '__main__':
    count = 0
    for n in range(2, 11):
        for mu in (F(1, 7), F(1, 4), F(1, 2), F(3, 4), F(6, 7)):
            check(n, mu)
            count += 1
    print(f'VERIFY_OK: {count} exact rational covariance, mixing and inverse-temperature checks')
