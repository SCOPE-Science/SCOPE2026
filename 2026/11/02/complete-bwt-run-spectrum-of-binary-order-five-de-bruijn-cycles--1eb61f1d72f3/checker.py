#!/usr/bin/env python3
"""Exhaustive, independent verification of cyclic-BWT run histograms for binary de Bruijn necklaces of order five."""
from collections import Counter

EXPECTED = {20: 38, 22: 426, 24: 840, 26: 608, 28: 130, 30: 6}
N = 32
M = 16


def runs(word):
    return 1 + sum(a != b for a, b in zip(word, word[1:]))


def by_lf_cycles():
    """Exhaust every last column permitted by de Bruijn distinct-window conditions."""
    spectrum = Counter()
    accepted = set()
    for mask in range(1 << M):
        orientations = [(mask >> i) & 1 for i in range(M)]
        b = tuple(z for a in orientations for z in (a, 1 - a))
        assert len(b) == N and b.count(0) == b.count(1) == M
        # LF maps BWT row j to the rank of its last symbol in the first column.
        seen_letter = [0, M]
        lf = []
        for bit in b:
            lf.append(seen_letter[bit])
            seen_letter[bit] += 1
        assert sorted(lf) == list(range(N))
        row = 0
        visited = set()
        while row not in visited:
            visited.add(row)
            row = lf[row]
        if row != 0 or len(visited) != N:
            continue
        assert runs(b) == 17 + sum(orientations[j] == orientations[j + 1]
                                    for j in range(M - 1))
        accepted.add(b)
        spectrum[runs(b)] += 1
    assert spectrum == EXPECTED, (dict(spectrum), EXPECTED)
    assert len(accepted) == 2048
    return spectrum, accepted


def independent_euler_tours():
    """Build every cyclic de Bruijn word by traversing each labeled edge once.

    A length-five window encodes an edge in the order-four binary de Bruijn graph.
    Rotate every tour to begin with the unique all-zero edge.
    """
    used = {0}
    path = [0]
    vertices_mask = (1 << 4) - 1
    def extend(vertex):
        if len(path) == N:
            if vertex == 0:
                yield tuple(path)
            return
        for bit in (0, 1):
            edge = 2 * vertex + bit
            if edge in used:
                continue
            used.add(edge)
            path.append(bit)
            yield from extend(edge & vertices_mask)
            path.pop()
            used.remove(edge)
    yield from extend(0)


def by_euler_tours():
    spectrum = Counter()
    columns = set()
    necklaces = set()
    for word in independent_euler_tours():
        assert len(word) == N
        windows = {tuple(word[(j + k) % N] for k in range(5)) for j in range(N)}
        assert len(windows) == N
        assert word not in necklaces
        necklaces.add(word)
        order = sorted(range(N), key=lambda start:
                       tuple(word[(start + h) % N] for h in range(N)))
        b = tuple(word[(start - 1) % N] for start in order)
        columns.add(b)
        spectrum[runs(b)] += 1
    assert spectrum == EXPECTED, dict(spectrum)
    assert len(necklaces) == len(columns) == 2048
    return spectrum, columns


def main():
    a, ac = by_lf_cycles()
    b, bc = by_euler_tours()
    assert a == b == EXPECTED
    assert ac == bc
    assert sum(a.values()) == 2048
    print('PASS: 65536 complementary-block columns exhausted; 2048 one-cycle LF permutations')
    print('PASS: 2048 independent Euler tours; circular suffix-array BWT agrees for every word')
    print('PASS: complete linear BWT-run spectrum:', dict(sorted(a.items())))


if __name__ == '__main__':
    main()
