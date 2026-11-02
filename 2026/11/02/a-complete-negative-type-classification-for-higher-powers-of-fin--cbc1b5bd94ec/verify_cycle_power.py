#!/usr/bin/env python3
"""Exact sign certificates for cyclic graph-power distance metrics.

No external dependencies. Finite tests support the algebraic proof, but do not
replace its all-parameter inequalities and embedded local witnesses.
"""
from collections import deque
from itertools import product
from math import cos, pi


def sign_sin_pi_fraction(a, b):
    """Exact sign of sin(pi*a/b) for integer a and positive integer b."""
    assert b > 0
    r = a % (2 * b)
    return (r > 0 and r < b) - (r > b and r < 2 * b)


def harmonic_sign(n, k, j):
    """Exact sign of the nonconstant distance eigenvalue, using integer signs."""
    assert 1 <= j < n and 1 <= k < n // 2 + 1
    h = ((n // 2) + k - 1) // k
    if (k * j) % n == 0:
        return -1  # removable singularity gives eigenvalue -h
    a = sign_sin_pi_fraction(h * k * j, n)
    b = sign_sin_pi_fraction(((h - 1) * k + 1) * j, n)
    c = sign_sin_pi_fraction(k * j, n)
    return -a * b * c


def cyclic_metric(n, k, i, j):
    m = abs(i - j)
    d = min(m, n - m)
    return (d + k - 1) // k


def quadratic(points, weights, k, n=None):
    assert sum(weights) == 0 and len(points) == len(weights)
    out = 0
    for i, wi in enumerate(weights):
        for j, wj in enumerate(weights):
            v = abs(points[i] - points[j])
            if n is not None:
                v = min(v, n - v)
            out += wi * wj * ((v + k - 1) // k)
    return out


def bfs_distances(n, k):
    neighbors = [[(x + d) % n for d in range(-k, k + 1) if d] for x in range(n)]
    distances = [-1] * n
    distances[0] = 0
    queue = deque([0])
    while queue:
        x = queue.popleft()
        for y in neighbors[x]:
            if distances[y] == -1:
                distances[y] = distances[x] + 1
                queue.append(y)
    return distances


def check():
    groups = 0
    # Exact spectral-sign enumeration only for the finitely many exceptional cases.
    expected_zero = {(3, 12): 5, (3, 14): 6, (3, 20): 11, (4, 18): 10}
    for (k, n), nullity in expected_zero.items():
        signs = [harmonic_sign(n, k, j) for j in range(1, n)]
        assert max(signs) == 0
        assert signs.count(0) == nullity
        groups += n - 1
    print('EXCEPTIONAL_SIGNS_OK', expected_zero)

    # A minimal finite range remains after the uniform large-order witnesses.
    frequency_witnesses = {
        9: 2, 10: 2, 11: 2, 13: 3,
        15: 2, 16: 2, 17: 2, 18: 5, 19: 5, 21: 2,
    }
    for n, j in frequency_witnesses.items():
        assert harmonic_sign(n, 3, j) == 1
        groups += 1

    # For powers at least four the two-dimensional/three-dimensional bands
    # are covered by exact integer-angle sign rules (rather than sampling).
    for k in range(4, 180):
        for n in range(2 * k + 3, 4 * k + 4):
            if k == 4 and n == 18:
                continue
            if n < 4 * k:
                j = 2
            elif n <= 4 * k + 2:
                j = 3
            else:
                j = 2
            assert harmonic_sign(n, k, j) == 1, (n, k, j)
            groups += 1
    print('ALL_BOUNDED_DIAMETER_SIGN_PATTERNS_OK')

    # Local six-point certificate covers every k>=4, n>=4k+4.
    w6 = [2, -2, -2, 3, -3, 2]
    for k in range(4, 180):
        sites = ([0, 2, k - 1, k + 1, 2 * k, 2 * k + 2]
                 if k == 4 else
                 [0, 2, k - 2, k + 1, 2 * k - 1, 2 * k + 2])
        assert quadratic(sites, w6, k) == 2
        assert quadratic(sites, w6, k, 4 * k + 4) == 2
        groups += 2

    # Local twelve-point certificate covers every n>=22 for k=3.
    w12 = [2, -1, -2, 1, 2, -2, -2, 2, 1, -2, -1, 2]
    assert quadratic(list(range(12)), w12, 3) == 2
    for n in (22, 23, 30, 99, 251):
        assert quadratic(list(range(12)), w12, 3, n) == 2
        groups += 1
    print('LOCAL_WITNESSES_OK')

    # Independent shortest-path reconstruction, including boundary orders.
    for k in range(3, 13):
        for n in range(2 * k + 1, min(7 * k + 12, 86)):
            distances = bfs_distances(n, k)
            for j in range(n):
                assert distances[j] == cyclic_metric(n, k, 0, j)
                groups += 1
    print('INDEPENDENT_SHORTEST_PATHS_OK')

    # Numerical independent DFT: cross-check exact integer sign oracle.
    for k in range(3, 12):
        for n in range(2 * k + 1, min(8 * k + 11, 120)):
            seq = [cyclic_metric(n, k, 0, j) for j in range(n)]
            for j in range(1, n):
                value = sum(seq[a] * cos(2 * pi * j * a / n) for a in range(n))
                exact_sign = harmonic_sign(n, k, j)
                if exact_sign > 0: assert value > -3e-8
                if exact_sign < 0: assert value < 3e-8
                if exact_sign == 0: assert abs(value) < 3e-8
                groups += 1
    print('NUMERICAL_FOURIER_CROSSCHECK_OK')
    print('CHECK_OK', groups)


if __name__ == '__main__':
    check()
