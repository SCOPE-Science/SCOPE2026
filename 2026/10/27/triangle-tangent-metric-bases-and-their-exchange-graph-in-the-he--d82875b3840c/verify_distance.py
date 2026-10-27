#!/usr/bin/env python3
"""Independent normal-vector / BFS / automorphism verification for Fano metric bases."""
import itertools, collections, json

# Point v is adjacent to line n exactly when the GF(2) dot product vanishes.
N = 14
adj = [set() for _ in range(N)]
for p in range(1,8):
    for n in range(1,8):
        if ((p & n).bit_count() % 2) == 0:
            adj[p-1].add(n+6)
            adj[n+6].add(p-1)
assert all(len(a)==3 for a in adj)

def all_dist(v):
    ds = [-1] * N
    ds[v] = 0
    q = collections.deque([v])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if ds[b] < 0:
                ds[b]=ds[a]+1
                q.append(b)
    assert -1 not in ds
    return ds
D = [all_dist(v) for v in range(N)]

# Exhaust all 2^14 subsets; never assume the metric-dimension value.
def bits(mask):
    return tuple(i for i in range(N) if mask & (1<<i))

def resolving(mask):
    S=bits(mask)
    return len({tuple(D[v][s] for s in S) for v in range(N)}) == N

count_by_size=collections.Counter()
optimal=set()
for mask in range(1<<N):
    if resolving(mask):
        count_by_size[mask.bit_count()] += 1
        if mask.bit_count()==5:
            optimal.add(mask)
assert all(count_by_size[k]==0 for k in range(5))
assert len(optimal)==168

# Build exchange neighbors via shared four-element subsets, independent of distance checker A.
index=collections.defaultdict(list)
for mask in optimal:
    for i in bits(mask):
        index[mask ^ (1<<i)].append(mask)
G={mask:set() for mask in optimal}
for vals in index.values():
    for a,b in itertools.combinations(vals,2):
        G[a].add(b);G[b].add(a)
assert len({tuple(sorted((a,b))) for a in G for b in G[a] if a < b}) == 420
assert {len(G[a]) for a in G}=={5}
profile_count=collections.Counter()
for source in optimal:
    ds={source:0};q=collections.deque([source])
    while q:
        a=q.popleft()
        for b in G[a]:
            if b not in ds:
                ds[b]=ds[a]+1;q.append(b)
    assert len(ds)==168
    c=collections.Counter(ds.values())
    profile_count[tuple(c[i] for i in range(max(c)+1))]+=1
assert profile_count=={(1,5,18,49,71,24):168}

# Generate all invertible 3x3 binary changes of coordinates.
def linmap(x, cols):
    out=0
    for i in range(3):
        if x & (1<<i):out ^= cols[i]
    return out

def normals_for_image(pmap,n):
    mapped={pmap[p] for p in range(1,8) if (p & n).bit_count()%2 == 0}
    return next(m for m in range(1,8) if {p for p in range(1,8) if (p&m).bit_count()%2==0}==mapped)

perms=[]
for cols in itertools.product(range(1,8),repeat=3):
    if len({linmap(v,cols) for v in range(8)})!=8:
        continue
    pm={p:linmap(p,cols) for p in range(1,8)}
    nm={n:normals_for_image(pm,n) for n in range(1,8)}
    perm=tuple(pm[v+1]-1 if v<7 else nm[v-6]+6 for v in range(14))
    assert all({perm[w] for w in adj[v]}==adj[perm[v]] for v in range(14))
    perms.append(perm)
assert len(perms)==168

def act(mask,perm):
    return sum(1<<perm[v] for v in bits(mask))
base=min(optimal)
first={act(base,perm) for perm in perms}
assert len(first)==84
# Polarity: point x <-> line whose normal is x.
polarity=tuple((v+7 if v<7 else v-7) for v in range(14))
assert all({polarity[w] for w in adj[v]}==adj[polarity[v]] for v in range(14))
second={act(m,polarity) for m in first}
assert len(first|second)==168 and first.isdisjoint(second) and first|second==optimal
tri=sum(len(G[a]&G[b]) for a in G for b in G[a])//6
assert tri==56
print(json.dumps({'subset_search': 1<<14, 'minimum_size':5,
 'resolving_by_size':sorted(count_by_size.items()), 'optimal':len(optimal),
 'edges':420,'degree':5,'triangles':tri,'connected':True,
 'profiles':[[list(a),b] for a,b in sorted(profile_count.items())],
 'GL3_order':len(perms),'GL3_orbit':len(first),'polarity_orbit':len(second),
 'full_automorphism_transitive':True},sort_keys=True))
