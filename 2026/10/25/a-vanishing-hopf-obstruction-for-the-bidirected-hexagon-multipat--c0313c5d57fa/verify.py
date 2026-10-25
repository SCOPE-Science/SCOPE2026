#!/usr/bin/env python3
"""Standalone integral combinatorial and cup-square verifier for X(BP_5)."""
import json
from pathlib import Path
from collections import Counter, deque

N = 6
ARCS = [(i, (i + 1) % N) for i in range(N)] + [((i + 1) % N, i) for i in range(N)]
FACET_CARDINALITIES = (12, 48, 76, 48, 12)
CO_SUPPORT = (11, 13, 21, 22, 26, 37, 38, 42)
CYCLE_TERMS = {21: -1, 84: 1, 273: -1, 336: -1,
               1029: 1, 1092: 1, 1281: -1, 1344: 1}


def vertices(mask):
    return [i for i in range(len(ARCS)) if mask & (1 << i)]


def boundary(mask):
    return [(mask ^ (1 << v), (-1) ** i)
            for i, v in enumerate(vertices(mask))]


def all_faces():
    ans = []
    for mask in range(1, 1 << len(ARCS)):
        if mask.bit_count() > N - 1:
            continue
        src = {}
        tgt = {}
        okay = True
        for index in vertices(mask):
            u, v = ARCS[index]
            if u in src or v in tgt:
                okay = False
                break
            src[u] = v
            tgt[v] = u
        if not okay:
            continue
        for start in range(N):
            seen = set()
            x = start
            while x in src and x not in seen:
                seen.add(x)
                x = src[x]
            if x in seen:
                okay = False
                break
        if okay:
            ans.append(mask)
    return sorted(ans)


def verify():
    cert = json.loads(Path(__file__).with_name('BP5_MATCHING.json').read_text(encoding='utf8'))
    assert cert['n'] == 5 and [tuple(a) for a in cert['arcs']] == ARCS
    faces = all_faces()
    F = set(faces)
    assert len(F) == 196
    assert tuple(sum(mask.bit_count() == k for mask in faces) for k in range(1, 6)) == FACET_CARDINALITIES

    pairs = [tuple(p) for p in cert['pairs']]
    crit = cert['critical']
    assert len(pairs) == 96 and len(crit) == 4
    assert Counter(x.bit_count() - 1 for x in crit) == {0: 1, 2: 1, 4: 2}
    used = set(crit)
    for small, large in pairs:
        assert small in F and large in F and large.bit_count() == small.bit_count() + 1
        assert (small & large) == small
        assert small not in used and large not in used
        used.update([small, large])
    assert used == F

    # Orient every Hasse edge downward except matched edges, oriented upward.
    pairset = set(pairs)
    adjacency = {x: [] for x in F}
    indegree = {x: 0 for x in F}
    for large in faces:
        for small, _ in boundary(large):
            if not small:  # No empty-face pairing in this unaugmented matching.
                continue
            if (small, large) in pairset:
                u, v = small, large
            else:
                u, v = large, small
            adjacency[u].append(v)
            indegree[v] += 1
    q = deque(x for x in F if indegree[x] == 0)
    visited = 0
    while q:
        x = q.popleft()
        visited += 1
        for y in adjacency[x]:
            indegree[y] -= 1
            if indegree[y] == 0:
                q.append(y)
    assert visited == len(F), 'Gradient cycle detected'

    # Integral two-cocycle: the coboundary vanishes on every 3-simplex.
    assert set(CO_SUPPORT) <= F
    assert all(x.bit_count() == 3 for x in CO_SUPPORT)
    co = set(CO_SUPPORT)
    for tetra in faces:
        if tetra.bit_count() == 4:
            assert sum(sign for tri, sign in boundary(tetra) if tri in co) == 0

    # An explicit primitive integral 2-cycle pairing once with the cocycle.
    assert set(CYCLE_TERMS) <= F
    assert all(x.bit_count() == 3 for x in CYCLE_TERMS)
    bd = Counter()
    for tri, weight in CYCLE_TERMS.items():
        for edge, sign in boundary(tri):
            bd[edge] += weight * sign
    assert all(x == 0 for x in bd.values())
    assert sum(weight for tri, weight in CYCLE_TERMS.items() if tri in co) == -1

    # The Alexander-Whitney cup square is zero as an integral 4-cochain.
    top = [x for x in faces if x.bit_count() == 5]
    assert len(top) == 12
    for simplex in top:
        vv = vertices(simplex)
        first = sum(1 << a for a in vv[:3])
        last = sum(1 << a for a in vv[2:])
        assert not (first in co and last in co)
    print('VERIFY_OK: f=(12,48,76,48,12), matching=(96 pairs; 0,2,4,4), '
          'integral primitive 2-cocycle, zero integral cup square')


if __name__ == '__main__':
    verify()
