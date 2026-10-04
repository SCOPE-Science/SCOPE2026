#!/usr/bin/env python3
from itertools import product, combinations

P = 5
W = 6

def inv(a):
    return pow(a, P-2, P)

def norm(v):
    v = tuple(x % P for x in v)
    for x in v:
        if x:
            z = inv(x)
            return tuple((z*y) % P for y in v)
    raise ValueError('zero vector')

points = sorted({norm(v) for v in product(range(P), repeat=3) if any(v)})
lines = sorted({norm(v) for v in product(range(P), repeat=3) if any(v)})
assert len(points) == len(lines) == 31
adj = {i: [] for i in range(31)}
for i, l in enumerate(lines):
    for j, p in enumerate(points):
        if sum(a*b for a,b in zip(l,p)) % P == 0:
            adj[i].append(j)
assert all(len(adj[i]) == W for i in adj)
assert all(sum(j in adj[i] for i in adj) == W for j in range(31))
assert all(len(set(adj[i]) & set(adj[k])) == 1 for i,k in combinations(range(31),2))

# Decompose the 6-regular bipartite Levi graph into six perfect matchings.
resid = {i:set(vs) for i,vs in adj.items()}
colors = {}
for color in range(1, W+1):
    mt = {}
    def aug(i, seen):
        for j in sorted(resid[i]):
            if j in seen:
                continue
            seen.add(j)
            if j not in mt or aug(mt[j], seen):
                mt[j] = i
                return True
        return False
    for i in range(31):
        assert aug(i, set())
    assert len(mt) == 31
    for j,i in mt.items():
        colors[(i,j)] = color
        resid[i].remove(j)
assert all(not resid[i] for i in resid)

code = []
for i in range(31):
    row = [0]*31
    for j in adj[i]:
        row[j] = colors[(i,j)]
    assert sorted(x for x in row if x) == list(range(1,W+1))
    code.append(tuple(row))

def hd(a,b):
    return sum(x != y for x,y in zip(a,b))

dists = [hd(code[i], code[j]) for i,j in combinations(range(31),2)]
assert min(dists) == 11
assert max(dists) == 11  # projective plane: every two lines meet
# Reverse direction on the constructed code.
supports = [{j for j,x in enumerate(row) if x} for row in code]
assert all(len(s) == W for s in supports)
assert all(len(supports[i] & supports[k]) == 1 for i,k in combinations(range(31),2))
for j in range(31):
    vals = [code[i][j] for i in range(31) if code[i][j]]
    assert sorted(vals) == list(range(1,W+1))

print('VERIFY_OK points=31 blocks=31 degree=6 edge_colors=6 code_size=31 min_distance=11 max_distance=11')
