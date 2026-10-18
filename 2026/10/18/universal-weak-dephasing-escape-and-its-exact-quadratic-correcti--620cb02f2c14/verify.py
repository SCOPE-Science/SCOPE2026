"""Finite-size numerical cross-checks for reflected-path weak-dephasing escape.

Run: python verify.py. Requires numpy and scipy. Finite checks do not prove
infinite all-size statements; the accompanying proof supplies those steps.
"""
import numpy as np
from scipy.linalg import eigvals, solve_continuous_lyapunov


def bright_data(L, g, kappa):
    H = np.zeros((L + 1, L + 1), dtype=complex)
    H[0, 1] = H[1, 0] = np.sqrt(2.0) * g
    for j in range(1, L):
        H[j, j + 1] = H[j + 1, j] = g
    P = np.zeros_like(H)
    P[0, 0] = 1.0
    B = np.eye(L + 1, dtype=complex) - P
    A = -1j * H - kappa / 2 * P
    return A, B


def candidate_T(L, g, kappa):
    T = np.zeros((L + 1, L + 1), dtype=complex)
    T[0, 0] = L / kappa
    for i in range(L + 1):
        for j in range(i, L + 1):
            if i == j == 0:
                continue
            beta = L + 1 - j
            if i == 0:
                if j % 2:
                    T[i, j] = -1j * beta / (2 * np.sqrt(2.0) * g)
            elif i == j:
                T[i, j] = L / kappa + kappa * i * beta / (8 * g * g)
            elif (j - i) % 2 == 0:
                T[i, j] = kappa * i * beta / (8 * g * g)
            else:
                T[i, j] = -1j * beta / (2 * g)
            if i < j:
                T[j, i] = T[i, j].conjugate()
    return T


def dense_liouvillian(L, g, kappa, gamma):
    n = 2 * L + 1
    H = np.zeros((n, n), dtype=complex)
    for j in range(n - 1):
        H[j, j + 1] = H[j + 1, j] = g
    P = np.zeros((n, n), dtype=complex)
    P[L, L] = 1
    eye = np.eye(n, dtype=complex)
    K = -1j * (np.kron(eye, H) - np.kron(H.T, eye))
    K -= kappa / 2 * (np.kron(eye, P) + np.kron(P.T, eye))
    D = -np.eye(n * n)
    for j in range(n):
        D[j + n * j, j + n * j] = 0
    return K + gamma * D


def check():
    num_lyapunov = num_spectra = num_coeff = 0
    max_residual = 0.0
    for L in range(1, 9):
        for g, kappa in [(.7, .4), (1.0, 2.3), (-1.4, 1.2), (2.0, 3.0)]:
            A, B = bright_data(L, g, kappa)
            T = candidate_T(L, g, kappa)
            T_independent = solve_continuous_lyapunov(A, -B)
            residual = np.linalg.norm(A @ T + T @ A.conj().T + B)
            independent_error = np.linalg.norm(T - T_independent)
            max_residual = max(max_residual, residual, independent_error)
            assert residual < 2e-9 and independent_error < 2e-8, (L, g, kappa)
            c = (L / (4 * kappa) + kappa * (L + 1) * (L + 2) / (192 * g * g))
            assert abs(np.trace(B @ T).real / (4 * L) - c) < 2e-9
            num_lyapunov += 1
    for L in range(1, 5):
        for g, kappa in [(1.0, 1.0), (.8, 1.7), (-1.2, .6)]:
            c = L / (4 * kappa) + kappa * (L + 1) * (L + 2) / (192 * g * g)
            for gamma in [2e-4, 5e-4, 1e-3]:
                eig = eigvals(dense_liouvillian(L, g, kappa, gamma))
                top = eig[np.argmax(eig.real)]
                assert top.real < 0
                assert abs(top.imag) < 1e-7
                assert abs((top.real + gamma / 2) / gamma**2 - c) < .08
                num_spectra += 1
                num_coeff += 1
    print(f'VERIFY_OK bright_lyapunov={num_lyapunov} dense_spectra={num_spectra} '
          f'quadratic_coefficients={num_coeff} max_matrix_residual={max_residual:.2e}')


if __name__ == '__main__':
    check()
