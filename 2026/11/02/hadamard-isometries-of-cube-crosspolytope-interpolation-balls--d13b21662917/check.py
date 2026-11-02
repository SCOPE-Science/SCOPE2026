"""Finite reproducibility diagnostics for Hadamard symmetries of max-norm gauges.

Only the accompanying mathematical argument proves the all-dimensional theorem.
Run: python3 check.py
"""
from itertools import combinations, product
from math import sqrt, isclose


def sylvester(k):
    H = [[1]]
    for _ in range(k):
        H = [r + r for r in H] + [r + [-v for v in r] for r in H]
    return H


def N(x, s):
    return max(max(map(abs, x)), sum(map(abs, x)) / s)


def transform(H, x):
    n = len(H)
    return [sum(a * b for a, b in zip(row, x)) / sqrt(n) for row in H]


def main():
    c = sqrt(2) - 1
    vertices2 = {(a, b) for a, b in
                 [*( (u, v * c) for u, v in product((-1, 1), repeat=2)),
                   *( (u * c, v) for u, v in product((-1, 1), repeat=2))]}
    H2 = sylvester(1)
    assert len(vertices2) == 8
    for x in vertices2:
        assert isclose(N(x, sqrt(2)), 1, abs_tol=1e-12)
        assert any(all(isclose(v, w, abs_tol=1e-12)
                       for v, w in zip(transform(H2, x), y)) for y in vertices2)
    print('Dimension 2: all 8 octagon vertices preserved')

    H4 = sylvester(2)
    vertices4 = []
    for i, j in combinations(range(4), 2):
        for ai, aj in product((-1, 1), repeat=2):
            x = [0, 0, 0, 0]
            x[i], x[j] = ai, aj
            vertices4.append(tuple(x))
    v4_set = set(vertices4)
    assert len(v4_set) == 24
    for x in vertices4:
        y = transform(H4, x)
        assert tuple(round(t) for t in y) in v4_set
        assert all(isclose(t, round(t), abs_tol=1e-12) for t in y)
    print('Dimension 4: all 24 vertices preserved')

    for power in (3, 4, 5):
        H = sylvester(power)
        n = len(H)
        for indices in combinations(range(n), 3):
            x = [int(i in indices) for i in range(n)]
            y = transform(H, x)
            assert sum(isclose(abs(t), 3 / sqrt(n), abs_tol=1e-12) for t in y) == n // 4
            assert sum(isclose(abs(t), 1 / sqrt(n), abs_tol=1e-12) for t in y) == 3 * n // 4
            assert isclose(N(y, sqrt(n)), 1.5, abs_tol=1e-12)
            assert isclose(N(x, sqrt(n)), max(1, 3 / sqrt(n)), abs_tol=1e-12)
        print('Dimension {}: all {} triple-support obstructions verified'.format(
            n, n * (n - 1) * (n - 2) // 6))


if __name__ == '__main__':
    main()
