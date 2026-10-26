#!/usr/bin/env python3
"""Independent finite check: build crown matchings as partial injections and slide edges.

Does not enumerate permutations as its states; only uses a marked-cycle profile
of the completed matching to reduce the exhaustive BFS starting points.
Usage: python verify_matchings.py
"""
from collections import Counter, deque
from itertools import permutations
import json


def matchings(n):
    for vacant_row in range(n):
        used_rows = [i for i in range(n) if i != vacant_row]
        for columns in permutations(range(n), n - 1):
            if all(i != c for i, c in zip(used_rows, columns)):
                p = [-1] * n
                for i, c in zip(used_rows, columns):
                    p[i] = c
                yield tuple(p)


def orbit_profile(m):
    n = len(m)
    used_cols = {v for v in m if v != -1}
    missing_col = next(i for i in range(n) if i not in used_cols)
    f = [missing_col + 1] + [0 if m[i] == -1 else m[i] + 1 for i in range(n)]
    seen = [False] * (n + 1)
    special = None
    other = []
    for start in range(n + 1):
        if seen[start]:
            continue
        cur = start
        count = 0
        contains_zero = False
        while not seen[cur]:
            seen[cur] = True
            contains_zero |= cur == 0
            cur = f[cur]
            count += 1
        if contains_zero:
            special = count
        else:
            other.append(count)
    return special, tuple(sorted(other))


def slide_neighbors(m):
    n = len(m)
    missing_row = m.index(-1)
    used = set(m)
    missing_col = next(i for i in range(n) if i not in used)
    for i, j in enumerate(m):
        if j == -1:
            continue
        if missing_row != j:
            q = list(m)
            q[i], q[missing_row] = -1, j
            yield tuple(q)
        if i != missing_col:
            q = list(m)
            q[i] = missing_col
            yield tuple(q)


def eccentricity_spheres(graph, source):
    depth = {source: 0}
    queue = deque([source])
    spheres = Counter()
    while queue:
        x = queue.popleft()
        spheres[depth[x]] += 1
        for y in graph[x]:
            if y not in depth:
                depth[y] = depth[x] + 1
                queue.append(y)
    assert len(depth) == len(graph)
    return [spheres[j] for j in range(max(spheres)+1)]


def verify(n):
    M = list(matchings(n))
    assert len(M) == len(set(M))
    Mset = set(M)
    G = {m: set(slide_neighbors(m)) for m in M}
    assert all(set(adj).issubset(Mset) for adj in G.values())
    assert all(m in G[v] for m,adj in G.items() for v in adj)
    marked_orbits = {}
    for m in M:
        marked_orbits.setdefault(orbit_profile(m), []).append(m)
    all_pairs = Counter()
    ecc = Counter()
    orbits = []
    for profile, members in sorted(marked_orbits.items()):
        spheres = eccentricity_spheres(G, members[0])
        for d, count in enumerate(spheres):
            all_pairs[d] += len(members) * count
        ecc[len(spheres)-1] += len(members)
        orbits.append(dict(marked_cycle=profile[0], other_cycles=list(profile[1]),
                           orbit_size=len(members),eccentricity=len(spheres)-1,
                           spheres=spheres))
    assert all(all_pairs[d]%2==0 for d in range(1,max(all_pairs)+1))
    return dict(n=n,vertices=len(M),edges=sum(len(v) for v in G.values())//2,
                orbit_count=len(orbits),degree_histogram=dict(sorted(Counter(map(len,G.values())).items())),
                radius=min(ecc),diameter=max(ecc),
                eccentricity_histogram=dict(sorted(ecc.items())),
                unordered_pair_distances=[all_pairs[d]//2 for d in range(1,max(all_pairs)+1)],
                orbit_data=orbits)

if __name__ == '__main__':
    for n in range(3,9):
        print(json.dumps(verify(n),sort_keys=True,separators=(',',':')))
