"""Exact enumeration of eight-point Walsh spectral pairs in F_2^4.

Requires Python 3.10+ and no third-party packages.
Run: python checker.py
"""
from collections import Counter
from itertools import combinations

N = 16
FULL = (1 << N) - 1
SETS = [sum(1 << x for x in s) for s in combinations(range(N), 8)]


def points(mask):
    return [x for x in range(N) if mask >> x & 1]


def translate(mask, t):
    return sum(1 << (x ^ t) for x in points(mask))


def antiperiod_count(mask):
    return sum(translate(mask, t) == (FULL ^ mask) for t in range(1, N))


def fourier_zero_mask(mask):
    s = points(mask)
    out = 0
    for w in range(1, N):
        coeff = sum(-1 if (w & x).bit_count() & 1 else 1 for x in s)
        if coeff == 0:
            out |= 1 << (w - 1)
    return out


def difference_mask(mask):
    s = points(mask)
    out = 0
    for i, x in enumerate(s):
        for y in s[i + 1:]:
            out |= 1 << ((x ^ y) - 1)
    return out


z_masks = [fourier_zero_mask(a) for a in SETS]
d_masks = Counter(difference_mask(b) for b in SETS)
spectra = [sum(v for d, v in d_masks.items() if d & ~z == 0)
           for z in z_masks]
anti = [antiperiod_count(a) for a in SETS]

assert len(SETS) == 12870
assert Counter(anti) == {0: 10080, 1: 1920, 2: 840, 8: 30}
assert Counter(spectra) == {0: 10080, 2: 1920, 4: 840, 256: 30}
assert all(n == (256 if t == 8 else 2 * t)
           for n, t in zip(spectra, anti))
assert sum(spectra) == 14880

# Distinct exact checks: the pair counts follow also from double-counting
# one and two independent antiperiod directions.
assert 15 * (2 ** 8) == 30 * 8 + 1920 + 2 * 840
assert 15 * 14 * (2 ** 4) == 30 * 8 * 7 + 2 * 840

print('CHECK_PASS: 12870 eight-point sets, spectral multiplicities 0:10080, 2:1920, 4:840, 256:30')
print('CHECK_PASS: direct Walsh orthogonality, antiperiod formula, pair-incidence 14880')
