#!/usr/bin/env python3
"""Independent exhaustive checker: metric-space algorithm on the Fano incidence graph."""
from itertools import combinations
from collections import Counter, deque
import json, hashlib

N = 14
adj = [set() for _ in range(N)]
for j in range(7):
    for p in ((j + 0) % 7, (j + 1) % 7, (j + 3) % 7):
        adj[p].add(7+j)
        adj[7+j].add(p)
assert all(len(a)==3 for a in adj)

# Independent BFS distances rather than using Fano incidence formulas.
dist = []
for root in range(N):
    d = [-1]*N
    d[root] = 0
    q = deque([root])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] < 0:
                d[w] = d[v] + 1
                q.append(w)
    assert all(x >= 0 for x in d)
    dist.append(d)

pair_distinguish_masks = []
for a in range(N):
    for b in range(a+1,N):
        pair_distinguish_masks.append(sum(1<<s for s in range(N) if dist[s][a] != dist[s][b]))
assert len(pair_distinguish_masks)==91

def good(mask):
    return all((mask & x).bit_count() >= 2 for x in pair_distinguish_masks)

def masks_of_size(k):
    for cc in combinations(range(N),k):
        yield sum(1<<i for i in cc)

for k in range(7):
    assert not any(good(s) for s in masks_of_size(k)), k
states = sorted(s for s in masks_of_size(7) if good(s))
assert len(states)==282
ids = {m:i for i,m in enumerate(states)}
reconfig = [set() for _ in states]
for i,s in enumerate(states):
    for out in range(N):
        if not (s>>out)&1: continue
        for enter in range(N):
            if (s>>enter)&1: continue
            new = s^(1<<out)^(1<<enter)
            j = ids.get(new)
            if j is not None:reconfig[i].add(j)
assert all(i in reconfig[j] for i,neis in enumerate(reconfig) for j in neis)
edges = sorted((i,j) for i,neis in enumerate(reconfig) for j in neis if i<j)
assert len(edges)==784
assert Counter(map(len,reconfig))=={0:2,4:56,6:224}
profile=Counter((s&127).bit_count() for s in states)
assert profile=={0:1,3:140,4:140,7:1}

components=[];unseen=set(range(len(states)))
while unseen:
    s=min(unseen)
    unseen.remove(s)
    q=[s]
    for v in q:
        for w in reconfig[v]:
            if w in unseen:
                unseen.remove(w)
                q.append(w)
    components.append(sorted(q))
assert Counter(map(len,components))=={1:2,280:1}
gi=[c for c in components if len(c)==280][0]
ecc={}
layer_types=Counter()
for root in gi:
    d={root:0};q=deque([root])
    while q:
        v=q.popleft()
        for w in reconfig[v]:
            if w not in d:
                d[w]=d[v]+1
                q.append(w)
    assert len(d)==280
    ecc[root]=max(d.values())
    layer_types[tuple(Counter(d.values()).get(t,0) for t in range(8))]+=1
assert Counter(ecc.values())=={6:224,7:56}
assert min(ecc.values())==6 and max(ecc.values())==7
assert Counter((len(reconfig[i]),ecc[i]) for i in gi)=={(6,6):168,(6,7):56,(4,6):56}
assert sorted(s for s in states if s&127 in (0,127))==[127,16256]

certificate = {'graph':'Heawood-Fano incidence','vertex_order':'points 0..6, lines 7..13',
 'states_hex':[f'{m:04x}' for m in states], 'exchange_edges':edges,
 'giant_component_indices':gi,'eccentricities_giant':[ecc[i] for i in gi]}
blob=json.dumps(certificate,sort_keys=True,separators=(',',':'))+'\n'
with open('reconfiguration_certificate.json','w',encoding='utf-8') as f:f.write(blob)
print('FULL_GRAPH_VERTICES',N,'FULL_GRAPH_EDGES',sum(map(len,adj))//2)
print('MINIMUM_2_METRIC_BASIS_SIZE',7)
print('BASIS_COUNT',len(states),'PROFILES',dict(sorted(profile.items())))
print('RECONFIGURATION_EDGES',len(edges),'DEGREES',dict(sorted(Counter(map(len,reconfig)).items())))
print('COMPONENT_SIZES',sorted(map(len,components)))
print('GIANT_RADIUS_DIAMETER',min(ecc.values()),max(ecc.values()))
print('GIANT_ECCENTRICITIES',dict(sorted(Counter(ecc.values()).items())))
print('GIANT_DEGREE_ECC_PAIRS',sorted(Counter((len(reconfig[i]),ecc[i]) for i in gi).items()))
print('DISTANCE_LAYER_TYPES',sorted(layer_types.items()))
print('CERTIFICATE_SHA256',hashlib.sha256(blob.encode('utf-8')).hexdigest())
print('VERIFY_OK')
