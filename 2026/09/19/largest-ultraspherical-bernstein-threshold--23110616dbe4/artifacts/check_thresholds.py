"""Numerically verify Hermite-edge thresholds for small degrees.

Uses NumPy's physicists-Hermite coefficient convention.
"""
from numpy.polynomial.hermite import hermroots
import numpy as np

for n in range(2, 11):
    c = np.zeros(n + 1)
    c[n] = 1.0
    roots = hermroots(c)
    h = max(float(x.real) for x in roots if abs(x.imag) < 1e-12 and x.real > 0)
    dstar = (2*h*h + 2*n - 1)/4
    print(f"{n:2d}  h={h:.12f}  d*={dstar:.12f}")
