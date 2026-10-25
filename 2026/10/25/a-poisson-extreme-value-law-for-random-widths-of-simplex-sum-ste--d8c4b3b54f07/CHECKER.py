"""Finite exact diagnostics for a star graph-associahedron random-width theorem.

Uses only Python's standard library. Running this does not certify the infinite
extreme-value limit; see RESULT.md for the mathematical proof.
"""
from fractions import Fraction
from itertools import combinations
from math import log, pi, isclose
from random import Random


def rank_formula(vec):
    h = vec[0]
    leaves = vec[1:]
    top = sorted(leaves, reverse=True)
    bot = sorted(leaves)
    high = sum(z > h for z in leaves)
    low = sum(z < h for z in leaves)
    def summation(seq, count):
        return sum((seq[j] / (2 ** (j + 1)) for j in range(count)), Fraction(0)) + h / (2 ** count)
    return summation(top, high) - summation(bot, low)


def subset_width(vec):
    m = len(vec) - 1
    leaves = range(1, m + 1)
    total = Fraction(0)
    for j in range(m + 1):
        for inds in combinations(leaves, j):
            values = [vec[0]] + [vec[i] for i in inds]
            total += max(values) - min(values)
    return total / 2**m

checks = 0
for m in range(1, 9):
    for shift in range(-4, 5):
        vec = [Fraction(shift, 7)] + [Fraction(((13 * j + 5) % 29) - 14, 11) for j in range(1, m + 1)]
        assert subset_width(vec) == rank_formula(vec), (m, shift)
        checks += 1

# Cumulants of the independent-exp limit: convergence to infinite polylog series.
def cumulant_half(r, length):
    return sum((1 - 2.0**(-k))**r / (k**r) for k in range(1, length + 1))

var = cumulant_half(2, 100000)
# Compute Li_2(1/4) from its rapidly convergent series.
li2q = sum((0.25**k)/(k*k) for k in range(1, 80))
closed_var = log(2)**2 + li2q
assert abs(var - closed_var) < 1.1e-5
assert cumulant_half(3, 3000) > 0.15

# Optional Monte Carlo corroboration for the exponential-series representation.
rng = Random(19092021)
samples = []
for _ in range(12000):
    x = 0.0
    for k in range(1, 81):
        x += (1 - 2.0**(-k)) / k * (rng.expovariate(1) - 1)
    samples.append(x)
empirical_var = sum((x - sum(samples) / len(samples))**2 for x in samples) / len(samples)
assert abs(empirical_var - closed_var) < 0.075
print('VERIFY_OK exact_subset_rank_identities=', checks,
      'limit_var=', round(closed_var, 9),
      'sample_var=', round(empirical_var, 5),
      'third_cumulant_positive=', True)
