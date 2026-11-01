"""Exact rational check for the numerical inequalities in the proof.

The generating-function and Cauchy--Schwarz arguments are analytical, not
proved by this finite arithmetic check.
"""
from fractions import Fraction as F

v = F(9, 7)
# Terms through degree two, with the remaining series bounded geometrically.
majorant = 1 + v + v**2/F(2) + (v**3/F(6))/(1-v/F(4))
assert majorant == F(6767, 1862)
assert majorant < F(15, 4)

lower = (F(9, 32) + F(81, 2048))**2
upper = F(1, 32)*(F(8, 7)*F(15, 4) - 1)
assert lower == F(431649, 4194304)
assert upper == F(23, 224)
assert lower - upper == F(6887, 29360128) > 0
print('CHECK_OK: uniform-shape rational exponential bounds and strict gap')
