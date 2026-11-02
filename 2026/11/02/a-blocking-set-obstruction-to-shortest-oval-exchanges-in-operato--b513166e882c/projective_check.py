"""Exact finite certificate: one-point exchanges among 4-arcs of PG(2,3).
Uses homogeneous ternary coordinates, 3x3 determinants and all-pairs BFS.
Run: python3 projective_check.py (Python standard library only).
"""
from itertools import combinations, product
from collections import Counter, deque

P = 3

def normalized(v):
    s = next(x for x in v if x)
    inv = 1 if s == 1 else 2
    return tuple((inv*x) % P for x in v)

points = sorted({normalized(v) for v in product(range(P), repeat=3) if any(v)})
assert len(points) == 13

def determinant(a, b, c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0])) % 3

lines = [frozenset(i for i,p in enumerate(points)
                   if sum(x*y for x,y in zip(v,p)) % 3 == 0)
         for v in points]
assert len(set(lines)) == 13 and all(len(l)==4 for l in lines)
assert all(sum({a,b} <= line for line in lines) == 1
           for a,b in combinations(range(13),2))

arcs = [frozenset(s) for s in combinations(range(13),4)
        if all(determinant(*(points[i] for i in tri)) != 0
               for tri in combinations(s,3))]
assert len(arcs) == 234
adj = [set() for _ in arcs]
for i,a in enumerate(arcs):
    for j in range(i):
        if len(a & arcs[j]) == 3:
            adj[i].add(j)
            adj[j].add(i)
assert all(len(nb) == 12 for nb in adj)
assert sum(map(len, adj)) // 2 == 1404

def bfs(start):
    d = [-1]*len(arcs)
    d[start] = 0
    Q = deque([start])
    while Q:
        i = Q.popleft()
        for j in adj[i]:
            if d[j] == -1:
                d[j] = d[i]+1
                Q.append(j)
    assert -1 not in d
    return d

joint = Counter()
for i,a in enumerate(arcs):
    dist = bfs(i)
    assert Counter(dist) == {0:1, 1:12, 2:60, 3:114, 4:47}
    for j,b in enumerate(arcs):
        if j >= i:
            continue
        k = len(a & b)
        excess = dist[j]-(4-k)
        assert excess in (0,1)
        nontrivial_block = all(bool((a|b)&line) for line in lines) and \
                           all(not line <= (a|b) for line in lines)
        assert (excess == 1) == nontrivial_block
        joint[k,dist[j]] += 1
    pair_defects = Counter()
    point_defects = Counter()
    for j,b in enumerate(arcs):
        if i == j: continue
        k = len(a & b)
        if k == 2 and dist[j] == 3:
            pair_defects[tuple(sorted(a & b))] += 1
        if k == 1 and dist[j] == 4:
            point_defects[next(iter(a & b))] += 1
    assert len(pair_defects) == 6 and all(n==1 for n in pair_defects.values())
    assert len(point_defects) == 4 and all(n==2 for n in point_defects.values())

assert joint == {
  (3,1):1404, (2,2):7020, (2,3):702,
  (1,3):12636, (1,4):936, (0,4):4563
}
print('PROJECTIVE_DETERMINANT_ALL_PAIRS_PASS')
print('arcs=234 edges=1404 diameter=4 degree=12')
print('per_arc_distances=(1,12,60,114,47)')
print('joint_intersection_distance=', sorted(joint.items()))
print('nontrivial_blocking_exactly_matches_extra_exchange')
print('six_one_per_common_pair_eight_two_per_common_point')
