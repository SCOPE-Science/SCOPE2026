#!/usr/bin/env python3
"""Reproducible finite checks for a planar saturation-oscillator theorem.

Requires Python 3, NumPy and SciPy. The analytic theorem, not this finite
experiment, proves existence and asymptotics for all sufficiently small a.
"""
from math import sqrt, pi, exp, isclose
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

C = (3 * pi / (8 * sqrt(2))) ** (2 / 3)

def evolution(initial_radius, a, b):
    def field(phi, state):
        r = float(state[0])
        x, y = r * np.cos(phi), -r * np.sin(phi)
        sx, sy = np.clip(x, -1, 1), np.clip(y, -1, 1)
        vx = (1 + a) * sx + b * sy - x
        vy = -b * sx + (1 + a) * sy - y
        radial = (x * vx + y * vy) / r
        clock = -(x * vy - y * vx) / (r * r)
        assert clock > b / 4, ('angular reversal', a, b, r, phi)
        divergence = ((1 + a) if abs(x) < 1 else 0) + ((1 + a) if abs(y) < 1 else 0) - 2
        return (radial / clock, 1 / clock, divergence / clock)
    sol = solve_ivp(field, (0, 2*pi), (initial_radius, 0, 0),
                    rtol=2e-10, atol=2e-11, max_step=0.009)
    if not sol.success:
        raise RuntimeError(sol.message)
    return tuple(float(v) for v in sol.y[:,-1])

def check_case(a, b):
    def displacement(r):
        return evolution(r, a, b)[0] - r
    radius = brentq(displacement, 1 + 0.10 * C * a**(2/3),
                   1 + 3.00 * C * a**(2/3), xtol=2e-11)
    r_final, period, log_multiplier = evolution(radius, a, b)
    assert abs(r_final-radius) < 1e-6
    amplitude_ratio = (radius-1)/(C*a**(2/3))
    period_ratio = (period-2*pi/b)/((2*pi/b)*a)
    contraction_ratio = (-log_multiplier)/((8*sqrt(2*C)/b)*a**(1/3))
    assert 0.84 < amplitude_ratio < 1.20, (a,b,amplitude_ratio)
    assert 0.80 < period_ratio < 1.30, (a,b,period_ratio)
    assert 0.80 < contraction_ratio < 1.22, (a,b,contraction_ratio)
    assert 0 < exp(log_multiplier) < 1
    return (a,b,amplitude_ratio,period_ratio,contraction_ratio)

def main():
    # Four clipping caps have this exact parabolic-area coefficient.
    assert isclose(4 * (4*sqrt(2)/3), 16*sqrt(2)/3, rel_tol=0, abs_tol=1e-15)
    assert isclose((16*sqrt(2)/3)*C**(3/2), 2*pi, rel_tol=1e-14)
    for b in (1.5, 2.0):
        for a in (0.004, 0.0006):
            print('finite check a,b,amplitude,period,logmult:', check_case(a, b))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
