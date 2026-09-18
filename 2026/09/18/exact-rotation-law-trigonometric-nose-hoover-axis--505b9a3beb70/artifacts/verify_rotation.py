"""Numerical check of the exact mechanical-period rotation law for a=0."""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.special import ellipk

B = 0.5
ENERGIES = (-1.8, -1.3, -0.8, -0.4, 0.4, 0.8, 1.0, 1.3, 1.8)


def wrap(angle):
    return (angle + np.pi) % (2 * np.pi) - np.pi


def initial_point(h):
    if h > 0:
        return 0.0, float(np.arccos(h - 1.0))
    return np.pi, float(np.arccos(h + 1.0))


def rhs(_t, q):
    x, y, z = q
    return (np.sin(y), -np.sin(x), B * (1.0 - 2.0 * np.cos(y)))


max_xy_return_error = 0.0
max_drift_error = 0.0
print("h,T,rho,xy_return_error,drift_error")
for h in ENERGIES:
    k2 = 1.0 - h * h / 4.0
    T = 4.0 * ellipk(k2)
    x0, y0 = initial_point(h)
    sol = solve_ivp(
        rhs,
        (0.0, T),
        (x0, y0, 0.0),
        method="DOP853",
        rtol=1e-11,
        atol=1e-13,
    )
    x1, y1, z1 = sol.y[:, -1]
    predicted_drift = B * T * (1.0 - h)
    rho = predicted_drift / (2.0 * np.pi)
    xy_error = max(abs(wrap(x1 - x0)), abs(wrap(y1 - y0)))
    drift_error = abs(z1 - predicted_drift)
    max_xy_return_error = max(max_xy_return_error, xy_error)
    max_drift_error = max(max_drift_error, drift_error)
    print(f"{h:+.1f},{T:.12f},{rho:.12f},{xy_error:.3e},{drift_error:.3e}")

print(f"max_xy_return_error={max_xy_return_error:.3e}")
print(f"max_drift_error={max_drift_error:.3e}")
assert max_xy_return_error < 2e-10
assert max_drift_error < 2e-10

# Numerical sanity check for strict monotonicity on the positive-energy branch.
grid = np.linspace(1e-3, 1.999, 2000)
C_values = (2.0 / np.pi) * (1.0 - grid) * ellipk(1.0 - grid * grid / 4.0)
max_forward_difference = float(np.max(np.diff(C_values)))
print(f"max_positive_branch_forward_difference={max_forward_difference:.3e}")
assert max_forward_difference < 0.0
