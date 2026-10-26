#!/usr/bin/env python3
"""Finite arithmetic cross-check for the exact sinusoidal star period-two formulas."""
import math
import numpy as np
from scipy.optimize import brentq

for n in (4, 5, 8):
    K = np.eye(n) + np.ones((n, n))
    for kappa in (2.1, 2.5, math.pi, 3.5, 5.0):
        if abs(kappa - math.pi) < 1e-12:
            delta = math.pi / 2
        else:
            delta = brentq(lambda x: 2*x/math.sin(x) - kappa,
                           1e-8, math.pi-1e-8)
        h = kappa/(n+1)
        low = np.full(n, math.pi-delta)
        high = np.full(n, math.pi+delta)
        next_low = (low + h*K.dot(np.sin(low)))%(2*math.pi)
        next_high = (high + h*K.dot(np.sin(high)))%(2*math.pi)
        assert np.max(np.abs(next_low-high)) < 1e-8
        assert np.max(np.abs(next_high-low)) < 1e-8
        Jlow = np.eye(n)+h*K@np.diag(np.cos(low))
        Jhigh = np.eye(n)+h*K@np.diag(np.cos(high))
        observed = np.sort(np.linalg.eigvals(Jhigh@Jlow).real)
        predicted = np.sort(np.array(
            [(1-kappa*math.cos(delta))**2]
            + [(1-h*math.cos(delta))**2]*(n-1)))
        assert np.max(np.abs(observed-predicted)) < 1e-8
        if kappa<math.pi: assert observed[-1]<1
        if kappa>math.pi: assert observed[0]>1
        if abs(kappa-math.pi)<1e-12:
            assert np.max(np.abs(observed-1))<1e-8
print('CHECKS_PASS')
