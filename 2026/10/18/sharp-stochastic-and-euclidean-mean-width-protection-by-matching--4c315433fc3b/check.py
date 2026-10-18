#!/usr/bin/env python3
"""Finite reproducibility checks for missing-edge symmetric-root support loss.

Run with Python 3 (standard library only): python3 check.py
The universal inequalities and asymptotics are proved in RESULT.md, not by this script.
"""
from itertools import combinations, permutations
from math import factorial, isclose
from random import Random


def loss(missing, scores):
    n = len(scores)
    all_range = max(scores) - min(scores)
    remaining = [(i, j) for i, j in combinations(range(n), 2)
                 if (i, j) not in missing]
    assert remaining
    return all_range - max(abs(scores[i] - scores[j]) for i, j in remaining)


def is_matching(edges):
    return len(set(v for edge in edges for v in edge)) == 2 * len(edges)


def finite_order_test(n, values):
    assert len(values) == n and len(set(values)) == n
    assert values == tuple(sorted(values))
    all_edges = tuple(combinations(range(n), 2))
    perms = tuple(permutations(values))
    gap = min(values[-1] - values[-2], values[1] - values[0])
    cases = 0
    strict_cases = 0
    for k in range(1, n // 2 + 1):
        bound = 2 * k * gap / (n * (n - 1))
        for rem in combinations(all_edges, k):
            f = frozenset(rem)
            total = 0.0
            for v in perms:
                d = loss(f, v)
                high = max(range(n), key=v.__getitem__)
                low = min(range(n), key=v.__getitem__)
                missing_extremes = tuple(sorted((high, low))) in f
                floor = gap if missing_extremes else 0.0
                assert d >= floor - 1e-12, (n, k, f, v, d, floor)
                if is_matching(f):
                    assert isclose(d, floor, abs_tol=1e-12), (n, k, f, v)
                total += d
            observed = total / factorial(n)
            assert observed >= bound - 1e-10
            if is_matching(f):
                assert isclose(observed, bound, abs_tol=1e-10)
            else:
                assert observed > bound + 1e-10, (n, k, rem, observed, bound)
                strict_cases += 1
            cases += 1
    return cases, strict_cases


def simulate_uniform(n=6, k=3, replicates=110000):
    rng = Random(937031)
    missing = frozenset((2 * i, 2 * i + 1) for i in range(k))
    aggregate = 0.0
    gap_aggregate = 0.0
    for _ in range(replicates):
        z = [rng.random() for _ in range(n)]
        zz = sorted(z)
        g = min(zz[1] - zz[0], zz[-1] - zz[-2])
        gap_aggregate += g
        aggregate += loss(missing, z)
    observed_eta = gap_aggregate / replicates
    observed_defect = aggregate / replicates
    target_eta = 1 / (2 * (n + 1))
    target_defect = k / (n * (n - 1) * (n + 1))
    assert abs(observed_eta - target_eta) < 0.002
    assert abs(observed_defect - target_defect) < 0.002
    return observed_eta, target_eta, observed_defect, target_defect


def main():
    for n, vec in [(4, (-10, -5, -1, 2)),
                   (5, (-10, -5, -1, 2, 4)),
                   (6, (-10, -5, -1, 2, 4, 10))]:
        cases, strict_cases = finite_order_test(n, vec)
        print(f'Exact permutation tests n={n}: {cases} deleted-edge sets, '
              f'{strict_cases} strictly nonmatching.')
    eta, exact_eta, loss_val, exact_loss = simulate_uniform()
    print(f'Uniform-label experiment: E min gaps {eta:.6f} vs {exact_eta:.6f}; '
          f'E support loss {loss_val:.6f} vs {exact_loss:.6f}.')
    print('All finite checks passed. Universal and asymptotic steps remain analytic.')


if __name__ == '__main__':
    main()
