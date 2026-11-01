#!/usr/bin/env python3
"""Independent exact finite cross-check of the closed-form Kneser family theorem."""
from collections import Counter, deque
from itertools import combinations
from math import comb


def test(n):
    edges = tuple(combinations(range(n), 2))
    number = len(edges)
    index = {edge: pos for pos, edge in enumerate(edges)}
    faces = {0}
    for four_set in combinations(range(n), 4):
        ids = [index[edge] for edge in combinations(four_set, 2)]
        for bits in range(64):
            faces.add(sum(1 << ids[j] for j in range(6) if bits & (1 << j)))
    for center in range(n):
        ids = [index[tuple(sorted((center, j)))] for j in range(n) if j != center]
        for bits in range(1 << (n - 1)):
            faces.add(sum(1 << ids[j] for j in range(n - 1) if bits & (1 << j)))
    ordered = sorted(faces)
    unmatched = set(faces)
    pairs = []
    for v in range(number):
        bit = 1 << v
        for lower in ordered:
            if lower in unmatched and not lower & bit and lower | bit in unmatched:
                unmatched.remove(lower)
                unmatched.remove(lower | bit)
                pairs.append((lower, lower | bit))
    predicted = set()
    for a, b, c, d in combinations(range(1, n), 4):
        predicted.add(sum(1 << index[t] for t in ((a, b), (b, c), (b, d), (c, d))))
    assert unmatched == predicted, (n, len(unmatched), len(predicted))
    nonempty = set(faces) - {0}
    matching = set(p for p in pairs if p[0] != 0)
    critical = nonempty - {f for pair in matching for f in pair}
    assert Counter(s.bit_count()-1 for s in critical) == ({0: 1, 3: comb(n-1, 4)} if n >= 5 else {0: 1})
    adjacency = {f: [] for f in nonempty}
    indegree = {f: 0 for f in nonempty}
    covers = 0
    for higher in ordered[1:]:
        for v in range(number):
            if not higher & (1 << v) or higher == 1 << v:
                continue
            lower = higher ^ (1 << v)
            covers += 1
            origin, target = (lower, higher) if (lower, higher) in matching else (higher, lower)
            adjacency[origin].append(target)
            indegree[target] += 1
    queue = deque(f for f in nonempty if indegree[f] == 0)
    explored = 0
    while queue:
        f = queue.popleft()
        explored += 1
        for g in adjacency[f]:
            indegree[g] -= 1
            if indegree[g] == 0:
                queue.append(g)
    assert explored == len(nonempty)
    return len(faces)-1, covers, len(matching), comb(n-1, 4)


for size in range(4, 10):
    f, c, pairs, spheres = test(size)
    print(f'underlying_symbols={size} nonempty_faces={f} covers={c} matched_pairs={pairs} spheres={spheres}')
print('ALL_FAMILY_CHECKS_PASS')
