import math
import numpy as np


def gs_matrices(A):
    a = A[0, 0]
    c = A[0, 1]
    d = A[1, 1]
    q = c * c / (a * d)
    T12 = np.array([[0.0, -c / a], [0.0, q]])
    T21 = np.array([[q, 0.0], [-c / d, 0.0]])
    return T12, T21, q


def matrix_from_spectrum(kappa, theta):
    ct = math.cos(theta)
    st = math.sin(theta)
    Q = np.array([[ct, -st], [st, ct]])
    return Q @ np.diag([1.0, kappa]) @ Q.T


def envelope(kappa):
    rho = (kappa - 1.0) / (kappa + 1.0)
    return rho * math.sqrt(1.0 + rho * rho)


def threshold():
    rho = math.sqrt((math.sqrt(5.0) - 1.0) / 2.0)
    return (1.0 + rho) / (1.0 - rho)


def main():
    max_formula_error = 0.0
    max_power_error = 0.0
    max_envelope_error = 0.0
    for kappa in [1.2, 2.0, 5.0, 10.0, 100.0]:
        grid_best = 0.0
        for theta in np.linspace(0.0, math.pi / 2.0, 20001):
            A = matrix_from_spectrum(kappa, theta)
            T12, T21, q = gs_matrices(A)
            a, c, d = A[0, 0], A[0, 1], A[1, 1]
            n12 = np.linalg.norm(T12, 2)
            n21 = np.linalg.norm(T21, 2)
            f12 = math.sqrt((c / a) ** 2 + q ** 2)
            f21 = math.sqrt((c / d) ** 2 + q ** 2)
            max_formula_error = max(max_formula_error, abs(n12 - f12), abs(n21 - f21))
            max_power_error = max(max_power_error, np.linalg.norm(T12 @ T12 - q * T12, 2), np.linalg.norm(T21 @ T21 - q * T21, 2))
            grid_best = max(grid_best, min(n12, n21))
        max_envelope_error = max(max_envelope_error, abs(grid_best - envelope(kappa)))
        print(f"kappa={kappa:g} grid_best={grid_best:.12f} closed={envelope(kappa):.12f}")

    kstar = threshold()
    print(f"kappa_star={kstar:.15f}")
    print(f"envelope(kappa_star)={envelope(kstar):.15f}")
    print(f"quartic_at_kappa_star={kstar**4 - 8*kstar**3 - 2*kstar**2 - 8*kstar + 1:.3e}")

    A6 = np.array([[2.0, 2.0], [2.0, 5.0]])
    T12, T21, _ = gs_matrices(A6)
    print(f"kappa6_bad_order={np.linalg.norm(T12, 2):.12f}")
    print(f"kappa6_good_order={np.linalg.norm(T21, 2):.12f}")

    for kappa in [10.0, 100.0, 1000.0]:
        A = np.array([[2.0, math.sqrt(kappa - 2.0)], [math.sqrt(kappa - 2.0), kappa - 1.0]])
        eig = np.linalg.eigvalsh(A)
        T12, T21, _ = gs_matrices(A)
        print(
            f"family kappa={kappa:g} eig=({eig[0]:.12f},{eig[1]:.12f}) "
            f"small_diag_first={np.linalg.norm(T12,2):.12f} large_diag_first={np.linalg.norm(T21,2):.12f}"
        )

    print(f"max_formula_error={max_formula_error:.3e}")
    print(f"max_power_error={max_power_error:.3e}")
    print(f"max_envelope_grid_error={max_envelope_error:.3e}")


if __name__ == "__main__":
    main()
