"""Independent deletion/girth computation for the 24-vertex McGee graph.
No seven-cycle list and no results from the other verifier are imported.
"""
from collections import deque
from itertools import combinations, product

n=24
adj={i: set() for i in range(n)}
for i in range(n):
    j=(i+1)%n
    adj[i].add(j);adj[j].add(i)
for i in range(n):
    j=(i+(12 if i%3==0 else (7 if i%3==1 else -7)))%n
    adj[i].add(j);adj[j].add(i)
assert all(len(adj[i])==3 for i in range(n))

def girth_after(deleted):
    allowed=set(range(n))-set(deleted)
    best=10**9
    for origin in allowed:
        dist={origin:0}; parent={origin:None};q=deque([origin])
        while q:
            v=q.popleft()
            for w in adj[v].intersection(allowed):
                if w not in dist:
                    dist[w]=dist[v]+1;parent[w]=v;q.append(w)
                elif parent[v]!=w:
                    best=min(best,dist[v]+dist[w]+1)
    return best

assert girth_after(())==7
assert all(girth_after(x)==7 for x in combinations(range(n),3))
answer={x for x in combinations(range(n),4) if girth_after(x)>7}
assert len(answer)==20
assert all(girth_after(x)==8 for x in answer)
expected={tuple(sorted(x)) for x in product((0,12),(3,15),(6,18),(9,21))}
expected.update({(1,5,13,17),(2,10,14,22),(4,8,16,20),(7,11,19,23)})
assert answer==expected

edge_count=0
components=[];remaining=set(answer)
while remaining:
    q=[remaining.pop()]
    for u in q:
        next_states=[v for v in remaining if len(set(u)&set(v))==3]
        for v in next_states:
            remaining.remove(v);q.append(v)
    components.append(len(q))
for u,v in combinations(answer,2):
    if len(set(u)&set(v))==3:edge_count+=1
assert sorted(components)==[1,1,1,1,16]
assert edge_count==32
print('girth_before=7; no_size_three_transversal=True; checked=2024')
print('all_optima_raise_girth_to=8; size_four_candidates=10626; optima=20')
print('component_sizes=16,1,1,1,1; exchange_edges=32')
print('VERIFY_OK')
