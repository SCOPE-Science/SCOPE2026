#!/usr/bin/env python3
"""Reproduce finite checks for a quantum walk with a lossy two-cycle junction."""
import math
from fractions import Fraction
import numpy as np
import sympy as sp


def adjacency(m, n):
    size = m + n - 1
    mat = np.zeros((size, size), dtype=np.int64)
    for vertices in ([0] + list(range(1, m)), [0] + list(range(m, size))):
        for a, b in zip(vertices, vertices[1:] + vertices[:1]):
            mat[a, b] = mat[b, a] = 1
    return mat


def predicted_dimension(m, n):
    d = math.gcd(m, n)
    extra = bool((m // d) % 2 and (n // d) % 2)
    return (m - 1) // 2 + (n - 1) // 2 + (d // 2 if extra else 0)


def constructed_basis(m, n):
    size, d = m + n - 1, math.gcd(m, n)
    vectors = []
    for q, offset in ((m, 1), (n, m)):
        positions = np.arange(1, q)
        for k in range(2, q, 2):
            vec = np.zeros(size)
            vec[offset:offset + q - 1] = math.sqrt(2 / q) * np.sin(np.pi * k * positions / q)
            vectors.append(vec)
    if (m // d) % 2 and (n // d) % 2:
        for r in range(1, d, 2):
            vec = np.zeros(size)
            vec[1:m] = math.sqrt(2 / (m + n)) * np.sin(np.pi * r * np.arange(1, m) / d)
            vec[m:] = -math.sqrt(2 / (m + n)) * np.sin(np.pi * r * np.arange(1, n) / d)
            vectors.append(vec)
    return np.array(vectors, dtype=np.float64).T


def survival(m, n, j):
    d = math.gcd(m, n)
    value = (2 / m) * sum(math.sin(math.pi * k * j / m) ** 2 for k in range(2, m, 2))
    if (m // d) % 2 and (n // d) % 2:
        value += (2 / (m + n)) * sum(math.sin(math.pi * r * j / d) ** 2 for r in range(1, d, 2))
    return value


def exact_hub_observability_rank(mat):
    s = mat.shape[0]
    sym = sp.Matrix(mat.tolist())
    e = sp.eye(s)[:, 0]
    rows = []
    for _ in range(s):
        rows.append(e.T)
        e = sym * e
    return sp.Matrix.vstack(*rows).rank()


pairs, rank_checks, local_checks = 0, 0, 0
for m in range(3, 13):
    for n in range(3, 13):
        adj = adjacency(m, n)
        degree = np.diag(adj.sum(axis=0))
        generators = [adj, degree - adj]
        B = constructed_basis(m, n)
        dimension = predicted_dimension(m, n)
        assert B.shape == (m + n - 1, dimension)
        assert np.max(np.abs(B[0, :])) < 1e-12
        assert np.linalg.norm(B.T @ B - np.eye(dimension)) < 1e-11
        for H in generators:
            for b in B.T:
                rayleigh = float(b @ H @ b)
                assert np.linalg.norm(H @ b - rayleigh * b) < 1e-10
            if max(m, n) <= 8:
                assert H.shape[0] - exact_hub_observability_rank(H) == dimension
                rank_checks += 1
        for j in range(1, m):
            assert abs(float(np.sum(B[j] ** 2)) - survival(m, n, j)) < 1e-11
            local_checks += 1
        pairs += 1
assert Fraction(1, 2) + Fraction(1, 4) == Fraction(3, 4)
assert abs(survival(3, 3, 1) - 0.75) < 1e-12
assert predicted_dimension(3, 3) == 3
print(f'PASS {pairs} graph pairs; {2*pairs} generator-eigenbasis checks; {rank_checks} exact Krylov ranks; {local_checks} localized probabilities; two-triangle test')
