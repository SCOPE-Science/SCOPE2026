"""Optional finite-section check of the quadrupole limit; requires NumPy and SciPy.
Run: python3 check_numeric.py
The finite-section experiment is not a proof of the infinite-dimensional theorem.
"""
import math
import numpy as np
from scipy.special import gammainc, gamma, gammaln

def kyfan(N, s, eps, matrix_size=22, angles=768):
    theta = np.arange(angles) * (2 * np.pi / angles)
    boundary = s + eps * np.cos(2 * theta)
    assert np.all(boundary > 0)
    matrix = np.empty((matrix_size, matrix_size), dtype=complex)
    for j in range(matrix_size):
        for k in range(j, matrix_size):
            a = (j + k) / 2 + 1
            moment = gammainc(a, boundary) * gamma(a)
            moment *= np.exp(-0.5 * (gammaln(j + 1) + gammaln(k + 1)))
            val = np.mean(moment * np.exp(1j * (k - j) * theta))
            matrix[j, k] = val
            matrix[k, j] = val.conjugate()
    return np.linalg.eigvalsh(matrix)[-N:].sum()

def main():
    for N, s in ((1, 1.3), (2, 1.3), (4, 2.2), (5, 4.1)):
        b = math.exp(-s) * s ** (N - 1) / math.factorial(N - 1)
        predicted = b * (2 * s + N + 1) / (4 * (s + N) * (s + N + 1))
        base = kyfan(N, s, 0)
        ratios = [(base - kyfan(N, s, eps)) / (eps * eps * predicted)
                  for eps in (0.1, 0.05, 0.02)]
        assert abs(ratios[-1] - 1) < 0.002, (N, s, ratios)
        assert abs(ratios[-1] - 1) < abs(ratios[0] - 1), (N, s, ratios)
    print("FOCK_KYFAN_QUADRUPOLE_FINITE_MATRIX_CHECKS_OK cases=12")

if __name__ == "__main__":
    main()
