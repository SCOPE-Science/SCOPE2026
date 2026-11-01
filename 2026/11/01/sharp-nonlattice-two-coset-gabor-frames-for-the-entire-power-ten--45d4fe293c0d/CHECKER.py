"""Finite consistency checks for the analytic two-coset Zak formula.

Run: python3 CHECKER.py. These checks do not prove any continuum claim.
"""
import cmath
import math

for p in (1.0, 1.5, 2.0, 4.0):
    for delta in (0.13, 0.31, 0.5, 0.77):
        predicted_a = 4.0 ** (1.0-p) * (1.0-abs(math.cos(math.pi*delta)))
        grid_min = float('inf')
        grid_max = 0.0
        for i in range(101):
            x = i/100
            a = (1-x)**p
            b = x**p
            for j in range(263):
                theta = 2*math.pi*j/263
                val = abs(a+b*cmath.exp(1j*theta))**2 + abs(a+b*cmath.exp(1j*(theta-2*math.pi*delta)))**2
                grid_min=min(grid_min,val)
                grid_max=max(grid_max,val)
                assert val >= predicted_a-1e-12
                assert val <= 2+1e-12
        assert grid_min-predicted_a < 3e-4, (p, delta, grid_min, predicted_a)
        assert abs(grid_max-2) < 1e-12
print('16 power-tent / offset grid checks passed; analytic proof remains essential')
