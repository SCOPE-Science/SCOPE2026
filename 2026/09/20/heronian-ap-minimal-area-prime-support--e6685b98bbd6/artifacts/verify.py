#!/usr/bin/env python3
"""Exact bounded check for the minimal-area-prime-support HAP classification."""

from math import isqrt

MAX_X = 3000

def strip_2_3(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    return n

def is_23_smooth(n: int) -> bool:
    return strip_2_3(n) == 1

total_pairs = 0
heronian_pairs = 0
two_prime_support = []
mismatches = []

for x in range(1, MAX_X + 1):
    for d in range(1, x):
        total_pairs += 1
        radicand = 3 * (x * x - d * d)
        z = isqrt(radicand)
        if z * z != radicand:
            continue

        heronian_pairs += 1
        area = x * z

        if area % 2 or area % 3 or strip_2_3(area) != 1:
            continue

        two_prime_support.append((x, d, area))
        predicted = (x == 2 * d and z == 3 * d and is_23_smooth(d))
        if not predicted:
            mismatches.append((x, d, z, area))

predicted_count = sum(
    1 for g in range(1, MAX_X // 2 + 1) if is_23_smooth(g)
)

print(f"MAX_X={MAX_X}")
print(f"total_parameter_pairs={total_pairs}")
print(f"heronian_parameter_pairs={heronian_pairs}")
print(f"two_prime_support_hits={len(two_prime_support)}")
print(f"predicted_hits={predicted_count}")
print(f"mismatches={len(mismatches)}")
if mismatches:
    for row in mismatches:
        print("MISMATCH", *row)
