#!/usr/bin/env python3
"""Check the common-delay threshold for the delayed signed consensus ring."""

import cmath
import math


def tau_critical(kp, kn, n_agents, k):
    theta = 2.0 * math.pi * k / n_agents
    rho = (math.sqrt(kp) - math.sqrt(kn)) / (
        math.sqrt(kp) + math.sqrt(kn)
    )
    omega = 2.0 * math.sqrt(kp * kn) * math.sin(theta)
    tau = math.atan(rho * math.tan(theta / 2.0)) / (
        math.sqrt(kp * kn) * math.sin(theta)
    )
    return theta, omega, tau


def characteristic(lam, kp, kn, theta, tau):
    a = kp - kn
    c = kp * cmath.exp(1j * theta) - kn * cmath.exp(-1j * theta)
    return lam + a - c * cmath.exp(-lam * tau)


kp = 2.0
kn = 1.0
n_agents = 20

vals = []
for k in range(1, n_agents // 2):
    theta, omega, tau = tau_critical(kp, kn, n_agents, k)
    residual = abs(characteristic(1j * omega, kp, kn, theta, tau))
    vals.append((k, theta, omega, tau, residual))

assert vals[0][3] == min(v[3] for v in vals)
assert max(v[4] for v in vals) < 1e-12

k, theta, omega, tau, residual = vals[0]
print(f"first mode k={k}")
print(f"theta={theta:.12f}")
print(f"omega={omega:.12f}")
print(f"tau_critical={tau:.12f}")
print(f"characteristic_residual={residual:.3e}")

rho = (math.sqrt(kp) - math.sqrt(kn)) / (
    math.sqrt(kp) + math.sqrt(kn)
)
limit = rho / (2.0 * math.sqrt(kp * kn))
print(f"large_N_limit={limit:.12f}")
