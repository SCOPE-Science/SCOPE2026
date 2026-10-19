"""Finite incidence enumeration of nontrivial seven-point blocking sets in PG(2,4).

Run with Python 3.10+.  No packages or external inputs are needed.
"""
import hashlib
import json
from collections import Counter, deque
from itertools import combinations, product


def mul(a, b):
    z = 0
    for i in range(2):
        for j in range(2):
            if (a >> i) & (b >> j) & 1:
                z ^= 1 << (i + j)
    if z & 4:
        z ^= 7  # t^2 = t + 1, in characteristic two.
    return z


inverse = {1: 1, 2: 3, 3: 2}


def canonical(v):
    pivot = next(a for a in v if a)
    return tuple(mul(a, inverse[pivot]) for a in v)


points = sorted({canonical(v) for v in product(range(4), repeat=3) if any(v)})
assert len(points) == 21
lines = sorted({sum(1 << i for i, p in enumerate(points)
                    if not (mul(c[0], p[0]) ^ mul(c[1], p[1]) ^ mul(c[2], p[2])))
                for c in points})
assert len(lines) == 21 and all(line.bit_count() == 5 for line in lines)
assert all(sum(bool((1 << i) & m) for m in lines) == 5 for i in range(21))
assert all((m & n).bit_count() == 1 for m, n in combinations(lines, 2))

minimal = []
for k in range(8):
    good = []
    for seq in combinations(range(21), k):
        s = sum(1 << j for j in seq)
        if all((s & m) != 0 and (s & m) != m for m in lines):
            good.append(s)
    if k < 7:
        assert not good, (k, len(good))
    else:
        minimal = sorted(good)
assert len(minimal) == 360
assert all(all((s & m).bit_count() in (1, 3) for m in lines) for s in minimal)

pair_counts = Counter()
adj = [[] for _ in minimal]
for i, s in enumerate(minimal):
    for j in range(i + 1, len(minimal)):
        overlap = (s & minimal[j]).bit_count()
        pair_counts[overlap] += 1
        assert 0 <= overlap <= 4
        if overlap == 4:
            adj[i].append(j)
            adj[j].append(i)
assert set(map(len, adj)) == {56}
assert sum(map(len, adj)) // 2 == 10080

joint = Counter()
ecc = Counter()
for source in range(360):
    distance = [-1] * 360
    distance[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                queue.append(v)
    assert Counter(distance) == {0: 1, 1: 56, 2: 287, 3: 16}
    ecc[max(distance)] += 1
    for target in range(source + 1, 360):
        overlap = (minimal[source] & minimal[target]).bit_count()
        d = distance[target]
        assert (d == 1) == (overlap == 4)
        assert (d == 3) == (overlap == 0)
        joint[(overlap, d)] += 1

# Each sorted hexadecimal row is the exact 21-bit incidence vector of one optimum.
certificate = ''.join(f'{m:06x}\n' for m in minimal).encode('ascii')
assert len(certificate) == 360 * 7
assert pair_counts == {0: 2880, 1: 7560, 2: 30240, 3: 13860, 4: 10080}
assert joint == {(0, 3): 2880, (1, 2): 7560, (2, 2): 30240,
                 (3, 2): 13860, (4, 1): 10080}
print(json.dumps({
    'method': 'all subsets of 21 points with at most 7 selected',
    'total_optima': len(minimal),
    'minimum_nontrivial_blocking_size': 7,
    'neighbor_degree': 56,
    'switching_edges': 10080,
    'distance_layers_per_optimum': [1, 56, 287, 16],
    'eccentricity_histogram': sorted(ecc.items()),
    'pairwise_intersection_histogram': sorted(pair_counts.items()),
    'intersection_distance_histogram': sorted((list(k), v) for k, v in joint.items()),
    'certificate_sha256': hashlib.sha256(certificate).hexdigest(),
}, sort_keys=True, separators=(',', ':')))
