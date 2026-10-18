#!/usr/bin/env python3
"""Exact finite enumeration of length-six abelian squares in binary order-five de Bruijn cycles."""
from collections import Counter, defaultdict

EXPECTED = {4:32, 5:96, 6:288, 7:384, 8:448,
            9:416, 10:224, 11:128, 12:32}
EXPECTED_ORBITS = {4:(4,6), 5:(0,24), 6:(8,68),
                   7:(0,96), 8:(8,108), 9:(0,104),
                   10:(8,52), 11:(0,32), 12:(4,6)}


def local_score(x, switch):
    first = ((x >> 3) & 1) + ((x >> 2) & 1)
    last = ((x >> 1) & 1) + (x & 1)
    return sum(int(a + first == last + (a ^ switch)) for a in (0, 1))


def pairings_census():
    counts = Counter()
    full = (1 << 32) - 1
    for switches in range(1 << 16):
        edge, visited = 0, 0
        for _ in range(32):
            if (visited >> edge) & 1:
                break
            visited |= 1 << edge
            vertex = edge & 15
            a = edge >> 4
            edge = (vertex << 1) | (a ^ ((switches >> vertex) & 1))
        if visited != full or edge != 0:
            continue
        score = sum(local_score(x, (switches >> x) & 1) for x in range(16))
        counts[score] += 1
    assert dict(counts) == EXPECTED, counts
    assert sum(counts.values()) == 2048
    return counts


def euler_cycles():
    # Every cyclic order-five de Bruijn word has precisely one occurrence of 00000.
    # Begin with that edge, and then use each of the 31 remaining edges once.
    used = 1
    bits = [0]
    def rec(vertex, used):
        if len(bits) == 32:
            if vertex == 0:
                yield ''.join(map(str, bits))
            return
        for bit in (0, 1):
            edge = (vertex << 1) | bit
            if not ((used >> edge) & 1):
                bits.append(bit)
                yield from rec(edge & 15, used | (1 << edge))
                bits.pop()
    yield from rec(0, used)


def canonical(word):
    n = len(word)
    i = (word + word).index('00000')
    assert i < n
    return (word + word)[i:i+n]


def direct_score(word):
    n = len(word)
    return sum(sum(int(word[(i+j) % n]) for j in range(3)) ==
               sum(int(word[(i+j) % n]) for j in range(3, 6))
               for i in range(n))


def direct_census():
    words = list(euler_cycles())
    assert len(words) == len(set(map(canonical, words))) == 2048
    scores = {canonical(w): direct_score(w) for w in words}
    assert Counter(scores.values()) == EXPECTED
    assert all(len({(w+w)[i:i+5] for i in range(32)}) == 32 for w in scores)
    seen, orbits = set(), defaultdict(Counter)
    for w, score in scores.items():
        if w in seen:
            continue
        opposite = ''.join('1' if a == '0' else '0' for a in w)
        orbit = {canonical(t) for t in (w, w[::-1], opposite, opposite[::-1])}
        assert all(scores[t] == score for t in orbit)
        assert len(orbit) in (2, 4)
        seen.update(orbit)
        orbits[score][len(orbit)] += 1
    assert len(seen) == 2048
    assert {s:(orbits[s][2],orbits[s][4]) for s in EXPECTED} == EXPECTED_ORBITS
    return orbits


if __name__ == '__main__':
    pairings_census()
    direct_census()
    print('ABELIAN_DEBRUIJN5_PASS pairing_assignments=65536 cyclic_tours=2048 '
          'direct_cycles=2048 orbit_classes=528')
