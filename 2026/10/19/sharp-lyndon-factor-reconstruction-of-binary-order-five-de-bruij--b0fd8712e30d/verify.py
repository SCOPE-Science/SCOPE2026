"""Exhaustive verification of Lyndon-factor reconstruction for binary B(2,5).

Run: python3 verify.py [profiles.csv]
Only the Python standard library is required.
"""
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

N = 32


def eulerian_cycles():
    """Enumerate directed Eulerian circuits with their unique 00000 edge first."""
    words = []

    def extend(path, visited):
        if len(path) == N:
            if (path[-1] & 15) == 0:
                words.append(''.join(str(edge >> 4) for edge in path))
            return
        source = path[-1] & 15
        for bit in (0, 1):
            edge = (source << 1) | bit
            if not (visited >> edge) & 1:
                extend(path + [edge], visited | (1 << edge))

    extend([0], 1)
    assert len(words) == len(set(words)) == 2048
    return set(words)


def pairing_cycles():
    """Enumerate all local binary incoming/outgoing bijections."""
    words = set()
    accepted = 0
    for assignment in range(1 << 16):
        successor = [0] * N
        for vertex in range(16):
            e0, e1 = vertex, vertex + 16
            f0, f1 = vertex * 2, vertex * 2 + 1
            if assignment & (1 << vertex):
                successor[e0], successor[e1] = f1, f0
            else:
                successor[e0], successor[e1] = f0, f1
        edges = []
        edge = 0
        while True:
            edges.append(edge)
            edge = successor[edge]
            if edge == 0:
                break
        if len(edges) == N:
            accepted += 1
            words.add(''.join(str(e >> 4) for e in edges))
    assert accepted == 2048 == len(words)
    return words


def is_lyndon_rotation(word):
    """Definition: strictly least among every nontrivial conjugate."""
    return all(word < word[j:] + word[:j] for j in range(1, len(word)))


def is_lyndon_suffix(word):
    """Equivalent characterization: strictly smaller than proper suffixes."""
    return all(word < word[j:] for j in range(1, len(word)))


def signature(word, predicate):
    """Numbers of distinct Lyndon circular factors at lengths 1,...,19."""
    assert len(word) == N
    doubled = word + word[:18]
    answer = []
    for length in range(1, 20):
        distinct = {doubled[i:i + length] for i in range(N)}
        assert all(len(v) == length for v in distinct)
        answer.append(sum(predicate(v) for v in distinct))
    return tuple(answer)


def verification():
    a = eulerian_cycles()
    b = pairing_cycles()
    assert a == b
    assert all(w[:5] == '00000' for w in a)
    all_five = {format(i, '05b') for i in range(32)}
    for w in a:
        assert { (w + w[:4])[i:i+5] for i in range(32)} == all_five
    records = {}
    for w in sorted(a):
        s = signature(w, is_lyndon_rotation)
        assert s == signature(w, is_lyndon_suffix)
        assert s[:5] == (2, 1, 2, 3, 6)
        records[w] = s
    outcomes = {}
    for cutoff in (16, 17, 18, 19):
        profiles = Counter(s[:cutoff] for s in records.values())
        outcomes[cutoff] = (len(profiles), sum(v*(v-1)//2 for v in profiles.values()))
    assert outcomes == {16: (2044, 4), 17: (2045, 3), 18: (2047, 1), 19: (2048, 0)}
    collisions = defaultdict(list)
    for w, s in records.items():
        collisions[s[:18]].append(w)
    pairs = [group for group in collisions.values() if len(group) > 1]
    assert pairs == [[
        '00000101001101110010001111101011',
        '00000111010111110010100110110001',
    ]]
    assert [records[w][18] for w in pairs[0]] == [1, 2]
    return records


def check_csv(records, path):
    with path.open(newline='', encoding='utf-8') as f:
        lines = list(csv.reader(f))
    assert lines[0] == ['cycle'] + [f'L{k}' for k in range(6, 20)]
    expected = [[w] + [str(v) for v in s[5:]] for w, s in sorted(records.items())]
    assert lines[1:] == expected


if __name__ == '__main__':
    data = verification()
    if len(sys.argv) > 1:
        check_csv(data, Path(sys.argv[1]))
    print('VERIFY_OK distinct_de_bruijn_cycles=2048 pairing_assignments=65536 '
          'independent_eulerian_enumeration=yes independent_lyndon_criteria=yes '
          'distinct_profiles_cutoff18=2047 unique_profiles_cutoff19=2048 '
          'sole_cutoff18_collision=2 cycles')
