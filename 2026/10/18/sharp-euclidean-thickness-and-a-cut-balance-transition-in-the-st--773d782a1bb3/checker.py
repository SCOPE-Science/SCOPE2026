"""Standalone finite cross-checks for a Euclidean-width theorem on simplex sums.

Run with Python 3.9+; no additional modules are needed. The all-n proof is analytic.
"""
from fractions import Fraction
from itertools import combinations
from random import Random
from math import sqrt


def connected_sets(n):
    result = set()
    for size in range(1, n):
        for start in range(n):
            result.add(frozenset((start + j) % n for j in range(size)))
    result.add(frozenset(range(n)))
    return tuple(result)


def width(u, blocks):
    return sum(max(u[i] for i in b) - min(u[i] for i in b) for b in blocks)


def cut_cost(n, subset, blocks):
    s = frozenset(subset)
    return sum(bool(s & b) and bool(b - s) for b in blocks)


def is_cyclic_interval(n, subset):
    s = frozenset(subset)
    return any(s == frozenset((i+j) % n for j in range(len(s))) for i in range(n))


def predicted_squared(n):
    if n == 4:
        return Fraction(48, 1)
    a = (n - 1) * (n - 2) // 2
    u = (n // 2) * (n - n // 2)
    return Fraction(n * (a + u) ** 2, u)


def verify():
    rng = Random(732411)
    cut_tests = vector_tests = 0
    for n in range(3, 11):
        blocks = connected_sets(n)
        assert len(blocks) == n * (n - 1) + 1
        observed = []
        for size in range(1, n):
            for subset in combinations(range(n), size):
                c = cut_cost(n, subset, blocks)
                u = size * (n - size)
                squared = Fraction(n*c*c, u)
                observed.append((squared, subset))
                a = (n - 1) * (n - 2) // 2
                assert c >= a + u
                assert (c == a + u) == is_cyclic_interval(n, subset)
                cut_tests += 1
        min_sq = min(value for value, _ in observed)
        assert min_sq == predicted_squared(n)
        for value, subset in observed:
            expected = len(subset) == 1 if n in (3, 4) else len(subset) in (n // 2, (n + 1) // 2)
            expected &= is_cyclic_interval(n, subset)
            if n == 3:
                expected = is_cyclic_interval(n, subset)  # includes complements
            if n == 4:
                expected = is_cyclic_interval(n, subset) and len(subset) in (1, 3)
            assert (value == min_sq) == expected, (n, subset, value, min_sq)
        lower = sqrt(float(min_sq))
        for _ in range(600):
            raw = [rng.gauss(0, 1) for _ in range(n)]
            mean = sum(raw) / n
            vals = [v - mean for v in raw]
            norm = sqrt(sum(v*v for v in vals))
            vals = [v / norm for v in vals]
            assert width(vals, blocks) >= lower - 1e-9
            vector_tests += 1
    print(f"VERIFY_OK sizes=3..10 cuts={cut_tests} direct_directions={vector_tests}")


if __name__ == '__main__':
    verify()
