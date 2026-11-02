#!/usr/bin/env python3
"""Exhaustive five-symbol, three-row Latin-rectangle Kempe graph certificate.

Run with Python 3.10 or later: python3 verify_primary.py
All labels are 0,1,2,3,4. A state is the concatenation of three rows.
"""
from itertools import permutations
from collections import Counter, deque

N = 5
perms = list(permutations(range(N)))
states = [a+b+c for a in perms for b in perms for c in perms
          if all(len({a[j], b[j], c[j]}) == 3 for j in range(N))]
assert len(states) == 66240
where = {state: i for i, state in enumerate(states)}
assert len(where) == len(states)


def adjacent_states(s):
    """Switch either colour across ONE whole connected bichromatic component."""
    output = set()
    for a in range(N):
        for b in range(a+1, N):
            edges = [(i, j) for i in range(3) for j in range(N)
                     if s[N*i+j] in (a, b)]
            assert len(edges) == 6
            unseen = set(edges)
            while unseen:
                comp = {unseen.pop()}
                queue = list(comp)
                while queue:
                    e = queue.pop()
                    for f in list(unseen):
                        if f[0] == e[0] or f[1] == e[1]:
                            unseen.remove(f)
                            comp.add(f)
                            queue.append(f)
                nxt = list(s)
                for i, j in comp:
                    idx = N*i+j
                    nxt[idx] = a+b-nxt[idx]
                t = tuple(nxt)
                assert t in where
                if t != s:
                    output.add(where[t])
    return output

adj = [adjacent_states(s) for s in states]
assert sum(map(len, adj)) == 1094400
assert all(i in adj[j] for i, nbrs in enumerate(adj) for j in nbrs)
assert Counter(map(len, adj)) == {15: 8640, 16: 14400, 17: 43200}
print('STATE_AND_EDGE_CENSUS_OK 66240 547200 degrees=15:8640,16:14400,17:43200')


def normalize(s):
    """Relabel symbols uniquely so that the first row is (0,1,2,3,4)."""
    p = {s[j]: j for j in range(N)}
    return tuple(p[x] for x in s)


def canonical(s):
    best = s
    for rows in permutations(range(3)):
        reordered = tuple(s[N*i+j] for i in rows for j in range(N))
        for cols in perms:
            t = tuple(reordered[N*i+cols[j]] for i in range(3) for j in range(N))
            best = min(best, normalize(t))
    return best

normalized = [s for s in states if s[:N] == tuple(range(N))]
assert len(normalized) == 552
classes = Counter(canonical(s) for s in normalized)
assert Counter(classes.values()) == {72: 1, 120: 1, 360: 1}
print('SYMMETRY_ORBITS_OK normalized=72,120,360 labeled=8640,14400,43200')

expected = {
    15: (72, [1, 15, 180, 1480, 8302, 27868, 26713, 1675, 6]),
    16: (120, [1, 16, 182, 1472, 8243, 27793, 26899, 1634]),
    17: (360, [1, 17, 191, 1540, 8609, 28689, 25974, 1219]),
}
for rep, count in classes.items():
    source = where[rep]
    distances = [-1] * len(states)
    distances[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if distances[v] == -1:
                distances[v] = distances[u]+1
                queue.append(v)
    assert -1 not in distances
    profile = Counter(distances)
    degree = len(adj[source])
    predicted_count, predicted_profile = expected[degree]
    assert count == predicted_count
    assert [profile[i] for i in range(len(predicted_profile))] == predicted_profile
    assert max(profile) == len(predicted_profile)-1
    print('DISTANCE_PROFILE_OK', 'degree', degree, 'orbit', 120*count,
          'eccentricity', max(profile), 'profile', predicted_profile)
print('FULL_PRIMARY_CERTIFICATE_OK radius=7 diameter=8 components=1')
