#!/usr/bin/env python3
"""Pure-stdlib certificate checker for binary weight-four non-overlapping codes."""
import itertools
import json
from collections import defaultdict
from pathlib import Path


def fixed_weight_words(n, weight=4):
    for occupied in itertools.combinations(range(n), weight):
        active = set(occupied)
        yield ''.join('1' if position in active else '0' for position in range(n))


def conflicts(u, v):
    assert len(u) == len(v)
    n = len(u)
    return any(u[:j] == v[-j:] or v[:j] == u[-j:] for j in range(1, n))


def least_rotation(w):
    return min(w[k:] + w[:k] for k in range(len(w)))


def test_code(words, n):
    assert len(words) == len(set(words)), 'Repeated codeword'
    assert all(len(w) == n and w.count('1') == 4 for w in words)
    for i, u in enumerate(words):
        assert not conflicts(u, u), ('bordered codeword', n, u)
        for v in words[i + 1:]:
            assert not conflicts(u, v), ('overlapping codewords', n, u, v)


def main():
    path = Path(__file__).with_name('certificate.json')
    record = json.loads(path.read_text(encoding='utf-8'))
    expected_necklaces = {5: 1, 6: 2, 7: 5, 8: 8, 9: 14, 10: 20, 11: 30, 12: 40}
    assert set(map(int, record['codes'])) == set(expected_necklaces)
    for n, orbit_count in expected_necklaces.items():
        ambient = list(fixed_weight_words(n))
        primitive = [w for w in ambient if len({w[k:] + w[:k] for k in range(n)}) == n]
        necklaces = {least_rotation(w) for w in primitive}
        assert len(necklaces) == orbit_count
        assert len(primitive) == n * orbit_count
        code = record['codes'][str(n)]
        test_code(code, n)
        assert len(code) == (39 if n == 12 else orbit_count)
        print(f'n={n}: {len(code)} non-overlapping words; {orbit_count} primitive necklaces')

    available = {w for w in fixed_weight_words(12) if not conflicts(w, w)}
    assert len(available) == 128
    cliques = record['overlap_cliques_12']
    assert len(cliques) == 39
    assert all(clique for clique in cliques)
    listed = [w for group in cliques for w in group]
    assert len(listed) == len(set(listed)) == 128
    assert set(listed) == available, 'Clique cover missing or adding eligible words'
    for group in cliques:
        for a, b in itertools.combinations(group, 2):
            assert conflicts(a, b), ('Non-conflicting pair in a clique', a, b)
    # Each feasible code meets each of these 39 pairwise-conflicting classes
    # in at most one word. Ineligible words fail their own border test.
    assert len(record['codes']['12']) == len(cliques) == 39
    print('Upper certificate: 128 eligible words partitioned into 39 conflict cliques')
    print('PASS: exact optimum at length 12 equals 39; first necklace-bound gap at length 12')


if __name__ == '__main__':
    main()
