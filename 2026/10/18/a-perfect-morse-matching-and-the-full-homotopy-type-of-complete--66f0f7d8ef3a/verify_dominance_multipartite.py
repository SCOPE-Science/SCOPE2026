#!/usr/bin/env python3
"""Exact finite checks for complete-multipartite dominance complexes.

Requires only Python's standard library. The mathematical theorem for arbitrary
part sizes is established by the relative-cell proof, not by these tests.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

CASES = ((2,2), (2,3), (3,3), (2,2,2), (3,3,3),
         (2,3,4), (2,2,2,2), (2,2,3,3), (4,4))


def construct(ms):
    assert len(ms) >= 2 and min(ms) >= 2
    parts, vertices = [], 0
    for m in ms:
        parts.append(tuple(range(vertices, vertices+m)))
        vertices += m
    full = (1 << vertices) - 1
    pmasks = [sum(1 << v for v in part) for part in parts]

    def dominates(rem):
        return sum(bool(rem & p) for p in pmasks) >= 2 or rem in pmasks

    faces = {s for s in range(1 << vertices) if dominates(full ^ s)}
    assert 0 in faces
    v = parts[0][0]
    bit = 1 << v
    link = {s for s in faces if not s & bit and (s | bit) in faces}
    relative = {s for s in faces if not s & bit and (s | bit) not in faces}
    assert len(faces) == 2 * len(link) + len(relative)

    B0 = full ^ pmasks[0]
    predicted_relative = {B0}
    for j in range(1, len(parts)):
        B = full ^ (pmasks[j] | bit)
        for t in range(1, (1 << len(parts[j]))-1):
            mask = sum(1 << parts[j][p] for p in range(len(parts[j])) if t & (1 << p))
            predicted_relative.add(B | mask)
    assert relative == predicted_relative, (ms, relative ^ predicted_relative)

    match = {s: s | bit for s in link}
    for j in range(1, len(parts)):
        B = full ^ (pmasks[j] | bit)
        w = 1 << parts[j][0]
        proper = (1 << len(parts[j]))-1
        for t in range(1, proper):
            mask = sum(1 << parts[j][p] for p in range(len(parts[j])) if t & (1 << p))
            low = B | mask
            high = low | w
            if (mask & w) == 0 and high in relative:
                assert low in relative
                assert low not in match
                match[low] = high

    matched = set(match) | set(match.values())
    assert len(matched) == 2 * len(match)
    assert matched <= faces
    critical = faces - matched
    actual = Counter(s.bit_count()-1 for s in critical)
    N = vertices
    expected = Counter({N-3: len(ms)-1})
    for m in ms:
        expected[N-m-1] += 1
    assert actual == expected, (ms, actual, expected)
    assert all((s ^ t).bit_count() == 1 and t.bit_count() == s.bit_count()+1
               for s,t in match.items())

    indegree = {s: 0 for s in faces}
    directed = defaultdict(list)
    for s in faces:
        for b in range(vertices):
            if not s & (1 << b):
                continue
            t = s ^ (1 << b)
            assert t in faces
            if match.get(t) == s:
                a, z = t, s
            else:
                a, z = s, t
            indegree[z] += 1
            directed[a].append(z)
    queue = deque(x for x in faces if not indegree[x])
    visited = 0
    while queue:
        s = queue.popleft()
        visited += 1
        for t in directed[s]:
            indegree[t] -= 1
            if indegree[t] == 0:
                queue.append(t)
    assert visited == len(faces), (ms, visited, len(faces))

    # Independent reduced F_2 simplicial boundary ranks.
    bysize = defaultdict(list)
    for s in faces:
        bysize[s.bit_count()].append(s)
    ranks = {}
    for d in range(1, vertices + 1):
        if not bysize.get(d):
            continue
        lowers = {s:i for i,s in enumerate(bysize[d-1])}
        pivots = {}
        for s in bysize[d]:
            column = 0
            for b in range(vertices):
                if s & (1 << b):
                    column ^= 1 << lowers[s ^ (1 << b)]
            while column:
                idx = column.bit_length()-1
                if idx in pivots:
                    column ^= pivots[idx]
                else:
                    pivots[idx] = column
                    break
        ranks[d] = len(pivots)
    beta = Counter({d-1:len(fs)-ranks.get(d, 0)-ranks.get(d+1, 0)
                    for d,fs in bysize.items() if d})
    beta[0] -= 1  # reduce H_0 over F_2
    beta = +beta
    assert beta == expected, (ms, beta, expected)
    print(f'{ms}: {len(faces)} faces; {len(match)} matched pairs; '
          f'{len(critical)} critical cells; reduced mod-2 homology {dict(beta)}; acyclic')


def main():
    for ms in CASES:
        construct(ms)
    print(f'All {len(CASES)} finite test cases passed.')

if __name__ == '__main__':
    main()
