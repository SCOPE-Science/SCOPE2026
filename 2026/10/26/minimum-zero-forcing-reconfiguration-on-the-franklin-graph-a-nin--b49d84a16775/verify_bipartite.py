#!/usr/bin/env python3
"""Independent Franklin-graph forcing and reconfiguration checker (Python stdlib)."""
from itertools import combinations
from collections import deque, Counter
import json

# A_r=2r, B_s=2s+1, with A_r--B_s iff s=r,r-1,r+2 (mod 6).
adjacency={v:set() for v in range(12)}
for r in range(6):
    for s in (r, r-1, r+2):
        a,b=2*r,2*(s%6)+1
        adjacency[a].add(b);adjacency[b].add(a)
assert len({tuple(sorted((a,b))) for a in adjacency for b in adjacency[a] if a<b})==18

# Serial, one-at-a-time zero forcing: at each iteration perform only the earliest legal force.
def succeeds(seed):
    colored=set(seed)
    while len(colored)<12:
        next_vertex=None
        for u in sorted(colored):
            uncolored=adjacency[u]-colored
            if len(uncolored)==1:
                next_vertex=uncolored.pop()
                break
        if next_vertex is None:
            return False
        colored.add(next_vertex)
    return True

assert not any(succeeds(c) for c in combinations(range(12),4))
configurations={frozenset(c) for c in combinations(range(12),5) if succeeds(c)}
assert len(configurations)==324
ordering=sorted(configurations,key=lambda c:tuple(sorted(c)))
position={s:i for i,s in enumerate(ordering)}
jumping=[set() for _ in ordering]
sliding=[set() for _ in ordering]
# Construct moves by replacing a particular source vertex with any available target.
for i,S in enumerate(ordering):
    for x in S:
        for y in range(12):
            if y in S:
                continue
            target=S.difference((x,)).union((y,))
            j=position.get(target)
            if j is None:
                continue
            jumping[i].add(j)
            if y in adjacency[x]:sliding[i].add(j)
assert all(i in jumping[j] for j,S in enumerate(jumping) for i in S)
assert all(i in sliding[j] for j,S in enumerate(sliding) for i in S)

def statistics(network):
    degrees=Counter(len(N) for N in network)
    dcounts=Counter(); ec=Counter()
    for origin in range(len(network)):
        distance=[-1]*len(network);distance[origin]=0
        queue=deque([origin])
        while queue:
            u=queue.popleft()
            for v in network[u]:
                if distance[v]==-1:
                    distance[v]=distance[u]+1
                    queue.append(v)
        assert -1 not in distance
        ec[max(distance)]+=1
        for v in range(origin+1,len(network)):
            dcounts[distance[v]]+=1
    return {'edges':sum(map(len,network))//2,'degree_histogram':dict(sorted(degrees.items())),
            'radius':min(ec),'diameter':max(ec),'eccentricities':dict(sorted(ec.items())),
            'pair_distances':dict(sorted(dcounts.items()))}

jump=statistics(jumping); slide=statistics(sliding)
assert jump['edges']==2910 and jump['radius']==jump['diameter']==5
assert slide['edges']==534 and slide['radius']==9 and slide['diameter']==13
max_neighbor_dist=-1; example=[]
for origin in range(len(ordering)):
    dist={origin:0}; queue=deque([origin])
    while queue:
        u=queue.popleft()
        for v in sliding[u]:
            if v not in dist:dist[v]=dist[u]+1;queue.append(v)
    for v in jumping[origin]:
        if origin<v and dist[v]>max_neighbor_dist:
            max_neighbor_dist=dist[v]
            example=[sorted(ordering[origin]),sorted(ordering[v])]
assert max_neighbor_dist==9
print(json.dumps({'model':'bipartite Z6 incidence', 'four_element_forcing_sets':0,
   'five_element_forcing_sets':len(ordering), 'token_jump':jump,'token_slide':slide,
   'max_slide_distance_among_jump_neighbors':max_neighbor_dist,
   'example_jump_neighbor_pair_with_slide_distance_nine':example}, sort_keys=True))
