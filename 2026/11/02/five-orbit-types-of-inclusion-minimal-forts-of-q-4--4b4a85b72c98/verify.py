#!/usr/bin/env python3
"""Exact fort and automorphism-orbit enumeration on the four-cube."""
from collections import Counter
from itertools import permutations

DIM = 4
NV = 1 << DIM
LIMIT = 1 << NV
NEIGHBORS = [sum(1 << (v ^ (1 << j)) for j in range(DIM)) for v in range(NV)]
EXPECTED = [(0x0660, 12), (0x0116, 16), (0x033c, 32),
            (0x1be4, 96), (0x19ea, 192)]


def fort_bitset(s):
    """A fort is nonempty and no outside vertex sees exactly one member."""
    return s != 0 and all(
        (NEIGHBORS[v] & s).bit_count() != 1
        for v in range(NV) if not (s & (1 << v))
    )


def fort_independent(s):
    """Different predicate: count neighbors as an explicit set of binary words."""
    if not s:
        return False
    selected = {v for v in range(NV) if (s >> v) & 1}
    for outside in set(range(NV)) - selected:
        touches = sum((outside ^ (1 << j)) in selected for j in range(DIM))
        if touches == 1:
            return False
    return True


def dp_minimal_forts():
    is_fort = bytearray(LIMIT)
    contains_fort = bytearray(LIMIT)
    minima = set()
    for s in range(1, LIMIT):
        is_fort[s] = fort_bitset(s)
        contains_proper = False
        bits = s
        while bits:
            bit = bits & -bits
            if contains_fort[s ^ bit]:
                contains_proper = True
                break
            bits ^= bit
        if is_fort[s] and not contains_proper:
            minima.add(s)
        contains_fort[s] = bool(is_fort[s] or contains_proper)
    return minima


def exhaustive_submask_minimal_forts():
    is_fort = bytearray(fort_independent(s) for s in range(LIMIT))
    minima = set()
    for s in range(1, LIMIT):
        if not is_fort[s]:
            continue
        t = (s - 1) & s
        while t:
            if is_fort[t]:
                break
            t = (t - 1) & s
        if t == 0:
            minima.add(s)
    return minima


def permute_vertex(v, p):
    return sum(((v >> j) & 1) << p[j] for j in range(DIM))


def cube_automorphisms():
    return [tuple(permute_vertex(v, p) ^ translation for v in range(NV))
            for p in permutations(range(DIM)) for translation in range(NV)]


def action(s, mapping):
    return sum(1 << mapping[v] for v in range(NV) if s & (1 << v))


def main():
    minima_a = dp_minimal_forts()
    minima_b = exhaustive_submask_minimal_forts()
    assert minima_a == minima_b
    assert len(minima_a) == 348
    assert Counter(s.bit_count() for s in minima_a) == {4: 28, 6: 32, 8: 288}
    maps = cube_automorphisms()
    assert len(maps) == len(set(maps)) == 384
    all_orbits = set()
    sizes = []
    for rep, expected_size in EXPECTED:
        assert rep in minima_a
        orbit = {action(rep, mapping) for mapping in maps}
        assert len(orbit) == expected_size
        assert min(orbit) == rep
        assert orbit <= minima_a and not (orbit & all_orbits)
        all_orbits.update(orbit)
        sizes.append(len(orbit))
    assert all_orbits == minima_a
    assert sizes == [12, 16, 32, 96, 192]
    print('VERIFY_OK Q4_minimal_forts=348 sizes=4:28,6:32,8:288 '
          'aut_group=384 orbits=12,16,32,96,192 '
          'distinct_predicates_and_minimality_algorithms=agree')


if __name__ == '__main__':
    main()
