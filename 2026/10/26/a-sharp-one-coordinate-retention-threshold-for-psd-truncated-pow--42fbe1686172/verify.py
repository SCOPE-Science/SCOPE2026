"""Reproducibility checks for the sharp one-coordinate retention boundary.

Only finite tests are carried out here; the all-dimension assertion is proved
in RESULT.md. Uses Python >=3.9 and NumPy.
"""
from fractions import Fraction
import numpy as np


def top_m(z, m):
    # Deterministic tie-breaking by ascending coordinate index.
    keep = np.argsort(-np.abs(z), kind='stable')[:m]
    out = np.zeros_like(z)
    out[keep] = z[keep]
    return out


def exact_witnesses():
    for m in [2, 3, 4, 5, 8, 13]:
        for q in [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)]:
            border = q * (m - 1) / m
            for factor in [Fraction(9, 10), Fraction(11, 10)]:
                a = border * factor
                # A = diag(1, (q/m) J_m), x0 = (a, 1, ..., 1, 0).
                Ax0 = [a] + [border] * m
                order = sorted(range(m + 1), key=lambda i: abs(Ax0[i]), reverse=True)
                leading_retained = (0 in order[:m])
                assert leading_retained == (factor > 1)
                initial_overlap2 = a*a / (a*a + m - 1)
                theta = q*q*(m-1) / (m*m + q*q*(m-1))
                assert (initial_overlap2 > theta) == (factor > 1)
                if factor < 1:
                    # The first iterate lies on the rank-one tail eigenvector,
                    # so every subsequent Rayleigh quotient is q instead of 1.
                    assert all(y == border for y in Ax0[1:])
    return 6 * 3 * 2


def random_retention_tests():
    rng = np.random.default_rng(260914620)
    count = 0
    for m in range(2, 9):
        for _ in range(65):
            n = int(rng.integers(m + 1, m + 7))
            q = float(rng.uniform(.08, .99))
            D = rng.standard_normal((n-1, n-1))
            B = D.T @ D
            B *= q / np.linalg.eigvalsh(B)[-1]
            A = np.zeros((n, n))
            A[0, 0] = 1
            A[1:, 1:] = B
            z = np.zeros(n-1)
            support = rng.choice(n-1, size=m-1, replace=False)
            z[support] = rng.standard_normal(m-1)
            z /= np.linalg.norm(z)
            theta = q*q*(m-1) / (m*m + q*q*(m-1))
            alpha2 = theta + rng.uniform(.002, .2) * (1-theta)
            x = np.concatenate(([np.sqrt(alpha2)], np.sqrt(1-alpha2)*z))
            initial_ratio = (1-alpha2)/alpha2
            for k in range(18):
                assert abs(x[0]) > 1e-12
                assert 1-float(x@A@x) <= q**(2*k)*initial_ratio / (1+q**(2*k)*initial_ratio) + 3e-12
                y = top_m(A@x, m)
                assert y[0] != 0
                x = y / np.linalg.norm(y)
            count += 1
    return count


if __name__ == '__main__':
    print('exact_fraction_witness_cases:', exact_witnesses())
    print('random_psd_matrix_trials:', random_retention_tests())
    print('status: PASS')
