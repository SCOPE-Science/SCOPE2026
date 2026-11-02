"""Independent exhaustive check of metric-basis reconfiguration of the 5-cube.
Requires only the Python standard library. Run: python direct_check.py.
"""
from collections import Counter, deque
from itertools import combinations

N=5
V=tuple(range(1<<N))
FULL=(1<<N)-1

def is_resolving(S):
    # Work directly with Hamming distances, not the classification theorem.
    return len({tuple((v^s).bit_count() for s in S) for v in V}) == len(V)

assert not any(is_resolving(S) for k in range(1,4) for S in combinations(V,k))
bases=[frozenset(S) for S in combinations(V,4) if is_resolving(S)]
assert len(bases)==1280
indices={s:i for i,s in enumerate(bases)}
adj=[set() for s in bases]
for i,S in enumerate(bases):
    for v in S:
        for w in V:
            if w not in S:
                j=indices.get((S-{v})|{w})
                if j is not None and j!=i:
                    adj[i].add(j)
assert sum(map(len,adj))//2==7680
assert Counter(map(len,adj))=={12:1280}

comps=[]
unseen=set(range(len(bases)))
while unseen:
    src=next(iter(unseen))
    q=deque([src]); unseen.remove(src); component={src}
    while q:
        for j in adj[q.popleft()]:
            if j in unseen:
                unseen.remove(j);component.add(j);q.append(j)
    comps.append(component)
assert len(comps)==16 and all(len(c)==80 for c in comps)

for comp in comps:
    for src in comp:
        distances={src:0};q=deque([src])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v not in distances:
                    distances[v]=distances[u]+1;q.append(v)
        assert len(distances)==80
        assert Counter(distances.values())=={0:1,1:12,2:30,3:28,4:9}
        assert all(d==4-len(bases[src]&bases[v]) for v,d in distances.items())

# Independent root-class construction in ambient vertex coordinates.
classes=[]
for root in range(16):  # choose one representative per antipodal pair of roots
    pairs=[frozenset((root^(1<<j),root^(1<<j)^FULL)) for j in range(5)]
    family=set()
    for omitted in range(5):
        used=[sorted(pairs[j]) for j in range(5) if j!=omitted]
        for mask in range(16):
            family.add(frozenset(used[t][(mask>>t)&1] for t in range(4)))
    assert len(family)==80
    classes.append(family)
assert set().union(*classes)==set(bases)
assert sum(len(x) for x in classes)==len(bases)
assert {frozenset(indices[s] for s in fam) for fam in classes}=={frozenset(x) for x in comps}
print('DIRECT_Q5_ALL_35960_QUADRUPLES_AND_ALL_1280_BFS_PASS')
print('BASES',len(bases),'COMPONENTS',len(comps),'COMPONENT_SIZE',len(comps[0]))
print('EDGES',sum(map(len,adj))//2,'SHELLS',dict(sorted(Counter(distances.values()).items())))
