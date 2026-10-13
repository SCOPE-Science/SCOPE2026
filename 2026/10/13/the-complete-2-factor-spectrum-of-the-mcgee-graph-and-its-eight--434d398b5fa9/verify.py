#!/usr/bin/env python3
"""Exhaustive finite verification of 2-factors of the 24-vertex McGee graph.

Run from this directory: python3 verify.py
Requires only the Python standard library.
"""
from collections import Counter, deque
from functools import lru_cache
import csv
from pathlib import Path

N = 24
SHIFTS = (-12, 7, -7)
EDGES = tuple(sorted(
    {tuple(sorted((i, (i + 1) % N))) for i in range(N)} |
    {tuple(sorted((i, (i + SHIFTS[i % 3]) % N))) for i in range(N)}
))
ADJ = tuple(tuple(sorted(w for a, b in EDGES for w in ((b,) if a == v else ((a,) if b == v else ())))) for v in range(N))
FULL = (1 << N) - 1
assert len(EDGES) == 36 and all(len(row) == 3 for row in ADJ)
assert all(v in ADJ[w] for v in range(N) for w in ADJ[v])


def bfs(root):
    d = [-1] * N
    d[root] = 0
    q = deque([root])
    while q:
        v = q.popleft()
        for w in ADJ[v]:
            if d[w] == -1:
                d[w] = d[v] + 1
                q.append(w)
    return tuple(d)

DIST = tuple(bfs(v) for v in range(N))
assert all(-1 not in row for row in DIST)
assert max(max(row) for row in DIST) == 4
# A girth test independent of the matching enumeration.
def girth():
    ans = N + 1
    for start in range(N):
        d = [-1] * N
        par = [-1] * N
        d[start] = 0
        q = deque([start])
        while q:
            v = q.popleft()
            for w in ADJ[v]:
                if d[w] < 0:
                    d[w], par[w] = d[v] + 1, v
                    q.append(w)
                elif par[v] != w:
                    ans = min(ans, d[v] + d[w] + 1)
    return ans
assert girth() == 7


def enumerate_matchings():
    out = []
    def visit(used, edges):
        if used == FULL:
            out.append(tuple(sorted(edges)))
            return
        rest = FULL ^ used
        v = (rest & -rest).bit_length() - 1
        for w in ADJ[v]:
            if not (used & (1 << w)):
                visit(used | (1 << v) | (1 << w), edges + [(min(v, w), max(v, w))])
    visit(0, [])
    return tuple(sorted(out))

MATCHINGS = enumerate_matchings()
assert len(MATCHINGS) == len(set(MATCHINGS)) == 60
assert all(len(m) == 12 and {x for e in m for x in e} == set(range(N)) for m in MATCHINGS)

# Independent memoized matching-number recurrence over unmatched masks.
@lru_cache(None)
def count_perfect(mask):
    if mask == 0:
        return 1
    v = (mask & -mask).bit_length() - 1
    return sum(count_perfect(mask ^ (1 << v) ^ (1 << w))
               for w in ADJ[v] if mask & (1 << w))
assert count_perfect(FULL) == len(MATCHINGS)


def cycle_profile(m):
    matching = frozenset(m)
    remaining = set(range(N))
    comp_adj = [[w for w in ADJ[v] if (min(v, w), max(v, w)) not in matching]
                for v in range(N)]
    assert all(len(row) == 2 for row in comp_adj)
    lengths = []
    while remaining:
        root = min(remaining)
        prev, v, k = -1, root, 0
        while v in remaining:
            remaining.remove(v)
            k += 1
            a, b = comp_adj[v]
            nxt = a if a != prev else b
            prev, v = v, nxt
        assert v == root
        lengths.append(k)
    return tuple(sorted(lengths))

PROFILES = {m: cycle_profile(m) for m in MATCHINGS}
CYCLE_COUNTS = Counter(PROFILES.values())
assert CYCLE_COUNTS == {(24,): 42, (8, 8, 8): 12, (12, 12): 6}

