"""Exact finite sanity checks for a geometric covering theorem.

The all-dimensional claim is proved analytically in RESULT.md.
This code checks rational identities and sampled unit vectors only.
"""
from fractions import Fraction
from math import comb, sqrt
import random


def rational_witness(d, chosen):
    m = d + 1
    p = len(chosen)
    q = m - p
    b = [Fraction(q, p) if i in chosen else Fraction(-1) for i in range(m)]
    assert sum(b) == 0
    assert min(abs(t) for t in b) == 1
    return b


def check_exact(d):
    m = d + 1
    all_partitions = [Fraction(m * max(p, m-p), min(p, m-p)) for p in range(1, m)]
    score = min(all_partitions)
    threshold_squared = Fraction(m, d) / score
    expected_squared = Fraction(1, d if d % 2 else d + 2)
    assert threshold_squared == expected_squared
    p = m // 2
    q = m - p
    chosen = set(range(p))
    b = rational_witness(d, chosen)
    assert sum(t * t for t in b) == score
    assert min(abs(t) for t in b) == 1
    # Confirm Gram normalization and the reconstruction map exactly.
    y2 = threshold_squared * sum(t*t for t in b)
    assert y2 == Fraction(m, d)
    for j in range(m):
        # (G*b)_j = (m/d) b_j, with G_ii=1, G_ij=-1/d.
        gram_bj = b[j] - Fraction(sum(b) - b[j], d)
        assert gram_bj == Fraction(m, d)*b[j]
    # Directions are indexed by balanced sign partitions up to reversal.
    unoriented = comb(m, p) // (2 if m % 2 == 0 else 1)
    if m % 2 == 0:
        assert 2 * unoriented == comb(m, p)
    else:
        assert unoriented == comb(m, p)


def check_sample(d, rng):
    m = d + 1
    cutoff = 1 / sqrt(d if d % 2 else d + 2)
    for _ in range(2000):
        z = [rng.gauss(0, 1) for _ in range(m)]
        mean = sum(z) / m
        centered = [t - mean for t in z]
        nrm = sqrt(sum(t*t for t in centered))
        y = [sqrt(m/d) * t / nrm for t in centered]
        assert abs(sum(y)) < 1e-12
        assert abs(sum(t*t for t in y) - m/d) < 1e-12
        assert min(abs(t) for t in y) <= cutoff + 1e-12


def main():
    for d in range(2, 51):
        check_exact(d)
    rng = random.Random(1379902)
    for d in range(2, 16):
        check_sample(d, rng)
    print('SIMPLEX_PLANK_PARITY_CHECKS_OK')


if __name__ == '__main__':
    main()
