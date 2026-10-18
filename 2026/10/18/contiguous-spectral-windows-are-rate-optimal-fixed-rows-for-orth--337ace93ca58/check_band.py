"""Reproduce the orthogonal-row subspace-constrained Kaczmarz band theorem."""
from itertools import combinations, product
from math import isclose
from random import Random


def rate(weights, keep):
    kept = [weights[j] for j in keep]
    return 1.0 - min(kept) / sum(kept)


def contiguous_best(weights, r):
    n = len(weights)
    bands = [tuple(range(i, i + r)) for i in range(n - r + 1)]
    best = min(rate(weights, j) for j in bands)
    return best, bands


def test_classification():
    rng = Random(32517)
    count = 0
    for n in range(3, 9):
        for r in range(2, n):
            for _ in range(50):
                weights = sorted([rng.uniform(0.15, 9.0) for j in range(n)], reverse=True)
                actual = min(rate(weights, j) for j in combinations(range(n), r))
                band, _ = contiguous_best(weights, r)
                assert isclose(actual, band, rel_tol=1e-12, abs_tol=1e-12)
                count += 1
    return count


def test_expected_k():
    # Enumerate every sampling path for a diagonal matrix with 4 modes.
    weights = (25.0, 9.0, 2.0, 1.0)
    keep = (1, 2, 3)
    probs = {i: weights[i] / sum(weights[j] for j in keep) for i in keep}
    err = {1: 2.0, 2: 3.0, 3: 4.0}
    count = 0
    for k in range(0, 5):
        lhs = 0.0
        for path in product(keep, repeat=k):
            probability = 1.0
            surviving = dict(err)
            for j in path:
                probability *= probs[j]
                surviving[j] = 0.0
            lhs += probability * sum(v * v for v in surviving.values())
            count += 1
        rhs = sum((err[j] ** 2) * ((1.0 - probs[j]) ** k) for j in keep)
        assert isclose(lhs, rhs, rel_tol=1e-11, abs_tol=1e-11)
    return count


def test_three_modes():
    count = 0
    for M in (2, 3, 7, 30, 1000):
        w = ((M + 1) ** 2, M ** 2, 1)
        best, _ = contiguous_best(w, 2)
        proxy = rate(w, (1, 2))
        closed_best = ((M + 1) ** 2) / (((M + 1) ** 2) + M ** 2)
        closed_proxy = M ** 2 / (M ** 2 + 1)
        assert isclose(best, closed_best, rel_tol=1e-13)
        assert isclose(proxy, closed_proxy, rel_tol=1e-13)
        assert proxy > best
        count += 1
    return count


if __name__ == '__main__':
    a = test_classification()
    b = test_expected_k()
    c = test_three_modes()
    print(f'PASS: {a} exhaustive subset / spectral-band comparisons; '
          f'{b} exact enumeration path checks; {c} analytic three-mode checks')
