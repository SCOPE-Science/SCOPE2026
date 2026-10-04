#!/usr/bin/env python3
"""Numerical consistency check for the exact scalar Hellinger boundary law.

This does not simulate B-adaPG's stepsize selector and is not used as proof.
It replays the theorem's scalar dual recursion with an independent positive,
divergent stepsize sequence and checks the predicted cumulative-step constants.
"""
import math

c = 1.7
t = -0.25
y = t / math.sqrt(1.0 - t*t)
S = 0.0

for j in range(1, 200001):
    gamma = 0.15 + 0.05 / (j ** 0.2)
    y += gamma * (c - t)
    S += gamma
    t = y / math.sqrt(1.0 + y*y)

ratio_dual = y / ((c - 1.0) * S)
ratio_boundary = 2.0 * (c - 1.0)**2 * S*S * (1.0 - t)
f_gap = 0.5 * (c - t)**2 - 0.5 * (c - 1.0)**2
ratio_objective = 2.0 * (c - 1.0) * S*S * f_gap

print(f"S={S:.12f}")
print(f"t={t:.12f}")
print(f"dual_ratio={ratio_dual:.12f}")
print(f"boundary_ratio={ratio_boundary:.12f}")
print(f"objective_ratio={ratio_objective:.12f}")

assert abs(ratio_dual - 1.0) < 2e-4
assert abs(ratio_boundary - 1.0) < 5e-4
assert abs(ratio_objective - 1.0) < 5e-4
