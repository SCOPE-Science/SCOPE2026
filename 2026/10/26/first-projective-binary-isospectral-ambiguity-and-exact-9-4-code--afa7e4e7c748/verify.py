#!/usr/bin/env python3
"""Exact finite classification and distortion witness for projective binary codes."""
import collections
import itertools
from fractions import Fraction


def rank(vectors):
    pivots = {}
    for value in vectors:
        x = value
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                break
    return len(pivots)


def spectrum(columns, k):
    return tuple(sorted(sum((x & col).bit_count() & 1 for col in columns)
                        for x in range(1, 1 << k)))


def linear_generators(k):
    vectors = range(1, 1 << k)
    return [tuple(1 << ((v ^ ((1 << i) if v & (1 << j) else 0)) - 1)
                   for v in vectors)
            for i in range(k) for j in range(k) if i != j]


def act(mask, generator):
    output = 0
    while mask:
        low = mask & -mask
        output |= generator[low.bit_length() - 1]
        mask -= low
    return output


# The transvections generate GL(k,2), so this is an exact orbit census.
for k in range(1, 5):
    count = (1 << k) - 1
    generators = linear_generators(k)
    seen = set()
    signatures = {}
    per_length = collections.Counter()
    for mask in range(1 << count):
        if mask in seen:
            continue
        seen.add(mask)
        orbit = [mask]
        for member in orbit:
            for generator in generators:
                other = act(member, generator)
                if other not in seen:
                    seen.add(other)
                    orbit.append(other)
        columns = [v for v in range(1, 1 << k) if mask & (1 << (v - 1))]
        if rank(columns) != k:
            continue
        key = (len(columns), spectrum(columns, k))
        assert key not in signatures, (k, key, mask, signatures.get(key))
        signatures[key] = min(orbit)
        per_length[len(columns)] += 1
    expected = {1: 1, 2: 2, 3: 6, 4: 36}[k]
    assert len(signatures) == expected, (k, len(signatures))
    print('projective full-dimensional orbits', k, len(signatures), sorted(per_length.items()))


# Every rank-5 set of <=7 columns has a basis among its columns.
# Mapping such a basis to the five unit columns produces one of these
# fixed-basis extensions. The normalization over every ordered basis of
# a set is an exact GL(5,2) orbit key, even when the set has symmetries.
unit = (1, 2, 4, 8, 16)
extras = tuple(v for v in range(1, 32) if v not in unit)


def canonical(columns):
    answer = (1 << 31) - 1
    for ordered_basis in itertools.permutations(columns, 5):
        coordinates = {0: 0}
        for i, b in enumerate(ordered_basis):
            for old, position in list(coordinates.items()):
                coordinates[old ^ b] = position | (1 << i)
        if len(coordinates) != 32:
            continue
        mask = 0
        for v in columns:
            mask |= 1 << (coordinates[v] - 1)
        answer = min(answer, mask)
    return answer


for m in (0, 1, 2):
    spectral_classes = collections.defaultdict(set)
    for addition in itertools.combinations(extras, m):
        columns = unit + addition
        spectral_classes[spectrum(columns, 5)].add(canonical(columns))
    assert all(len(v) == 1 for v in spectral_classes.values())
    assert len(spectral_classes) == (1, 4, 8)[m]
    print('dimension-five normalized census', 5 + m,
          'configurations', (1, 26, 325)[m],
          'equivalence classes', len(spectral_classes))

A = unit + (3, 5, 30)
B = unit + (3, 12, 21)
assert all(v != 0 for v in A + B)
assert len(set(A)) == len(set(B)) == 8
assert rank(A) == rank(B) == 5
assert spectrum(A, 5) == spectrum(B, 5)
expected_spectrum = (2,) * 3 + (3,) * 8 + (4,) * 7 + (5,) * 8 + (6,) * 5
assert spectrum(A, 5) == expected_spectrum


def weight(columns, u):
    return sum((u & v).bit_count() & 1 for v in columns)

min_a = [u for u in range(1, 32) if weight(A, u) == 2]
min_b = [u for u in range(1, 32) if weight(B, u) == 2]
assert min_a == [8, 16, 24] and min_b == [2, 8, 16]
assert rank(min_a) == 2 and rank(min_b) == 3
assert canonical(A) != canonical(B)

# The image list specifies an invertible map of coefficient spaces.
image_basis = (1, 4, 7, 8, 20)
assert rank(image_basis) == 5

def map_coefficients(u):
    v = 0
    for i in range(5):
        if u & (1 << i):
            v ^= image_basis[i]
    return v

ratios = [Fraction(weight(B, map_coefficients(u)), weight(A, u))
          for u in range(1, 32)]
assert min(ratios) == Fraction(2, 3)
assert max(ratios) == Fraction(3, 2)
assert max(ratios) / min(ratios) == Fraction(9, 4)
print('witness: [8,5] projective, W=1+3z2+8z3+7z4+8z5+5z6,')
print('minimum-word spans:', rank(min_a), rank(min_b), 'distortion:',
      str(max(ratios) / min(ratios)))
print('PROJECTIVE_ISOSPECTRAL_DISTORTION_VERIFY_OK')
