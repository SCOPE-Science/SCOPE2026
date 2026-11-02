#!/usr/bin/env python3
"""Numerical diagnostic for cycle-square geodesic Fourier formulas.
The all-order proof is analytic; finite computations here are corroboration only.
Standard-library Python 3; run: python3 check.py
"""
import cmath
import math
from collections import deque


def predicted(n, j):
    if j == 0:
        h = n // 2
        return h * (h + 1) / 2 + ((h + 1) // 2 if n % 2 else 0)
    t = math.pi * j / n
    if n % 2 == 0:
        return -(1 - (-1) ** j) / (4 * math.sin(t) ** 2) - (n / 4 if j == n // 2 else 0)
    c = math.cos(t)
    h = n // 2
    return -(1 / (1 + (-1) ** j * c) + (-1) ** (h + j) / c) / 4


def graph_distances(n):
    near = [{(v + d) % n for d in (-2, -1, 1, 2) if d % n} for v in range(n)]
    dist = [[-1] * n for _ in range(n)]
    for root in range(n):
        q = deque([root])
        dist[root][root] = 0
        while q:
            u = q.popleft()
            for v in near[u]:
                if dist[root][v] == -1:
                    dist[root][v] = dist[root][u] + 1
                    q.append(v)
    return dist


checks = 0
for n in range(3, 129):
    matrix = graph_distances(n)
    first = matrix[0]
    assert all(first[k] == (min(k, n - k) + 1) // 2 for k in range(n))
    checks += n
    assert all(matrix[i][j] == first[(j - i) % n] for i in range(n) for j in range(n))
    checks += n * n
    for j in range(n):
        observed = sum(first[k] * cmath.exp(-2j * math.pi * j * k / n) for k in range(n))
        expected = predicted(n, j)
        assert abs(observed.imag) < 1e-8, (n, j, observed)
        assert abs(observed.real - expected) < 1e-8, (n, j, observed, expected)
        checks += 2
    positive = [j for j in range(1, n) if predicted(n, j) > 1e-8]
    if n % 2 == 0:
        expected_positive = []
    elif n % 4 == 3:
        expected_positive = [j for j in range(1, n) if (j if j <= n // 2 else n - j) % 2 == 0]
    else:
        expected_positive = [j for j in range(1, n) if (j if j <= n // 2 else n - j) % 2 == 1 and 3 * (j if j <= n // 2 else n - j) > n]
    assert positive == expected_positive, (n, positive, expected_positive)
    zeros = sum(abs(predicted(n, j)) < 1e-8 for j in range(1, n))
    expected_zeros = (n // 2 - (2 if n % 4 == 0 else 1)) if n % 2 == 0 else (2 if n % 12 == 9 else 0)
    assert zeros == expected_zeros, (n, zeros, expected_zeros)
    checks += 2

# Exact n=9 cancellation at Fourier frequencies 3 and 6.
first9 = graph_distances(9)[0]
residue_totals = [sum(first9[k] for k in range(r, 9, 3)) for r in range(3)]
assert residue_totals == [4, 4, 4]
assert [n for n in range(3, 129) if all(predicted(n, j) <= 1e-8 for j in range(1, n))] == [n for n in range(3, 129) if n % 2 == 0 or n in (3, 5, 9)]
print('CHECK_OK', checks, 'BFS, circulant Fourier, sign and nullity assertions', 'n=3..128', 'n9_residue_totals=', residue_totals)
