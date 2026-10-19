#!/usr/bin/env python3
"""Exact finite cross-checks for the singular-value occupancy theorem."""
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict


def branch_matrix(m, symbol):
    A = [[0] * m for _ in range(m)]
    if symbol == 0:
        for i in range(m):
            A[i][i] = 2 if i == 0 else 1
    else:
        A[0][m - 1] = -2
        for i in range(1, m):
            A[i][i - 1] = 1
    return A


def multiply(A, B):
    m = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(m))
             for j in range(m)] for i in range(m)]


def poly_counts_dp(m, n):
    states = {(0, (0,) * m): 1}
    for _ in range(n):
        next_states = defaultdict(int)
        for (r, counts), weight in states.items():
            for s in (0, 1):
                new_r = (r + s) % m
                new_counts = list(counts)
                new_counts[new_r] += 1
                next_states[(new_r, tuple(new_counts))] += weight
        states = next_states
    ans = defaultdict(int)
    for (_, counts), weight in states.items():
        ans[counts] += weight
    assert sum(ans.values()) == 2 ** n
    return dict(ans)


def poisson_functions(m):
    out = []
    for i in range(m):
        f = [Q(int(r == i)) - Q(1, m) for r in range(m)]
        g = [Q(0)]
        for r in range(m - 1):
            g.append(g[-1] - 2 * f[r])
        assert g[-1] - 2 * f[-1] == g[0]
        Pg = [(g[r] + g[(r + 1) % m]) / 2 for r in range(m)]
        assert all(g[r] - Pg[r] == f[r] for r in range(m))
        assert max(g) - min(g) == Q(2 * (m - 1), m)
        out.append((f, Pg))
    return out


def run():
    checks = 0
    for m in range(2, 7):
        functions = poisson_functions(m)
        for n in range(1, 9):
            hist = defaultdict(int)
            for bits in product((0, 1), repeat=n):
                A = [[int(i == j) for j in range(m)] for i in range(m)]
                state, counts, states_before = 0, [0] * m, []
                for s in bits:
                    states_before.append(state)
                    A = multiply(branch_matrix(m, s), A)
                    state = (state + s) % m
                    counts[state] += 1
                singular_values_squared = sorted(sum(A[i][j] ** 2 for i in range(m))
                                                 for j in range(m))
                assert singular_values_squared == sorted(4 ** c for c in counts)
                assert sum(sum(A[i][j] * A[i][k] for i in range(m))
                           for j in range(m) for k in range(j + 1, m)) == 0
                for i, (f, Pg) in enumerate(functions):
                    mart = sum((1 - 2 * s) * f[r]
                               for s, r in zip(bits, states_before))
                    lhs = Q(counts[i]) - Q(n, m)
                    assert lhs == mart + Pg[0] - Pg[state]
                    assert abs(lhs - mart) <= Q(2 * (m - 1), m)
                    checks += 1
                hist[tuple(counts)] += 1
            assert dict(hist) == poly_counts_dp(m, n)
            checks += 1
        # Exact covariance averaged over the uniform invariant cycle.
        f = [[Q(int(r == i)) - Q(1, m) for r in range(m)] for i in range(m)]
        for i in range(m):
            for j in range(m):
                cov = sum(f[i][r] * f[j][r] for r in range(m)) / m
                target = Q(int(i == j), m) - Q(1, m * m)
                assert cov == target
                checks += 1
    # M=3, n=2 finite-time non-multinomial distribution.
    assert poly_counts_dp(3, 2) == {
        (2, 0, 0): 1, (1, 1, 0): 1,
        (0, 2, 0): 1, (0, 1, 1): 1,
    }
    print('VERIFY_OK', checks)


if __name__ == '__main__':
    run()
