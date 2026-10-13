"""Finite, independent numerical checks of the Kulli path-windmill rank theorem.

Requires NumPy. The unrestricted theorem follows from the accompanying proof;
these tests do not certify infinitely many graph orders.
"""
import math
import numpy as np


def adjacency(blades: int, length: int) -> np.ndarray:
    order = 1 + blades * length
    matrix = np.zeros((order, order), dtype=float)
    for blade in range(blades):
        first = 1 + blade * length
        for k in range(length):
            matrix[0, first + k] = matrix[first + k, 0] = 1
        for k in range(length - 1):
            matrix[first + k, first + k + 1] = 1
            matrix[first + k + 1, first + k] = 1
    return matrix


def average_mixing(matrix: np.ndarray) -> np.ndarray:
    eigvals, eigvecs = np.linalg.eigh(matrix)
    result = np.zeros_like(matrix)
    left = 0
    while left < len(eigvals):
        right = left + 1
        while right < len(eigvals) and abs(eigvals[right] - eigvals[left]) < 1e-8:
            right += 1
        block = eigvecs[:, left:right]
        projector = block @ block.T
        result += projector * projector
        left = right
    return result


def main() -> None:
    trials = 0
    worst_null = 0.0
    smallest_positive = 1.0
    separation = 0
    profile_tests = 0
    max_n = 0
    for m in range(2, 12):
        L = m + 1
        positions = np.arange(1, m + 1)
        profiles = np.vstack([np.sin(np.pi * j * positions / L) ** 2 for j in range(1, m + 1)])
        assert np.linalg.matrix_rank(profiles, tol=1e-9) == math.ceil(m / 2)
        profile_tests += 1
        B = np.diag(np.ones(m - 1), 1) + np.diag(np.ones(m - 1), -1)
        for j in range(2, m + 1, 2):
            theta = j * np.pi / L
            lam = 2 * np.cos(theta)
            # A symmetric solution of (lam*I-B)w=1 at the even path mode.
            w = (1 - np.cos(positions * theta)) / (lam - 2)
            assert np.max(np.abs((lam * np.eye(m) - B) @ w - 1)) < 2e-11
            assert abs(sum(w) - L / (lam - 2)) < 2e-11
            separation += 1
        for b in range(3, 7):
            A = adjacency(b, m)
            M = average_mixing(A)
            eigen = np.linalg.eigvalsh(M)
            expected = 1 + b * math.ceil(m / 2)
            observed = int(np.sum(eigen > 1e-8))
            assert observed == expected, (m, b, observed, expected)
            assert np.min(eigen) > -2e-12
            smallest_positive = min(smallest_positive, float(eigen[-expected]))
            for blade in range(b):
                for k in range(m // 2):
                    contrast = np.zeros(len(A))
                    contrast[1 + blade * m + k] = 1
                    contrast[1 + blade * m + m - 1 - k] = -1
                    worst_null = max(worst_null, float(np.linalg.norm(M @ contrast)))
            max_n = max(max_n, len(A))
            trials += 1
    assert worst_null < 1e-10
    assert smallest_positive > 1e-8
    assert (1 + 3 * math.ceil(3 / 2)) == 7
    print(f'VERIFY_OK graph_cases={trials} max_order={max_n} '
          f'path_span_tests={profile_tests} even_mode_resolvents={separation} '
          f'm3_b3_rank=7/10 max_kernel_residual={worst_null:.2e} '
          f'min_positive_mode={smallest_positive:.3e}')


if __name__ == '__main__':
    main()
