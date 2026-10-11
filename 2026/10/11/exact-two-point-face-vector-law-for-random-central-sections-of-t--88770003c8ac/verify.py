"""Standalone checks for the exact Haar central 4-cube section face-vector law.

The mathematical proof uses a complete sign-level argument and a Cauchy ratio.
These finite computations check its combinatorial cases, not the probability theorem.
"""
from itertools import product
from random import Random
from math import isclose


def generic(a):
    return all(sum(s * t for s, t in zip(signs, a)) != 0
               for signs in product((-1, 1), repeat=4))


def crossings(a):
    out = 0
    for axis in range(4):
        other = [a[j] for j in range(4) if j != axis]
        for signs in product((-1, 1), repeat=3):
            v = sum(s*x for s, x in zip(signs, other))
            out += abs(v) < abs(a[axis])
    return out


def main():
    count = 0
    counts = {8: 0, 12: 0}
    for a in product(range(1, 9), repeat=4):
        if not generic(a):
            continue
        expected = 8 if 2 * max(a) > sum(a) else 12
        actual = crossings(a)
        assert actual == expected, (a, actual, expected)
        counts[actual] += 1
        count += 1
    assert count > 1000, count
    assert all(counts.values()), counts
    # Haar sampling: iid Gaussians have uniformly distributed directions.
    rng = Random(314159)
    trials = 50000
    eight = 0
    for _ in range(trials):
        a = [abs(rng.gauss(0, 1)) for j in range(4)]
        eight += 2*max(a) > sum(a)
    observed = eight / trials
    assert abs(observed - 1/3) < 0.015, observed
    print('VERIFY_OK', 'exact_generic_integer_normals', count,
          'face_counts', counts,
          'gaussian_eight_frequency', round(observed, 5))


if __name__ == '__main__':
    main()
