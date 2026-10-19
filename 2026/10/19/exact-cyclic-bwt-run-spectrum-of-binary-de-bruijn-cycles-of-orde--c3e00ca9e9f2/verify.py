#!/usr/bin/env python3
"""Exhaustive exact BWT-run census for binary de Bruijn necklaces of order five.

Two independent generation routes: de Bruijn graph circuits and LF permutations.
"""
from collections import Counter
from fractions import Fraction

ORDER = 5
N = 1 << ORDER
EXPECTED = {20:38, 22:426, 24:840, 26:608, 28:130, 30:6}


def cyclic_bwt(word):
    n = len(word)
    rotations = sorted(range(n), key=lambda i: word[i:] + word[:i])
    return ''.join(word[(i-1) % n] for i in rotations)


def run_count(word):
    return 1 + sum(a != b for a, b in zip(word, word[1:]))


def necklace_circuits():
    # Each cyclic order-five de Bruijn word contains 00000 exactly once.
    # Begin at the vertex 0000, traverse the edge labelled 0 first.
    # All remaining edges are used exactly once in a closed Eulerian walk.
    bits = [0]
    initial = 1  # edge (vertex 0000, label 0) has integer ID zero
    def visit(vertex, used):
        if len(bits) == N:
            if vertex == 0:
                yield ''.join(str(b) for b in bits)
            return
        for bit in (0, 1):
            edge = (vertex << 1) | bit
            if not (used & (1 << edge)):
                bits.append(bit)
                yield from visit(edge & 15, used | (1 << edge))
                bits.pop()
    yield from visit(0, initial)


def direct_census():
    histogram = Counter()
    images = set()
    words = set()
    examples = {}
    for word in necklace_circuits():
        assert len(word) == N and word[0] == '0'
        assert len({(word+word[:4])[i:i+5] for i in range(N)}) == N
        assert word not in words
        words.add(word)
        image = cyclic_bwt(word)
        images.add(image)
        assert all(image[2*j:2*j+2] in {'01', '10'} for j in range(16))
        r = run_count(image)
        histogram[r] += 1
        examples.setdefault(r, word)
    assert len(words) == 2048
    assert len(images) == 2048
    return histogram, images, examples


def cycle_from_last_column(last):
    counts = [0, 0]
    permutation = []
    for c in last:
        bit = int(c)
        permutation.append((16 if bit else 0) + counts[bit])
        counts[bit] += 1
    assert counts == [16, 16]
    position = 0
    visited = 0
    for _ in range(N):
        if visited & (1 << position):
            return False
        visited |= 1 << position
        position = permutation[position]
    return visited == (1 << N) - 1 and position == 0


def lf_census():
    histogram = Counter()
    images = set()
    for mask in range(1 << 16):
        # Each length-two BWT block contains one zero and one one.
        last = ''.join(('10' if mask & (1 << j) else '01') for j in range(16))
        if cycle_from_last_column(last):
            images.add(last)
            histogram[run_count(last)] += 1
    assert len(images) == 2048
    return histogram, images


def main():
    first, a, examples = direct_census()
    second, b = lf_census()
    assert a == b
    assert first == second == EXPECTED
    assert sum(EXPECTED.values()) == 2048
    assert min(first) == 20 and max(first) == 30
    mu = Fraction(sum(r * count for r, count in first.items()), 2048)
    variance = sum(Fraction(count, 2048) * (r - mu) ** 2
                   for r, count in first.items())
    assert mu == Fraction(195, 8) and variance == Fraction(211, 64)
    assert all(20 <= k <= 30 and k % 2 == 0 for k in first)
    # Representative witnesses permit spot checks independent of the histogram.
    for count, word in examples.items():
        assert run_count(cyclic_bwt(word)) == count
    print('VERIFY_OK order5 necklaces=2048 orientations=65536 independent_methods=2 '
          'bwt_sets_identical=2048 histogram=' + ','.join(f'{r}:{first[r]}' for r in sorted(first)))

if __name__ == '__main__':
    main()
