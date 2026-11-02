#!/usr/bin/env python3
"""Exhaustive Q4 minimum-zero-forcing and one-exchange metric certificate.

Python 3 standard library only. Vertex i is its binary four-bit word;
bit i of a 16-bit integer indicates membership of vertex i.
"""
from collections import Counter, deque
from itertools import combinations, permutations

DIM = 4
V = 1 << DIM
FULL = (1 << V) - 1
NEIGHBOR = [sum(1 << (u ^ (1 << j)) for j in range(DIM)) for u in range(V)]


def closure(mask):
    """Synchronous standard colour-change rule and its propagation time."""
    rounds = 0
    while mask != FULL:
        fresh = 0
        for u in range(V):
            if mask & (1 << u):
                white = NEIGHBOR[u] & (~mask)
                if white and not white & (white - 1):
                    fresh |= white
        if not fresh:
            return False, None
        mask |= fresh
        rounds += 1
    return True, rounds


def subset_masks(k):
    for sub in combinations(range(V), k):
        yield sum(1 << i for i in sub)


assert not any(closure(m)[0] for m in subset_masks(7))
states = [mask for mask in subset_masks(8) if closure(mask)[0]]
assert len(states) == 2360
position = {mask: idx for idx, mask in enumerate(states)}
assert len(position) == len(states)
assert all((FULL ^ mask) in position for mask in states)

neighbors = []
for mask in states:
    adjacent = {
        position[mask ^ (1 << removed) ^ (1 << added)]
        for removed in range(V) if mask & (1 << removed)
        for added in range(V) if not mask & (1 << added)
        if mask ^ (1 << removed) ^ (1 << added) in position
    }
    neighbors.append(sorted(adjacent))

assert all(i in neighbors[j] for i, ns in enumerate(neighbors) for j in ns)
assert sum(map(len, neighbors)) // 2 == 22848
degree_hist = Counter(map(len, neighbors))
assert dict(sorted(degree_hist.items())) == {
    14: 384, 18: 384, 19: 384, 20: 432,
    22: 480, 23: 192, 24: 104,
}

propagation = Counter(closure(m)[1] for m in states)
assert dict(sorted(propagation.items())) == {1: 8, 2: 816, 3: 1152, 4: 384}

automorphisms = []
for perm in permutations(range(DIM)):
    linear = [sum(((i >> j) & 1) << perm[j] for j in range(DIM)) for i in range(V)]
    for translate in range(V):
        automorphisms.append([x ^ translate for x in linear])
assert len(automorphisms) == 384


def image(mask, automorphism):
    return sum(1 << automorphism[i] for i in range(V) if mask & (1 << i))


seen = set()
orbits = []
for mask in states:
    if mask in seen:
        continue
    members = {image(mask, g) for g in automorphisms}
    assert members <= position.keys()
    assert not (members & seen)
    seen.update(members)
    rep = min(members)
    orbits.append((rep, len(members)))
assert seen == set(states)
assert Counter(size for _, size in orbits) == Counter({8: 1, 48: 1, 96: 2, 192: 3, 384: 4})

ordered_distances = Counter()
excess_hist = Counter()
orbit_rows = []
for mask, orbit_size in orbits:
    src = position[mask]
    distance = [-1] * len(states)
    distance[src] = 0
    queue = deque([src])
    while queue:
        u = queue.popleft()
        for w in neighbors[u]:
            if distance[w] < 0:
                distance[w] = distance[u] + 1
                queue.append(w)
    assert min(distance) == 0 and max(distance) == 8
    distribution = Counter(distance)
    for d, count in distribution.items():
        ordered_distances[d] += orbit_size * count
    for target, d in zip(states, distance):
        ambient = 8 - (mask & target).bit_count()
        assert d >= ambient
        excess_hist[d - ambient] += orbit_size
    orbit_rows.append((f'{mask:04x}', orbit_size, len(neighbors[src]), closure(mask)[1]))

assert dict(sorted(ordered_distances.items())) == {
    0: 2360, 1: 45696, 2: 355776, 3: 1274880,
    4: 2110368, 5: 1361280, 6: 371184,
    7: 45696, 8: 2360,
}
assert sum(ordered_distances.values()) == len(states) ** 2
assert dict(sorted(excess_hist.items())) == {0: 5458192, 1: 105600, 2: 5808}
wiener = sum(d * count for d, count in ordered_distances.items()) // 2
assert wiener == 11197808

print('MINIMUM_SETS', len(states))
print('EXCHANGE_EDGES', sum(map(len, neighbors)) // 2)
print('COMPLEMENT_CLOSURE', len(states))
print('AUTOMORPHISM_ORBITS', len(orbits))
print('ORBIT_REPRESENTATIVES_HEX_MASK_SIZE_DEGREE_PROPAGATION')
for row in orbit_rows:
    print(*row)
print('DEGREE_COUNTS', dict(sorted(degree_hist.items())))
print('PROPAGATION_COUNTS', dict(sorted(propagation.items())))
print('ORDERED_DISTANCE_COUNTS', dict(sorted(ordered_distances.items())))
print('JOHNSON_EXCESS_COUNTS', dict(sorted(excess_hist.items())))
print('RADIUS_DIAMETER', 8, 8)
print('WIENER', wiener)
print('PRIMARY_CERTIFICATE_PASS')
