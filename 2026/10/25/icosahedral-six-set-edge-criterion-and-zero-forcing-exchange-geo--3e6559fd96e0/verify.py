#!/usr/bin/env python3
"""Exhaustive, self-contained certificate for the icosahedral zero-forcing classification.

Use Python 3.8+ (standard library only): python3 verify.py.
Every subset, automorphism, and exchange shortest path is inspected exhaustively.
"""
from collections import Counter, deque
from itertools import combinations

N = 12
FULL = (1 << N) - 1

# Explicit two-pentagon construction of the ordinary icosahedral graph:
# poles 0,11; upper ring 1..5; lower ring 6..10.
E = set()
def edge(u, v):
    if u == v:
        raise AssertionError("loop")
    E.add((min(u, v), max(u, v)))
for i in range(5):
    a, b = 1+i, 6+i
    edge(0, a)
    edge(11, b)
    edge(a, 1+(i+1)%5)
    edge(b, 6+(i+1)%5)
    edge(a, b)
    edge(a, 6+(i-1)%5)
assert len(E) == 30
adj = [set() for _ in range(N)]
for a,b in E:
    adj[a].add(b); adj[b].add(a)
assert all(len(s)==5 for s in adj)
mask_of_nb = [sum(1 << j for j in adj[i]) for i in range(N)]

# An independently written sequential forcing procedure, working with sets.
def sequential_forcing(initial):
    blue = {i for i in range(N) if initial & (1 << i)}
    while True:
        forced = None
        for i in sorted(blue):
            white_neighbors = adj[i] - blue
            if len(white_neighbors) == 1:
                forced = next(iter(white_neighbors)); break
        if forced is None: return len(blue) == N
        blue.add(forced)

# Bit-mask parallel forcing (all available forces occur per round).
def parallel_forcing(initial):
    current = initial
    rounds = 0
    while True:
        new = 0
        for v in range(N):
            if current & (1 << v):
                white = mask_of_nb[v] & (FULL ^ current)
                if white and (white & (white-1)) == 0:
                    new |= white
        if not new: return current == FULL, rounds
        current |= new
        rounds += 1

success = []
poly = Counter()
propagation = Counter()
for m in range(1 << N):
    p, r = parallel_forcing(m)
    assert p == sequential_forcing(m), ("forcing disagreement", m)
    if p:
        success.append(m)
        poly[m.bit_count()] += 1
        if m.bit_count()==6: propagation[r] += 1
assert dict(poly) == {6:200,7:480,8:450,9:220,10:66,11:12,12:1}
assert dict(propagation) == {2:20,3:180}
minimum = {m for m in success if m.bit_count()==6}
assert len(minimum)==200 and not any(m.bit_count() < 6 for m in success)

# Independently enumerate automorphisms by permutation backtracking.
# The partial map is checked for both adjacency and nonadjacency.
def all_automorphisms():
    maps = {}
    used = set()
    output = []
    def rec():
        if len(maps) == N:
            output.append(tuple(maps[i] for i in range(N)))
            return
        unmapped = [x for x in range(N) if x not in maps]
        x = max(unmapped, key=lambda a: (sum(z in maps for z in adj[a]), -a))
        for y in range(N):
            if y in used: continue
            if all(((x in adj[z]) == (y in adj[maps[z]])) for z in maps):
                maps[x] = y
                used.add(y)
                rec()
                used.remove(y)
                del maps[x]
    rec()
    return output

perms = all_automorphisms()
assert len(perms)==120 and len(set(perms))==120
assert all(all(((u,v) in E) == (tuple(sorted((p[u],p[v]))) in E)
               for u in range(N) for v in range(u+1,N)) for p in perms)

def transform(m, p):
    return sum(1 << p[i] for i in range(N) if m & (1 << i))

