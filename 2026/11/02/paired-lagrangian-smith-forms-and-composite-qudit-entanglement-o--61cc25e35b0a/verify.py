"""Exact reproducibility checks for the paired-Lagrangian cut spectrum.
Run: python verify.py  (requires sympy and numpy).  All matrix entries are integers.
"""
from itertools import product
from math import comb, gcd, prod
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def H(m):
    N = (1 << m) - 1
    return sp.Matrix(N, N, lambda i, j: (((int(i) + 1) & (int(j) + 1)).bit_count() & 1))


def C(m):
    # Rows: U* followed by W*; columns: all (a,b) with nonzero a and b.
    h = H(m)
    n = h.rows
    return sp.Matrix(2 * n, n * n, lambda i, j:
                     h[i, j % n] if i < n else h[i - n, j // n])


def expected_snf(m):
    return [2 ** j for j in range(m)
            for _ in range(2 * comb(m, j + 1) - (j == m - 1))]


def rank_formula(m, d):
    himage = prod((d // gcd(d, 2 ** j)) ** comb(m, j + 1)
                  for j in range(m))
    assert himage * himage * gcd(d, 2 ** (m - 1)) % d == 0
    return himage ** 2 * gcd(d, 2 ** (m - 1)) // d


def dot_image(m, d):
    h = H(m)
    n = h.rows
    rows = [tuple(int(h[i, j]) for i in range(n)) for j in range(n)]
    return {tuple(sum(t * x for t, x in zip(row, vec)) % d for row in rows)
            for vec in product(range(d), repeat=n)}


def direct_cut_image(m, d):
    mat = C(m)
    nrows, ncols = mat.shape
    columns = [tuple(int(mat[i, j]) for i in range(nrows)) for j in range(ncols)]
    return {tuple(sum(t * x for t, x in zip(col, vec)) % d for col in columns)
            for vec in product(range(d), repeat=nrows)}


def direct_qubit_density(m):
    # A self-contained Hilbert-space check for Sp(4,2) with two-context cut.
    assert m == 2
    n = (1 << m) - 1
    v = [(a, 0) for a in range(1, n + 1)] + [(0, b) for b in range(1, n + 1)]
    v += [(a, b) for a in range(1, n + 1) for b in range(1, n + 1)]
    na, nb = 2 * n, n * n
    edges = [(i, j) for i in range(len(v)) for j in range(i + 1, len(v))
             if ((((v[i][0] & v[j][1]).bit_count() +
                    (v[i][1] & v[j][0]).bit_count()) & 1) == 1)]
    psi = np.empty((1 << na, 1 << nb), dtype=float)
    for a in range(1 << na):
        for b in range(1 << nb):
            bits = a | (b << na)
            phase = sum(((bits >> i) & 1) * ((bits >> j) & 1) for i, j in edges) & 1
            psi[a, b] = (1 if phase == 0 else -1) / np.sqrt(1 << len(v))
    rho = psi @ psi.T
    eigs = np.linalg.eigvalsh(rho)
    rank = rank_formula(m, 2)
    assert np.allclose(eigs[-rank:], [1 / rank] * rank, atol=1e-12)
    assert np.max(abs(eigs[:-rank])) < 1e-12
    return rank


def main():
    num = 0
    for m in range(1, 7):
        h = H(m)
        n = h.rows
        # Zeta factorization: H = Z diag((-2)^(|S|-1)) Z^T,
        # using nonempty binary subsets and integer arithmetic.
        z = sp.Matrix(n, n, lambda i, j: int(((int(i) + 1) & (int(j) + 1)) == int(j) + 1))
        ds = sp.diag(*[(-2) ** ((j + 1).bit_count() - 1) for j in range(n)])
        assert z * ds * z.T == h
        assert z.det() in (-1, 1) if m <= 4 else True
        num += 1
    for m in (2, 3):
        mat = C(m)
        ds = smith_normal_form(mat, domain=ZZ)
        got = sorted(abs(int(ds[i, i])) for i in range(min(ds.shape)) if ds[i, i])
        assert got == sorted(expected_snf(m)), (m, got)
        for d in (2, 3, 4, 6, 8):
            actual = prod(d // gcd(d, x) for x in got)
            assert actual == rank_formula(m, d)
            num += 1
    for m, dims in ((2, (2, 3, 4, 5, 6, 8)), (3, (2, 3, 4))):
        for d in dims:
            img = dot_image(m, d)
            predicted_h = prod((d // gcd(d, 2 ** j)) ** comb(m, j + 1) for j in range(m))
            assert len(img) == predicted_h
            constant_count = sum(tuple([c] * ((1 << m) - 1)) in img for c in range(d))
            assert constant_count == d // gcd(d, 2 ** (m - 1))
            num += 1
    for d in (2, 3, 4, 5, 6):
        assert len(direct_cut_image(2, d)) == rank_formula(2, d)
        num += 1
    assert len(direct_cut_image(3, 2)) == rank_formula(3, 2)
    num += 1
    assert direct_qubit_density(2) == 16
    print(f'VERIFY_OK checks={num + 1}, exact Smith, modular images and a direct quantum spectrum')


if __name__ == '__main__':
    main()
