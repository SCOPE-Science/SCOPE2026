#!/usr/bin/env python3
"""Independent arithmetic checks for a geometric finite-field obstruction.

The geometric bound h <= 21 is a cited theorem, NOT certified by this script.
"""
from math import comb

q = 37
assert comb(28, 2) == 378
assert q*q + 8*q + 1 == 1666
# Hasse-Weil for genus 3: 38-6*sqrt(37)>1, because 37>6*sqrt(37).
assert 37*37 > 36*37
# Integer point counts must consequently satisfy N >= 2.
minimum_N = 2
maximum = -1
attainers = []
for h in range(22):
    for e in range(127):
        f = 378 - 6*h - 3*e
        if f < 0: continue
        assert 6*h + 3*e + f == 378
        v = 6*h + 2*e
        if v > maximum:
            maximum = v
            attainers = [(h, e, f)]
        elif v == maximum:
            attainers.append((h, e, f))
assert maximum == 294
assert (21, 84, 0) in attainers
# Fullness would force 6h+2e=(q-24)^2+N+125 >=296.
assert (q-24)**2 + minimum_N + 125 == 296
assert maximum < (q-24)**2 + minimum_N + 125
print('VERIFY_OK: 28 bitangents, max incidence 294, branch points >=2, fullness impossible at q=37')