# Classify ALL size-six subsets; an orbit and count certificate for the
# edge-count characterization and full symmetry classification.
remaining = {sum(1 << j for j in c) for c in combinations(range(N), 6)}
assert len(remaining)==924
orbits = []
while remaining:
    rep = min(remaining)
    orbit = {transform(rep, p) for p in perms}
    assert rep in orbit and orbit <= remaining
    remaining -= orbit
    e = sum(bool(rep & (1 << u)) and bool(rep & (1 << v)) for u,v in E)
    yes, rounds = parallel_forcing(rep)
    assert all(parallel_forcing(m)[0] == yes for m in orbit)
    assert all(sum(bool(m & (1<<u)) and bool(m & (1<<v)) for u,v in E)==e for m in orbit)
    orbits.append((rep,len(orbit),e,yes,rounds))
expected_orbits = [
    (63,12,10,False,0), (95,60,9,True,3), (111,20,9,True,2),
    (123,120,8,True,3), (126,60,7,False,0), (243,120,7,False,0),
    (245,30,7,False,0), (250,30,6,False,0), (359,60,7,False,1),
    (363,120,6,False,0), (365,20,6,False,0), (371,30,7,False,0),
    (374,120,6,False,0), (498,10,6,False,0), (715,12,5,False,0),
    (723,60,5,False,0), (726,30,6,False,0), (756,10,6,False,0)
]
assert orbits == expected_orbits, ("orbit table disagreement", orbits)
assert sum(sz for _,sz,*_ in orbits)==924
for m in (sum(1 << i for i in c) for c in combinations(range(N),6)):
    e = sum(bool(m & (1 << a)) and bool(m & (1 << b)) for a,b in E)
    assert (m in minimum) == (e in (8,9))

# Build zero-forcing exchange graph using Hamming distance exactly two.
vertices = sorted(minimum)
index = {v:i for i,v in enumerate(vertices)}
nei = [set() for _ in vertices]
for i,m in enumerate(vertices):
    for a in range(N):
        if not m & (1 << a): continue
        for b in range(N):
            if m & (1 << b): continue
            mm = m ^ (1 << a) ^ (1 << b)
            if mm in index: nei[i].add(index[mm])
assert all(i in nei[j] for j in range(len(vertices)) for i in nei[j])
assert sum(map(len, nei)) == 2640
assert sorted(Counter(len(v) for v in nei).items())==[(11,120),(16,60),(18,20)]
# Independent pairwise Hamming-distance check of all graph edges.
assert all((j in nei[i]) == ((vertices[i]^vertices[j]).bit_count()==2)
           for i in range(len(vertices)) for j in range(len(vertices)) if i!=j)

pair_distance = Counter(); eccentricity = Counter()
for i in range(len(vertices)):
    dist={i:0}
    queue=deque([i])
    while queue:
        u=queue.popleft()
        for v in nei[u]:
            if v not in dist:
                dist[v]=dist[u]+1
                queue.append(v)
    assert len(dist)==200
    eccentricity[max(dist.values())]+=1
    for j,d in dist.items():
        if j>i:pair_distance[d]+=1
assert dict(pair_distance)=={1:1320,2:5160,3:6300,4:5010,5:2010,6:100}
assert dict(eccentricity)=={6:200}
assert sum(pair_distance.values())==19900

# All minimum-set orbits have the expected exchange degrees and timing.
assert [(rep,sz,deg) for rep,sz,e,yes,t in orbits if yes for deg in [len(nei[index[rep]])]] == [
    (95,60,16),(111,20,18),(123,120,11)
]
print('VERIFY_OK')
print('icosahedral graph: 12 vertices, 30 edges, |Aut|=120')
print('zero forcing polynomial:',dict(sorted(poly.items())))
print('minimum: 6; minimum sets: 200; propagation:',dict(propagation))
print('six-vertex subset orbits:',len(orbits),'minimum orbits:',[(r,s,e,t) for r,s,e,y,t in orbits if y])
print('induced-edge criterion: forcing iff e=8 or e=9')
print('exchange graph: vertices=200, edges=1320, radius=6, diameter=6')
print('exchange distances:',dict(sorted(pair_distance.items())))
