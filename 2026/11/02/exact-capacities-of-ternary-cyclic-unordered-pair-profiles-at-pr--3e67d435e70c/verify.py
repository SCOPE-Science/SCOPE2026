#!/usr/bin/env python3
"""Standalone finite checks of unordered ternary cyclic adjacent-pair profiles.

The general theorem is proved by Eulerian multigraphs; these tests are
finite regression checks, not a substitute for the proof.
"""
from collections import defaultdict
from itertools import product


def word_profile(word):
    pairs = [0] * 6
    index = {(0, 0): 0, (1, 1): 1, (2, 2): 2,
             (0, 1): 3, (0, 2): 4, (1, 2): 5}
    for a, b in zip(word, word[1:] + word[:1]):
        pairs[index[tuple(sorted((a, b)))]] += 1
    return tuple(pairs)


def candidate_profiles(counts):
    """Parameterize every feasible profile using graph degrees and connectivity."""
    a, b, c = counts
    for x in range(2 * min(a, b) + 1):
        for y in range(2 * min(a, c) + 1):
            if (x + y) % 2 or x + y > 2 * a:
                continue
            for z in range(2 * min(b, c) + 1):
                if (x + z) % 2 or (y + z) % 2:
                    continue
                if x + z > 2 * b or y + z > 2 * c:
                    continue
                if sum(t > 0 for t in (x, y, z)) < 2:
                    continue
                yield (a - (x + y) // 2,
                       b - (x + z) // 2,
                       c - (y + z) // 2, x, y, z)


def raw_count(a, b, c):
    """Coefficient of (1+tuv)/((1-t)(1-u)(1-v)(1-tu)(1-tv)(1-uv))."""
    total = 0
    for parity in (0, 1):
        for i in range(max(0, a - parity + 1)):
            for j in range(max(0, a - parity - i + 1)):
                for k in range(max(0, min(b - parity - i, c - parity - j) + 1)):
                    if i + j + parity <= a and i + k + parity <= b and j + k + parity <= c:
                        total += 1
    return total


def count_formula(a, b, c):
    if min(a, b, c) <= 0:
        raise ValueError('all three counts must be positive')
    return raw_count(a, b, c) - 1 - min(a, b) - min(a, c) - min(b, c)


def E(t):
    if t < 0:
        return 0
    return (sum((s + 2) * (s + 1) // 2 for s in range(t + 1))
            + sum((t - 2 * h + 2) * (t - 2 * h + 1) // 2
                  for h in range(1, t // 2 + 1)))


def balanced_formula(m):
    return m * (m * m + 3 * m - 2) // 2


def euler_witness(p):
    """Generate actual cyclic word from an undirected Eulerian multigraph."""
    edges = []
    for u, v, number in ((0, 0, p[0]), (1, 1, p[1]), (2, 2, p[2]),
                         (0, 1, p[3]), (0, 2, p[4]), (1, 2, p[5])):
        edges.extend((u, v) for _ in range(number))
    adj = [[] for _ in range(3)]
    for eid, (u, v) in enumerate(edges):
        adj[u].append(eid)
        adj[v].append(eid)
    used = [False] * len(edges)
    pos = [0] * 3
    stack, circuit = [0], []
    while stack:
        u = stack[-1]
        while pos[u] < len(adj[u]) and used[adj[u][pos[u]]]:
            pos[u] += 1
        if pos[u] == len(adj[u]):
            circuit.append(stack.pop())
        else:
            eid = adj[u][pos[u]]
            used[eid] = True
            a, b = edges[eid]
            stack.append(b if a == u else a)
    assert all(used) and len(circuit) == len(edges) + 1
    assert circuit[0] == circuit[-1]
    word = tuple(circuit[:-1])
    assert word_profile(word) == p
    return word


def run():
    checks = 0
    for n in range(3, 12):
        observed = defaultdict(set)
        for word in product((0, 1, 2), repeat=n):
            counts = (word.count(0), word.count(1), word.count(2))
            if min(counts) > 0:
                observed[counts].add(word_profile(word))
        for a in range(1, n - 1):
            for b in range(1, n - a):
                c = n - a - b
                expected = set(candidate_profiles((a, b, c)))
                assert observed[(a, b, c)] == expected, (a, b, c)
                assert len(expected) == count_formula(a, b, c), (a, b, c)
                checks += 1
        print('brute length', n, 'composition classes', len(observed))
    witness_count = 0
    for a in range(1, 6):
        for b in range(1, 6):
            for c in range(1, 6):
                predicted = set(candidate_profiles((a, b, c)))
                assert len(predicted) == count_formula(a, b, c)
                for p in predicted:
                    w = euler_witness(p)
                    assert tuple(w.count(i) for i in (0, 1, 2)) == (a, b, c)
                    witness_count += 1
    for m in range(1, 151):
        assert E(m) + E(m - 1) - 3 * m - 1 == balanced_formula(m)
        assert count_formula(m, m, m) == balanced_formula(m)
    print('PASS: direct exhaustive words length 3..11; compositions', checks)
    print('PASS: Eulerian witnesses', witness_count)
    print('PASS: balanced formula m=1..150')

if __name__ == '__main__':
    run()
