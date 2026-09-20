#!/usr/bin/env python3
"""Verify the quarter-turn cocycle identities in the accompanying result."""
import math
import numpy as np

sigma = 2.0
omega = math.pi / 2.0
D = np.diag([sigma, sigma**-1])


def R(theta):
    return np.array([[math.cos(theta), -math.sin(theta)],
                     [math.sin(theta),  math.cos(theta)]], dtype=float)


def A(theta):
    return R(theta + omega) @ D @ R(-theta)


def direct_product(theta, L):
    P = np.eye(2)
    for j in range(L):
        P = A(theta + j * omega) @ P
    return P


def closed_product(theta, L):
    return R(theta + L * omega) @ np.linalg.matrix_power(D, L) @ R(-theta)


def rho(M):
    return float(np.max(np.abs(np.linalg.eigvals(M))))


def svmax(M):
    return float(np.linalg.svd(M, compute_uv=False)[0])


theta = 0.371
max_product_residual = 0.0
max_singular_rate_residual = 0.0
rows = []
for L in range(1, 9):
    P = direct_product(theta, L)
    C = closed_product(theta, L)
    max_product_residual = max(max_product_residual, float(np.max(np.abs(P - C))))

    full_rho = max(1.0, rho(P))
    h = math.log(full_rho) / L
    expected_h = math.log(sigma) if L % 2 == 0 else 0.0
    assert abs(h - expected_h) < 2e-11

    singular_rate = math.log(max(1.0, svmax(P))) / L
    max_singular_rate_residual = max(max_singular_rate_residual,
                                     abs(singular_rate - math.log(sigma)))
    assert abs(singular_rate - math.log(sigma)) < 2e-11
    rows.append((L, h, singular_rate))

# Smooth conjugacy H(theta,v)=(theta,R(-theta)v) sends the fiber map to D.
for j in range(8):
    th = theta + j * omega
    conjugated = R(-(th + omega)) @ A(th) @ R(th)
    assert np.max(np.abs(conjugated - D)) < 2e-12

# Every one-step fiber Jacobian is non-normal for sigma != 1.
B = A(theta)
normality_defect = float(np.max(np.abs(B @ B.T - B.T @ B)))
assert normality_defect > 1.0

print("sigma =", sigma)
print("top Lyapunov exponent =", math.log(sigma))
for L, h, srate in rows:
    print(f"L={L:2d}  h_L={h:.15f}  singular_rate={srate:.15f}")
print("max_product_residual =", f"{max_product_residual:.3e}")
print("max_singular_rate_residual =", f"{max_singular_rate_residual:.3e}")
print("normality_defect =", f"{normality_defect:.15f}")
print("all_checks_passed = True")
