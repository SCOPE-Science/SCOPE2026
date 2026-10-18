"""Exact two-coloring flip geometry of PG(2,3); Python 3 standard library only."""
from itertools import product, combinations
from collections import Counter, deque
from hashlib import sha256

F = range(3)

def normalized(v):
    a = next(x for x in v if x)
    scale = {1: 1, 2: 2}[a]
    return tuple(scale*x % 3 for x in v)

points = sorted({normalized(v) for v in product(F, repeat=3) if any(v)})
forms = sorted({normalized(v) for v in product(F, repeat=3) if any(v)})
assert len(points) == len(forms) == 13

# Construction I: homogeneous coordinates and the dot-product incidence test.
inc1 = tuple(sorted(sum(1 << i for i, p in enumerate(points)
                        if sum(p[j]*u[j] for j in range(3)) % 3 == 0)
                    for u in forms))

# Construction II: nine affine points, four ideal points, twelve affine lines
# (three lines in each of four parallel classes), and the ideal line.
aff = [(x, y, 1) for x in F for y in F]
ideal = [(1, m, 0) for m in F] + [(0, 1, 0)]
point_index = {p:i for i,p in enumerate(points)}
mask = lambda vs: sum(1 << point_index[normalized(v)] for v in vs)
inc2 = []
for m in F:
    for b in F:
        inc2.append(mask([(x,(m*x+b)%3,1) for x in F] + [(1,m,0)]))
for a in F:
    inc2.append(mask([(a,y,1) for y in F] + [(0,1,0)]))
inc2.append(mask(ideal))
assert tuple(sorted(inc2)) == inc1
lines = inc1
universe = (1 << 13) - 1
assert all(L.bit_count() == 4 for L in lines)
assert all(sum((L >> p)&1 for L in lines) == 4 for p in range(13))
assert all(sum(bool((L>>i)&1 and (L>>j)&1) for L in lines) == 1
           for i in range(13) for j in range(i+1,13))

# Exhaustively check the no-monochromatic-line constraint in two equivalent ways.
valid1 = {s for s in range(1 << 13)
          if all(0 < (s&L).bit_count() < 4 for L in lines)}
valid2 = {s for s in range(1 << 13)
          if all((s & L) != 0 and ((universe ^ s) & L) != 0 for L in inc2)}
assert valid1 == valid2
assert len(valid1) == 468
assert Counter(s.bit_count() for s in valid1) == Counter({6:234, 7:234})

# Independently construct all vertexless-triangle six-point configurations.
triangles = set()
for a,b,c in combinations(lines,3):
    corners = (a&b)|(b&c)|(c&a)
    if corners.bit_count() != 3:  # the three lines are concurrent
        continue
    off_corners = (a|b|c) & ~corners
    assert off_corners.bit_count() == 6
    triangles.add(off_corners)
assert len(triangles) == 234
assert triangles == {s for s in valid1 if s.bit_count() == 6}

# Construction A: independently flip each of the thirteen coordinates.
vertices = sorted(valid1)
loc = {s:i for i,s in enumerate(vertices)}
adj = [tuple(sorted(loc[t] for p in range(13) if (t := s^(1<<p)) in valid1))
       for s in vertices]
# Construction B: take all pairs of valid words and select distance-one pairs.
adj2 = [tuple(j for j,t in enumerate(vertices) if (s^t).bit_count() == 1)
        for s in vertices]
assert adj == adj2
assert Counter(map(len,adj)) == Counter({3:468})
assert sum(map(len,adj))//2 == 702

# Exhaustive all-source shortest paths. BFS is exact for unit-length graphs.
by_distance = Counter()
by_penalty = Counter()
ecc = []
per_source_penalty = set()
for source, s in enumerate(vertices):
    distances = [-1]*len(vertices)
    distances[source] = 0
    queue = deque([source])
    while queue:
        v=queue.popleft()
        for w in adj[v]:
            if distances[w] == -1:
                distances[w] = distances[v]+1
                queue.append(w)
    assert min(distances) == 0  # checks that every vertex was reached
    assert all(d >= 0 for d in distances)
    ecc.append(max(distances))
    penalties = Counter()
    for target,t in enumerate(vertices):
        d = distances[target]
        h = (s^t).bit_count()
        assert d >= h and (d-h) % 2 == 0
        assert d-h in (0,2)
        by_distance[d] += 1
        by_penalty[d-h] += 1
        penalties[d-h] += 1
    per_source_penalty.add((penalties[0], penalties[2]))
assert min(ecc) == max(ecc) == 13
assert per_source_penalty == {(356,112)}
assert by_penalty == Counter({0:166608,2:52416})
assert sum(by_distance.values()) == len(vertices)**2
assert sum(by_distance[k] for k in range(14)) == 468**2
assert len(vertices)*(len(vertices)-1)//2 == 109278
assert 52416//2 == 26208

# Derive the line intersection spectrum for all six-point color classes.
spectra = {tuple(sum((s&L).bit_count() == k for L in lines) for k in (1,2,3))
           for s in triangles}
assert spectra == {(6,3,4)}

# Diagnostic symmetry: all 468 vertices have the same distance-shell profile.
profile_set = set()
for i,s in enumerate(vertices):
    distances = {i:0}; Q=deque([i])
    while Q:
        x = Q.popleft()
        for y in adj[x]:
            if y not in distances:
                distances[y] = distances[x]+1
                Q.append(y)
    profile_set.add(tuple(Counter(distances.values())[k] for k in range(14)))
assert len(profile_set) == 1
shells = next(iter(profile_set))
print('points=13 lines=13',flush=True)
print('colorings=468; six/seven=234/234; vertexless_triangles=234')
print('flip_graph_vertices=468 edges=702 regular_degree=3 connected=yes')
print('radius=13 diameter=13')
print('all_ordered_pairs=219024 hamming_geodesic=166608 detour_two=52416')
print('all_unordered_distinct_pairs=109278 geodesic=83070 detour_two=26208')
print('detour_two_per_coloring=112')
print('distance_shells=' + repr(shells))
print('exact_full_enumeration=PASS')
