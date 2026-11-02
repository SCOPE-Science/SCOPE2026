"""Exhaustive finite certificate for the Frucht zero-forcing speed filtration.

Run: python verify_direct.py
The vertex labels are fixed only for reproducibility; all assertions are
invariant under graph isomorphisms.
"""
from itertools import combinations
from collections import Counter, deque
from hashlib import sha256

N = 12
EDGES = [(0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),
         (3,9),(4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11)]
ALL = (1 << N) - 1
NEIGH = [0] * N
for u,v in EDGES:
    NEIGH[u] |= 1 << v
    NEIGH[v] |= 1 << u
assert len(set(tuple(sorted(e)) for e in EDGES)) == 18
assert all(x.bit_count() == 3 for x in NEIGH)

def parallel_propagation(mask):
    current, steps = mask, 0
    while current != ALL:
        add = 0
        for u in range(N):
            if current >> u & 1:
                white = NEIGH[u] & ~current
                if white and white & (white - 1) == 0:
                    add |= white
        if not add:
            return None
        current |= add
        steps += 1
    return steps

def masks_of_size(k):
    return [sum(1 << j for j in c) for c in combinations(range(N), k)]

assert not any(parallel_propagation(m) is not None
               for k in range(4) for m in masks_of_size(k))
S = [m for m in masks_of_size(4) if parallel_propagation(m) is not None]
assert len(S) == 89
ROSTER_SHA256 = sha256(','.join(str(m) for m in sorted(S)).encode()).hexdigest()
assert ROSTER_SHA256 == 'ced4bd0df213493a9ce37d11a5d15d181998edcdc493efe0d439870c99d57d1b'
TIME = [parallel_propagation(m) for m in S]
assert Counter(TIME) == {3:8,4:32,5:43,6:6}

# All pairs of minimum sets differing in one selected vertex.
NBR = [set() for _ in S]
for i,a in enumerate(S):
    for j in range(i+1,len(S)):
        b = S[j]
        if (a ^ b).bit_count() == 2:
            NBR[i].add(j)
            NBR[j].add(i)
assert sum(map(len,NBR)) // 2 == 366

def induced(indices):
    indices = set(indices)
    seen, parts = set(), []
    for i in indices:
        if i in seen:
            continue
        component, queue = set([i]), [i]
        seen.add(i)
        for v in queue:
            for w in NBR[v] & indices:
                if w not in seen:
                    seen.add(w)
                    component.add(w)
                    queue.append(w)
        parts.append(component)
    return sorted(parts,key=len,reverse=True)

def edges_in(indices):
    indices = set(indices)
    return sum(len(NBR[i] & indices) for i in indices) // 2

FAST = [i for i,t in enumerate(TIME) if t == 3]
COMP = induced(FAST)
assert list(map(len,COMP)) == [6,2]
assert edges_in(FAST) == 10
assert edges_in(COMP[0]) == 9
assert all(len(NBR[i] & COMP[0]) == 3 for i in COMP[0])
# The six-vertex component is triangular prism: two triangles with
# a perfect matching across them.  No graph-isomorphism library needed.
TRIANGLES = [set(c) for c in combinations(COMP[0], 3)
             if all(v in NBR[u] for u,v in combinations(c,2))]
assert len(TRIANGLES) == 2 and TRIANGLES[0].isdisjoint(TRIANGLES[1])
assert sum(len(NBR[i] & TRIANGLES[1]) for i in TRIANGLES[0]) == 3
assert len(NBR[next(iter(COMP[1]))] & COMP[1]) == 1

for bound, vertices, edges, parts in [(3,8,10,[6,2]),
                                     (4,40,100,[40]),
                                     (5,83,322,[83]),
                                     (6,89,366,[89])]:
    subset = [i for i,t in enumerate(TIME) if t <= bound]
    assert (len(subset),edges_in(subset),list(map(len,induced(subset)))) == \
           (vertices,edges,parts)

# The diameter of the four-round filtration is 8, and every fast
# state in one component is at least four exchanges from the other.
V4 = {i for i,t in enumerate(TIME) if t <= 4}
def distances(start, admissible):
    dis = {start:0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in NBR[u] & admissible:
            if v not in dis:
                dis[v] = dis[u] + 1
                q.append(v)
    return dis
assert max(max(distances(i,V4).values()) for i in V4) == 8
assert min(distances(i,V4)[j] for i in COMP[0] for j in COMP[1]) == 4
for bound, diameter in [(5,6),(6,6)]:
    valid = {i for i,t in enumerate(TIME) if t <= bound}
    assert max(max(distances(i,valid).values()) for i in valid) == diameter

print('DIRECT_ALL_794_CANDIDATES_OF_SIZE_AT_MOST_FOUR_PASS')
print('FRUCHT_89_SETS_366_EXCHANGES_FAST_PRISM_PLUS_EDGE_PASS')
