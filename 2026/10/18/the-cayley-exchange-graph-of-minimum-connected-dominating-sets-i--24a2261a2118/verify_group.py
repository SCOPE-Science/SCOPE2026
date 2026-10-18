"""Independent path-orbit and affine-Cayley certificate for Q4 domination."""
from itertools import combinations, permutations
from collections import deque, Counter

N = 16
ADJ = {v: frozenset(v ^ (1 << b) for b in range(4)) for v in range(N)}
ALL = frozenset(range(N))

def dominates(s):
    return ALL == s.union(*(ADJ[v] for v in s))

def induce_connected(s):
    f = [next(iter(s))]
    visited = {f[0]}
    for u in f:
        for w in s.intersection(ADJ[u]):
            if w not in visited:
                visited.add(w)
                f.append(w)
    return visited == s

# Generate connected sets by extending connected sets one vertex at a time;
# this does not enumerate all fixed-cardinality combinations as in the
# independent subset verifier.
connected = {frozenset([v]) for v in range(N)}
for cardinality in range(2, 7):
    grown = set()
    for s in connected:
        perimeter = set().union(*(ADJ[v] for v in s)) - s
        for v in perimeter:
            grown.add(s | {v})
    connected = grown
    assert all(induce_connected(s) for s in connected)
    if cardinality < 6:
        assert not any(dominates(s) for s in connected)
        if cardinality == 5:
            assert len(connected) == 784
            assert max(len(s.union(*(ADJ[v] for v in s))) for s in connected) == 14
    else:
        optimal = {s for s in connected if dominates(s)}
        assert len(connected) == 1952
        assert len(optimal) == 192

# Any ordered five-step direction sequence (a,b,c,d,a) with all four
# letters different specifies an induced dominating six-vertex path.
paths = set()
for origin in range(N):
    for q in permutations(range(4)):
        word = (*q, q[0])
        v = origin
        points = [v]
        for b in word:
            v ^= 1 << b
            points.append(v)
        s = frozenset(points)
        assert len(s) == 6 and dominates(s)
        assert sorted(len(ADJ[v].intersection(s)) for v in s) == [1,1,2,2,2,2]
        paths.add(s)
assert len(paths) == 192 and paths == optimal

base = frozenset((0,1,2,5,10,13))
assert base in optimal

def sign(p):
    return (-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))
A4 = tuple(p for p in permutations(range(4)) if sign(p) == 1)
IDENTITY = ((0,1,2,3), 0)

def linear(p, v):
    return sum(1 << p[i] for i in range(4) if (v >> i)&1)

def apply(g, s):
    p,t = g
    return frozenset(linear(p, v) ^ t for v in s)

def product(g, h):
    p,t = g; q,u = h
    return tuple(p[q[i]] for i in range(4)), t ^ linear(p, u)

def inverse(g):
    p,t = g
    q = tuple(p.index(i) for i in range(4))
    return q, linear(q, t)

H = tuple((p,t) for p in A4 for t in range(N))
assert len(H) == 192
orbit = {apply(g,base): g for g in H}
assert len(orbit) == 192 and set(orbit) == optimal
# Since group size and orbit size coincide, the action is free and transitive.

# Find ALL legal one-vertex replacements of the chosen base explicitly.
base_neighbours = set()
for u in base:
    for w in ALL-base:
        s = (base-{u})|{w}
        if s in optimal:base_neighbours.add(s)
assert len(base_neighbours) == 4
K = tuple(orbit[s] for s in sorted(base_neighbours, key=lambda x: tuple(sorted(x))))
expected_set = {
    ((1,0,3,2),0),
    ((2,3,0,1),5),
    ((2,0,1,3),4),
    ((1,2,0,3),1)
}
assert set(K) == expected_set
assert {inverse(g) for g in K} == set(K)

# A path in the right Cayley graph is a sequence of right multiplication
# by these generators.  This verifies the exact graph rather than merely
# the abstract orbit.
for g in H:
    here = apply(g,base)
    actual = {(here-{u})|{w} for u in here for w in ALL-here
              if (here-{u})|{w} in optimal}
    via_group = {apply(product(g,k),base) for k in K}
    assert actual == via_group

layer = {IDENTITY:0}
queue = deque([IDENTITY])
while queue:
    u=queue.popleft()
    for k in K:
        v=product(u,k)
        if v not in layer:
            layer[v]=layer[u]+1
            queue.append(v)
assert len(layer)==192
histogram=Counter(layer.values())
assert [histogram[i] for i in range(8)] == [1,4,10,23,45,76,30,3]

# Parity-doubled group walk certifies the shortest odd relation.
visited = {(IDENTITY,0):0}
queue = deque([(IDENTITY,0)])
while queue:
    state,b=queue.popleft()
    for k in K:
        v=(product(state,k),1-b)
        if v not in visited:
            visited[v] = visited[(state,b)]+1
            queue.append(v)
assert visited[(IDENTITY,1)] == 11

assert all(not ((u^w).bit_count()==1) for s in optimal for u in s
               for w in ALL-s if (s-{u})|{w} in optimal)
print('CONNECTED_SETS_OF_SIZE_5 784 MAX_CLOSED_NEIGHBORHOOD 14')
print('CONNECTED_SETS_OF_SIZE_6 1952 OPTIMAL 192')
print('DOMINATING_PATH_PATTERN (a,b,c,d,a) WHERE a,b,c,d DISTINCT')
print('AFFINE_EVEN_PERMUTATION_GROUP 192 REGULAR_ORBIT true')
print('CAYLEY_GENERATORS ' + repr(sorted(K)))
print('CAYLEY_EDGES 384')
print('DISTANCE_LAYERS ' + ','.join(str(histogram[i]) for i in range(8)))
print('ODD_GIRTH 11')
print('TOKEN_SLIDES 0')
print('VERIFY_OK')
