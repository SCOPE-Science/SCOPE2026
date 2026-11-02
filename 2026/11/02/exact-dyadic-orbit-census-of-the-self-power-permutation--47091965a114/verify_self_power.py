#!/usr/bin/env python3
"""Independent finite checker for the dyadic self-power orbit census.
Run as: python3 verify_self_power.py
Only the Python standard library is required. Finite verification is not a proof.
"""
from collections import Counter


def v2(n):
    if n == 0:
        raise ValueError("valuation at zero is not needed")
    return (n & -n).bit_length() - 1


def period_formula(k, x):
    mod = 1 << k
    if k == 1 or x in (1, mod - 1):
        return 1
    if x % 4 == 1:
        return 1 << max(0, k - 2 * v2(x - 1))
    r = v2(x + 1)
    if k <= r + 1:
        return 1
    return 1 << max(1, k - 3 * r + 1)


def cycle_counts_formula(k):
    if k == 1:
        return Counter({1: 1})
    counts = Counter({1: 2})
    for s in range(2, k):
        size = 1 << (k - s - 1)
        a = 1 << max(0, k - 2 * s)
        b = 1 if k <= s + 1 else 1 << max(1, k - 3 * s + 1)
        assert size % a == size % b == 0
        counts[a] += size // a
        counts[b] += size // b
    return counts


def check(upper=15):
    total_states = total_cycles = 0
    for k in range(1, upper + 1):
        modulus = 1 << k
        domain = range(1, modulus, 2)
        mapping = {x: pow(x, x, modulus) for x in domain}
        assert len(mapping) == len(set(mapping.values())), ('not bijective', k)
        cycles = Counter()
        visited = set()
        for seed in mapping:
            if seed in visited:
                continue
            orbit = []
            state = seed
            while state not in visited:
                visited.add(state)
                orbit.append(state)
                state = mapping[state]
            assert state == seed, ('nonperiodic state', k, seed)
            length = len(orbit)
            for member in orbit:
                assert length == period_formula(k, member), ('wrong period', k, member, length)
            cycles[length] += 1
        expected = cycle_counts_formula(k)
        assert cycles == expected, ('wrong cycle census', k, cycles, expected)
        assert sum(t * number for t, number in cycles.items()) == modulus // 2
        if k >= 6:
            assert max(cycles) == 1 << (k - 4)
            assert cycles[max(cycles)] == 2
        total_states += modulus // 2
        total_cycles += sum(cycles.values())
        if k in (1, 4, 6, 8, 12, 15):
            print('k=', k, 'cycle_counts=', sorted(cycles.items()))
    print('VERIFY_OK:', total_states, 'distinct odd states;', total_cycles,
          'cycles; complete orbit decompositions for k=1..%d' % upper)


if __name__ == '__main__':
    check()
