"""Exact rational checks for the intrinsic John ellipsoids of complete-graph tree polytopes.

The all-order theorem is proved analytically. These are finite reproducibility checks,
not substitutes for that proof.
"""
from fractions import Fraction as F
from itertools import combinations


def data(n):
    m = n * (n - 1) // 2
    return m, n - 1, n * (n - 3) // 2


def ellipsoid(n):
    if n in (4, 5):
        return F(n - 2, n * (n - 1)), F(2, n * (n - 3))
    assert n >= 6
    a = F(4 * (n - 1), n * (n - 2) * (n + 1))
    return a, a


def norms(n, s):
    m, _, _ = data(n)
    k = s * (s - 1) // 2
    total = F(k * (m - k), m)
    alpha = F(s * (n - s) * (s - 1) ** 2, n * (n - 2))
    return alpha, total - alpha


def edge_norms(n):
    return F(2, n), F(n - 3, n - 1)


def test_all_facets():
    count = 0
    for n in range(4, 300):
        a, b = ellipsoid(n)
        alpha, beta = edge_norms(n)
        assert a * alpha + b * beta == F(4, n * n)
        for s in range(2, n):
            A, B = norms(n, s)
            assert A >= 0 and B >= 0
            gap2 = F((s - 1) ** 2 * (n - s) ** 2, n * n)
            support2 = a * A + b * B
            assert support2 <= gap2, (n, s, support2, gap2)
            expected_contact = ((n == 4 and s in (2, 3)) or
                                (n == 5 and s == 4))
            assert (support2 == gap2) == expected_contact, (n, s)
            count += 1
        assert a > 0 and b > 0
        assert (a == b) == (n >= 6)
    return count


def test_kkt():
    for n in (4, 5):
        a, b = ellipsoid(n)
        r2 = F(4 * (n - 1), n * (n - 2) * (n + 1))
        assert a < r2 < b
        A = F(n - 2, n * (n - 1))
        assert a == A
        edge_w = F(4, n * n) / b
        star_w = F((n - 2) ** 2, n * n) * (1 - a / b) / ((n - 2) * a)
        m, du, dw = data(n)
        assert edge_w > 0 and star_w > 0
        assert edge_w * m + star_w * n == m - 1
        assert (edge_w / F(4, n * n)) * b == 1
        assert (edge_w / F(4, n * n)) * a + (star_w / F((n - 2) ** 2, n * n)) * (n - 2) * a == 1
        # Without the co-singleton constraint, volume is maximized at the round point.
        assert F(du, dw) == (F(2, n) / F(n - 3, n - 1))
    for n in range(6, 300):
        a, b = ellipsoid(n)
        edge_w = F(4, n * n) / b
        assert edge_w == F(data(n)[0] - 1, data(n)[0])
        # The closest subset shell is farther away than the edge shell.
        assert F(n - 2, n * (n - 1)) > a


def mul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def assert_same(A, B):
    assert len(A) == len(B)
    for r, t in zip(A, B):
        assert r == t


def test_full_matrices():
    for n in range(4, 9):
        edges = list(combinations(range(n), 2))
        m = len(edges)
        # Projector to the affine translation space of fixed edge sum.
        H = [[F(int(i == j)) - F(1, m) for j in range(m)] for i in range(m)]
        # Standard component of permutation action on unordered vertex pairs.
        U = []
        for e in edges:
            row = []
            for f in edges:
                common = len(set(e).intersection(f))
                row.append(F(common, n - 2) - F(4, n * (n - 2)))
            U.append(row)
        W = [[H[i][j] - U[i][j] for j in range(m)] for i in range(m)]
        assert_same(mul(U, U), U)
        assert_same(mul(W, W), W)
        assert_same(mul(U, W), [[F(0)] * m for _ in range(m)])
        assert sum(U[i][i] for i in range(m)) == n - 1
        assert sum(W[i][i] for i in range(m)) == n * (n - 3) // 2
        # Cut-normal energy from actual matrices, not only formulas.
        for s in range(2, n):
            S = set(range(s))
            vec = [F(int(e[0] in S and e[1] in S)) for e in edges]
            Au = sum((vec[i] * U[i][j] * vec[j] for i in range(m) for j in range(m)), F(0))
            Bw = sum((vec[i] * W[i][j] * vec[j] for i in range(m) for j in range(m)), F(0))
            assert (Au, Bw) == norms(n, s)


if __name__ == "__main__":
    tested = test_all_facets()
    test_kkt()
    test_full_matrices()
    print("EXACT_VERIFICATION_OK", "facet_orbits=", tested,
          "john_kkt_orders=", 296, "projection_orders=", 5)
