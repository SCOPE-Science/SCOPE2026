#!/usr/bin/env python3
"""Exact finite census of Chen-Fox-Lyndon factors for binary de Bruijn cycles of order five.

Only standard-library integers, strings and sets are used. Python 3.9 or later.
"""
from collections import Counter

N = 32


def feedback_cycles():
    """Enumerate all edge-permutation feedback maps on 5-bit windows."""
    found = set()
    valid_tables = 0
    for table in range(1 << 16):
        v = 0
        edges = []
        visited = 0
        for _ in range(N):
            if (visited >> v) & 1:
                break
            visited |= 1 << v
            edges.append(v)
            v = ((v << 1) & 31) | ((v >> 4) ^ ((table >> (v & 15)) & 1))
        if len(edges) == N and v == 0:
            valid_tables += 1
            word = ''.join(str(e >> 4) for e in edges)
            assert word.startswith('00000')
            found.add(word)
    assert valid_tables == len(found), 'distinct feedback maps produced equal necklaces'
    return found


def euler_cycles():
    """Independent complete edge-simple Euler-tour search on the 16-vertex graph."""
    found = set()

    def descend(vertex, used, edges):
        if len(edges) == N:
            if vertex == 0:
                found.add(''.join(str(e >> 4) for e in edges))
            return
        for bit in (0, 1):
            edge = (vertex << 1) | bit
            if not (used >> edge) & 1:
                descend(edge & 15, used | (1 << edge), edges + [edge])

    # Every 5-bit word occurs exactly once, so anchor the unique 00000 edge.
    descend(0, 1, [0])
    return found


def duval_factors(word):
    """Duval's linear-time Chen-Fox-Lyndon decomposition."""
    out = []
    start = 0
    while start < len(word):
        i = start
        j = start + 1
        while j < len(word) and word[i] <= word[j]:
            if word[i] < word[j]:
                i = start
            else:
                i += 1
            j += 1
        step = j - i
        while start <= i:
            out.append(word[start:start + step])
            start += step
    return out


def is_lyndon(word):
    return all(word < word[p:] + word[:p] for p in range(1, len(word)))


def slow_factors(word):
    """Independent definition-level longest-Lyndon-prefix implementation."""
    factors = []
    while word:
        length = max(k for k in range(1, len(word) + 1) if is_lyndon(word[:k]))
        factors.append(word[:length])
        word = word[length:]
    assert all(factors[i] >= factors[i + 1] for i in range(len(factors) - 1))
    return factors


def valid_cycle(word):
    double = word + word[:4]
    return len(word) == N and len({double[i:i + 5] for i in range(N)}) == N


def census():
    f = feedback_cycles()
    e = euler_cycles()
    assert f == e and len(f) == 2048
    rooted = Counter()
    cycle_maximums = Counter()
    extrema = []
    profile = Counter()
    for word in sorted(f):
        assert valid_cycle(word)
        counts = []
        for shift in range(N):
            cut = word[shift:] + word[:shift]
            a = duval_factors(cut)
            b = slow_factors(cut)
            assert a == b
            assert ''.join(a) == cut
            counts.append(len(a))
            rooted[len(a)] += 1
            if len(a) == 16:
                extrema.append((word, shift, cut, tuple(a)))
        assert counts.count(1) == 1
        assert min(counts) == 1
        cycle_maximums[max(counts)] += 1
        profile[tuple(counts)] += 1
    expected_rooted = {
        1: 2048, 2: 8304, 3: 11896, 4: 12698,
        5: 10946, 6: 7944, 7: 4903, 8: 3083,
        9: 1820, 10: 995, 11: 480, 12: 247,
        13: 120, 14: 39, 15: 11, 16: 2,
    }
    expected_max = {
        7: 2, 8: 94, 9: 484, 10: 640, 11: 421,
        12: 237, 13: 118, 14: 39, 15: 11, 16: 2,
    }
    assert rooted == Counter(expected_rooted), (rooted, expected_rooted)
    assert cycle_maximums == Counter(expected_max), (cycle_maximums, expected_max)
    assert sum(rooted.values()) == 65536
    assert sum(cycle_maximums.values()) == 2048
    assert len(extrema) == 2
    for w, shift, cut, fact in extrema:
        assert len(fact) == 16
    return rooted, cycle_maximums, extrema


if __name__ == '__main__':
    r, c, extrema = census()
    print('ROOTED', sorted(r.items()))
    print('CYCLE_MAXIMA', sorted(c.items()))
    for item in extrema:
        print('EXTREMUM', item)
    print('VERIFY_OK')
