#!/usr/bin/env python3
"""Numerical cross-checks of composition sums and optimal two-block allocation.
Pure Python 3 standard library. Finite checks do not establish the asymptotic theorem.
"""
from itertools import product
from math import gamma, pi, sqrt, prod

ZETA_HALF = -1.4603545088095868128894991525153


def composition_functions(max_order, n_max):
    a = [0.0] + [1.0 / sqrt(j) for j in range(1, n_max + 1)]
    coefficients = list(a)
    out = {}
    for order in range(1, max_order + 1):
        running = 0.0
        vals = [0.0] * (n_max + 1)
        for n in range(1, n_max + 1):
            running += coefficients[n]
            vals[n] = running
        out[order] = vals
        if order < max_order:
            # Coefficients of Li_{1/2}(z)^{order+1}.
            next_coeff = [0.0] * (n_max + 1)
            for j in range(1, n_max):
                cj = coefficients[j]
                if not cj:
                    continue
                for k in range(1, n_max - j + 1):
                    next_coeff[j + k] += cj * a[k]
            coefficients = next_coeff
    return out


def beta(order):
    return (order * ZETA_HALF / sqrt(pi) *
            gamma(1.0 + order / 2.0) / gamma((order + 1.0) / 2.0))


def alpha(p, q):
    return (p * beta(q) / sqrt(q) - q * beta(p) / sqrt(p)) / ((p + q) ** 1.5)


def main():
    nmax = 2500
    funcs = composition_functions(4, nmax)
    count = 0
    for r in range(1, 5):
        for n in range(r, min(11, nmax + 1)):
            direct = sum(1.0 / sqrt(prod(items))
                         for items in product(range(1, n + 1), repeat=r)
                         if sum(items) <= n)
            # Above includes only a tiny exact composition census.
            assert abs(direct - funcs[r][n]) < 1e-10 * max(1.0, direct)
            count += 1
    print('composition_crosschecks', count)

    for p, q in [(1, 1), (2, 1), (1, 2), (3, 1), (2, 2), (3, 2)]:
        if p > 4 or q > 4:
            continue
        for N in (120, 500, 1500, 2500):
            vals = [(funcs[p][m] * funcs[q][N - m], m)
                    for m in range(p, N - q + 1)]
            best_m = max(vals)[1]
            predicted = p * N / (p + q) + alpha(p, q) * sqrt(N)
            assert abs(best_m - predicted) < 3.0, (p, q, N, best_m, predicted)
            print('allocation', p, q, N, best_m,
                  'two_term_prediction', round(predicted, 8),
                  'error', round(best_m - predicted, 8))

    for r in range(1, 5):
        N = 2500
        lead = pi ** (r / 2.0) / gamma(1.0 + r / 2.0)
        empirical_beta = sqrt(N) * (funcs[r][N] / (lead * N ** (r / 2.0)) - 1.0)
        assert abs(empirical_beta - beta(r)) < 0.2
        print('asymptotic', r, 'measured_beta', round(empirical_beta, 8),
              'expected_beta', round(beta(r), 8))
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
