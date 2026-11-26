"""Recompute the complete ordinary-zero-forcing orbit census of Q4."""
from collections import Counter
from itertools import permutations
import json
from pathlib import Path

FULL = (1 << 16) - 1
NEIGHBORS = [sum(1 << (v ^ (1 << j)) for j in range(4)) for v in range(16)]


def bits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit


def finishing_time(black):
    rounds = 0
    while black != FULL:
        targets = 0
        for bit in bits(black):
            white = NEIGHBORS[bit.bit_length()-1] & (FULL ^ black)
            if white.bit_count() == 1:
                targets |= white
        if targets == 0:
            return -1
        rounds += 1
        black |= targets
    return rounds


def group_images():
    images = set()
    for coordinate_order in permutations(range(4)):
        for t in range(16):
            images.add(tuple(1 << (t ^ sum(((v >> i) & 1) << j
                                           for i, j in enumerate(coordinate_order)))
                             for v in range(16)))
    return images


def main():
    expected = json.loads(Path(__file__).with_name('CLASSIFICATION.json').read_text())
    times = tuple(map(finishing_time, range(FULL+1)))
    successful = {s for s, time in enumerate(times) if time >= 0}
    size = min(s.bit_count() for s in successful)
    assert size == expected['zero_forcing_number']
    minimal = {s for s in successful if all(times[s ^ v] < 0 for v in bits(s))}
    assert minimal == {s for s in successful if s.bit_count() == size}
    assert len(minimal) == expected['inclusion_minimal_count']
    assert sorted({s.bit_count() for s in minimal}) == expected['inclusion_minimal_sizes']

    group = group_images()
    assert len(group) == expected['automorphism_group_order']
    remaining = set(minimal)
    rows = []
    while remaining:
        s = min(remaining)
        indices = [b.bit_length()-1 for b in bits(s)]
        orbit = {sum(g[i] for i in indices) for g in group}
        assert orbit <= remaining
        assert all(times[t] == times[s] for t in orbit)
        rows.append({'representative': s, 'size': len(orbit), 'rounds': times[s]})
        remaining.difference_update(orbit)
    assert rows == expected['minimum_orbits']
    assert Counter(str(times[s]) for s in minimal) == expected['minimum_synchronous_round_counts']
    print(f'Checked {len(times)} subsets: {len(minimal)} minimum sets, {len(rows)} orbits.')


if __name__ == '__main__':
    main()
