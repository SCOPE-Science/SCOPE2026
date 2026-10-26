"""Numerical checks of orientation-reversal constructions for a cycle phase map.

Requires Python 3 and NumPy. These finite computations do not prove the
universal theorem; its proof uses the exact cycle spectrum and degree theory.
"""
import math
import numpy as np


def incidence(n):
    b = np.zeros((n, n), dtype=float)
    for j in range(n):
        b[j, j] = 1.0
        b[(j - 1) % n, j] = -1.0
    return b


def count_signs(values, tol=1e-9):
    return (int(np.sum(values < -tol)), int(np.sum(abs(values) <= tol)))


def check():
    cases = 0
    for n in range(3, 41):
        b = incidence(n)
        k = b @ b.T
        lam = 4.0 if n % 2 == 0 else 2.0 + 2.0 * math.cos(math.pi / n)
        assert abs(np.linalg.eigvalsh(k)[-1] - lam) < 2e-12
        boundary = np.linalg.eigvalsh(np.eye(n) - k / lam)
        assert count_signs(boundary)[0] == 0
        boundary_cosines = np.full(n, -1.0)
        if n % 2:
            boundary_cosines[-1] = 1.0
        endpoint_j = np.eye(n) + (b * boundary_cosines[np.newaxis, :]) @ b.T / lam
        assert count_signs(np.linalg.eigvalsh(endpoint_j)) == (0, 1)
        for factor in (1.00001, 1.01, 1.1, 2.0, 5.0, 100.0):
            h = factor / lam
            c0 = -1 / (h * lam)
            critical_d = np.full(n, c0)
            if n % 2:
                critical_d[-1] = 1.0
            critical_j = np.eye(n) + h * ((b * critical_d[np.newaxis, :]) @ b.T)
            assert count_signs(np.linalg.eigvalsh(critical_j)) == (0, 1)
            signs = [1] * ((n - (n % 2)) // 2) + [-1] * ((n - (n % 2)) // 2)
            if n % 2:
                signs += [0]
            assert len(signs) == n
            success = False
            eps = min((1 + c0) / 4, 0.001)
            for _ in range(25):
                c = c0 - eps
                a = math.acos(c)
                z = np.array([s * a for s in signs])
                assert abs(sum(z)) < 1e-10
                d = np.cos(z)
                j = np.eye(n) + h * ((b * d[np.newaxis, :]) @ b.T)
                eigs = np.linalg.eigvalsh(j)
                if count_signs(eigs)[0] == 1 and count_signs(eigs)[1] == 0:
                    success = True
                    break
                eps *= 0.5
            assert success, (n, factor, eigs)
            plus = np.linalg.eigvalsh(np.eye(n) + h * k)
            assert min(plus) > 0
            cases += 1
    print(f'VERIFY_OK negative_orientation_samples={cases} ring_sizes=38')


if __name__ == '__main__':
    check()
