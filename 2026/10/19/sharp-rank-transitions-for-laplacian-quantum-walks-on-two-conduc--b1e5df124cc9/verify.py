"""Separate finite checks for two-conductance weighted-star Laplacian mixing.

Requires Python 3 and NumPy. All pairwise edge groups have positive weights.
Numerical spectral projectors are computed from the *full* Laplacian; the
analytic quotient-space eigenvectors are not used in these checks.
"""
from fractions import Fraction as Q
import numpy as np


def laplacian(p, q, a, b):
    n = 1 + p + q
    l = np.zeros((n, n), dtype=float)
    for i, w in enumerate([a] * p + [b] * q, 1):
        l[0, 0] += w
        l[i, i] = w
        l[0, i] = l[i, 0] = -w
    return l


def mixing(l):
    values, vectors = np.linalg.eigh(l)
    n = len(values)
    m = np.zeros_like(l)
    i = 0
    while i < n:
        j = i + 1
        while j < n and abs(values[j] - values[i]) < 1e-8:
            j += 1
        e = vectors[:, i:j] @ vectors[:, i:j].T
        m += e * e
        i = j
    return m


def d3(matrix):
    return (matrix[0][0] * (matrix[1][1]*matrix[2][2] - matrix[1][2]*matrix[2][1])
            - matrix[0][1] * (matrix[1][0]*matrix[2][2] - matrix[1][2]*matrix[2][0])
            + matrix[0][2] * (matrix[1][0]*matrix[2][1] - matrix[1][1]*matrix[2][0]))

profiles = 0
entries = 0
for p in range(1, 8):
    for q in range(1, 8):
        for a, b in [(1, 2), (2, 3), (1, 5), (3, 1), (2, 2)]:
            l = laplacian(p, q, a, b)
            m = mixing(l)
            eig = np.linalg.eigvalsh(m)
            nullity = int(np.sum(eig < 1e-8))
            if a == b:
                expected = int(p + q == 2)
            elif p == q == 1:
                expected = 1
            else:
                expected = int(p == 2) + int(q == 2)
            assert nullity == expected, (p, q, a, b, eig, expected)
            if p == q == 1:
                z = np.array([b-a, a, -b], dtype=float)
                assert np.linalg.norm(m @ z) < 1e-8
            assert np.max(abs(m.sum(axis=1) - 1.0)) < 1e-9
            if a != b and p + q >= 3:
                for start, size in [(1, p), (p+1, q)]:
                    if size == 2:
                        z = np.zeros(p + q + 1)
                        z[start] = 1
                        z[start+1] = -1
                        assert np.linalg.norm(m @ z) < 1e-8
                aa, bb = Q(a), Q(b)
                S = p*aa + q*bb
                t = [[Q(1), S, S*S + p*aa*aa + q*bb*bb],
                     [Q(1), aa, (p+1)*aa*aa],
                     [Q(1), bb, (q+1)*bb*bb]]
                det = d3(t)
                right = aa*bb*(aa*(p-1)*(p+1-q) - bb*(q-1)*(q+1-p))
                assert det == right
                assert det != 0
            profiles += 1
            entries += m.size
print(f'VERIFY_OK full_laplacian_profiles={profiles} matrix_entries={entries} exact_moment_determinants={7*7*4-4}')
