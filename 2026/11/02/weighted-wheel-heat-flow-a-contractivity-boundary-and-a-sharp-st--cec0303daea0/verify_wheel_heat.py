#!/usr/bin/env python3
"""Independent finite checks of wheel heat-Lipschitz formulas (standard library only).

Finite checks support but do not establish the universal analytic theorem.
"""
from fractions import Fraction
from itertools import product
from math import exp, log, sqrt


def potentials(m):
    for x in product((-1, 0, 1), repeat=m):
        if all(abs(x[i] - x[(i + 1) % m]) <= 1 for i in range(m)):
            yield x


def predicted_slope(m, r):
    return max(r * (m - 9), r * (m - 5) - 2)


def exact_slope(m, r, ps):
    return max(r * sum(x) - r - 2 - x[1] - x[-1]
               for x in ps if x[0] == -1)


def generator(m, r, which):
    n = m + 1
    L = [[0.0] * n for _ in range(n)]
    def add(i, j, w):
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    if which in ('full', 'star'):
        for i in range(1, n):
            add(0, i, r)
    if which in ('full', 'rim'):
        for j in range(1, n):
            add(j, (j % m) + 1, 1.0)
    return L


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def heat(m, r, t, which='full'):
    L = generator(m, r, which)
    n = m + 1
    rate = max(L[i][i] for i in range(n))
    if rate == 0:
        return [[float(i == j) for j in range(n)] for i in range(n)]
    Q = [[float(i == j) - L[i][j] / rate for j in range(n)]
         for i in range(n)]
    P = [[float(i == j) for j in range(n)] for i in range(n)]
    H = [[0.0] * n for _ in range(n)]
    x = rate * t
    weight = exp(-x)
    for k in range(240):
        for i in range(n):
            for j in range(n):
                H[i][j] += weight * P[i][j]
        if k > x + 30 * sqrt(x + 1) and weight < 1e-17:
            break
        P = matmul(P, Q)
        weight *= x / (k + 1)
    assert max(abs(sum(H[i]) - 1.0) for i in range(n)) < 2e-11
    return H


def lip_norm(H, ps):
    m = len(H) - 1
    edges = [(0, i) for i in range(1, m + 1)] + [
        (i + 1, (i + 1) % m + 1) for i in range(m)]
    ans = 0.0
    for i, j in edges:
        diff = [H[i][k] - H[j][k] for k in range(1, m + 1)]
        ans = max(ans, *(abs(sum(d * x for d, x in zip(diff, f))) for f in ps))
    return ans


def envelope(m, s):
    return (2 - 4 / m) * exp(-s) - (1 - 4 / m) * exp(-(m + 1) * s)


def maximizer(m):
    return log((m + 1) * (m - 4) / (2 * (m - 2))) / m


def main():
    numbers = [Fraction(1, 10), Fraction(1, 2), Fraction(2, 3),
               Fraction(1, 1), Fraction(2, 1), Fraction(3, 1)]
    stored = {}
    for m in range(5, 11):
        ps = list(potentials(m))
        stored[m] = ps
        for r in numbers:
            exact = exact_slope(m, r, ps)
            predicted = predicted_slope(m, r)
            assert exact == predicted, (m, r, exact, predicted)
        print('EXACT_SLOPE_OK', 'rim_vertices=', m, 'potentials=', len(ps))

    # The semigroups are computed independently by stochastic uniformization.
    cases = [(5, .3, .13), (6, 1.5, .09), (6, 2.5, .004),
             (7, .8, .07), (7, 1.2, .025), (8, .5, .07),
             (8, .8, .025), (9, .3, .09), (9, .8, .03),
             (10, .1, .025), (10, 1.0, .05)]
    for m, r, t in cases:
        ps = stored[m]
        H = heat(m, r, t)
        lam = lip_norm(H, ps)
        bound = envelope(m, r * t)
        assert 0 < lam <= bound + 2e-11, (m, r, t, lam, bound)
        if (m, r) == (6, 1.5):
            assert lam < 1
        if (m, r) == (6, 2.5):
            assert lam > 1
        if (m, r) in [(7, 1.2), (8, .8), (9, .8), (10, .1)]:
            assert lam > 1, (m, r, lam)
        if (m, r) in [(5, .3), (7, .8), (8, .5), (9, .3)]:
            assert lam < 1, (m, r, lam)
        # The cycle Laplacian and radial star Laplacian commute.
        S, R = generator(m, r, 'star'), generator(m, r, 'rim')
        AB, BA = matmul(S, R), matmul(R, S)
        assert max(abs(AB[i][j] - BA[i][j]) for i in range(m+1)
                   for j in range(m+1)) < 1e-12
        # Compare the full heat kernel with product of factor heat kernels.
        product_heat = matmul(heat(m, r, t, 'star'), heat(m, r, t, 'rim'))
        assert max(abs(H[i][j] - product_heat[i][j]) for i in range(m+1)
                   for j in range(m+1)) < 1e-10
    print('HEAT_UNIFORMIZATION_OK cases=', len(cases))

    for m in [6, 7, 8, 10, 30, 100, 1000]:
        s = maximizer(m)
        exact_peak = (2 * (m - 2) / (m + 1)) * (
            2 * (m - 2) / ((m + 1) * (m - 4))) ** (1 / m)
        assert abs(exact_peak - envelope(m, s)) < 2e-13
        assert exact_peak < 2
        assert s > 0
    assert envelope(5, 0) == 1
    assert envelope(5, .1) < 1
    assert 1.98 < envelope(1000, maximizer(1000)) < 2
    print('ENVELOPE_OK sharp_family_limit=2')
    print('ALL_WHEEL_HEAT_CHECKS_OK')


if __name__ == '__main__':
    main()
