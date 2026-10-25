#!/usr/bin/env python3
"""Exhaustive certificate for length-restricted alternating-cycle exchanges in the Coxeter graph.
Only Python standard library is required. All assignments of 28 vertices are searched.
"""
import json
from collections import Counter, deque
from itertools import combinations

# Fano lines, and the 28 triples that are not Fano lines.
lines = {frozenset((t, (t+1)%7, (t+3)%7)) for t in range(7)}
vertices = [c for c in combinations(range(7),3) if frozenset(c) not in lines]
assert len(vertices)==28
edges=[(i,j) for i in range(28) for j in range(i+1,28) if not(set(vertices[i]) & set(vertices[j]))]
assert len(edges)==42
adj=[set() for _ in vertices]
for i,j in edges:adj[i].add(j);adj[j].add(i)
assert {len(s) for s in adj}=={3}
def girth(neighbor):
    best=len(neighbor)+1
    for start in range(len(neighbor)):
        dist={start:0};parent={start:-1};q=deque([start])
        while q:
            u=q.popleft()
            for v in neighbor[u]:
                if v not in dist:
                    dist[v]=dist[u]+1;parent[v]=u;q.append(v)
                elif parent[u]!=v:
                    best=min(best,dist[u]+dist[v]+1)
    return best
assert girth(adj)==7
eid={e:k for k,e in enumerate(edges)}

# Select an uncovered vertex with minimum remaining eligible partners.
def enum(mask,chosen):
    if not mask:
        yield tuple(sorted(chosen));return
    candidates=[i for i in range(28) if mask>>i&1]
    pivot=min(candidates,key=lambda i:len([j for j in adj[i] if mask>>j&1]))
    for j in sorted(adj[pivot]):
        if mask>>j&1:
            a,b=sorted((pivot,j))
            yield from enum(mask^(1<<a)^(1<<b),chosen+[eid[(a,b)]])
matchings=sorted(set(enum((1<<28)-1,[])))
assert len(matchings)==84 and all(len(m)==14 for m in matchings)

# Comparing all unordered pairs is exhaustive for graph edges.
flip={ell:[set() for _ in matchings] for ell in [8,10]}
for i in range(84):
    for j in range(i+1,84):
        d=set(matchings[i])^set(matchings[j]); L=len(d)
        if L not in flip:continue
        deg=Counter(w for edge_id in d for w in edges[edge_id])
        if len(deg)==L and all(val==2 for val in deg.values()):
            flip[L][i].add(j);flip[L][j].add(i)

# Exhaustive breadth-first distances.
distances=[]
for src in range(84):
    dist={src:0};q=deque([src])
    while q:
        u=q.popleft()
        for v in sorted(flip[10][u]):
            if v not in dist:dist[v]=dist[u]+1;q.append(v)
    assert len(dist)==84
    distances.append(dist)
profile=Counter(tuple(Counter(d.values()).get(k,0) for k in range(max(d.values())+1)) for d in distances)
assert profile=={(1,4,12,25,28,13,1):84},profile
assert sorted(len(v) for v in flip[8])==[1]*84
assert sorted(len(v) for v in flip[10])==[4]*84
antipodes={i:next(v for v in range(84) if distances[i][v]==6) for i in range(84)}
assert all(len([j for j in distances[i] if distances[i][j]==6])==1 for i in range(84))
assert all(antipodes[antipodes[i]]==i for i in range(84))
# The antipodes have exactly two alternating cycles, not one 24-cycle.
def cycles_of_difference(a,b):
    d=set(matchings[a])^set(matchings[b]);nxt={}
    for e in d:
        u,v=edges[e];nxt.setdefault(u,[]).append(v);nxt.setdefault(v,[]).append(u)
    assert all(len(x)==2 for x in nxt.values())
    remain=set(nxt); lengths=[]
    while remain:
        root=min(remain);seen={root};stack=[root]
        while stack:
            u=stack.pop()
            for v in nxt[u]:
                if v not in seen:seen.add(v);stack.append(v)
        remain-=seen;lengths.append(len(seen))
    return tuple(sorted(lengths))
all_two_cycle_pairs=[(i,j) for i in range(84) for j in range(i+1,84)
                     if cycles_of_difference(i,j)==(8,16)]
assert len(all_two_cycle_pairs)==42
assert all(distances[i][j]==6 for i,j in all_two_cycle_pairs)
assert all(cycles_of_difference(i,antipodes[i])==(8,16) for i in range(84))
assert all(distances[i][next(iter(flip[8][i]))]==5 for i in range(84))

# Adjacency certificates are 0-indexed, using lexicographically ordered perfect matchings.
certificate={'edges':edges,'matching_edges':[list(m) for m in matchings],
    'flip10_adj': [sorted(a) for a in flip[10]],'flip8_adj':[sorted(a) for a in flip[8]],
    'antipode':[antipodes[i] for i in range(84)]}
with open('fano_certificate.json','w',encoding='utf8') as handle:
    json.dump(certificate,handle,separators=(',',':'),sort_keys=True)
    handle.write('\n')
result={'graph_order':28,'graph_edges':42,'perfect_matchings':84,
        'flip8_edges':sum(map(len,flip[8]))//2,
        'flip10_edges':sum(map(len,flip[10]))//2,
        'flip8_components':42, 'flip10_degree':4,'flip10_connected':True,
        'flip10_distance_distribution':[1,4,12,25,28,13,1],
        'flip10_radius':6,'flip10_diameter':6,
        'unique_antipodal_pairs':42,'antipodal_symmetric_difference_cycles':[8,16],
        'only_8_plus_16_pairs_are_antipodal':True,
        'all_8_cycle_flip_pairs_are_distance_5_under_10_flips':True}
print(json.dumps(result,sort_keys=True,separators=(',',':')))
