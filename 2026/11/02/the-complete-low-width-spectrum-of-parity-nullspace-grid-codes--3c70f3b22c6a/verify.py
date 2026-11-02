#!/usr/bin/env python3
"""Exact finite base certification for low-width even-neighborhood grid codes.

Run: python3 verify.py. Requires Python standard library only.
"""
from collections import Counter
from itertools import combinations

PERIOD = {1: 3, 2: 4, 3: 6, 4: 5}


def step(width, vector):
    return vector ^ ((vector << 1) & ((1 << width) - 1)) ^ (vector >> 1)


def sequence(width, length, seed):
    last, current = 0, seed
    columns = []
    for _ in range(length):
        columns.append(current)
        last, current = current, last ^ step(width, current)
    return columns, current


def code(width, length):
    return [tuple(cols) for seed in range(1 << width)
            for cols, boundary in [sequence(width, length, seed)] if boundary == 0]


def as_set(columns, width):
    return frozenset((i, j) for j, bits in enumerate(columns)
                     for i in range(width) if bits & (1 << i))


def prime(columns, width):
    return all(v != 0 for v in columns) and all(
        any(v & (1 << i) for v in columns) for i in range(width)
    )


def expected(width, length):
    h = length + 1
    if width == 1 and h % 3 == 0:
        t = h // 3
        return Counter({0: 1, 2*t: 1}), (2*t,)
    if width == 2:
        if h % 4 == 0:
            t = h // 4
            return Counter({0:1, 4*t:3}), (4*t, 6*t)
        if h % 4 == 2:
            t = h // 2
            return Counter({0:1, 2*t:1}), (2*t,)
    if width == 3:
        if h % 6 == 0:
            t = h // 6
            return Counter({0:1, 8*t:7}), (8*t, 12*t, 14*t)
        if h % 6 == 3:
            t = h // 3
            return Counter({0:1, 4*t:3}), (4*t, 6*t)
    if width == 4 and h % 5 == 0:
        t = h // 5
        return Counter({0:1, 8*t:13, 12*t:2}), (8*t, 12*t, 14*t, 16*t)
    return Counter({0:1}), ()


def subspace_supports(width, length):
    words = code(width, length)
    dim = (len(words)).bit_length() - 1
    assert (1 << dim) == len(words)
    # Each distinct subspace is the span of one or more independent ordered bases.
    # Directly deduplicate their complete word sets; no specialized packages.
    subsets = {}
    words = [as_set(w, width) for w in words]
    for rank in range(1, dim+1):
        spaces = set()
        histogram = Counter()
        for vectors in combinations(words[1:], rank):
            span = {frozenset()}
            for vector in vectors:
                span |= {point.symmetric_difference(vector) for point in list(span)}
            if len(span) != (1 << rank):
                continue
            key = frozenset(span)
            if key in spaces:
                continue
            spaces.add(key)
            histogram[len(frozenset().union(*span))] += 1
        subsets[rank] = dict(sorted(histogram.items()))
    return subsets


RANKS = {
    1: (1, 1, 0),
    2: (2, 1, 2, 0),
    3: (3, 3, 1, 3, 3, 0),
    4: (4, 4, 4, 4, 0),
}

BASE = {
    (1, 2): ({1:{2:1}}, 1),
    (2, 1): ({1:{2:1}}, 1),
    (2, 3): ({1:{4:3}, 2:{6:1}}, 2),
    (3, 2): ({1:{4:3}, 2:{6:1}}, 2),
    (3, 5): ({1:{8:7}, 2:{12:7}, 3:{14:1}}, 4),
    (4, 4): ({1:{8:13,12:2}, 2:{12:22,14:12,16:1},
              3:{14:4,15:8,16:3}, 4:{16:1}}, 15),
}


def direct_parity(width, length, cols):
    for j in range(length):
        for i in range(width):
            x = (cols[j] >> i) & 1
            if i: x ^= (cols[j] >> (i-1)) & 1
            if i+1 < width: x ^= (cols[j] >> (i+1)) & 1
            if j: x ^= (cols[j-1] >> i) & 1
            if j+1 < length: x ^= (cols[j+1] >> i) & 1
            if x: return False
    return True


def main():
    # Exact verification of the finite transfer/Fibonacci-matrix identities
    # using images of every basis vector, without symbolic algebra packages.
    for width, expected_ranks in RANKS.items():
        ranks = []
        for index in range(1, PERIOD[width] + 1):
            images = []
            for basis_bit in range(width):
                _, image = sequence(width, index - 1, 1 << basis_bit)
                images.append(image)
            span = {0}
            for v in images:
                span |= {x ^ v for x in tuple(span)}
            ranks.append(len(span).bit_length() - 1)
        assert tuple(ranks) == expected_ranks, (width, ranks)
        assert ranks[-1] == 0 and ranks[-2] == width
    counts = 0
    for width in range(1, 5):
        for length in range(1, 73):
            patterns = code(width, length)
            exp, hierarchy = expected(width, length)
            actual = Counter(sum(x.bit_count() for x in seq) for seq in patterns)
            assert actual == exp, (width, length, actual, exp)
            for pattern in patterns:
                assert direct_parity(width, length, pattern)
            counts += 1
    for (width, length), (expected_supports, expected_prime) in BASE.items():
        actual_supports = subspace_supports(width, length)
        assert actual_supports == expected_supports, (width, length, actual_supports)
        prime_count = sum(prime(x, width) for x in code(width, length) if any(x))
        assert prime_count == expected_prime, (width, length, prime_count)
    # The periodic reflection gives an internal zero column between successive blocks;
    # verify prime counts beyond the base explicitly, including the all-zero case.
    for width in range(1,5):
        for length in range(1,73):
            actual_primes = sum(prime(c,width) for c in code(width,length) if any(c))
            target = BASE.get((width,length),({},0))[1]
            assert actual_primes == target, (width,length,actual_primes,target)
    # Completely independent exhaustive direct neighborhood test on all binary
    # arrays with up to 16 cells, without using the column recurrence.
    checked = 0
    for width in range(1, 5):
        for length in range(1, 5):
            if width*length > 16: continue
            direct = Counter()
            for mask in range(1 << (width*length)):
                cols = [sum(((mask >> (j*width+i)) & 1) << i
                            for i in range(width)) for j in range(length)]
                if direct_parity(width,length,cols):
                    direct[mask.bit_count()] += 1
                checked += 1
            expected_poly,_ = expected(width,length)
            assert direct == expected_poly, (width,length,direct,expected_poly)
    print(f'VERIFY_OK width_length_cases={counts} base_support_cases={len(BASE)} matrix_rank_identities={len(RANKS)} direct_assignments={checked}')

if __name__ == '__main__':
    main()
