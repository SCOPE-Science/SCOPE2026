"""Reproduce finite-dimensional checks for a coherently driven dissipative qubit.

Requirements: numpy, scipy. These tests corroborate an analytic asymptotic
proof; they do not certify an infinite-parameter limit by enumeration.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

IDENTITY = np.eye(2, dtype=complex)
LOWER = np.array([[0, 1], [0, 0]], dtype=complex)
RAISE = LOWER.conj().T
SIGMA_X = LOWER + RAISE


def liouvillian(omega):
    hamiltonian = 0.5 * omega * SIGMA_X
    decay = RAISE @ LOWER
    def generator(x):
        return (-1j * (hamiltonian @ x - x @ hamiltonian)
                + LOWER @ x @ RAISE - 0.5 * (decay @ x + x @ decay))
    basis = []
    for row in range(2):
        for col in range(2):
            matrix = np.zeros((2, 2), dtype=complex)
            matrix[row, col] = 1
            basis.append(matrix)
    return np.column_stack([generator(x).reshape(4) for x in basis])


def partial_transpose_choi(omega, elapsed):
    superoperator = expm(elapsed * liouvillian(omega))
    choi = np.zeros((4, 4), dtype=complex)
    for a in range(2):
        for b in range(2):
            input_matrix = np.zeros((2, 2), dtype=complex)
            input_matrix[a, b] = 1
            evolved = (superoperator @ input_matrix.reshape(4)).reshape(2, 2)
            for i in range(2):
                for j in range(2):
                    choi[2 * i + a, 2 * j + b] = evolved[i, j] / 2
    partial = choi.reshape(2, 2, 2, 2).transpose(0, 3, 2, 1).reshape(4, 4)
    assert np.max(np.abs(partial - partial.conj().T)) < 1e-11
    return partial


def min_eigenvalue(omega, elapsed):
    return float(np.linalg.eigvalsh(partial_transpose_choi(omega, elapsed))[0])


def run():
    for omega in (0.08, 0.045, 0.025):
        for shift in (-1.0, 1.0):
            elapsed = 4 * math.log(1 / omega) + shift
            obtained = min_eigenvalue(omega, elapsed) / omega**4
            predicted = (1 - math.exp(-shift)) / 2
            assert abs(obtained - predicted) < 0.065, (
                omega, shift, obtained, predicted)
        transition = brentq(lambda t: min_eigenvalue(omega, t),
                            4 * math.log(1 / omega) - 2,
                            4 * math.log(1 / omega) + 2,
                            xtol=1e-10)
        assert abs(transition - 4 * math.log(1 / omega)) < 0.22
    for elapsed in (0.2, 1.0, 4.0, 10.0):
        assert min_eigenvalue(0.0, elapsed) < -1e-6
    print('VERIFY_OK weak_drive_scaled_PPT=6 first_EB_times=3 zero_drive=4')


if __name__ == '__main__':
    run()
