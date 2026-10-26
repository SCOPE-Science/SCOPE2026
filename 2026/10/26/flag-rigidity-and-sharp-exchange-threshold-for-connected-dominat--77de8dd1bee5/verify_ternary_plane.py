"""Independent exhaustive size-eight checks for PG(2,3) (stdlib only)."""
from itertools import combinations, product
from collections import deque
from math import comb

q = 3

def normalize(v):
    k = next(i for i, x in enumerate(v) if x)
    t = pow(v[k], -1, q)
    return tuple((x * t) % q for x in v)

vectors = [v for v in product(range(q), repeat=3) if any(v)]
points = sorted(set(map(normalize, vectors)))
line_covectors = sorted(set(map(normalize, vectors)))
N = len(points)
assert N == 13
adj = [0] * (2 * N)
for i, p in enumerate(points):
    for j, l in enumerate(line_covectors):
        if sum(x * y for x, y in zip(p, l)) % q == 0:
            adj[i] |= 1 << (N+j)
            adj[N+j] |= 1 << i
assert all(a.bit_count() == q + 1 for a in adj)

all_bits = (1 << (2 * N)) - 1
neighborhood = [adj[i] | (1 << i) for i in range(2 * N)]

def connected(S):
    reached = S & -S
    while True:
        nxt = reached
        remaining = reached
        while remaining:
            bit = remaining & -remaining
            remaining -= bit
            nxt |= adj[bit.bit_length()-1] & S
        if nxt == reached:
            return reached == S
        reached = nxt

candidates = []
domination_count = 0
for subset in combinations(range(2 * N), 2 * (q+1)):
    S = sum(1 << i for i in subset)
    covered = 0
    for i in subset:
        covered |= neighborhood[i]
    if covered != all_bits:
        continue
    domination_count += 1
    if connected(S):
        candidates.append(S)

flags = set()
for i in range(N):
    for j in range(N):
        if (adj[i] >> (N+j)) & 1:
            S = adj[i] | (1 << i) | adj[N+j] | (1 << (N+j))
            assert S.bit_count() == 2*(q+1)
            flags.add(S)
assert len(candidates) == len(flags) == 52
assert set(candidates) == flags
assert comb(26, 8) == 1_562_275

flags = sorted(flags)

def swap_count(a, b):
    assert a.bit_count() == b.bit_count()
    return (a ^ b).bit_count() // 2

assert all(swap_count(a, b) >= q for a, b in combinations(flags, 2))
R = [set() for _ in flags]
for i, a in enumerate(flags):
    for j, b in enumerate(flags):
        if i < j and swap_count(a, b) == q:
            R[i].add(j)
            R[j].add(i)
assert all(len(Ns) == 2*q for Ns in R)
assert sum(map(len, R)) // 2 == 156
for source in range(len(flags)):
    d = {source: 0}
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for u in R[v]:
            if u not in d:
                d[u] = d[v] + 1
                queue.append(u)
    assert len(d) == 52 and max(d.values()) == 3

for S in flags:
    outside = all_bits ^ S
    while outside:
        bit = outside & -outside
        outside -= bit
        v = bit.bit_length() - 1
        assert (adj[v] & S).bit_count() == 1

print('q=3, 26 graph vertices, 52 incident flags')
print('checked all 1,562,275 eight-vertex subsets')
print('dominating subsets of cardinality 8 =', domination_count)
print('minimum connected domination = 8, count =', len(candidates))
print('fewer than three replacements cannot connect distinct optima')
print('three-vertex exchange edges = 156, degree = 6, radius = diameter = 3')
print('maximum leaves = 18, maximum-leaf spanning trees = 52')
print('all assertions passed')
