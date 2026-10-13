#!/usr/bin/env python3
"""Numerical corroboration of a reversible-confinement epidemic endpoint theorem."""
from fractions import Fraction
import math

q = float(Fraction(5, 3))
eta = float(Fraction(100, 33))
r = float(Fraction(27, 10))
k = eta * r
assert q > 0 and eta > 0 and r > 0

# Exact rational identity for the claimed first-order response coefficient.
u_rat = Fraction(1, 5)
response_exact = Fraction(27, 10) * u_rat / ((1 + Fraction(5, 3)) * (1 - Fraction(27, 10) * u_rat))
assert response_exact == Fraction(81, 184)


def field(x, y, z):
    return (-k * x * z - q * x + y, q * x - y, eta * (r * x - 1) * z)


def compute_endpoint(u, seed, step=0.02, total_time=35.0):
    x, y, z = u, q * u, seed
    assert x + y + z <= 1.0
    nsteps = round(total_time / step)
    for _ in range(nsteps):
        a1, b1, c1 = field(x, y, z)
        a2, b2, c2 = field(x + step*a1/2, y + step*b1/2, z + step*c1/2)
        a3, b3, c3 = field(x + step*a2/2, y + step*b2/2, z + step*c2/2)
        a4, b4, c4 = field(x + step*a3, y + step*b3, z + step*c3)
        nx = x + step*(a1 + 2*a2 + 2*a3 + a4)/6
        ny = y + step*(b1 + 2*b2 + 2*b3 + b4)/6
        nz = z + step*(c1 + 2*c2 + 2*c3 + c4)/6
        assert min(nx, ny, nz) >= -1e-12
        assert nx + ny + nz <= x + y + z + 1e-11
        x, y, z = nx, ny, nz
    assert z < 2e-12
    assert abs(y - q*x) < 1e-10
    return x

u = float(u_rat)
response = float(response_exact)
for seed, tolerance in ((1e-3, 0.012), (1e-5, 0.001)):
    observed = u - compute_endpoint(u, seed)
    predicted = response * seed
    comparison_bound = r * u * seed / ((1+q) * (1-r*u))
    assert 0 < observed <= comparison_bound + 1e-11
    assert abs(observed / predicted - 1) < tolerance

# Numerical construction of a trajectory ending at an interior target.
target = 0.30
seed = 1e-4
lo, hi = 0.295, 0.305
assert lo < target < hi < min(1/r, 1/(1+q))
assert compute_endpoint(lo, seed) < target < compute_endpoint(hi, seed)
for _ in range(30):
    mid = (lo + hi)/2
    if compute_endpoint(mid, seed) < target:
        lo = mid
    else:
        hi = mid
solution = (lo + hi)/2
assert abs(compute_endpoint(solution, seed) - target) < 1e-9
print('VERIFY_OK')
print('u', u)
print('first_order_coefficient', response)
print('constructed_seeded_initial_u', solution)
print('constructed_final_x', compute_endpoint(solution, seed))
