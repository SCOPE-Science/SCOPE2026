#!/usr/bin/env python3
import math
import numpy as np
from scipy.integrate import solve_ivp

# Source-sharpening stress test. This script is supplementary to the analytic proof.
a = np.array([1.0, 1.5])
b = np.array([1.0, 2.0])
c = np.array([0.8, 1.5])
p = np.array([10.0, 12.0])
z0 = np.array([2.0, 0.3, 5.0])

assert np.all(c <= b)
assert p[0]**2 > 4*a[0] and p[1]**2 > 4*a[1]
R0 = c.sum()/(1.0+b.sum())
assert R0 < 1.0

# Generic algebraic checks on a few nonnegative states.
for x in [np.array([0.0,0.0]), np.array([0.2,3.0]), np.array([2.0,0.1]), np.array([10.0,4.0])]:
    D = 1.0 + np.dot(b,x)
    g = np.dot(c,x)/D - 1.0
    assert g <= -1.0/D + 1e-14

M = np.maximum(1.0, z0[:2])
Dmax = 1.0 + np.dot(b,M)


def rhs(t,z):
    x = z[:2]
    y = z[2]
    D = 1.0 + np.dot(b,x)
    dx = a*x*(1.0-x) - p*x*y/D
    dy = y*(np.dot(c,x)/D - 1.0)
    return np.r_[dx,dy]

sol = solve_ivp(rhs, (0.0, 250.0), z0, rtol=1e-10, atol=1e-12, max_step=0.05)
assert sol.success
x_end = sol.y[:2,-1]
y_end = sol.y[2,-1]
assert np.max(np.abs(x_end-1.0)) < 2e-6, x_end
assert y_end < 1e-20, y_end

# Check the analytic exponential upper bound at all computed nodes.
y_bound = z0[2]*np.exp(-sol.t/Dmax)
assert np.all(sol.y[2] <= y_bound*(1+2e-9) + 1e-12)

print('R0=', R0)
print('Dmax=', Dmax)
print('end=', x_end.tolist(), y_end)
print('VERIFY_OK')
