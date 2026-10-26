"""Recompute zero-forcing and optimum exchange census of Mycielski(C5).

Run with Python 3 standard library: python3 verify.py
"""
from collections import Counter, deque
from itertools import combinations
from math import comb

N = 11
FULL = (1 << N) - 1
EDGES = set()

def edge(a, b):
    assert a != b
    EDGES.add(tuple(sorted((a, b))))

for i in range(5):
    edge(i, (i + 1) % 5)
    edge(5 + i, (i - 1) % 5)
    edge(5 + i, (i + 1) % 5)
    edge(5 + i, 10)
assert len(EDGES) == 20
ADJ = [0] * N
for u, v in EDGES:
    ADJ[u] |= 1 << v
    ADJ[v] |= 1 << u
assert [x.bit_count() for x in ADJ] == [4]*5 + [3]*5 + [5]
assert all(not (ADJ[u] & ADJ[v]) for u, v in EDGES)  # Triangle-free

# Independent 3-colorability obstruction (plain exact backtracking).
order = sorted(range(N), key=lambda x: -ADJ[x].bit_count())
def is_k_colorable(k):
    assigned = [-1] * N
    def dfs(t):
        if t == N:
            return True
        v = order[t]
        used = {assigned[u] for u in range(N) if (ADJ[v] >> u) & 1}
        for c in range(k):
            if c not in used:
                assigned[v] = c
                if dfs(t + 1):
                    return True
                assigned[v] = -1
        return False
    return dfs(0)
assert not is_k_colorable(3) and is_k_colorable(4)

def synchronous(seed):
    """Simultaneously apply every legal force using pre-round colors."""
    black, rounds = seed, 0
    while True:
        new = 0
        for v in range(N):
            if (black >> v) & 1:
                white_neighbors = ADJ[v] & ~black
                if white_neighbors and not (white_neighbors & (white_neighbors - 1)):
                    new |= white_neighbors
        if not new:
            return black == FULL, rounds
        black |= new
        rounds += 1

def sequential(seed):
    """An independently ordered one-at-a-time closure algorithm."""
    colored = {i for i in range(N) if (seed >> i) & 1}
    while True:
        changed = False
        for v in sorted(colored, reverse=True):
            targets = [w for w in range(N) if (ADJ[v] >> w) & 1 and w not in colored]
            if len(targets) == 1:
                colored.add(targets[0])
                changed = True
                break
        if not changed:
            return len(colored) == N

success = Counter()
prop_by_cardinality = Counter()
minimum = set()
for mask in range(1 << N):
    ok, t = synchronous(mask)
    assert ok == sequential(mask), (mask, ok)
    if ok:
        k = mask.bit_count()
        success[k] += 1
        prop_by_cardinality[k,t] += 1
        if k == 5:
            minimum.add(mask)
assert [success[i] for i in range(12)] == [0,0,0,0,0,175,370,320,165,55,11,1]
assert len(minimum) == 175
assert {t:prop_by_cardinality[5,t] for t in range(3,6)} == {3:55,4:100,5:20}
assert sum(success.values()) == 1097

# Full automorphism group: the apex is distinguished by degree 5;
# shadows are degree 3; original 5-cycle is degree 4, so every
# automorphism restricts to one of its 10 dihedral symmetries.
permutations = []
for offset in range(5):
    for sign in (-1,1):
        p = [((offset + sign*i) % 5) for i in range(5)]
        p += [5+((offset + sign*i) % 5) for i in range(5)]
        p += [10]
        assert {tuple(sorted((p[u],p[v]))) for u,v in EDGES} == EDGES
        permutations.append(p)
assert len({tuple(p) for p in permutations}) == 10

def image(mask, permutation):
    return sum(1 << permutation[v] for v in range(N) if mask & (1<<v))

remaining = minimum.copy()
orbits = []
while remaining:
    representative = min(remaining)
    orbit = {image(representative, p) for p in permutations}
    assert orbit <= minimum
    remaining -= orbit
    orbits.append((representative, len(orbit), synchronous(representative)[1]))
assert len(orbits) == 19
assert Counter(size for _,size,_ in orbits) == Counter({5:3, 10:16})
assert sum(size for _,size,_ in orbits) == len(minimum)

# Build exchange edges independently by scanning pairs AND by legal swaps.
pair_edges = set()
for a,b in combinations(sorted(minimum),2):
    if (a^b).bit_count() == 2:
        pair_edges.add((a,b))
swap_edges = set()
for a in minimum:
    for u in range(N):
        if a & (1<<u):
            for v in range(N):
                if not (a & (1<<v)):
                    b = a ^ (1<<u) ^ (1<<v)
                    if b in minimum:
                        swap_edges.add(tuple(sorted((a,b))))
assert pair_edges == swap_edges and len(pair_edges) == 1180
neighbors = {a:set() for a in minimum}
for a,b in pair_edges:
    neighbors[a].add(b)
    neighbors[b].add(a)

pair_dist = Counter()
ecc = Counter()
for start in minimum:
    distance = {start:0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in neighbors[u]:
            if v not in distance:
                distance[v] = distance[u] + 1
                q.append(v)
    assert len(distance) == len(minimum)
    ecc[max(distance.values())] += 1
    for v,d in distance.items():
        if start < v:
            pair_dist[d] += 1
assert ecc == Counter({4:30,5:145})
assert pair_dist == Counter({1:1180,2:4780,3:6445,4:2610,5:210})
assert sum(pair_dist.values()) == comb(175,2)
assert sum(len(neighbors[v]) for v in minimum) == 2*1180

print('VERIFY_OK')
print('Grotzsch vertices=11 edges=20 chromatic_number=4 triangle_free=true')
print('zero_forcing_number=5 polynomial_coefficients='+str([success[i] for i in range(12)]))
print('minimum_sets=175 dihedral_orbits=19 orbit_sizes='+str(dict(Counter(s for _,s,_ in orbits))))
print('propagation_by_round='+str({t:prop_by_cardinality[5,t] for t in (3,4,5)}))
print('exchange_vertices=175 exchange_edges=1180 radius=4 diameter=5')
print('exchange_eccentricities='+str(dict(ecc))+' distances='+str(dict(pair_dist)))
for rep,size,rounds in orbits:
    print('ORBIT', ','.join(str(j) for j in range(N) if (rep >> j) & 1),size,rounds)
