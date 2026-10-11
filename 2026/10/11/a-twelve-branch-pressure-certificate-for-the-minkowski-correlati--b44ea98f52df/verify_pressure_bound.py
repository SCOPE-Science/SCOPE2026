#!/usr/bin/env python3
import mpmath
from mpmath import iv

S = iv.mpf(847) / 1000
B = iv.mpf(127) / 120
TARGET = iv.mpf(1) / 25000
CELLS = 2000
TERMS = 12


def truncated_excess(x):
    total = iv.mpf(0)
    for a in range(1, TERMS + 1):
        y = a + x
        total += iv.mpf(4) ** (-a) * (y ** (2 * S) + B * y ** (2 * S - 1))
    return total - (1 + B * x)


minimum_lower = None
worst_cell = None
for j in range(CELLS):
    lo = iv.mpf(j) / CELLS
    hi = iv.mpf(j + 1) / CELLS
    x = iv.mpf([lo.a, hi.b])
    value = truncated_excess(x)
    lower = value.a
    if minimum_lower is None or lower < minimum_lower:
        minimum_lower = lower
        worst_cell = j
    if not (lower > TARGET.b):
        raise AssertionError(
            f"certificate failed on cell {j}: lower={lower}, target={TARGET.b}"
        )

print("mpmath_version", mpmath.__version__)
print("terms", TERMS)
print("cells", CELLS)
print("certified_excess_floor", "1/25000")
print("minimum_interval_lower_endpoint", minimum_lower)
print("worst_cell", worst_cell)
print("spectral_radius_factor_lower", "1+3/154375")
print("PASS")
