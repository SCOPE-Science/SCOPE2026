#!/usr/bin/env python3
"""Finite exact sanity checks for the Lucas root-count formula."""
from math import isqrt

def formula(t: int) -> int:
    # Exact floor(T/sqrt(2)) and floor(T/sqrt(3)) without floating point.
    f2 = isqrt((t * t) // 2)
    f3 = isqrt((t * t) // 3)
    return 4*t**3 - 2*t**2 - 2*t - 2*f2 - 2*f3

def is_root_of_unity_ratio(a: int, b: int) -> bool:
    if a == 0 or b == 0:
        return True
    # Ratio orders 1, 3, 4, 6, plus the order-2 case A=0.
    if a % 2 == 0 and b == (a // 2)**2:  # repeated root, order 1
        return True
    if b == a*a:                         # order 3
        return True
    if a % 2 == 0 and b == 2*(a // 2)**2:  # order 4
        return True
    if a % 3 == 0 and b == 3*(a // 3)**2:  # order 6
        return True
    return False

def direct_count(t: int) -> int:
    total = 0
    for b in range(-t*t, t*t + 1):
        max_a = (t*t + b) // t
        for a in range(-max_a, max_a + 1):
            if is_root_of_unity_ratio(a, b):
                continue
            total += 1
    return total

for T in range(2, 41):
    assert formula(T) == direct_count(T), (T, formula(T), direct_count(T))
print("VERIFY_OK: exact formula agrees with direct enumeration for integer radii 2..40")
