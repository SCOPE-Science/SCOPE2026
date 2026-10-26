#!/usr/bin/env python3
"""Check the flat-band Kitaev-chain dimerization and small-block polynomials.

Uses only the Python standard library. Numerical checks support, but do not
replace, the exact invariant-subspace proof in RESULT.md.
"""
from math import sqrt

TOL = 2e-10
J = 1.0
GAMMAS = (0.0, 1.0 / 3.0, 1.0, 7.0 / 3.0)


def zero_matrix(n):
    return [[0j for _ in range(n)] for _ in range(n)]


def matmul(a, b):
    n, k, m = len(a), len(b), len(b[0])
    out = zero_matrix(n)
    for i in range(n):
        for q in range(k):
            z = a[i][q]
            if z:
                for j in range(m):
                    out[i][j] += z * b[q][j]
    return out


def adjoint(a):
    return [[a[j][i].conjugate() for j in range(len(a))]
            for i in range(len(a[0]))]


def original_matrix(n, m, gamma):
    h = zero_matrix(2 * n)
    sz = ((1, 0), (0, -1))
    sx = ((0, 1), (1, 0))
    for k in range(n - 1):
        for a in range(2):
            for b in range(2):
                val = -J * sz[a][b] / 2 + 1j * J * sx[a][b] / 2
                h[2*k+a][2*(k+1)+b] = val
                h[2*(k+1)+b][2*k+a] = val.conjugate()
    for site, sign in ((m - 1, 1), (n - m, -1)):
        for a in range(2):
            h[2*site+a][2*site+a] += 1j * gamma * sign * sz[a][a] / 2
    return h


def uv_transform(n):
    u = (1j / sqrt(2), 1 / sqrt(2))
    v = (-1j / sqrt(2), 1 / sqrt(2))
    q = zero_matrix(2 * n)
    for k in range(n):
        for a in range(2):
            q[2*k+a][2*k] = u[a]
            q[2*k+a][2*k+1] = v[a]
    return q


def expected_uv_matrix(n, m, gamma):
    h = zero_matrix(2 * n)
    # Dimer links |k,u> <-> |k+1,v>.
    for k in range(n - 1):
        iu, iv_next = 2*k, 2*(k+1)+1
        h[iu][iv_next] = J
        h[iv_next][iu] = J
    # In the (u,v) basis, sigma_z = -(|u><v|+|v><u|).
    for site, sign in ((m - 1, 1), (n - m, -1)):
        iu, iv = 2*site, 2*site+1
        val = -1j * gamma * sign / 2
        h[iu][iv] = val
        h[iv][iu] = val
    return h


def poly_tridiagonal(off_diagonal):
    # Coefficients in ascending powers of lambda.
    d0 = [1.0 + 0j]
    d1 = [0j, 1.0 + 0j]
    for a in off_diagonal:
        nxt = [0j] * (max(len(d1) + 1, len(d0)))
        for i, c in enumerate(d1):
            nxt[i + 1] += c
        for i, c in enumerate(d0):
            nxt[i] -= a * a * c
        d0, d1 = d1, nxt
    return d1


def close_poly(got, want):
    size = max(len(got), len(want))
    a = got + [0j] * (size - len(got))
    b = want + [0j] * (size - len(want))
    return all(abs(x-y) < TOL for x, y in zip(a, b))


def check_block_polynomials(gamma):
    p3 = poly_tridiagonal((-1j*gamma/2, J))
    e3 = [0j, -J*J + gamma*gamma/4, 0j, 1+0j]
    p4 = poly_tridiagonal((J, -1j*gamma/2, J))
    e4 = [J**4, 0j, gamma*gamma/4 - 2*J*J, 0j, 1+0j]
    p6 = poly_tridiagonal((J, -1j*gamma/2, J, 1j*gamma/2, J))
    e6 = [-J**6, 0j, 3*J**4 - gamma*gamma*J*J/2 + gamma**4/16,
          0j, -3*J*J + gamma*gamma/2, 0j, 1+0j]
    assert close_poly(p3, e3), ("P3", gamma, p3, e3)
    assert close_poly(p4, e4), ("P4", gamma, p4, e4)
    assert close_poly(p6, e6), ("P6", gamma, p6, e6)


def main():
    cases = 0
    for n in (4, 6, 8, 10):
        for m in range(1, n // 2 + 1):
            q = uv_transform(n)
            for gamma in GAMMAS:
                h = original_matrix(n, m, gamma)
                transformed = matmul(matmul(adjoint(q), h), q)
                expected = expected_uv_matrix(n, m, gamma)
                for i in range(2*n):
                    for j in range(2*n):
                        assert abs(transformed[i][j] - expected[i][j]) < TOL, (
                            "basis mismatch", n, m, gamma, i, j,
                            transformed[i][j], expected[i][j])
                check_block_polynomials(gamma)
                cases += 1
    print(f"PASS: {cases} matrix-transform cases; all 3x3, 4x4, and 6x6 determinant recurrences verified.")


if __name__ == "__main__":
    main()
