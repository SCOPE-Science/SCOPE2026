"""Numerical cross-checks of the spectral density projection phase boundary.

Requires Python 3.10+ and numpy 1.24+. Run: python verify_density.py
Finite tests corroborate but do not replace the analytic proof.
"""
import math
import numpy as np


def sp(A, p):
    return float(np.linalg.norm(np.linalg.eigvalsh(A), ord=p))


def density_projection(A):
    vals, U = np.linalg.eigh(A)
    lo, hi = float(min(vals) - 2), float(max(vals) + 2)
    for _ in range(100):
        tau = (lo + hi) / 2
        if float(np.maximum(vals - tau, 0).sum()) > 1:
            lo = tau
        else:
            hi = tau
    new_vals = np.maximum(vals - (lo + hi) / 2, 0)
    return (U * new_vals) @ U.conj().T


def check_traceless_quartic():
    # Exact Gaussian-integer matrix arithmetic, without eigenvalue rounding.
    def multiply(A, B):
        out = []
        for i in range(3):
            row = []
            for j in range(3):
                re = im = 0
                for k in range(3):
                    x, y = A[i][k]
                    u, v = B[k][j]
                    re += x * u - y * v
                    im += x * v + y * u
                row.append((re, im))
            out.append(row)
        return out

    count = 0
    for a in [-2, -1, 0, 1, 2]:
        for b in [-2, -1, 0, 1, 2]:
            H = [[(a, 0), (1, 0), (0, 2)],
                 [(1, 0), (b, 0), (1, -1)],
                 [(0, -2), (1, 1), (-a-b, 0)]]
            H2 = multiply(H, H)
            H4 = multiply(H2, H2)
            tr2 = sum(H2[i][i][0] for i in range(3))
            tr4 = sum(H4[i][i][0] for i in range(3))
            assert 2 * tr4 == tr2**2
            count += 1
    return count


def check_nonexpansive_tests():
    rng = np.random.default_rng(2718)
    count = 0
    for n, p in [(2, 1.3), (2, 4), (2, 7), (3, 2), (3, 4), (4, 2)]:
        for _ in range(25):
            X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            A = (X + X.conj().T) / 2
            A += (1 - np.trace(A).real) / n * np.eye(n)
            X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
            B = (X + X.conj().T) / 2
            B += (1 - np.trace(B).real) / n * np.eye(n)
            assert sp(density_projection(A) - density_projection(B), p) <= sp(A - B, p) + 1e-8
            count += 1
    return count


def check_expansive_witnesses():
    count = 0
    Y = np.array([[1., 0., 1.], [0., -1., 0.], [1., 0., 0.]])
    Z = np.diag([1., 1., -2.])
    phi = (1 + math.sqrt(5)) / 2
    for p in [1.5, 2.5, 3, 3.5, 4.5, 5, 7]:
        dp = (phi ** (p - 3) + phi ** (3 - p)) / math.sqrt(5) - 1
        assert abs(dp) > 1e-6
        t = -math.copysign(0.0005, dp)
        H = Y + t * Z
        assert sp(Y, p) > sp(H, p)
        delta, eps = 1e-7, 1e-9
        A = np.diag([1 / 3, 2 / 3 + delta, -delta])
        assert sp(density_projection(A + eps * H) - density_projection(A), p) > sp(eps * H, p)
        count += 1
    Y4 = np.diag([1., 1., -2., 0.])
    Z4 = np.diag([1., 1., 1., -3.])
    for p in [1.5, 1.8, 2.5, 3, 4, 5, 7]:
        dp = 2 - 2 ** (p - 1)
        assert abs(dp) > 1e-6
        t = -math.copysign(0.0005, dp)
        H = Y4 + t * Z4
        assert sp(Y4, p) > sp(H, p)
        A = np.diag([(1 + 0.01) / 3] * 3 + [-0.01])
        eps = 1e-6
        assert sp(density_projection(A + eps * H) - density_projection(A), p) > sp(eps * H, p)
        count += 1
    return count


if __name__ == '__main__':
    c1 = check_traceless_quartic()
    c2 = check_nonexpansive_tests()
    c3 = check_expansive_witnesses()
    print(f'DENSITY_PROJECTION_CHECK_OK exact-polynomial={c1} numerical-nonexpansive={c2} numerical-expansive={c3}')
