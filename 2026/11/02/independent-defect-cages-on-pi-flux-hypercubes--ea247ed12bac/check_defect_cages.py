"""Reproduce exact and numerical checks for edge defects on pi-flux hypercubes.

Requires Python 3, NumPy, and SymPy. All matrices are generated here.
"""
from itertools import combinations
from math import sqrt
import numpy as np
import sympy as sp


def hopping(d):
    n = 1 << d
    h = np.zeros((n, n), dtype=np.int64)
    for u in range(n):
        for j in range(d):
            v = u ^ (1 << j)
            parity = (u & ((1 << j) - 1)).bit_count() % 2
            h[u, v] = -1 if parity else 1
    assert np.array_equal(h, h.T)
    assert np.array_equal(h @ h, d * np.eye(n, dtype=np.int64))
    return h


def edges(d):
    return [(u, u ^ (1 << j)) for u in range(1 << d)
            for j in range(d) if u < (u ^ (1 << j))]


def compatible(e, f):
    return all((u ^ v).bit_count() >= 2 for u in e for v in f)


def matchings(d, k):
    ee = edges(d)
    selected = []
    # Two deterministic distinct orderings test nontrivial placements.
    for order in (ee, ee[::-1]):
        chosen = []
        for e in order:
            if all(compatible(e, f) for f in chosen):
                chosen.append(e)
                if len(chosen) == k:
                    break
        if len(chosen) == k and chosen not in selected:
            selected.append(chosen)
    return selected


def eigen_prediction(d, strengths):
    k = len(strengths)
    expected = [-sqrt(d)] * ((1 << (d - 1)) - 2 * k)
    expected += [sqrt(d)] * ((1 << (d - 1)) - 2 * k)
    for a in strengths:
        r = sqrt(a * a + 4 * (d - a))
        hi, lo = (r + a) / 2, (r - a) / 2
        expected.extend([-hi, -lo, lo, hi])
    return np.sort(np.asarray(expected))


def main():
    z, a, d = sp.symbols('z a d')
    small = sp.Matrix([[0, -a, d - a, 0],
                       [-a, 0, 0, d - a],
                       [1, 0, 0, 0], [0, 1, 0, 0]])
    actual = sp.factor(small.charpoly(z).as_expr())
    want = sp.expand((z*z + a*z + a - d) * (z*z - a*z + a - d))
    assert sp.expand(actual - want) == 0
    print('Exact symbolic four-dimensional characteristic polynomial: PASS')

    cases = 0
    worst = 0.0
    cages = 0
    for dim in range(2, 9):
        base = hopping(dim)
        for k in range(1, min(3, 1 << (dim - 2)) + 1):
            for matching in matchings(dim, k):
                for strength_choice in range(3):
                    alpha = [1.0 if strength_choice == 0 else
                             (0.25 + (idx % 3) * 0.25 if strength_choice == 1 else
                              0.125 + (idx % 4) * 0.2)
                             for idx in range(k)]
                    h = base.astype(np.float64)
                    for (u, v), loss in zip(matching, alpha):
                        h[u, v] *= 1 - loss
                        h[v, u] *= 1 - loss
                    diff = np.max(np.abs(np.linalg.eigvalsh(h) -
                                         eigen_prediction(dim, alpha)))
                    assert diff < 2e-10, (dim, k, matching, diff)
                    worst = max(worst, diff)
                    cases += 1
                # Verify local cages and mutual orthogonality exactly.
                subspaces = []
                for u, v in matching:
                    columns = np.stack([np.eye(1 << dim, dtype=np.int64)[:, u],
                                        np.eye(1 << dim, dtype=np.int64)[:, v],
                                        base[:, u], base[:, v]], axis=1)
                    assert np.linalg.matrix_rank(columns) == 4
                    allowed = set([u, v])
                    allowed.update(np.flatnonzero(base[:, u]).tolist())
                    allowed.update(np.flatnonzero(base[:, v]).tolist())
                    assert len(allowed) == 2 * dim
                    assert set(np.flatnonzero(columns.any(axis=1))).issubset(allowed)
                    assert np.array_equal(base @ (base @ columns), dim * columns)
                    for other in subspaces:
                        assert np.count_nonzero(other.T @ columns) == 0
                    subspaces.append(columns)
                    cages += 1
    print(f'Numerical eigenvalue comparisons: {cases} PASS; worst max error {worst:.3g}')
    print(f'Exact local cage and pairwise orthogonality tests: {cages} PASS')

    h3 = sp.Matrix(hopping(3))
    def delete_pair(pair):
        m = h3.copy()
        for u, v in pair:
            m[u, v] = m[v, u] = 0
        return sp.factor(m.charpoly(z).as_expr())
    induced = delete_pair([(0, 1), (6, 7)])
    not_induced = delete_pair([(0, 1), (2, 3)])
    expected_induced = (z*z - 1)**2 * (z*z - 4)**2
    expected_noninduced = (z**4 - 5*z*z + 5)**2
    assert sp.expand(induced - expected_induced) == 0
    assert sp.expand(not_induced - expected_noninduced) == 0
    print('Exact 3-cube induced-versus-noninduced spectral boundary: PASS')
    print('All checks passed.')


if __name__ == '__main__':
    main()
