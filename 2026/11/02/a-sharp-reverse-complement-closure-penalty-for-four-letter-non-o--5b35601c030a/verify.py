#!/usr/bin/env python3
"""Reproduce an exact DNA reverse-complement-closed length-4 nonoverlap census.

Stdlib Python 3, no external files. Outputs VERIFY_OK on successful checks.
"""
from collections import Counter
from functools import lru_cache
from itertools import permutations, product

ALPHABET = range(4)   # 0=A, 1=C, 2=G, 3=T
COMPLEMENT = (3, 2, 1, 0)
LENGTH = 4


def reverse_complement(word):
    return tuple(COMPLEMENT[x] for x in reversed(word))


def compatible(x, y):
    # Check BOTH directions. For x=y this excludes self-overlapping words.
    return all(x[:j] != y[-j:] and y[:j] != x[-j:]
               for j in range(1, LENGTH))


def construct_graph():
    words = list(product(ALPHABET, repeat=LENGTH))
    unbordered = [x for x in words if compatible(x, x)]
    rc_sets = {min(x, reverse_complement(x)):
               tuple(sorted({x, reverse_complement(x)}))
               for x in unbordered}
    orbits = sorted(o for o in rc_sets.values()
                    if all(compatible(x, y) for x in o for y in o))
    nbrs = []
    for i, o in enumerate(orbits):
        nbrs.append(sum((1 << j) for j, p in enumerate(orbits)
                        if i != j and all(compatible(x, y)
                            for x in o for y in p)))
    return words, unbordered, orbits, nbrs


def verify():
    words, unbordered, orbits, nbrs = construct_graph()
    N = len(orbits)
    weights = tuple(map(len, orbits))
    assert (len(words), len(unbordered), N) == (256, 180, 56)
    assert Counter(weights) == {1: 12, 2: 44}
    assert sum(t.bit_count() for t in nbrs) // 2 == 540
    assert all((nbrs[i] >> j) & 1 == (nbrs[j] >> i) & 1
               for i in range(N) for j in range(N))
    assert all((nbrs[i] >> i) & 1 == 0 for i in range(N))

    # Exhaustive include/exclude recurrence on the induced graph of a mask.
    # Each codebook corresponds to exactly one clique of RC-orbit vertices.
    @lru_cache(maxsize=None)
    def best(mask):
        if not mask:
            return (0, 1)
        v_bit = mask & -mask
        v = v_bit.bit_length() - 1
        without_value, without_count = best(mask ^ v_bit)
        with_value, with_count = best(mask & nbrs[v])
        with_value += weights[v]
        if without_value > with_value:
            return (without_value, without_count)
        if with_value > without_value:
            return (with_value, with_count)
        return (with_value, with_count + without_count)

    full = (1 << N) - 1
    assert best(full) == (17, 32)
    assert best.cache_info().currsize == 398

    # A second recursion enumerates all winners. Independent direct checks
    # below validate each of their original 4^4-word constraints.
    optimal_sets = set()
    def collect(mask, picked, score):
        if not mask:
            assert score == 17
            optimal_sets.add(tuple(sorted(picked)))
            return
        v_bit = mask & -mask
        v = v_bit.bit_length() - 1
        target, _ = best(mask)
        if target == best(mask ^ v_bit)[0]:
            collect(mask ^ v_bit, picked, score)
        if target == weights[v] + best(mask & nbrs[v])[0]:
            collect(mask & nbrs[v], picked + (v,), score + weights[v])
    collect(full, (), 0)
    assert len(optimal_sets) == 32
    assert all(Counter(weights[i] for i in S) == {1: 5, 2: 6}
               for S in optimal_sets)
    codebooks = {frozenset(x for i in S for x in orbits[i])
                 for S in optimal_sets}
    assert len(codebooks) == 32
    for code in codebooks:
        assert len(code) == 17
        assert {reverse_complement(x) for x in code} == code
        assert all(compatible(x, y) for x in code for y in code)

    # Enumerate equivalence under all permutations preserving Watson-Crick
    # complementation; this group has 8 elements.
    group = [p for p in permutations(ALPHABET)
             if all(p[COMPLEMENT[x]] == COMPLEMENT[p[x]] for x in ALPHABET)]
    assert len(group) == 8
    left = set(codebooks)
    representative_codes = []
    while left:
        code = min(left, key=lambda a: tuple(sorted(a)))
        orbit = {frozenset(tuple(p[x] for x in word) for word in code)
                 for p in group}
        assert orbit <= codebooks
        assert len(orbit) == 8
        left -= orbit
        representative_codes.append(code)
    assert len(representative_codes) == 4

    # Independent weighted-clique branching bound. Greedy stable sets color
    # the candidate graph, giving a valid upper bound from class max weights.
    calls = 0
    maximum = 0
    count = 0
    def bb(mask, score):
        nonlocal calls, maximum, count
        calls += 1
        if not mask:
            if score > maximum:
                maximum, count = score, 1
            elif score == maximum:
                count += 1
            return
        remaining, ordering, bounds, total = mask, [], [], 0
        while remaining:
            pool, class_max = remaining, 0
            previous_len = len(ordering)
            while pool:
                bit = pool & -pool
                i = bit.bit_length() - 1
                ordering.append(i)
                class_max = max(class_max, weights[i])
                remaining &= ~bit
                pool &= ~bit & ~nbrs[i]
            total += class_max
            bounds.extend([total] * (len(ordering) - previous_len))
        for i, bound in zip(reversed(ordering), reversed(bounds)):
            if score + bound < maximum:
                return
            bb(mask & nbrs[i], score + weights[i])
            mask &= ~(1 << i)
    bb(full, 0)
    assert (maximum, count) == (17, 32)
    assert calls == 293

    print('WORDS', len(words))
    print('UNBORDERED', len(unbordered))
    print('RC_ORBITS', N)
    print('ORBIT_WEIGHTS', dict(Counter(weights)))
    print('COMPATIBLE_PAIRS', sum(x.bit_count() for x in nbrs)//2)
    print('DP_STATES', best.cache_info().currsize)
    print('OPTIMUM_AND_CODEBOOKS', maximum, count)
    print('INDEPENDENT_BB_CALLS', calls)
    print('SYMMETRY_CLASSES', len(representative_codes), 'EACH_SIZE', 8)
    for code in sorted(representative_codes,
                       key=lambda c: tuple(sorted(c))):
        print('REP', ' '.join(''.join(str(x) for x in word)
                              for word in sorted(code)))
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
