"""Independent exact finite cyclic-permutation checks of root-gap moment cutoffs.

Run with Python 3; only standard-library dependencies. Exhaustive tests are
corroboration of the analytic identities, not an infinite proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def expected_density(i):
    return Fraction(i * 2 ** (i + 1),
                    (i + 1) * (i + 2) * (i + 4) * factorial(i))


def gap_count(p, gap):
    k = len(p)
    valleys = [j for j in range(k)
               if p[j] < p[(j - 1) % k] and p[j] < p[(j + 1) % k]]
    if len(valleys) < 2:
        return 0
    return sum((valleys[(j + 1) % len(valleys)] - valleys[j]) % k == gap
               for j in range(len(valleys)))


def exact_moments(i, k):
    # Cyclic location symmetry permits fixing the smallest priority at site 0.
    # All other (k-1)! rankings then occur with equal probability.
    count = total = squared = 0
    frequencies = {}
    for tail in permutations(range(1, k)):
        d = gap_count((0,) + tail, i + 1)
        count += 1
        total += d
        squared += d * d
        frequencies[d] = frequencies.get(d, 0) + 1
    assert count == factorial(k - 1)
    mean = Fraction(total, count)
    variance = Fraction(squared, count) - mean * mean
    return mean, variance, frequencies


def run():
    checks = 0
    for i in range(1, 7):
        k = i + 3
        mean, _, freq = exact_moments(i, k)
        assert mean == (i + 4) * expected_density(i)
        assert set(freq) <= ({0, 2} if i == 1 else {0, 1})
        checks += 2
    known = [(1, 8, Fraction(1772, 14175), Fraction(29, 28350)),
             (2, 10, Fraction(32, 405), Fraction(1, 2025))]
    for i, k, b, delta in known:
        mean, var, _ = exact_moments(i, k)
        assert mean == k * expected_density(i)
        assert var == k * (b + delta)
        checks += 2
    print('PASS:', checks,
          'independent exact assertions; all cyclic rankings at cutoff i=1..6 '
          'and variance boundary i=1,2')


if __name__ == '__main__':
    run()
