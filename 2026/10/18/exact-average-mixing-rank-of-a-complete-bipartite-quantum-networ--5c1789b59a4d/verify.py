"""Check the single-bond complete-bipartite quantum average-mixing rank theorem.

Requirements: Python 3, sympy, numpy.
The rational computation uses the diagonal image of the symmetric commutant;
the independent floating calculation uses grouped spectral projectors.
Neither finite test supplies the theorem's infinite proof.
"""
from itertools import product
import sympy as sp
import numpy as np


def target_nullity(a, b, g):
    if g == 1:
        return int(a == 2) + int(b == 2)
    return int(a <= 3) + int(b <= 3) + int(a == b and a >= 3)


def rational_hamiltonian(a, b, g):
    n = a + b
    H = sp.zeros(n)
    for i in range(a):
        for j in range(a, n):
            H[i, j] = H[j, i] = g if (i == 0 and j == a) else 1
    return H


def exact_commutant_rank(a, b, g):
    """Rank of diagonals of the *entire symmetric commutant*, over Q.

    The average-state map is orthogonal projection onto the full commutant,
    so its restricted Gram rank equals the diagonal-image dimension.
    Skew matrices in the commutant have zero diagonal and may be ignored.
    """
    H = rational_hamiltonian(a, b, g)
    n = H.rows
    pairs = [(i, j) for i in range(n) for j in range(i, n)]
    index = {ij: k for k, ij in enumerate(pairs)}
    def locate(i, j):
        return index[(min(i, j), max(i, j))]
    eq = sp.zeros(n * (n - 1) // 2, len(pairs))
    row = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(n):
                eq[row, locate(k, j)] += H[i, k]
                eq[row, locate(i, k)] -= H[k, j]
            row += 1
    basis = eq.nullspace()
    diagonal_image = sp.Matrix([[v[index[(i, i)]] for v in basis]
                                for i in range(n)])
    return diagonal_image.rank()


def spectral_rank(a, b, g):
    n = a + b
    H = np.zeros((n, n), dtype=float)
    H[:a, a:] = 1.0
    H[a:, :a] = 1.0
    H[0, a] = H[a, 0] = float(g)
    values, vectors = np.linalg.eigh(H)
    P = []
    i = 0
    while i < n:
        j = i + 1
        while j < n and abs(values[j] - values[i]) < 1.e-9:
            j += 1
        V = vectors[:, i:j]
        P.append(V @ V.T)
        i = j
    avg = sum((e * e for e in P), np.zeros((n, n)))
    eig = np.linalg.eigvalsh(avg)
    if eig[0] < -1.e-8:
        raise AssertionError('average mixing not positive semidefinite')
    return int(np.count_nonzero(eig > 1.e-7)), n * n


def main():
    exact_cases = 0
    for a, b, g in product(range(2, 8), range(2, 8),
                           (sp.Integer(0), sp.Rational(1, 2),
                            sp.Integer(1), sp.Integer(2), sp.Integer(3))):
        want = a + b - target_nullity(a, b, g)
        got = exact_commutant_rank(a, b, g)
        if got != want:
            raise AssertionError(('exact', a, b, g, got, want))
        exact_cases += 1

    spectral_cases = 0
    entries = 0
    for a, b, g in product(range(2, 8), range(2, 8),
                           (0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 7.0)):
        got, count = spectral_rank(a, b, g)
        want = a + b - target_nullity(a, b, g)
        if got != want:
            raise AssertionError(('spectral', a, b, g, got, want))
        spectral_cases += 1
        entries += count
    print('VERIFY_OK exact_commutant_cases={} spectral_profiles={} '
          'spectral_entries={} a_b=2..7'.format(exact_cases,
                                                 spectral_cases, entries))


if __name__ == '__main__':
    main()
