#!/usr/bin/env python3
"""Numerical consistency probe for critical Gaussian Gabor dual norms.

Requires NumPy. Numerical integration is not a proof of the asymptotic.
"""
import math
import numpy as np

qk = np.arange(15, dtype=float)
series = 2.0 * np.sum((-1.0) ** qk * (2 * qk + 1) * np.exp(-np.pi * (qk + 0.5) ** 2))
constant = 4.0 / (np.pi * series * series)
print("theta1 derivative:", series)
print("predicted leading constant:", constant)
resolution = 1100
z = (np.arange(resolution) + 0.5) / resolution
x, xi = z[:, None], z[None, :]
zak = np.zeros((resolution, resolution), dtype=complex)
for k in range(-4, 5):
    zak += np.exp(-np.pi * (x-k)**2) * np.exp(2j*np.pi*k*xi)
for m, n in [(1, 0), (4, 0), (10, 0), (20, 0), (40, 0), (80, 0), (50, 50)]:
    numerator = np.abs(np.exp(2j*np.pi*(n*x-m*xi)) - (-1)**(m+n))**2
    norm_squared = float(np.mean(numerator / np.abs(zak)**2))
    radius = math.hypot(m, n)
    print(m, n, "norm_squared=", norm_squared,
          "minus_C_log_R=", norm_squared-constant*math.log(radius))
