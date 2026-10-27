"""Illustrative finite-dimensional checks for logarithmic Hilbert-matrix sections."""
import math
import numpy as np
from scipy.special import jn_zeros


def section(alpha, N):
    m = np.arange(N + 1, dtype=float)[:, None]
    n = np.arange(N + 1, dtype=float)[None, :]
    return np.sqrt((n + 1) / (m + 1)) / (m + n + 1) / np.log(n + 2) ** (alpha / 2)


def step_kernel_value(alpha, N, m, n):
    T = math.log(N + 2)
    dm = math.log((m + 2) / (m + 1))
    dn = math.log((n + 2) / (n + 1))
    return ((n + 1) / (m + n + 1) / math.sqrt((m + 1) * dm)
            / math.sqrt((n + 1) * dn) * (T / math.log(n + 2)) ** (alpha / 2))


def check():
    for alpha in (1.2, 1.5, 1.8):
        nu = (alpha - 1) / (2 - alpha)
        # Integer nu for alpha=1.5; other nu use scipy.special.jv bracketing below.
        from scipy.special import jv
        from scipy.optimize import brentq
        zeros = []
        left, right = 1e-6, 0.02
        while len(zeros) < 3:
            if jv(nu, left) * jv(nu, right) < 0:
                zeros.append(brentq(lambda x: jv(nu, x), left, right, xtol=1e-13))
            left, right = right, right + 0.02
        target = [2 / ((2 - alpha) * z) for z in zeros]
        assert target[0] > target[1] > target[2] > 0
        for N in (31, 95, 255):
            A = section(alpha, N)
            T = math.log(N + 2)
            for m, n in ((0, 0), (1, 7), (N // 3, 2 * N // 3), (N, N)):
                dm = math.log((m + 2) / (m + 1))
                dn = math.log((n + 2) / (n + 1))
                kernel_from_matrix = A[m, n] * T ** (alpha / 2 - 1) * T / math.sqrt(dm * dn)
                assert math.isclose(kernel_from_matrix, step_kernel_value(alpha, N, m, n), rel_tol=5e-13)
            sing = np.linalg.svd(A, compute_uv=False)
            assert sing[0] > sing[1] > sing[2] > 0
            assert math.isclose(float(np.sum(sing**2)), float(np.sum(A**2)), rel_tol=2e-13)
            print(f"alpha={alpha}, N={N}, normalized top3={np.round(sing[:3] / T**(1-alpha/2),6)}")
        print(f"alpha={alpha}, Volterra Bessel top3={np.round(target,6)}")
    print('CHECK_OK: finite kernel identities, singular masses and Bessel reference values')


if __name__ == '__main__':
    check()
