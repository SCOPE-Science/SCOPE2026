"""Exact vertex-switch graph for factor partitions of the labeled eight-point clique.

Standalone Python 3 standard library. Prints deterministic invariant certificate.
"""
from itertools import combinations, permutations
from collections import Counter, deque

n = 8
edges = tuple(combinations(range(n), 2))
edge_id = {e: i for i, e in enumerate(edges)}
full = (1 << len(edges)) - 1

def matchings(vertices):
    if not vertices:
        yield 0
        return
    a = vertices[0]
    for b in vertices[1:]:
        rest = tuple(x for x in vertices if x != a and x != b)
        for m in matchings(rest):
            yield m | (1 << edge_id[(a,b)])

ms = tuple(sorted(matchings(tuple(range(n)))))
assert len(ms) == 105
mi = {m: i for i, m in enumerate(ms)}
through = [[j for j, m in enumerate(ms) if (m >> i) & 1] for i in range(28)]
fac = []
def partition(used, chosen):
    if used == full:
        fac.append(tuple(sorted(chosen)))
        return
    e = next(i for i in range(28) if not ((used >> i) & 1))
    for j in through[e]:
        if not (used & ms[j]):
            partition(used | ms[j], chosen + [j])
partition(0, [])
fac = tuple(sorted(set(fac)))
assert len(fac) == 6240
idx = {f:i for i,f in enumerate(fac)}

neighbor = [set() for _ in fac]
cycle_types = Counter()
for i, f in enumerate(fac):
    col = {}
    for t, j in enumerate(f):
        for e in range(28):
            if (ms[j] >> e) & 1: col[edges[e]] = t
    for a, b in edges:
        retained = col[(a,b)]
        other = [z for z in range(n) if z not in (a,b)]
        adjacent = {z:set() for z in other}
        for t in range(7):
            if t == retained: continue
            x = next(z for z in other if col[tuple(sorted((a,z)))] == t)
            y = next(z for z in other if col[tuple(sorted((b,z)))] == t)
            adjacent[x].add(y)
            adjacent[y].add(x)
        unseen = set(other)
        comps = []
        while unseen:
            seed = min(unseen)
            q = [seed]
            seen = {seed}
            unseen.remove(seed)
            for u in q:
                for v in sorted(adjacent[u]):
                    if v not in seen:
                        seen.add(v)
                        unseen.remove(v)
                        q.append(v)
            comps.append(seen)
        cycle_types[tuple(sorted(len(c) for c in comps))] += 1
        if len(comps) == 1: continue
        for component in comps:
            after = col.copy()
            for z in component:
                az = tuple(sorted((a,z)))
                bz = tuple(sorted((b,z)))
                after[az], after[bz] = after[bz], after[az]
            masks = [0]*7
            for e, t in after.items(): masks[t] |= 1<<edge_id[e]
            new = tuple(sorted(mi[m] for m in masks))
            j = idx[new]
            if j != i: neighbor[i].add(j)
assert all(i in neighbor[j] for i, row in enumerate(neighbor) for j in row)
print('number_of_perfect_matchings', len(ms))
print('number_of_factorizations', len(fac))
print('vertex_cycle_signatures', sorted(cycle_types.items()))
print('vertex_switch_edge_count', sum(map(len,neighbor))//2)
print('degree_histogram', sorted(Counter(map(len,neighbor)).items()))
seen = set()
components = []
for i in range(len(fac)):
    if i in seen: continue
    queue = [i]
    seen.add(i)
    for v in queue:
        for j in neighbor[v]:
            if j not in seen: seen.add(j); queue.append(j)
    components.append(queue)
print('component_sizes', sorted(map(len,components)))

# All S_8 orbits, derived without consulting factor-switch geometry.
perm_images=[]
for perm in permutations(range(n)):
    mapping = tuple(edge_id[tuple(sorted((perm[a],perm[b])))] for a,b in edges)
    image = []
    for m in ms:
        newmask = 0
        while m:
            bit = m & -m
            newmask |= 1 << mapping[bit.bit_length()-1]
            m ^= bit
        image.append(mi[newmask])
    perm_images.append(tuple(image))
remaining = set(range(len(fac)))
orbits=[]
for i in range(len(fac)):
    if i not in remaining: continue
    f = fac[i]
    orbit = {idx[tuple(sorted(p[j] for j in f))] for p in perm_images}
    assert orbit <= remaining
    remaining -= orbit
    orbits.append((i,orbit))
assert not remaining
print('orbit_sizes_and_degrees', sorted((len(orb),len(neighbor[rep])) for rep,orb in orbits))
all_ecc = Counter()
for rep, orb in orbits:
    dist = [-1]*len(fac)
    dist[rep] = 0
    q = deque([rep])
    while q:
        u = q.popleft()
        for v in neighbor[u]:
            if dist[v] < 0:
                dist[v] = dist[u]+1
                q.append(v)
    assert -1 not in dist
    ecc = max(dist)
    all_ecc[ecc] += len(orb)
    print('orbit_distance',len(orb),len(neighbor[rep]),ecc,tuple(Counter(dist)[j] for j in range(ecc+1)))
print('eccentricity_histogram', sorted(all_ecc.items()))
print('VERIFY_OK')
