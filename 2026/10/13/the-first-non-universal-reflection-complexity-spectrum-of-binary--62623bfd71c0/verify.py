#!/usr/bin/env python3
"""Exact reflection-class census for binary order-five de Bruijn cycles.

The exhaustive domain is all 2**16 binary feedback tables on length-4 states.
A table is retained precisely when it yields one 32-state cycle from state zero.
No third-party modules are required.
"""
from collections import Counter


def reverse_bits(x, width):
    y = 0
    for _ in range(width):
        y = (y << 1) | (x & 1)
        x >>= 1
    return y


def cycle_for_table(table):
    state = 0
    seen = set()
    states = []
    while state not in seen:
        seen.add(state)
        states.append(state)
        suffix = state & 15
        bit = ((state >> 4) & 1) ^ ((table >> suffix) & 1)
        state = ((state << 1) & 31) | bit
    if state != 0 or len(seen) != 32:
        return None
    return states


def direct_complexity(states, length):
    bits = [(state >> 4) & 1 for state in states]
    distinct = set()
    for i in range(32):
        factor = tuple(bits[(i + j) % 32] for j in range(length))
        distinct.add(min(factor, factor[::-1]))
    return len(distinct)


def invariants(table):
    a = z = 0
    for s in range(16):
        r = reverse_bits(s, 4)
        if s < r and ((table >> s) & 1) == ((table >> r) & 1):
            a += 1
        elif s == r and ((table >> s) & 1) == 0:
            z += 1
    return a, z


def main():
    spectrum = Counter()
    joint = Counter()
    examples = {}
    distinct_cycles = set()
    for table in range(1 << 16):
        states = cycle_for_table(table)
        if states is None:
            continue
        word = ''.join(str(state >> 4) for state in states)
        assert word not in distinct_cycles
        distinct_cycles.add(word)
        assert word[:5] == '00000'
        r5 = direct_complexity(states, 5)
        r6 = direct_complexity(states, 6)
        a, z = invariants(table)
        assert r5 == 20
        assert r6 == 28 - 2*a + z
        spectrum[r6] += 1
        joint[(a, z, r6)] += 1
        examples.setdefault((a, z, r6), (table, word))
    expected_spectrum = {22: 576, 25: 960, 26: 192, 28: 256, 29: 64}
    expected_joint = {
        (0, 1, 29): 64, (1, 0, 26): 192, (1, 2, 28): 256,
        (2, 1, 25): 960, (3, 0, 22): 576,
    }
    assert dict(spectrum) == expected_spectrum, spectrum
    assert dict(joint) == expected_joint, joint
    assert len(distinct_cycles) == 2048
    print('VERIFY_OK tables=65536 cycles=2048 r5=20')
    print('r6_distribution', sorted(spectrum.items()))
    print('joint_(A,Z,r6)', sorted(joint.items()))
    print('representatives_(A,Z,r6)_and_words', sorted(examples.items()))


if __name__ == '__main__':
    main()
