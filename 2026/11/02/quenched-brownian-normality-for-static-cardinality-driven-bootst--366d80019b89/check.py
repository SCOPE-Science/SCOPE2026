"""Finite exact checks for the static Pascal-sign scenery theorem.

Checks finite Lucas parity, submask covariance, an overlap inequality,
and expected squared empirical averages under independent biased bits.
These checks do not establish any infinite-dimensional limit.
"""
from fractions import Fraction
from itertools import product
from math import comb

N = 64
assertions = 0

def downset(s):
    return {k for k in range(s+1) if (k & s) == k}

for s in range(N):
    d = downset(s)
    assert len(d) == 1 << s.bit_count()
    assertions += 1
    for j in range(s + 1):
        assert (comb(s,j) % 2 == 1) == (j in d)
        assertions += 1
    for t in range(s):
        e = downset(t)
        assert len(d ^ e) >= (1 << min(s.bit_count(), t.bit_count()))
        assertions += 1

profiles = (
    [Fraction(1,2)] * 9,
    [Fraction(1,3)] * 9,
    [Fraction(2,5), Fraction(3,5)] * 4 + [Fraction(1,4)],
    [Fraction(1,4), Fraction(1,3), Fraction(3,4)] * 3,
)
for probabilities in profiles:
    m = len(probabilities)
    means_by_s = []
    cov_by_pair = []
    for s in range(m):
        d = downset(s)
        mean = Fraction(1)
        for k in d:
            mean *= (1-2*probabilities[k])
        means_by_s.append(mean)
        values = []
        for bits in product((0,1),repeat=m):
            vals = [(-1 if sum(bits[k] for k in downset(t))%2 else 1) for t in range(m)]
            mass = Fraction(1)
            for k,b in enumerate(bits):
                mass *= probabilities[k] if b else 1-probabilities[k]
            values.append((mass,vals))
        measured_mean = sum((mass*vals[s] for mass,vals in values),Fraction(0))
        assert measured_mean == mean
        assertions += 1
    for s in range(m):
        for t in range(s):
            measured = sum((mass*vals[s]*vals[t] for mass,vals in values),Fraction(0))
            expected = Fraction(1)
            for k in downset(s)^downset(t):
                expected *= (1-2*probabilities[k])
            assert measured == expected
            assertions += 1
    for count in range(1,m+1):
        exact_empirical_second = sum(
            (mass*Fraction(sum(vals[:count])**2,count**2) for mass,vals in values),
            Fraction(0))
        formula_empirical_second = sum(
            (Fraction(1) if s == t else
             __import__('functools').reduce(lambda a,k: a*(1-2*probabilities[k]),downset(s)^downset(t),Fraction(1)))
            for s in range(count) for t in range(count)
        )/count**2
        assert exact_empirical_second == formula_empirical_second
        assertions += 1
print('PASS exact assertions:',assertions)
print('PASS: Lucas parity, downset-distance inequality, biased product correlations, and empirical second moments')
print('LIMIT: finite checks only; almost-sure and functional limit theorems require the analytical argument')
