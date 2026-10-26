"""Exact finite checks for a graph-dependent metapopulation dispersal theorem.

Run with Python 3.9+ (standard library only): python verify.py
Finite arithmetic checks supplement, rather than replace, the proof.
"""
from fractions import Fraction as Q
from math import sqrt


def star_polynomial(m, a, f, u):
    n = m + 1
    return a * (a + n * f) * u * u - 2 * m * f * u - m


def discriminant_coefficient(m, a):
    n = m + 1
    return a * (m - 1) ** 2 - 4 * m * n


def crossover_polynomial(m, a, f):
    n = m + 1
    delta = discriminant_coefficient(m, a)
    return -delta * f * f + 4 * m * (2 * a + n) * f + 4 * a * m


def positive_root(m, a, f):
    n = m + 1
    return (m * f + sqrt(m * m * f * f + m * a * (a + n * f))) / (a * (a + n * f))


def kernel_capacity(m, a, f, xi=1.):
    return xi * f / (1 + f) * positive_root(m, a, f)


def exact_solve(matrix, rhs):
    n = len(rhs)
    M = [[Q(matrix[i][j]) for j in range(n)] + [Q(rhs[i])] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if M[i][k])
        M[k], M[pivot] = M[pivot], M[k]
        v = M[k][k]
        M[k] = [x / v for x in M[k]]
        for i in range(n):
            if i != k:
                c = M[i][k]
                M[i] = [x - c * y for x, y in zip(M[i], M[k])]
    return [row[-1] for row in M]


def degree_energy(edges, n):
    degree = [0] * n
    L = [[0] * n for _ in range(n)]
    for i, j in edges:
        degree[i] += 1
        degree[j] += 1
        L[i][i] += 1
        L[j][j] += 1
        L[i][j] -= 1
        L[j][i] -= 1
    dbar = Q(sum(degree), n)
    h = [Q(d) - dbar for d in degree]
    system = [[Q(L[i][j]) + Q(1, n) for j in range(n)] for i in range(n)]
    u = exact_solve(system, h)
    assert sum(u) == 0
    assert all(sum(L[i][j] * u[j] for j in range(n)) == h[i] for i in range(n))
    return dbar, sum(h[i] * u[i] for i in range(n))


def check():
    identity_checks = 0
    sign_checks = 0
    for m in range(2, 33):
        n = m + 1
        for a in [Q(1), Q(2), Q(3), Q(5), Q(10), Q(20), Q(40)]:
            for f in [Q(1, 4), Q(1), Q(3), Q(5), Q(21), Q(100)]:
                det = a * (a + n * f)
                # Two-dimensional star sector of (a I + fL)^(-1) A.
                b11, b12 = m * f / det, m * (a + f) / det
                b21, b22 = (a + m * f) / det, m * f / det
                assert (b11 + b22) * det == 2 * m * f
                assert (b11 * b22 - b12 * b21) * det == -m
                # A positive threshold u equals the asymptotic capacity
                # when mu=u, where u contains the Monod prefactor.
                u = Q(2 * m, a * n) * (1 + f) / f
                lhs = star_polynomial(m, a, f, u) * a * f * f * n * n / m
                assert lhs == crossover_polynomial(m, a, f)
                identity_checks += 1
                q = crossover_polynomial(m, a, f)
                rel = kernel_capacity(m, float(a), float(f)) - float(Q(2 * m, a * n))
                if q != 0:
                    assert (rel > 0) == (q < 0)
                sign_checks += 1
    energy_checks = 0
    for m in range(2, 22):
        edges = [(0, j) for j in range(1, m + 1)]
        dbar, S = degree_energy(edges, m + 1)
        assert dbar == Q(2 * m, m + 1)
        assert S == Q(m * (m - 1) ** 2, (m + 1) ** 2)
        energy_checks += 1
    # An additional non-star connected network tests the pseudoinverse
    # definition and zero-sum normalization.
    dbar, S = degree_energy([(0, 1), (1, 2), (2, 3), (1, 4), (4, 5)], 6)
    assert S > 0 and dbar == Q(5, 3)
    # A 21-patch exact ecological threshold witness.
    m, a, f = 20, Q(10), Q(5)
    mu_for_capacity_one_fifth = Q(1, 5) * (1 + f) / f
    assert mu_for_capacity_one_fifth == Q(6, 25)
    assert star_polynomial(m, a, f, mu_for_capacity_one_fifth) == Q(-44, 25)
    assert Q(2 * m, a * (m + 1)) == Q(4, 21) < Q(1, 5)
    assert kernel_capacity(m, float(a), float(f)) > 0.2
    assert kernel_capacity(m, float(a), 100000) < 0.2
    # First-order large-exploration correction on the star.
    for m in [3, 9, 20]:
        n = m + 1
        dbar = 2 * m / n
        S = m * (m - 1) ** 2 / n ** 2
        for a in [2., 5., 10., 40.]:
            f = 100000.
            estimate = dbar / a + (S / (n * dbar) - dbar / a) / f
            assert abs(kernel_capacity(m, a, f) - estimate) < 2e-8
    print('PASS: %d exact polynomial/matrix identities' % identity_checks)
    print('PASS: %d spectral comparison checks' % sign_checks)
    print('PASS: %d exact graph-energy checks' % energy_checks)
    print('PASS: 21-patch exact threshold witness and large-f asymptotic checks')


if __name__ == '__main__':
    check()
