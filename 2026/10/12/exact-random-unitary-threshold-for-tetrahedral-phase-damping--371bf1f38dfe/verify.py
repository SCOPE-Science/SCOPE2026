#!/usr/bin/env python3
"""Independent exact checks for a four-level phase-damping channel.

Uses only Python standard-library Gaussian-integer arithmetic; finite phase-grid
checks corroborate, but do not establish, the analytic all-phases inequality.
"""

from itertools import product
from fractions import Fraction

K = (
    (0, 1, 1, 1),
    (1, 0, 1j, -1j),
    (1, -1j, 0, 1j),
    (1, 1j, -1j, 0),
)
Z = (
    (1, 1, 1, 1),
    (1, 1, -1j, 1j),
    (1, 1j, 1, -1j),
    (1, -1j, 1j, 1),
)


def inner_k(z):
    return sum(z[i].conjugate() * K[i][j] * z[j]
               for i in range(4) for j in range(4))


def main():
    # Hermitian conference matrix and exact minimal polynomial.
    for i in range(4):
        for j in range(4):
            assert K[i][j] == complex(K[j][i]).conjugate()
            assert sum(K[i][r] * K[r][j] for r in range(4)) == (3 if i == j else 0)
    assert all(inner_k(z) == 6 for z in Z)

    # Exact four-element boundary decomposition into phase Gram matrices.
    for i in range(4):
        for j in range(4):
            actual = Fraction(1, 4) * sum(z[i] * complex(z[j]).conjugate() for z in Z)
            target = (1 if i == j else 0) + K[i][j] / 2
            assert actual == target, (i, j, actual, target)

    # Verify all boundary generators are distinct projective phase vectors.
    assert len(set(Z)) == 4
    assert all(z[0] == 1 and all(abs(v) == 1 for v in z) for z in Z)

    # Exact arithmetic for a finite, nonexhaustive all-phase sanity grid.
    vals = (1, -1, 1j, -1j)
    grid_max = max(inner_k((1,) + z).real for z in product(vals, repeat=3))
    maxima = [(1,) + z for z in product(vals, repeat=3)
              if inner_k((1,) + z) == grid_max]
    assert grid_max == 6
    assert set(maxima) == set(Z)

    # Boundary Gram has rank four: eigenvalues 1 +/- sqrt(3)/2,
    # each twice (the K minimal polynomial yields this exactly).
    # Strict positivity follows from (sqrt(3)/2)^2 = 3/4 < 1.
    assert Fraction(3, 4) < 1

    # Fourier diagonal-unitary twirl generates full basis dephasing.
    F = tuple(tuple((1j) ** (j * k) for j in range(4)) for k in range(4))
    for i in range(4):
        for j in range(4):
            c = sum(f[i] * f[j].conjugate() for f in F) / 4
            assert c == (1 if i == j else 0)

    # Saturation forces equal weights: imaginary first-row entries give
    # w2=w3=w4, then real C(1,2) and normalization give all weights 1/4.
    assert all(sum(Fraction(1, 4) * z[0] * z[j].conjugate() for z in Z) == Fraction(1, 2)
               for j in (1, 2, 3))
    print("VERIFY_OK conference_identity=16 boundary_gram=16 finite_phase_grid=64"
          " four_extremizers=4 dephasing_twirl=16")


if __name__ == "__main__":
    main()
