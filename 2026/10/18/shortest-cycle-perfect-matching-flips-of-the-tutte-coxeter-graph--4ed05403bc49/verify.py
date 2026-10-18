"""Exact matching and shortest-alternating-cycle flip census.

Run: python3 verify.py [optional-certificate-filename]
Uses only the Python standard library. Vertex sets and checks are finite and exact.
"""
import itertools
import json
import sys
from collections import Counter, deque

U = range(6)
duads = list(itertools.combinations(U, 2))
assert len(duads) == 15

# All partitions of six labels into three disjoint pairs.
def partitions(remaining):
    if not remaining:
        yield ()
        return
    a = min(remaining)
    for b in sorted(remaining - {a}):
        for rest in partitions(remaining - {a, b}):
            yield tuple(sorted(((a, b),) + rest))

synthemes = sorted(set(partitions(frozenset(U))))
assert len(synthemes) == 15
E = tuple((d, 15+s) for d in range(15) for s in range(15)
          if duads[d] in synthemes[s])
assert len(E) == 45
edge_index = {e:i for i,e in enumerate(E)}
g = [set() for _ in range(30)]
for u,v in E:
    g[u].add(v)
    g[v].add(u)
assert all(len(a) == 3 for a in g)

# Fix all left vertices in increasing order: each perfect matching occurs once.
choices = [[edge_index[(i,15+j)] for j in range(15)
            if duads[i] in synthemes[j]] for i in range(15)]
matchings = []
def enumerate_matchings(i,used,ids):
    if i == 15:
        matchings.append(tuple(sorted(ids)))
        return
    for e in choices[i]:
        v = E[e][1] - 15
        if not used >> v & 1:
            enumerate_matchings(i+1,used | 1<<v,ids+[e])
enumerate_matchings(0,0,[])
matchings = sorted(set(matchings))
assert len(matchings) == 288
M = [frozenset(m) for m in matchings]

# Complement of a perfect matching is a 2-factor because the graph is cubic.
def complement_type(m):
    h = [set() for _ in range(30)]
    for eid,(u,v) in enumerate(E):
        if eid not in m:
            h[u].add(v)
            h[v].add(u)
    assert all(len(x) == 2 for x in h)
    seen=set(); sizes=[]
    for r in range(30):
        if r in seen: continue
        pending=[r]; seen.add(r); count=0
        while pending:
            z=pending.pop();count+=1
            for w in h[z]:
                if w not in seen:seen.add(w);pending.append(w)
        sizes.append(count)
    return tuple(sorted(sizes))
classes = tuple(complement_type(m) for m in M)
assert Counter(classes) == {(30,):144,(10,20):144}

# All undirected graph cycles of length 8, canonicalized by their edge sets.
cycles=set()
def walk(path):
    if len(path)==8:
        if path[0] in g[path[-1]]:
            eids = tuple(sorted(edge_index[tuple(sorted((path[i],path[(i+1)%8])))]
                                for i in range(8)))
            cycles.add(eids)
        return
    for w in sorted(g[path[-1]]):
        if w > path[0] and w not in path:
            walk(path+[w])
for v in range(30):
    walk([v])
cycles = sorted(cycles)
assert len(cycles)==90

idx={m:i for i,m in enumerate(M)}
links=set(); cycle_counts=[]
for cy in cycles:
    chosen=set(cy)
    nalt=0
    for i,m in enumerate(M):
        if len(m & chosen) == 4:
            nalt+=1
            replaced=frozenset(m ^ chosen)
            assert replaced in idx, (i,cy)
            j=idx[replaced]
            links.add((min(i,j),max(i,j)))
    cycle_counts.append(nalt)
assert Counter(cycle_counts)=={32:90}  # 16 undirected matching-flips per cycle
links=sorted(links)
assert len(links)==1440
# Independently compare every pair of states to rule out omitted 8-cycle flips.
assert links == [(i,j) for i in range(288) for j in range(i+1,288)
                 if len(M[i]^M[j])==8]

adj=[[] for _ in range(288)]
for i,j in links:
    adj[i].append(j);adj[j].append(i)
assert Counter(map(len,adj)) == {10:288}
assert all(classes[i] != classes[j] for i,j in links)
profiles=[]; ecc=[]
for source in range(288):
    distances=[-1]*288; distances[source]=0
    q=deque([source])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if distances[v]<0:
                distances[v]=distances[u]+1
                q.append(v)
    assert -1 not in distances
    profiles.append(tuple(Counter(distances)[k] for k in range(7)))
    ecc.append(max(distances))
prof_H=(1,10,42,97,101,37,0)
prof_T=(1,10,45,97,96,37,2)
assert all((profiles[i]==prof_H and ecc[i]==5) if classes[i]==(30,)
           else (profiles[i]==prof_T and ecc[i]==6) for i in range(288))
assert Counter(ecc)=={5:144,6:144}

certificate = {
    'description': 'Exact perfect-matching and eight-cycle flip census of the duad-syntheme incidence graph',
    'duads': [list(x) for x in duads],
    'synthemes': [[list(p) for p in s] for s in synthemes],
    'edges': [list(e) for e in E],
    'eight_cycles_as_edge_indices': [list(c) for c in cycles],
    'matchings_as_edge_indices': [list(m) for m in matchings],
    'complement_cycle_types': [list(c) for c in classes],
    'flip_edges_as_matching_indices': [list(e) for e in links],
    'distance_histograms_from_every_matching': [list(p) for p in profiles]
}
raw=(json.dumps(certificate,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n').encode('utf-8')
if len(sys.argv)>1:
    path=sys.argv[1]
    with open(path,'wb') as out:out.write(raw)
print('graph_vertices=30 graph_edges=45 8_cycles=90')
print('perfect_matchings=288 complement_30=144 complement_10_20=144')
print('eight_cycle_flip_edges=1440 degree=10 connected=yes bipartite_by_complement=yes')
print('hamiltonian_complement_distances='+str(prof_H))
print('split_complement_distances='+str(prof_T))
print('radius=5 diameter=6 eccentricities_5=144 eccentricities_6=144')
print('alternating_per_cycle=32 certificates_bytes='+str(len(raw)))
print('VERIFY_OK')
