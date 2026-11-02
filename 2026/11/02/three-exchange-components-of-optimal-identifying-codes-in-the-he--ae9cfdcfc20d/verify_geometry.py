#!/usr/bin/env python3
"""Independent F2-vector incidence construction and set-based code checker."""
from itertools import combinations, permutations
from collections import Counter, deque

# Here a line is represented by its nonzero F2^3 normal vector, NOT by the
# cyclic difference-set labelling used in the other program.
P = frozenset(range(1, 8))
L = frozenset(range(1, 8))
def dot(a,b):
    return ((a & b).bit_count() % 2)
incidence = {(p,l) for p in P for l in L if dot(p,l) == 0}
assert len(incidence) == 21
assert all(sum((p,l) in incidence for l in L) == 3 for p in P)
assert all(sum((p,l) in incidence for p in P) == 3 for l in L)
assert all(sum((p,l) in incidence and (q,l) in incidence for l in L) == 1
           for p,q in combinations(P, 2))

points = {(0,p) for p in P}
lines = {(1,l) for l in L}
U = points | lines
closed = {v: {v} for v in U}
for p,l in incidence:
    closed[(0,p)].add((1,l))
    closed[(1,l)].add((0,p))

def valid(S):
    seen = set()
    for v in U:
        trace = frozenset(S & closed[v])
        if not trace or trace in seen:
            return False
        seen.add(trace)
    return True

# Directly enumerate Cartesian choices of selected points and selected lines.
codes = set()
pcounts = Counter()
for pcount in range(8):
    for pc in combinations(sorted(P), pcount):
        for lc in combinations(sorted(L), 7 - pcount):
            S = frozenset({(0,p) for p in pc} | {(1,l) for l in lc})
            if valid(S):
                codes.add(S)
                pcounts[pcount] += 1
assert len(codes) == 268
assert pcounts == {0:1,1:21,3:112,4:112,6:21,7:1}
assert not any(valid(frozenset(t)) for k in range(7) for t in combinations(sorted(U),k))
states = sorted(codes, key=lambda s:tuple(sorted(s)))

# Explicit exhaustive exchange testing, not the xor-bit rule.
def nbrgraph(cap):
    graph = {S:set() for S in states}
    for S in states:
        outside = U - S
        for r in range(1,cap + 1):
            for removed in combinations(sorted(S), r):
                reduced = S - set(removed)
                for inserted in combinations(sorted(outside), r):
                    T = frozenset(reduced | set(inserted))
                    if T in codes:
                        graph[S].add(T)
    assert all(S in graph[T] for T in graph for S in graph[T])
    return graph

def cc(graph):
    remaining = set(graph)
    answer = []
    while remaining:
        s = remaining.pop()
        component = {s}
        queue = [s]
        for v in queue:
            for w in graph[v]:
                if w in remaining:
                    remaining.remove(w)
                    component.add(w)
                    queue.append(w)
        answer.append(component)
    return answer

def distances(graph, initial):
    d = {initial:0}
    q = deque([initial])
    while q:
        s = q.popleft()
        for t in graph[s]:
            if t not in d:
                d[t] = d[s] + 1
                q.append(t)
    return d

r1 = nbrgraph(1)
assert sorted(len(x) for x in cc(r1)) == [22,22,224]
assert sum(map(len,r1.values())) // 2 == 658
assert Counter(map(len,r1.values())) == {4:56,5:210,21:2}
r2 = nbrgraph(2)
assert len(cc(r2)) == 1
assert sum(map(len,r2.values())) // 2 == 4438
assert Counter(max(distances(r2,S).values()) for S in states) == {3:224,4:42,5:2}

# The 168 collineations of the Fano plane and the point-line duality give
# the full 336-element automorphism group of this incidence graph.
line_pts = {l:frozenset(p for p in P if (p,l) in incidence) for l in L}
line_lookup = {v:l for l,v in line_pts.items()}
perms = []
for tup in permutations(sorted(P)):
    pp = dict(zip(sorted(P),tup))
    if all(frozenset(pp[p] for p in pointset) in line_lookup for pointset in line_pts.values()):
        ll = {l:line_lookup[frozenset(pp[p] for p in line_pts[l])] for l in L}
        perms.append((pp,ll))
assert len(perms) == 168

def image_code(S, pp, ll, dual):
    t = set()
    for side,v in S:
        if side == 0: t.add((1 if dual else 0,pp[v]))
        else: t.add((0 if dual else 1,ll[v]))
    # Applying duality only after the collineation is valid because our
    # dot-product point/normal labels define a self-dual incidence model.
    return frozenset(t)

unseen = set(states)
orbits = []
while unseen:
    s = next(iter(unseen))
    orbit = {image_code(s,pp,ll,dual) for pp,ll in perms for dual in (False,True)}
    assert orbit <= codes
    unseen -= orbit
    orbits.append(orbit)
assert sorted(map(len,orbits)) == [2,42,56,168]
assert sorted((len(o),tuple(sorted(set(len(r1[s]) for s in o)))) for o in orbits) == [
    (2,(21,)), (42,(5,)), (56,(4,)), (168,(5,))]
print('HEAWOOD_IDENTIFY_VECTOR_GEOMETRY_PASS')
print('collineation_group=168 duality_orbits=2,42,56,168')
print('exchange_components=22,22,224 at_most_two_diameter=5')
