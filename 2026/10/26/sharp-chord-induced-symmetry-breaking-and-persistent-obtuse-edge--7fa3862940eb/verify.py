#!/usr/bin/env python3
"""Finite numerical checks for the chorded even-cycle Kuramoto formulas.

Uses only the Python standard library. The analytical all-size proof is in RESULT.md;
these floating-point tests are corroboration, not a certificate for all sizes.
"""
import math


def threshold(m):
    return 2.0 * math.cos(math.pi / m) / m


def weight_from_x(m, x):
    return 2.0 * math.cos(math.pi / m) * math.sin(x) / math.sin(m * x)


def angles(m, x, sign=1):
    a = math.pi / m + x
    b = math.pi / m - x
    return [sign * (j * a if j <= m else m * a + (j - m) * b)
            for j in range(2 * m)]


def hessian_and_residual(m, k, phase):
    N = 2 * m
    H = [[0.0] * N for _ in range(N)]
    rhs = [0.0] * N
    edges = [(i, (i + 1) % N, 1.0) for i in range(N)]
    edges.append((0, m, k))
    for i, j, w in edges:
        t = phase[j] - phase[i]
        current = w * math.sin(t)
        conductance = w * math.cos(t)
        rhs[i] += current
        rhs[j] -= current
        H[i][i] += conductance
        H[j][j] += conductance
        H[i][j] -= conductance
        H[j][i] -= conductance
    return H, max(abs(t) for t in rhs)


def positive_on_quotient(H):
    # Cholesky on the principal minor; a Laplacian with a single constant kernel
    # is positive on the phase quotient exactly when this minor is positive.
    M = [row[1:] for row in H[1:]]
    n = len(M)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            x = M[i][j] - sum(L[i][r] * L[j][r] for r in range(j))
            if i == j:
                if x <= 1.e-12:
                    return False
                L[i][j] = math.sqrt(x)
            else:
                L[i][j] = x / L[j][j]
    return True


def energy(H, v):
    return sum(v[i] * sum(H[i][j] * v[j] for j in range(len(v)))
               for i in range(len(v)))


def harmonic_test(m):
    return [j / m if j <= m else (2 * m - j) / m for j in range(2 * m)]


def invert_weight(m, k):
    low, high = 0.0, math.pi / m
    for _ in range(90):
        mid = (low + high) / 2.0
        if weight_from_x(m, mid) < k:
            low = mid
        else:
            high = mid
    return (low + high) / 2.0


def run():
    tested = 0
    for m in (4, 5, 6, 7, 8, 9, 12, 16):
        critical = threshold(m)
        obtuse_boundary = 2 * math.cos(math.pi / m) * math.sin(math.pi / (2 * m))
        assert obtuse_boundary > critical
        # Test the original symmetric twist on both sides of its threshold.
        for mult, expected_stability in ((0.5, True), (0.99, True),
                                         (1.01, False), (2., False)):
            k = mult * critical
            H, residual = hessian_and_residual(m, k, angles(m, 0.))
            assert residual < 2e-12
            if expected_stability:
                assert positive_on_quotient(H)
            else:
                v = harmonic_test(m)
                assert abs(energy(H, v) - (critical - k)) < 5.e-11
                assert energy(H, v) < 0
            tested += 1
        # Separately assemble vector fields and Hessians for each branch.
        for fraction in (0.125, 0.25, 0.5, 0.75, 0.875):
            x = fraction * math.pi / m
            k = weight_from_x(m, x)
            assert k > critical
            expected_cos = -math.cos(m * x)
            if fraction == 0.5:
                assert abs(expected_cos) < 1e-12
                assert abs(k - obtuse_boundary) < 1e-12
            else:
                assert (expected_cos < 0) == (k < obtuse_boundary)
            for branch_sign in (-1, +1):
                for x_sign in (-1, +1):
                    H, residual = hessian_and_residual(
                        m, k, angles(m, x_sign * x, branch_sign))
                    assert residual < 3e-11, (m, k, x, residual)
                    assert positive_on_quotient(H), (m, k, x)
                    tested += 1
        # Inversion tests are logically independent of the generated x-grid.
        for mult in (1.01, 1.1, 2., 10., 100.):
            k = mult * critical
            x = invert_weight(m, k)
            assert 0 < x < math.pi / m
            assert abs(weight_from_x(m, x) / k - 1) < 2e-10
            tested += 1
    print('VERIFY_OK')
    print('SIZES 4 5 6 7 8 9 12 16')
    print('VECTOR_FIELD_AND_HESSIAN_TESTS', tested)
    print('CRITICAL_K_M4', repr(threshold(4)))
    print('OBTUSE_END_K_M4', repr(2 * math.cos(math.pi / 4) * math.sin(math.pi / 8)))
    print('Finite numerical corroboration only; all-size proof analytical')


if __name__ == '__main__':
    run()
