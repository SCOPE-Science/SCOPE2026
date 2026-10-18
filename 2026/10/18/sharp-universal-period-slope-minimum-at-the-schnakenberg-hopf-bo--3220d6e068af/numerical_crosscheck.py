#!/usr/bin/env python3
"""Optional finite-amplitude period shooting; for corroboration, not proof.

Requires NumPy and SciPy. Run: python3 numerical_crosscheck.py
"""
from math import pi, sqrt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root

for s in (0.5, 1 / sqrt(3), 0.85):
    for mu in (0.003, 0.001):
        A = (1 - 3*s*s + mu) / (2*s*s)
        B, C, D, lam = 2/s, -1/s, 1/(s*s), mu/s

        def field(t, Y):
            q, p = Y
            return (p + lam*q + A*q*q + B*q*p + C*q**3 + D*q*q*p, -q)

        def closure(X):
            q0, tau_period = X
            sol = solve_ivp(field, (0, tau_period), (q0, 0),
                            rtol=2e-12, atol=2e-14, method='DOP853')
            return sol.y[0,-1]-q0, sol.y[1,-1]

        numerical = root(closure, (2*s*sqrt(mu), 2*pi), tol=1e-10)
        assert numerical.success and numerical.x[0] > 0
        actual_slope = (numerical.x[1]/(2*pi)-1)/mu
        predicted = (9*s**4-5*s*s+1)/(6*s*s)
        print('s=%.9f mu=%.4f physical_period=%.10f observed_slope=%.9f '
              'leading_coefficient=%.9f' %
              (s, mu, numerical.x[1]/s, actual_slope, predicted))
