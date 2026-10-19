#!/usr/bin/env python3
"""Reproduce the finite certificate for the period-doubling factor comparison."""
from collections import defaultdict
from itertools import product

ALPHABET = '01'
SEED_A = '0101010001'
SEED_B = '1000101010'


def morphism(word):
    return ''.join('01' if symbol == '0' else '00' for symbol in word)


def iterate(word, steps):
    for _ in range(steps):
        word = morphism(word)
    return word


def signatures(word, order):
    # After a new letter c, all subsequences ending in c derive from
    # subsequences in the previous prefix. Descend by length to avoid reuse.
    patterns = {''.join(p) for r in range(1, order + 1)
                for p in product(ALPHABET, repeat=r)}
    count = {'': 1}
    for symbol in word:
        for r in range(order - 1, -1, -1):
            for pattern in product(ALPHABET, repeat=r):
                prefix = ''.join(pattern)
                count[prefix + symbol] = (
                    count.get(prefix + symbol, 0) + count.get(prefix, 0)
                )
    return tuple(count.get(pattern, 0)
                 for r in range(1, order + 1)
                 for pattern in (''.join(p) for p in product(ALPHABET, repeat=r)))


def exact_factors(length):
    block = {symbol: iterate(symbol, 4) for symbol in ALPHABET}
    return set((block[first] + block[second])[offset:offset + length]
               for first, second in ('00', '01', '10')
               for offset in range(16))


def direct_factors(word, length):
    return {word[i:i + length] for i in range(len(word) - length + 1)}


def verify():
    fixed = iterate('0', 10)
    assert set(direct_factors(fixed, 2)) == {'00', '01', '10'}
    counts = []
    for length in range(1, 11):
        factors = exact_factors(length)
        assert factors == direct_factors(fixed, length), length
        classes = defaultdict(set)
        for factor in factors:
            classes[signatures(factor, 3)].add(factor)
        non_singletons = sorted(sorted(cluster) for cluster in classes.values()
                                if len(cluster) > 1)
        counts.append((length, len(factors), len(classes)))
        if length < 10:
            assert not non_singletons, (length, non_singletons)
        else:
            assert non_singletons == [[SEED_A, SEED_B]], non_singletons
    assert counts == [
        (1, 2, 2), (2, 3, 3), (3, 5, 5), (4, 6, 6),
        (5, 8, 8), (6, 10, 10), (7, 11, 11), (8, 12, 12),
        (9, 14, 14), (10, 16, 15),
    ]
    assert signatures(SEED_A, 3) == signatures(SEED_B, 3)
    assert signatures(SEED_A, 4) != signatures(SEED_B, 4)
    for power in range(5):
        a, b = iterate(SEED_A, power), iterate(SEED_B, power)
        assert a != b
        assert signatures(a, 3) == signatures(b, 3)
    print('factor classes by length (n, factor count, 3-binomial count):')
    for line in counts:
        print(*line)
    print('unique pair at length 10:', SEED_A, SEED_B)
    print('ALL CHECKS PASSED')


if __name__ == '__main__':
    verify()
