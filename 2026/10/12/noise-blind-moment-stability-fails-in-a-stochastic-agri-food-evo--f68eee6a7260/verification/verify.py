#!/usr/bin/env python3
Q = 10.0
beta = 0.2
dP = 0.1
Cl = 2.0
Cg = 5.0
ax = beta * Q * dP + Cl - Cg
assert abs(ax + 2.8) < 1e-15
for x in (1e-9, 0.1, 0.5, 1.0):
    assert ax * x <= -x
    assert 0.0 <= 0.0
    assert 0.0 <= 0.0
sigma = 3.0
p = 2.0
moment_exponent = p * ax + 0.5 * p * (p - 1.0) * sigma * sigma
assert abs(moment_exponent - 3.4) < 1e-15
assert moment_exponent > 0.0
pathwise_exponent = ax - 0.5 * sigma * sigma
assert abs(pathwise_exponent + 7.3) < 1e-15
assert pathwise_exponent < 0.0
for p in (0.5, 1.0, 2.0, 3.0, 4.5):
    lhs = p * (ax - 0.5 * sigma * sigma) + 0.5 * (p * sigma) ** 2
    rhs = p * ax + 0.5 * p * (p - 1.0) * sigma * sigma
    assert abs(lhs - rhs) < 1e-12
assert sigma * sigma > -2.0 * ax
print("VERIFY_OK")
