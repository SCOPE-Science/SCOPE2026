#!/usr/bin/env python3
import math

TARGET = 2.0 * math.sqrt(3.0) / math.pi
EVEN_TARGET = 32.0 * math.sqrt(3.0) / (math.pi ** 2)
ODD_TARGET = 16.0 * math.sqrt(3.0) / (math.pi ** 2)

m, n = 2, 1
last_even = None
last_odd = None
for r in range(1, 16):
    if r > 1:
        m, n = 2*m + 3*n, m + 2*n
    assert m*m - 3*n*n == 1
    assert (n % 2) == (r % 2)
    d = 1.0 / (math.sqrt(3.0)*n + m)
    reciprocal_sine = 1.0 / (n * math.sin(math.pi*d))
    if n % 2 == 0:
        last_even = reciprocal_sine
    else:
        last_odd = reciprocal_sine

assert last_even is not None and last_odd is not None
assert abs(last_even - TARGET) < 1e-10
assert abs(last_odd - TARGET) < 1e-10
even_width = (16.0 / math.pi) * last_even
odd_width = (8.0 / math.pi) * last_odd
assert abs(even_width - EVEN_TARGET) < 1e-9
assert abs(odd_width - ODD_TARGET) < 1e-9
print(f"VERIFY_OK reciprocal={TARGET:.15f} even_limsup={EVEN_TARGET:.15f} odd_limsup={ODD_TARGET:.15f}")
