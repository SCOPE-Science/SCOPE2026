#!/usr/bin/env python3
"""Exact, standalone certificate of an optimal cyclic pair metric layout
for the extended binary Golay [24,12,8] code. Python 3.8+ stdlib only.
"""
from collections import Counter
from itertools import combinations

N = 24
GENERATOR_EXPONENTS = (0, 1, 5, 6, 7, 9, 11)
ORDER = (12, 7, 20, 15, 9, 14, 19, 11, 2, 3, 8, 23,
         6, 18, 16, 21, 1, 0, 22, 10, 17, 4, 13, 5)


def make_words():
    generator = sum(1 << j for j in GENERATOR_EXPONENTS)
    words = []
    for message in range(1 << 12):
        bits23 = 0
        for i in range(12):
            if message & (1 << i):
                bits23 ^= generator << i
        assert bits23 < (1 << 23)
        # Extend to even parity; coordinate 23 is the parity coordinate.
        word = bits23 | ((bits23.bit_count() & 1) << 23)
        words.append(word)
    assert len(set(words)) == 4096
    return words


def pair_weight(word, order):
    # Independent direct pair enumeration rather than the adjacency formula.
    return sum(bool(word & (1 << order[i]) or
                    word & (1 << order[(i + 1) % N]))
               for i in range(N))


def internal_edges(word, order):
    return sum(bool(word & (1 << order[i])) and
               bool(word & (1 << order[(i + 1) % N]))
               for i in range(N))


def run():
    assert len(ORDER) == N and set(ORDER) == set(range(N))
    words = make_words()
    hamming = Counter(w.bit_count() for w in words)
    assert hamming == {0: 1, 8: 759, 12: 2576, 16: 759, 24: 1}
    octads = [w for w in words if w.bit_count() == 8]

    # Independently check that weight-eight words form S(5,8,24).
    pentads = set()
    for word in octads:
        support = [i for i in range(N) if word & (1 << i)]
        assert len(support) == 8
        for subset in combinations(support, 5):
            value = sum(1 << i for i in subset)
            assert value not in pentads
            pentads.add(value)
    assert len(pentads) == 759 * 56 == 42504
    assert len(pentads) == 42504  # C(24,5)

    adjacency = Counter(internal_edges(w, ORDER) for w in octads)
    assert adjacency == {0: 30, 1: 118, 2: 240, 3: 234, 4: 137}
    assert max(adjacency) == 4
    pair_spectrum = Counter(pair_weight(w, ORDER) for w in words)
    assert pair_spectrum == {
        0: 1, 12: 137, 13: 236, 14: 246, 15: 150,
        16: 152, 17: 480, 18: 884, 19: 644, 20: 479,
        21: 292, 22: 246, 23: 118, 24: 31
    }
    assert sum(pair_spectrum.values()) == 4096
    assert min(pair_weight(w, ORDER) for w in words if w) == 12
    for w in octads:
        assert pair_weight(w, ORDER) == 16 - internal_edges(w, ORDER)

    # Any cyclic pentad of positions belongs to an octad: this witnesses
    # the universal bound for every coordinate order by the design property.
    for start in range(N):
        mask = sum(1 << ORDER[(start + j) % N] for j in range(5))
        assert mask in pentads
        assert sum((w & mask) == mask for w in octads) == 1

    print('HAMMING', sorted(hamming.items()))
    print('OCTAD_INTERNAL_EDGES', sorted(adjacency.items()))
    print('PAIR_SPECTRUM', sorted(pair_spectrum.items()))
    print('STEINER_PENTADS', len(pentads))
    print('OPTIMAL_PAIR_DISTANCE', 12)
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
