"""Reproducibility check for powered rotation-angle distances on two finite rotation groups.

Requires numpy (only for numerical spectral cross-checks); all class counts and
character-polynomial comparisons are computed with integer arithmetic.
"""
from itertools import permutations, product
from math import pi, log, isclose
import numpy as np

PSTAR = log(4 / 3) / log(3 / 2)

def parity(perm):
    return (-1) ** sum(perm[i] > perm[j] for i in range(3) for j in range(i + 1, 3))

def rotational_matrices(tetrahedral=False):
    matrices = []
    for perm in permutations(range(3)):
        for signs in product([-1, 1], repeat=3):
            if parity(perm) * np.prod(signs) != 1:
                continue
            if tetrahedral and parity(perm) != 1:
                continue
            mat = np.zeros((3, 3), dtype=int)
            for i, j in enumerate(perm):
                mat[i, j] = signs[i]
            matrices.append(mat)
    assert len(matrices) == (12 if tetrahedral else 24)
    return matrices

def distance_classes(mats):
    table = np.empty((len(mats), len(mats)), dtype=float)
    for i, a in enumerate(mats):
        for j, b in enumerate(mats):
            trace = int(np.trace(a.T @ b))
            table[i, j] = {3: 0.0, 1: 0.5, 0: 2 / 3, -1: 1.0}[trace]
    return table

def eigenvalues_analytic(p, tetra):
    z = 1.0
    two_thirds = (2 / 3) ** p
    half = 0.5 ** p
    if tetra:
        return sorted([3 * z - 4 * two_thirds] * 2 + [-z] * 9)
    sign = -3 * z + 8 * two_thirds - 6 * half
    rep2 = 3 * z - 4 * two_thirds
    rep31 = z - 2 * half
    rep211 = -3 * z + 2 * half
    return sorted([sign] + [rep2] * 4 + [rep31] * 9 + [rep211] * 9)

def test_group(tetra):
    mats = rotational_matrices(tetra)
    d = distance_classes(mats)
    vals, counts = np.unique(np.round(d[0, :], 12), return_counts=True)
    found = dict(zip(vals.tolist(), counts.tolist()))
    expected = {0.0: 1, 0.666666666667: 8, 1.0: 3} if tetra else {
        0.0: 1, 0.5: 6, 0.666666666667: 8, 1.0: 9}
    assert found == expected, (found, expected)
    n = len(mats)
    H = np.eye(n) - np.ones((n,n)) / n
    for p in [0.125, 0.5, PSTAR - 0.01, PSTAR, PSTAR + 0.01, 1, 1.5, 2]:
        A = d ** p
        eig = np.linalg.eigvalsh(A)
        given = eigenvalues_analytic(p, tetra)
        assert np.allclose(eig[:-1], given, atol=3e-12), (tetra,p,eig,given)
        centered = -0.5 * H @ A @ H
        expected_min_dim = n - 1 if p < PSTAR - 1e-9 else (9 if tetra else 19)
        if p <= PSTAR:
            assert np.linalg.eigvalsh(centered).min() >= -4e-12
            if abs(p-PSTAR)<1e-12:
                assert sum(np.linalg.eigvalsh(centered)>2e-10) == expected_min_dim
            else:
                assert sum(np.linalg.eigvalsh(centered)>2e-10) == n-1
        else:
            assert np.linalg.eigvalsh(centered).min() < -1e-8
    print('PASS', 'tetrahedral' if tetra else 'octahedral', 'group_size',n,
          'class_counts',found,'critical_exponent',PSTAR,
          'critical_embedding_dimension',9 if tetra else 19)

if __name__ == '__main__':
    test_group(True)
    test_group(False)
    print('All character spectra, class multiplicities, endpoint ranks and sign transitions verified.')
