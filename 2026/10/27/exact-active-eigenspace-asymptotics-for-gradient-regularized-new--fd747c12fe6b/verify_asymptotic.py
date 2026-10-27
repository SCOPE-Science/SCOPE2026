#!/usr/bin/env python3
"""Finite numerical sanity check for the exact SPD-quadratic asymptotics."""
import math

H = 2.0
lambdas = (2.0, 5.0, 9.0)
# The component at eigenvalue 2 is absent; the lowest active eigenvalue is 5.
x = [0.0, 1.0, 0.5]
lambda_star = 5.0
last_x_ratio = last_g_ratio = None
for _ in range(11):
    s = math.sqrt(sum(t * t for t in x))
    g = math.sqrt(sum((lam * t) ** 2 for lam, t in zip(lambdas, x)))
    r = math.sqrt(H * g)
    x_next = [r * t / (lam + r) for lam, t in zip(lambdas, x)]
    s_next = math.sqrt(sum(t * t for t in x_next))
    g_next = math.sqrt(sum((lam * t) ** 2 for lam, t in zip(lambdas, x_next)))
    last_x_ratio = s_next / (s ** 1.5)
    last_g_ratio = g_next / (g ** 1.5)
    x = x_next
expected_x = math.sqrt(H / lambda_star)
expected_g = math.sqrt(H) / lambda_star
assert abs(last_x_ratio - expected_x) < 1e-5
assert abs(last_g_ratio - expected_g) < 1e-5
assert abs(x[2] / x[1]) < 0.002
print("x_ratio", format(last_x_ratio, ".12g"))
print("gradient_ratio", format(last_g_ratio, ".12g"))
print("high_mode_to_active_mode", format(abs(x[2] / x[1]), ".12g"))
print("VERIFY_OK")
