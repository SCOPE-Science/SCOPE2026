"""Exhaustive finite certificate for connected-domination exchange on the four-cube."""
from itertools import combinations
from collections import Counter, deque

BITS = tuple(range(4))
POINTS = tuple(range(16))
NEIGHBORS = tuple(tuple(v ^ (1 << b) for b in BITS) for v in POINTS)
CLOSED = tuple((1 << v) | sum(1 << w for w in NEIGHBORS[v]) for v in POINTS)
FULL = (1 << 16) - 1

def is_connected(mask):
    if not mask:
        return False
    start = (mask & -mask).bit_length() - 1
    seen, frontier = 0, [start]
    seen |= 1 << start
    for u in frontier:
        for v in NEIGHBORS[u]:
            if mask & (1 << v) and not (seen & (1 << v)):
                seen |= 1 << v
                frontier.append(v)
    return seen == mask

def is_dominating(mask):
    covered = 0
    for v in POINTS:
        if mask & (1 << v):
            covered |= CLOSED[v]
    return covered == FULL

def is_path6(mask):
    degrees = sorted(sum(bool(mask & (1 << w)) for w in NEIGHBORS[v])
                     for v in POINTS if mask & (1 << v))
    return degrees == [1, 1, 2, 2, 2, 2]

# All 16 choose k masks are checked for each k <= 6.  The restriction
# to connected masks is independently tested, not assumed from a path list.
for k in range(1, 6):
    candidates = (sum(1 << v for v in c) for c in combinations(POINTS, k))
    assert not any(is_connected(s) and is_dominating(s) for s in candidates)

states = sorted(sum(1 << v for v in c) for c in combinations(POINTS, 6)
                if is_connected(sum(1 << v for v in c))
                and is_dominating(sum(1 << v for v in c)))
assert len(states) == 192
assert all(is_path6(s) for s in states)

index = {s: i for i, s in enumerate(states)}
JUMP = [set() for _ in states]
SLIDE = [set() for _ in states]
for i, s in enumerate(states):
    present = [v for v in POINTS if s & (1 << v)]
    absent = [v for v in POINTS if not s & (1 << v)]
    for u in present:
        for v in absent:
            j = index.get(s ^ (1 << u) ^ (1 << v))
            if j is not None:
                JUMP[i].add(j)
                if u ^ v in (1, 2, 4, 8):
                    SLIDE[i].add(j)
assert all(len(nbr) == 4 for nbr in JUMP)
assert all(len(nbr) == 0 for nbr in SLIDE)
assert all(i in JUMP[j] for j, nbr in enumerate(JUMP) for i in nbr)
assert sum(map(len, JUMP)) // 2 == 384

def distance_layers(source):
    levels = {source: 0}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in JUMP[u]:
            if v not in levels:
                levels[v] = levels[u] + 1
                queue.append(v)
    return Counter(levels.values())

expected = {0: 1, 1: 4, 2: 10, 3: 23, 4: 45, 5: 76, 6: 30, 7: 3}
assert all(dict(distance_layers(i)) == expected for i in range(len(states)))

# Odd closed walks become paths in a parity double-cover.  The first
# return to the same vertex with flipped parity gives odd girth.
def shortest_odd_closed_walk(source):
    start = (source, 0)
    reached = {start: 0}
    queue = deque([start])
    while queue:
        u, parity = queue.popleft()
        for v in JUMP[u]:
            candidate = (v, parity ^ 1)
            if candidate not in reached:
                reached[candidate] = reached[(u, parity)] + 1
                queue.append(candidate)
    return reached[(source, 1)]

assert shortest_odd_closed_walk(0) == 11
assert all(shortest_odd_closed_walk(i) == 11 for i in range(192))
print('Q4_CONNECTED_DOMINATION_MINIMUM 6')
print('OPTIMAL_SETS 192')
print('ALL_INDUCE_P6 true')
print('TOKEN_JUMP_GRAPH vertices=192 edges=384 degree=4 connected=true diameter=7')
print('TOKEN_SLIDE_GRAPH vertices=192 edges=0')
print('DISTANCE_LAYERS ' + ','.join(str(expected[i]) for i in range(8)))
print('ODD_GIRTH 11')
print('VERIFY_OK')
