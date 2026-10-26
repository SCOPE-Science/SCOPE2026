"""Exact finite checks for quadratic weighted-Bergman Hankel channels.

Requires only the Python standard library. The universal result is proved
analytically in RESULT.md; this script checks finite instances.
"""
from fractions import Fraction as F
from math import isclose, sqrt


def moment(beta, n):
    ans = F(1)
    for j in range(n):
        ans *= F(j + 1) / (beta + j)
    return ans


def gram_channel(beta, n):
    ans = moment(beta, n + 2) / moment(beta, n)
    if n >= 2:
        ans -= moment(beta, n) / moment(beta, n - 2)
    return ans


def closed_channel(beta, n):
    if n == 0:
        return F(2) / (beta * (beta + 1))
    return 2 * (beta - 1) * (2 * beta * n + beta + 2 * n*n - 2) / (
        (beta+n-2)*(beta+n-1)*(beta+n)*(beta+n+1))


def crossing(k):
    return (k + 3 + sqrt(9*k*k + 18*k + 1)) / 2


def qpoly(beta, n):
    return beta*beta - (n+3)*beta - 2*n*n - 3*n + 2


checks = 0
weights = [F(p, q) for p in range(2, 81) for q in (1, 2, 3, 5, 7)
           if F(p, q) > 1 and F(p, q) < 35]
for beta in weights:
    xs = [gram_channel(beta, n) for n in range(45)]
    for n, x in enumerate(xs):
        assert x == closed_channel(beta, n)
        checks += 1
    assert xs[1] > xs[0]
    checks += 1
    for n in range(1, 43):
        diff = 4*(beta-1)*qpoly(beta, n) / (
            (beta+n-2)*(beta+n-1)*(beta+n)*(beta+n+1)*(beta+n+2))
        assert xs[n+1] - xs[n] == diff
        checks += 1
    winner = max(range(45), key=lambda j: xs[j])
    expected = 1
    while beta > crossing(expected):
        expected += 1
    assert winner == expected
    checks += 1
    linear_norm_sq = F(1) / beta
    quad_norm_sq = xs[winner]
    assert (quad_norm_sq > linear_norm_sq) == (beta < 2)
    assert (quad_norm_sq == linear_norm_sq) == (beta == 2)
    assert (quad_norm_sq < linear_norm_sq) == (beta > 2)
    checks += 3
assert crossing(1) > 4 and crossing(1) < 5
checks += 1
for beta_float in (100., 500., 1000.):
    beta = F(int(beta_float))
    winner = int(beta_float/2)
    candidates = [closed_channel(beta, j) for j in range(winner-6, winner+7)]
    scaled = float(max(candidates)) * beta_float
    assert abs(scaled - 16/27) < 2 / beta_float
    checks += 1
print('PASS:', checks, 'exact rational identities/comparisons and asymptotic checks')
