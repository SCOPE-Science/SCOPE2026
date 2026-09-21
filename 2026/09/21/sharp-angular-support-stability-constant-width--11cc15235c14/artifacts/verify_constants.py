#!/usr/bin/env python3
"""Numerical checks for the sharp constants in the constant-width stability record."""
from math import pi, tan

def general_partial_sum(N: int) -> float:
    return sum(1.0 / ((2*k + 1)**2 - 1.0) for k in range(1, N + 1))

def symmetry_partial_sum(q: int, N: int) -> float:
    return sum(1.0 / (q*q*(2*k + 1)**2 - 1.0) for k in range(N))

for N in (1, 2, 5, 10, 100, 10000):
    s = general_partial_sum(N)
    exact = N / (4.0*(N + 1.0))
    assert abs(s - exact) < 1e-13
    print(f"N={N:5d}  S_N={s:.15f}  D/delta^2={pi/(2*s):.15f}")

print(f"limit constant 2*pi={2*pi:.15f}")

for q in (3, 5, 7, 9):
    numerical = symmetry_partial_sum(q, 200000)
    closed = pi/(4.0*q)*tan(pi/(2.0*q))
    constant = pi/(2.0*closed)
    assert abs(numerical - closed) < 3e-7
    print(f"q={q:2d}  S_q={closed:.15f}  sharp_constant={constant:.15f}")


from math import cos, sin

def angular_partial_sum(d: float, N: int) -> float:
    return sum(2.0*(1.0-cos((2*k+1)*d))/(((2*k+1)**2)-1.0)
               for k in range(1, N+1))

def angular_kernel(d: float) -> float:
    return 0.5*(1.0-cos(d)) + (pi/2.0-d)*sin(d)

for d in (0.1, 0.4, 0.8, pi/2, 2.4, pi):
    approx = angular_partial_sum(d, 200000)
    exact = angular_kernel(d)
    assert abs(approx-exact) < 6e-6
    print(f"d={d:.12f}  M(d)={exact:.15f}  partial={approx:.15f}")
