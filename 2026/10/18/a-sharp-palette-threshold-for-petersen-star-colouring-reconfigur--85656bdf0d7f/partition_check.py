#!/usr/bin/env python3
"""Independent exhaustive set-partition verification of the Petersen star-colouring transition."""
from itertools import combinations, permutations
from collections import Counter, defaultdict, deque

points = tuple(combinations(range(5), 2))
position = {p: i for i, p in enumerate(points)}
neighbor = [set() for _ in range(10)]
for i, a in enumerate(points):
    for j, b in enumerate(points):
        if i != j and set(a).isdisjoint(b):
            neighbor[i].add(j)

# All undirected, not necessarily induced, paths on four distinct vertices.
paths = set()
for b in range(10):
    for c in neighbor[b]:
        for a in neighbor[b] - {c}:
            for d in neighbor[c] - {b, a}:
                p = (a, b, c, d)
                paths.add(min(p, p[::-1]))
assert len(paths) == 60

def star(parts):
    owner = [-1] * 10
    for i, block in enumerate(parts):
        for v in block:
            owner[v] = i
    for u in range(10):
        if any(owner[u] == owner[v] for v in neighbor[u]):
            return False
    for a, b, c, d in paths:
        if owner[a] == owner[c] and owner[b] == owner[d]:
            return False
    return True

def part_key(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks)))

# Build each set partition once, by adding each successive point either to an
# existing block or as a new singleton. No color-vector recursion is used.
all_partitions = []
def partition_dfs(v, blocks):
    if v == 10:
        all_partitions.append(part_key(blocks))
        return
    for i in range(len(blocks)):
        blocks[i].add(v)
        partition_dfs(v + 1, blocks)
        blocks[i].remove(v)
    blocks.append({v})
    partition_dfs(v + 1, blocks)
    blocks.pop()
partition_dfs(0, [])
assert len(all_partitions) == 115975
valid = [p for p in all_partitions if star(p)]
byk = Counter(map(len, valid))
assert byk == Counter({5: 64, 6: 410, 7: 655, 8: 255, 9: 30, 10: 1}), byk
states = [p for p in valid if len(p) <= 6]
assert len(states) == 474
lookup = {p: i for i, p in enumerate(states)}

# A single recoloring moves exactly one element between blocks; dropping an
# empty block or opening a singleton is allowed. Color-block labels are absent.
N = [set() for _ in states]
for i, p in enumerate(states):
    for bi, block in enumerate(p):
        for v in block:
            rest = [set(x) for x in p]
            rest[bi].remove(v)
            rest = [x for x in rest if x]
            for j in range(len(rest) + (len(rest) < 6)):
                q = [set(x) for x in rest]
                if j == len(rest):
                    q.append({v})
                else:
                    q[j].add(v)
                target = lookup.get(part_key(q))
                if target is not None and target != i:
                    N[i].add(target)
assert all(i in N[j] for i, s in enumerate(N) for j in s)
assert sum(map(len, N)) // 2 == 1260
assert Counter(len(N[i]) for i, p in enumerate(states) if len(p) == 5) == Counter({5: 24, 6: 40})

# The named six-color graph has 720 label assignments per partition. Its
# degrees are computed independently by valid single-site substitutions.
counts = defaultdict(Counter)
for p in states:
    color = [None] * 10
    for k, block in enumerate(p):
        for v in block:
            color[v] = k
    deg = 0
    for v in range(10):
        for target in range(6):
            if target == color[v]:
                continue
            changed = color[:]
            changed[v] = target
            if star(tuple(tuple(i for i, c in enumerate(changed) if c == t)
                          for t in set(changed))):
                deg += 1
    counts[len(p)][deg] += 1
assert counts[5] == Counter({10: 64}), counts[5]
assert counts[6] == Counter({3: 20, 4: 90, 6: 150, 7: 120, 8: 30}), counts[6]
edges_labeled = 720 * sum(d * multiplicity for D in counts.values()
                           for d, multiplicity in D.items()) // 2
assert edges_labeled == 1094400

# Symmetries of KG(5,2) come from permutations of five underlying points.
actions = []
for sigma in permutations(range(5)):
    actions.append([position[tuple(sorted((sigma[a], sigma[b])))] for a, b in points])
seen = set()
orbits = []
for i, p in enumerate(states):
    if i in seen:
        continue
    images = set()
    for action in actions:
        q = part_key(tuple(tuple(action[v] for v in block) for block in p))
        images.add(lookup[q])
    seen.update(images)
    orbits.append((len(p), len(images)))
assert len(seen) == 474 and len(orbits) == 11
assert Counter(orbits) == Counter({(5,10):1,(5,30):1,(5,24):1,
                                  (6,60):3,(6,30):3,(6,20):1,(6,120):1})

print('Petersen edges=15 undirected_4_paths=60 Bell_10=115975')
print('valid partition classes by exact colors:', sorted(byk.items()))
print('at_most_six partitions=474 quotient_edges=1260 quotient_connected=', end='')
seen = {0};queue = deque([0])
while queue:
    u = queue.popleft()
    for w in N[u]:
        if w not in seen:
            seen.add(w)
            queue.append(w)
print(len(seen) == 474)
assert len(seen) == 474
print('named_six_palette_vertices=341280 named_edges=', edges_labeled)
print('partition_degrees:', sorted((k, sorted(C.items())) for k, C in counts.items()))
print('Petersen_and_color_automorphism_orbits:', sorted(orbits))
print('ALL_ASSERTIONS_PASSED')
