"""Standalone exact-arithmetic checks for the five-weight mean-crossing theorem.

Only Python's standard library is required. Finite checks illustrate, but do not
replace, the theorem's analytic proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def compositions(n, k):
    if k == 1:
        yield (n,)
    else:
        for a in range(n + 1):
            for tail in compositions(n - a, k - 1):
                yield (a,) + tail


def coefficient_counts(weights, p):
    """Counts qualifying subsets of each size, with exact rational comparisons."""
    counts = []
    for k in range(6):
        counts.append(sum(sum(weights[i] for i in subset) >= p
                          for subset in combinations(range(5), k)))
    return counts


def probability(counts, p):
    q = 1 - p
    return sum(counts[k] * p**k * q**(5 - k) for k in range(6))


def binomial_tail(n, k, p):
    return sum(comb(n, j) * p**j * (1-p)**(n-j) for j in range(k, n+1))


assert binomial_tail(4, 2, F(1,4)) == F(67,256)
assert binomial_tail(4, 2, F(1,4)) - F(1,4) == F(3,256)
assert binomial_tail(5, 2, F(1,5)) == F(821,3125)
assert F(821,3125) - F(1,4) > F(3,256)

# Exact polynomial identity, checked at more than its degree many points.
for denominator in (11, 17):
    for numerator in range(denominator + 1):
        p = F(numerator, denominator)
        lower = binomial_tail(5,3,p) + 6*p*p*(1-p)**3
        assert lower - p == p*(p-1)*(3*p*p-5*p+1)

checked = 0
no_heavy = 0
for denom in (12, 16, 20):
    for weight_numerators in compositions(denom, 5):
        weights = tuple(F(x, denom) for x in weight_numerators)
        for p in (F(1,5), F(9,40), F(1,4), F(13,50), F(3,10), F(1,3)):
            counts = coefficient_counts(weights, p)
            event = probability(counts, p)
            assert event >= p
            if max(weights) < p:
                assert event - p > F(3,256)
                assert counts[0] == 0 and counts[1] == 0
                assert counts[3:] == [10,5,1]
                assert counts[2] >= (10 if p <= F(1,4) else 6)
                no_heavy += 1
            checked += 1

# A strictly positive weight family approaches the optimal stability gap.
for N in (24, 100, 1000, 10000):
    p = F(1,4) + F(1,N)
    eps = F(1,N)
    weights = (eps,) + ((1-eps)/4,)*4
    assert max(weights) < p <= F(1,3)
    counts = coefficient_counts(weights, p)
    event = probability(counts, p)
    assert event == binomial_tail(4,2,p)
    assert event - p > F(3,256)

print(f'OK: {checked} exact five-weight cases, {no_heavy} light-stake cases;')
print('polynomial identities and sharp limiting construction checked.')
