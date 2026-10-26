#!/usr/bin/env python3
"""Exact rank-three first-order type closure for finite threshold graphs.

Run: python3 verify.py
All arithmetic is exact; the script requires only the Python standard library.
"""
from collections import Counter, deque
from pathlib import Path
import json


def graph(word):
    """Start from K_1; 0 adds an isolated vertex, 1 a universal vertex."""
    rows = [0]
    for c in word:
        n = len(rows)
        if c == '0':
            rows.append(0)
        elif c == '1':
            rows = [r | (1 << n) for r in rows] + [(1 << n) - 1]
        else:
            raise ValueError('Nonbinary creation word')
    return tuple(rows)


def signature(rows):
    """Exact rank-3 type, expressed by adjacency patterns of 3 pebbles.

    A vertex type contains the two self-pair extension flags and a bitset
    recording all distinct second-pebble rank-1 types. For x != y those
    types are E(x,y) and the four realizable (E(x,z),E(y,z)) patterns.
    """
    n = len(rows)
    full = (1 << n) - 1
    types = set()
    for x in range(n):
        pair_types = 0
        ax = rows[x]
        for y in range(n):
            if y == x:
                continue
            ay = rows[y]
            outside = full ^ (1 << x) ^ (1 << y)
            quadrants = (
                int(bool(outside & ~ax & ~ay))
                | (int(bool(outside & ~ax & ay)) << 1)
                | (int(bool(outside & ax & ~ay)) << 2)
                | (int(bool(outside & ax & ay)) << 3)
            )
            key = (((ax >> y) & 1) << 4) | quadrants
            pair_types |= 1 << key
        others = full ^ (1 << x)
        types.add((int(bool(ax & others)),
                   int(bool(others & ~ax)), pair_types))
    return tuple(sorted(types))


def independent_type(rows):
    """Generic Hintikka recursion, independent of the compressed formula."""
    n = len(rows)

    def atomic(tup):
        return (
            tuple(int(tup[i] == tup[j])
                  for i in range(len(tup)) for j in range(i + 1, len(tup))),
            tuple(int(bool(rows[tup[i]] & (1 << tup[j])))
                  for i in range(len(tup)) for j in range(i + 1, len(tup))),
        )

    def rank_one(x, y):
        return (atomic((x, y)),
                frozenset(atomic((x, y, z)) for z in range(n)))

    def rank_two(x):
        return frozenset(rank_one(x, y) for y in range(n))

    return frozenset(rank_two(x) for x in range(n))


def calculate():
    initial = signature(graph(''))
    first = {initial: 0}
    words = ['']
    transitions = []
    todo = deque([0])
    while todo:
        i = todo.popleft()
        target = []
        for bit in '01':
            nxt = signature(graph(words[i] + bit))
            if nxt not in first:
                first[nxt] = len(words)
                words.append(words[i] + bit)
                todo.append(first[nxt])
            target.append(first[nxt])
        transitions.append(target)
    return words, transitions


def verify():
    manifest = json.loads(Path(__file__).with_name('canonical_classes.json').read_text(encoding='utf-8'))
    words, transitions = calculate()
    assert manifest['schema_version'] == 1
    assert manifest['rank'] == 3
    assert len(words) == 357 == len(transitions)
    assert len(manifest['states']) == 357
    length_counts = Counter(len(w) + 1 for w in words)
    assert dict(sorted(length_counts.items())) == {
        1: 1, 2: 2, 3: 4, 4: 6, 5: 8, 6: 10,
        7: 16, 8: 26, 9: 38, 10: 48, 11: 54, 12: 54,
        13: 44, 14: 26, 15: 12, 16: 6, 17: 2,
    }
    assert sorted(w for w in words if len(w) == 16) == [
        '0110011011001100', '1001001100110011',
    ]
    seen_independent = {}
    for i, (word, target) in enumerate(zip(words, transitions)):
        entry = manifest['states'][i]
        assert entry['id'] == i
        assert entry['word'] == word
        assert entry['vertices'] == len(word) + 1
        assert entry['signature'] == [list(t) for t in signature(graph(word))]
        assert entry['transitions'] == target
        full_type = independent_type(graph(word))
        assert full_type not in seen_independent, (i, seen_independent.get(full_type))
        seen_independent[full_type] = i
        for bit, j in zip('01', target):
            # Independently verify the exact rank-3 type of all 714 transitions.
            assert independent_type(graph(word + bit)) == independent_type(graph(words[j]))
    assert len(seen_independent) == 357
    # A separate exhaustive enumeration of all creation words up to 12 bits.
    representative_types = {signature(graph(w)) for w in words}
    tested = 0
    for n in range(13):
        for code in range(1 << n):
            w = format(code, '0%db' % n) if n else ''
            assert signature(graph(w)) in representative_types
            tested += 1
    assert tested == 8191
    print('NUMBER_OF_CLASSES=357')
    print('SHARP_REPRESENTATIVE_BOUND=17')
    print('MAXIMAL_MINIMAL_WORDS=0110011011001100,1001001100110011')
    print('VERIFIED_TRANSITIONS=714')
    print('INDEPENDENT_TYPES=357')
    print('EXHAUSTIVE_SHORT_CREATION_WORDS=8191')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
