#!/usr/bin/env python3
"""Independent geometric graph and simplicial mod-2 chain computation.

The 24 vertex coordinates are permutations of (±1,±(1+sqrt(2)),
±(1+sqrt(2))) with consistent cube-corner signs. Algebra in
Z[sqrt(2)] decides unit-edge adjacency without floating point.
"""
from collections import Counter

N = 24

def coord(b, axis):
    signs = [1 if not (b >> i) & 1 else -1 for i in range(3)]
    return tuple((signs[i], 0 if i == axis else signs[i]) for i in range(3))

def dist2(a, b):
    rational = radical = 0
    for (x, y), (z, w) in zip(a, b):
        u, v = x-z, y-w
        rational += u*u+2*v*v
        radical += 2*u*v
    return rational, radical

points = [coord(b, axis) for b in range(8) for axis in range(3)]
assert len(set(points)) == 24
edge_pairs = [(i, j) for i in range(N) for j in range(i+1, N)
              if dist2(points[i], points[j]) == (4, 0)]
assert len(edge_pairs) == 36
adj = [0]*N
for i, j in edge_pairs:
    adj[i] |= 1 << j
    adj[j] |= 1 << i
assert all(mask.bit_count() == 3 for mask in adj)
# Different enumeration: double an already-built face set along each
# new vertex rather than recursively extending it by a next index.
faces = [0]
for i in range(N):
    bit = 1 << i
    extra = [s | bit for s in faces if not (s & adj[i])]
    faces.extend(extra)
assert len(faces) == 26441
levels = [[] for _ in range(8)]
for s in faces:
    if s:
        levels[s.bit_count()-1].append(s)
assert [len(row) for row in levels] == [24,240,1296,4092,7632,8056,4272,828]

ranks = [0]
for d in range(1, 8):
    index = {s:i for i,s in enumerate(levels[d-1])}
    pivots = {}
    for s in levels[d]:
        x = 0
        remaining = s
        while remaining:
            bit = remaining & -remaining
            remaining ^= bit
            x ^= 1 << index[s ^ bit]
        while x:
            k = x.bit_length()-1
            if k in pivots:
                x ^= pivots[k]
            else:
                pivots[k] = x
                break
    ranks.append(len(pivots))
assert ranks == [0,23,217,1079,3013,4619,3433,828]
# beta_0 is reduced, all others ordinary= reduced.
bettis = [len(levels[0])-ranks[1]-1]
for d in range(1,7):
    bettis.append(len(levels[d])-ranks[d]-ranks[d+1])
bettis.append(len(levels[7])-ranks[7])
assert bettis == [0,0,0,0,0,4,11,0]
print('PASS: geometric edges=',len(edge_pairs),'nonempty faces=',len(faces)-1)
print('PASS: simplicial boundary ranks mod 2=',ranks[1:])
print('PASS: reduced Betti ranks mod 2=',bettis)