# All graph automorphisms: a permutation of V is an automorphism exactly when
# it preserves shortest-path distances between every pair of vertices.
# The search is complete: at each node every remaining image respecting
# all already assigned distances is tried, and impossible partial maps prune.
def automorphisms():
    p = [-1] * N
    used = [False] * N
    out = []
    def visit(k):
        if k == N:
            out.append(tuple(p))
            return
        best_v, best_images = None, None
        known = [(u, p[u]) for u in range(N) if p[u] >= 0]
        for v in range(N):
            if p[v] >= 0:
                continue
            images = [w for w in range(N) if not used[w]
                      and all(DIST[v][u] == DIST[w][im] for u, im in known)]
            if not images:
                return
            if best_images is None or len(images) < len(best_images):
                best_v, best_images = v, images
            if len(best_images) == 1:
                break
        for image in best_images:
            p[best_v] = image
            used[image] = True
            visit(k + 1)
            used[image] = False
            p[best_v] = -1
    visit(0)
    return tuple(sorted(out))

AUT = automorphisms()
assert len(AUT) == len(set(AUT)) == 32
assert all(set(p) == set(range(N)) for p in AUT)
assert all({tuple(sorted((p[a], p[b]))) for a, b in EDGES} == set(EDGES) for p in AUT)


def under(m, p):
    return tuple(sorted(tuple(sorted((p[a], p[b]))) for a, b in m))

not_seen = set(MATCHINGS)
ORBITS = []
while not_seen:
    rep = min(not_seen)
    orbit = {under(rep, p) for p in AUT}
    assert orbit <= not_seen
    assert len({PROFILES[t] for t in orbit}) == 1
    not_seen -= orbit
    ORBITS.append((PROFILES[rep], len(orbit), rep))
ORBITS.sort(key=lambda x: (x[0], x[1], x[2]))
assert len(ORBITS) == 8
ORBIT_COUNTS = Counter((p, k) for p, k, _ in ORBITS)
assert ORBIT_COUNTS == {((8, 8, 8), 4): 1, ((8, 8, 8), 8): 1,
                        ((12, 12), 2): 1, ((12, 12), 4): 1,
                        ((24,), 2): 1, ((24,), 8): 1, ((24,), 16): 2}
assert sum(k for _, k, _ in ORBITS) == len(MATCHINGS)


def encode(m):
    return ';'.join('%02d-%02d' % (v, w) for v, w in m)

# Embedded witness tables are independently checked, not used by the search.
here = Path(__file__).resolve().parent
with (here / 'orbits.csv').open(newline='', encoding='utf-8') as fh:
    listed = list(csv.DictReader(fh))
assert len(listed) == len(ORBITS)
assert [(x['cycle_type'], int(x['orbit_size']), x['matching_edges']) for x in listed] == [
    ('+'.join(map(str, p)), k, encode(m)) for p, k, m in ORBITS]
with (here / 'matchings.csv').open(newline='', encoding='utf-8') as fh:
    listed_match = list(csv.DictReader(fh))
assert len(listed_match) == len(MATCHINGS)
assert [(x['matching_edges'], x['cycle_type']) for x in listed_match] == [
    (encode(m), '+'.join(map(str, PROFILES[m]))) for m in MATCHINGS]

print('VERIFY_OK McGee LCF=[-12,7,-7]^8 vertices=24 edges=36 girth=7 diameter=4')
print('VERIFY_OK independent_matching_dp=60 recursive_matchings=60')
print('VERIFY_OK two_factor_types=8+8+8:12,12+12:6,24:42')
print('VERIFY_OK automorphisms=32 perfect_matching_orbits=8 orbit_distribution=2x1+4x2+8x2+16x2')
print('VERIFY_OK orbits.csv=exact matchings.csv=exact')
