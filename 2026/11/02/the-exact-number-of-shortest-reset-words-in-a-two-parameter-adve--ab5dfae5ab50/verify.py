#!/usr/bin/env python3
"""Independent finite checks for a shortest-reset-word enumeration theorem.

Uses only the Python standard library. Run: python verify.py
"""
import collections
import itertools
import math
import random


def transitions(k, m):
    n = k + m + 1
    maps = []
    for i in range(1, k + 1):
        maps.append(tuple(0 if q == i else q for q in range(n)))
    for r in range(1, m + 1):
        maps.append(tuple(q + 1 if r <= q < r + k else r if q == r + k else q for q in range(n)))
    return maps


def move(subset, transformation):
    out = 0
    while subset:
        bit = subset & -subset
        p = bit.bit_length() - 1
        out |= 1 << transformation[p]
        subset -= bit
    return out


def shortest_count(k, m):
    maps = transitions(k, m)
    start = (1 << (k + m + 1)) - 1
    Q = collections.deque([start])
    distance = {start: 0}
    ways = {start: 1}
    while Q:
        s = Q.popleft()
        for T in maps:
            t = move(s, T)
            if t not in distance:
                distance[t] = distance[s] + 1
                ways[t] = ways[s]
                Q.append(t)
            elif distance[t] == distance[s] + 1:
                ways[t] += ways[s]
    return distance[1], ways[1]


def permitted(events, k, m):
    position = {name: p for p, name in enumerate(events)}
    if any(position[f'C{j}'] >= position[f'H{j}'] for j in range(1, m + 1)):
        return False
    cpos = sorted(position[f'C{j}'] for j in range(1, m + 1))
    return all(position[f'D{k-j+1}'] < cpos[j - 1] for j in range(1, m + 1))


def decode_events(events, k, m):
    """Convert a valid event ordering into a letter word, or fail loudly."""
    T = transitions(k, m)
    pos = {q: q for q in range(1, k + m + 1)}
    w = []
    for event in events:
        kind, ind = event[0], int(event[1:])
        token = ind if kind == 'D' else k + ind
        assert token in pos
        place = pos[token]
        if kind == 'C':
            assert place > k and k not in pos.values()
        else:
            assert place <= k
        w.append(place)
        transform = T[place - 1]
        pos = {p: transform[q] for p, q in pos.items() if transform[q] != 0}
    assert not pos
    return tuple(w)


def run():
    cases = 0
    for m in range(1, 6):
        for k in range(2 * m - 1, 13):
            if k + m > 15:
                continue
            length, count = shortest_count(k, m)
            expected = math.factorial(k + 2 * m) // (6 ** m)
            assert math.factorial(k + 2 * m) % (6 ** m) == 0
            assert length == k + 2 * m, (k, m, length)
            assert count == expected, (k, m, count, expected)
            cases += 1
    print(f'INDEPENDENT_POWER_AUTOMATON_BFS: {cases} parameter pairs PASS')

    exact = [(1, 1), (2, 1), (3, 2), (4, 2)]
    for k, m in exact:
        labels = [f'D{i}' for i in range(1, k + 1)] + [f'C{i}' for i in range(1, m + 1)] + [f'H{i}' for i in range(1, m + 1)]
        words = set()
        good = 0
        for p in itertools.permutations(labels):
            if permitted(p, k, m):
                good += 1
                words.add(decode_events(p, k, m))
        length, count = shortest_count(k, m)
        assert good == count == len(words) == math.factorial(length) // (6 ** m)
        print(f'EXHAUSTIVE_EVENT_BIJECTION: k={k}, m={m}, {good} distinct words PASS')

    rng = random.Random(9178032)
    samples = 0
    for k, m in [(5, 3), (6, 3), (7, 4), (9, 5), (11, 6)]:
        labels = [f'D{i}' for i in range(1, k + 1)] + [f'C{i}' for i in range(1, m + 1)] + [f'H{i}' for i in range(1, m + 1)]
        valid = 0
        for trial in range(100000):
            p = list(labels)
            rng.shuffle(p)
            if permitted(p, k, m):
                w = decode_events(p, k, m)
                assert len(w) == k + 2 * m
                valid += 1
        samples += valid
        print(f'SEEDED_VALID_EVENT_SIMULATION: k={k}, m={m}, {valid} valid samples PASS')
    print(f'TOTAL_VALID_RANDOM_SAMPLES: {samples}')
    # The stated range is not a vacuous all-parameter extrapolation.
    assert shortest_count(2, 2) == (6, 16)
    print('BOUNDARY_EXAMPLE: k=2, m=2 gives 16 rather than 20 PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
