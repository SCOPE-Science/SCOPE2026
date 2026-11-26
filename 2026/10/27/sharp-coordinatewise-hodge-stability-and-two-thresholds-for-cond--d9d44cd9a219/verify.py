"""Exact algebraic checks for the six-rim threshold certificates."""

from fractions import Fraction as F
from math import comb


p = [1, -1, -1, 0, 1, 0, -1, 1, 1]
factorized = [0] * 13
transformed = [0] * 9
for j, c in enumerate(p):
    factorized[j] += c
    factorized[j + 4] -= c
    for h in range(j + 1):
        for k in range(9 - j):
            transformed[h + k] += c * comb(j, h) * comb(8 - j, k) * 2**(8 - j - k)

assert factorized == [1, -1, -1, 0, 0, 1, 0, 1, 0, 0, 1, -1, -1]
assert transformed == [79, 219, 224, 89, 1, 1, 11, 6, 1]
assert 1 - F(1, 2) - F(1, 2)**2 - F(1, 2)**6 == F(15, 64)

g = [F(j, 1105) for j in (1188, 784, 576, 512, 576, 784)]
for j in range(6):
    assert F(9, 4)*g[j] - g[j-1] - g[(j+1) % 6] == (j == 0)
rim = 2*(1 - F(1, 4)*g[0]) + (g[0] - g[3])
spoke = 1 + (g[0] - g[3])
assert rim == F(2292, 1105) and rim > 2 > spoke
print("Checked the polynomial certificates and the six-rim rational witness.")
