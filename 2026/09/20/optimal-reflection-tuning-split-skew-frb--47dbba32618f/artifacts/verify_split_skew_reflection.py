#!/usr/bin/env python3
"""Numerical checks for the split-skew reflected-backward stability formulas."""
import math
import numpy as np

SQRT3 = math.sqrt(3.0)
THETA = (1.0 + SQRT3) / 4.0
C2 = (8.0 / 3.0) * (7.0 * SQRT3 - 12.0)
C = math.sqrt(C2)


def threshold_sq(theta, gamma):
    if theta <= 0.5:
        return 0.0
    if gamma >= 2.0 * theta + 1.0:
        return math.inf
    return (gamma + 2.0 * theta - 1.0) / ((gamma + theta) ** 2 * (2.0 * theta + 1.0 - gamma))


def roots(theta, gamma, tau):
    # (1+i gamma tau) r^2 - (1-i(1+theta)tau) r - i theta tau = 0
    coeff = [1.0 + 1j * gamma * tau,
             -(1.0 - 1j * (1.0 + theta) * tau),
             -1j * theta * tau]
    return np.roots(coeff)


def rho(theta, gamma, tau):
    return float(np.max(np.abs(roots(theta, gamma, tau))))


def check_classification(theta, gamma, tau):
    r = rho(theta, gamma, tau)
    th2 = threshold_sq(theta, gamma)
    predicted = (tau > 0.0 and (math.isinf(th2) or tau * tau < th2))
    observed = r < 1.0 - 1e-10
    # Skip a tiny numerical band around the exact boundary.
    if not math.isinf(th2) and abs(tau * tau - th2) < 1e-8:
        return True
    return predicted == observed


print("theta_star", format(THETA, ".16f"))
print("c_star_sq", format(C2, ".16f"))
print("c_star", format(C, ".16f"))
print("gamma_tie_1", format(0.0, ".16f"))
print("gamma_tie_2", format(0.5, ".16f"))
print("standard_FRB_ceiling", format(0.5, ".16f"))
print("relative_improvement_percent", format(100.0 * (C / 0.5 - 1.0), ".12f"))

# Boundary checks.
for g in [0.0, 0.5]:
    rr = roots(THETA, g, C)
    print("boundary", g, "roots", *[complex(z) for z in rr], "moduli", *[abs(z) for z in rr])

# A point where standard FRB is unstable but tuned reflection is stable across a broad gamma scan.
tau = 0.55
print("rho_standard_matched", format(rho(1.0, 1.0, tau), ".15f"))
for g in [0.0, 0.5, 1.0]:
    print("rho_tuned", g, format(rho(THETA, g, tau), ".15f"))

grid = np.linspace(0.0, 10.0, 20001)
rhos = np.array([rho(THETA, float(g), tau) for g in grid])
imax = int(np.argmax(rhos))
print("tuned_grid_max_rho", format(float(rhos[imax]), ".15f"), "at_gamma", format(float(grid[imax]), ".6f"))

# Exact phase-diagram spot checks, including both finite-threshold and unconditional regimes.
checks = 0
for theta in [0.55, THETA, 0.8, 1.0, 1.4]:
    for gamma in [0.0, 0.1, 0.5, 1.0, 2.0, 4.0]:
        th2 = threshold_sq(theta, gamma)
        candidates = [0.03, 0.2, 0.55, 1.0, 2.0]
        if math.isfinite(th2) and th2 > 0:
            tstar = math.sqrt(th2)
            candidates += [0.8 * tstar, 1.2 * tstar]
        for t in candidates:
            if not check_classification(theta, gamma, t):
                raise AssertionError((theta, gamma, t, rho(theta, gamma, t), th2))
            checks += 1
print("phase_spot_checks", checks, "all_passed")

# Confirm theta=1 recovers Shehu's split-skew threshold for gamma<3.
for gamma in [0.0, 0.25, 1.0, 2.5]:
    lhs = threshold_sq(1.0, gamma)
    rhs = 1.0 / ((1.0 + gamma) * (3.0 - gamma))
    if abs(lhs - rhs) > 1e-13:
        raise AssertionError((gamma, lhs, rhs))
print("theta1_reduction", "passed")

# Coarse minimization over gamma confirms the robust optimum locally and compares nearby theta.
def robust_ceiling(theta):
    if theta <= 0.5:
        return 0.0
    upper = 2.0 * theta + 1.0
    gs = np.linspace(0.0, upper * (1.0 - 1e-7), 100001)
    vals = np.sqrt(np.array([threshold_sq(theta, float(g)) for g in gs]))
    return float(np.min(vals))

for theta in [0.60, 0.65, THETA, 0.72, 0.80, 1.0]:
    print("robust_ceiling_scan", format(theta, ".15f"), format(robust_ceiling(theta), ".15f"))
