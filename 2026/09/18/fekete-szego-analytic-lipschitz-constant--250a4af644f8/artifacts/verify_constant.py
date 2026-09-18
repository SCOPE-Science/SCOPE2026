#!/usr/bin/env python3
import math

sigma = 9.0 / 14.0
E = 3.0 * (1.0 + 2.0 * math.exp(-4.0)) * sigma * sigma
lam = 4.0 * sigma * math.sqrt(math.sinh(1.0 / (sigma * sigma)))
c0 = math.cos(E) * math.exp(-lam)

print(f"sigma = {sigma:.15f}")
print(f"E = {E:.15f}")
print(f"lambda = {lam:.15f}")
print(f"c0 = {c0:.15e}")

assert E < math.pi / 2.0
assert c0 > 6.49e-4
