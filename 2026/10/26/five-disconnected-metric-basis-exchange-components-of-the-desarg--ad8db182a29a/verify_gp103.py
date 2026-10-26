"""Independent exhaustive verification on generalized Petersen GP(10,3).

No geometric 2-subset model or closed-form distance table is used.
Requires only the Python standard library.
"""
from itertools import combinations
from collections import Counter, deque
import json
n=10
adj=[set() for _ in range(2*n)]
def edge(u,v):
    adj[u].add(v)
    adj[v].add(u)
for i in range(n):
    edge(i,(i+1)%n)
    edge(i,n+i)
    edge(n+i,n+(i+3)%n)
assert len(adj)==20 and all(len(x)==3 for x in adj)
D=[]
for u in range(20):
    dist=[None]*20
    dist[u]=0
    q=deque([u])
    while q:
        a=q.popleft()
        for b in adj[a]:
            if dist[b] is None:
                dist[b]=dist[a]+1
                q.append(b)
    assert all(x is not None for x in dist)
    D.append(dist)

def good(B):
    return len({tuple(D[u][w] for w in B) for u in range(20)})==20
assert all(not good(B) for B in combinations(range(20),2))
B={frozenset(t) for t in combinations(range(20),3) if good(t)}
assert len(B)==160
E=Counter()
for t in B:
    for u in t:
        for v in range(20):
            if v not in t:
                nt=frozenset(t-{u}|{v})
                if nt in B:E[t]+=1
assert set(E.values())=={9}
components=[]
remaining=set(B)
profiles=Counter()
while remaining:
    start=next(iter(remaining))
    dist={start:0}
    q=deque([start])
    while q:
        A=q.popleft()
        for v in range(20):
            if v in A: continue
            for u in A:
                Z=frozenset(A-{u}|{v})
                if Z in B and Z not in dist:
                    dist[Z]=dist[A]+1
                    q.append(Z)
    components.append(set(dist))
    remaining.difference_update(dist)
    assert len(dist)==32
    profiles.update({tuple(Counter(dist.values()).get(d,0) for d in range(4)):1})
assert sorted(map(len,components))==[32]*5
# Explicit, independently checkable graph isomorphism to the bipartite
# Kneser representation. The mapping is GP index -> signed pair index.
from itertools import combinations as choose
pair_labels = tuple(choose(range(5), 2))
canonical_map = (0,17,6,11,9,10,7,16,1,19,18,3,12,5,14,8,13,2,15,4)
assert sorted(canonical_map) == list(range(20))
for u in range(20):
    su,au = divmod(canonical_map[u], 10)
    for v in range(20):
        sv,av = divmod(canonical_map[v], 10)
        expected = su != sv and set(pair_labels[au]).isdisjoint(pair_labels[av])
        assert (v in adj[u]) == expected
assert profiles=={(1,9,15,7):5}
print(json.dumps({
   'graph':'GP(10,3)', 'vertices':20, 'edges':30,
   'tested_pairs':190,'tested_triples':1140,
   'metric_dimension':3, 'bases':len(B),
   'component_sizes':sorted(map(len,components)),
   'edges_of_exchange_graph':sum(E.values())//2,
   'exchange_degree':9, 'component_distance_profile':[1,9,15,7],
   'component_diameter':3, 'explicit_isomorphism_confirmed':True,
}, sort_keys=True))
