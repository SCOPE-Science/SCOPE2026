#!/usr/bin/env python3
"""Verification for the period-two spectral-radius parity obstruction.

Requires Python 3.13+ and NumPy 2.3+.
"""
import math
import numpy as np

a = 0.2
b = -0.8
s = 0.8

R = np.array([[0.0, -1.0], [1.0, 0.0]])
A = s * R
M = np.diag([math.exp(2*a), math.exp(2*b)])
B = M @ np.linalg.inv(A)

def F(x, y):
    f1 = 1 - 3*x*x + 2*x*x*x
    f2 = (
        s*x
        + (-2*s + math.exp(2*b)/s)*x*x
        + (s - math.exp(2*b)/s)*x*x*x
    )
    g1 = -s + (s + math.exp(2*a)/s)*x
    return np.array([f1 + g1*y, f2])

def DF(x, y):
    d11 = -6*x + 6*x*x + (s + math.exp(2*a)/s)*y
    d12 = -s + (s + math.exp(2*a)/s)*x
    d21 = (
        s
        + 2*(-2*s + math.exp(2*b)/s)*x
        + 3*(s - math.exp(2*b)/s)*x*x
    )
    d22 = 0.0
    return np.array([[d11, d12], [d21, d22]])

p0 = np.array([0.0, 0.0])
p1 = np.array([1.0, 0.0])

assert np.allclose(F(*p0), p1)
assert np.allclose(F(*p1), p0)
assert np.allclose(DF(*p0), A)
assert np.allclose(DF(*p1), B)
assert np.allclose(B @ A, M)

def spectral_radius(P):
    return float(np.max(np.abs(np.linalg.eigvals(P))))

def sigma_max(P):
    return float(np.linalg.svd(P, compute_uv=False)[0])

def block(start_phase, L):
    P = np.eye(2)
    phase = start_phase
    for _ in range(L):
        J = A if phase == 0 else B
        P = J @ P
        phase = 1 - phase
    return P

rho_A = spectral_radius(A)
rho_B = spectral_radius(B)
assert rho_A < 1.0 and rho_B < 1.0

rows = []
for L in range(1, 11):
    Ps = [block(0, L), block(1, L)]
    hL = sum(math.log(spectral_radius(P)) for P in Ps) / (2*L)
    gL = sum(math.log(sigma_max(P)) for P in Ps) / (2*L)
    expected_h = a if L % 2 == 0 else 0.5*(a+b)
    assert abs(hL - expected_h) < 1e-12
    assert abs(gL - a) < 1e-12
    rows.append((L, hL, gL))

print(f"a={a:.12f}, b={b:.12f}, s={s:.12f}")
print(f"rho(A)={rho_A:.12f}")
print(f"rho(B)={rho_B:.12f}")
print("BA =", np.array2string(B @ A, precision=12))
print(f"Lyapunov exponents per step: ({a:.12f}, {b:.12f})")
print(" L          h_L          g_L")
for L, hL, gL in rows:
    print(f"{L:2d}  {hL: .12f}  {gL: .12f}")
print("all_checks_passed=True")
