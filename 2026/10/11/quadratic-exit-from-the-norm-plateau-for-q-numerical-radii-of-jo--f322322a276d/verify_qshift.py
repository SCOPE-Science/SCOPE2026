"""Independent finite-dimensional numerical checks for the analytic Jordan-shift formula.

Requires NumPy and SciPy. These checks are consistency tests, not a proof
of the theorem in arbitrary dimension.
"""
from math import cos, sin, pi
import numpy as np
from scipy.optimize import minimize_scalar


def singular_norm(n, t):
    J = np.diag(np.ones(n - 1), 1)
    return float(np.linalg.svd(J + t * np.eye(n), compute_uv=False)[0])


def envelope(n, q):
    if q <= cos(pi / n):
        return 1.0
    if q == 1.0:
        return cos(pi / (n + 1))
    objective = lambda t: singular_norm(n, t) - q * t
    r = minimize_scalar(objective, bounds=(0.0, 2.0), method="bounded",
                        options={"xatol": 2e-13})
    assert r.success and r.x > 0.0
    return float(r.fun)


def run():
    for n in range(4, 9):
        q0 = cos(pi / n)
        coefficient = n / (2 * (n + 2) * sin(pi / n) ** 2)
        assert abs(singular_norm(n, 0) - 1) < 1e-13
        assert envelope(n, q0 - 0.1) == 1.0
        assert envelope(n, q0) == 1.0
        assert envelope(n, 1.0) == cos(pi / (n + 1))
        for delta in (0.0005, 0.001):
            if q0 + delta >= 1.0:
                continue
            val = envelope(n, q0 + delta)
            inferred = (1.0 - val) / (delta * delta)
            assert val < 1.0
            assert abs(inferred / coefficient - 1) < 0.02, (n, delta, inferred, coefficient)
        # Confirm the second-order singular-norm expansion directly.
        for t in (0.0005, 0.001):
            slope = (n + 2) / n * sin(pi / n) ** 2
            residual = singular_norm(n, t) - (1 + q0 * t + slope * t * t / 2)
            assert abs(residual) < 0.02 * t * t, (n, t, residual)
    print("JORDAN_Q_RADIUS_EDGE_NUMERICAL_CHECK_OK")


if __name__ == "__main__":
    run()
