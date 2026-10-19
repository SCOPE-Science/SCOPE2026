"""Independent numerical spot checks for an exact complete-graph Lindbladian theorem.

Requires Python 3.10+ and NumPy. All finite-size computations are checks, not
substitutes for the dimension-independent proof in RESULT.md.
"""
from math import sqrt
import numpy as np

CHECKS = 0
MAX_ERROR = 0.0


def check(error: float, tolerance: float, description: str):
    global CHECKS, MAX_ERROR
    error = float(error)
    CHECKS += 1
    MAX_ERROR = max(MAX_ERROR, error)
    if not np.isfinite(error) or error > tolerance:
        raise AssertionError(f"{description}: error={error}, tolerance={tolerance}")


def full_liouvillian(n: int, J: float, gamma: float) -> np.ndarray:
    h = J * (np.ones((n, n)) - np.eye(n))
    matrix = np.zeros((n * n, n * n), dtype=complex)
    for j in range(n):
        for k in range(n):
            e = np.zeros((n, n), dtype=complex)
            e[j, k] = 1
            out = -1j * (h @ e - e @ h)
            out -= gamma * (e - np.diag(np.diag(e)))
            matrix[:, j * n + k] = out.reshape(-1)
    return matrix


def predicted(n: int, J: float, gamma: float) -> np.ndarray:
    coeffs = [1., 2. * gamma, gamma * gamma + n * n * J * J,
              2. * n * gamma * J * J]
    cubic = np.roots(coeffs)
    return np.concatenate(([0.], np.repeat(-gamma, (n - 1) * (n - 2)),
                           np.repeat(cubic, n - 1)))


def match_eigenvalues(actual: np.ndarray, expected: np.ndarray) -> float:
    used = np.zeros(len(actual), dtype=bool)
    biggest = 0.
    for z in expected:
        distances = np.abs(actual - z)
        distances[used] = np.inf
        idx = int(np.argmin(distances))
        biggest = max(biggest, float(distances[idx]))
        used[idx] = True
    return biggest


def actual_gap(eigenvalues: np.ndarray) -> float:
    nonzero = [z for z in eigenvalues if abs(z) > 1e-8]
    return min(-z.real for z in nonzero)


def main():
    for n in range(3, 9):
        for J in (0.4, 1.1):
            r_star = J * sqrt(n / (n - 2))
            gamma_star = (n - 1) * r_star
            for factor in (0.03, 0.25, 0.7, 1.0, 1.35, 3.0, 9.0):
                gamma = factor * gamma_star
                full = np.linalg.eigvals(full_liouvillian(n, J, gamma))
                theory = predicted(n, J, gamma)
                error = match_eigenvalues(full, theory)
                check(error, 2e-6, f"spectrum n={n}, J={J}, factor={factor}")
                gap = actual_gap(full)
                check(max(0., gap - r_star), 2e-7,
                      f"universal upper bound n={n}, factor={factor}")
                if factor == 1.0:
                    check(abs(gap-r_star), 2e-7,
                          f"sharp gap n={n}, J={J}")
                else:
                    check(max(0., gap-r_star+1e-7), 2e-7,
                          f"strict below optimum n={n}, factor={factor}")
            # The cubic has the analytically asserted root at the proposed optimum.
            check(abs((-r_star)**3+2*gamma_star*r_star*r_star
                      -(gamma_star**2+n*n*J*J)*r_star
                      +2*n*gamma_star*J*J),
                  1e-8, f"exact cubic root n={n}")
    print(f"PASS: {CHECKS} numerical checks, max absolute discrepancy {MAX_ERROR:.3e}")


if __name__ == '__main__':
    main()
