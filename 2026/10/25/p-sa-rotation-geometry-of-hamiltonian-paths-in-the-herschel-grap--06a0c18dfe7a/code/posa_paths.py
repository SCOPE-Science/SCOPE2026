# Exhaustive Hamiltonian paths and Posa rotations of an explicitly defined graph.
from collections import Counter, deque

V = range(11)
E = set()
for x,y,rr in ((0,1,(5,6)),(1,2,(7,8)),(2,0,(9,10))):
    for z in rr:
        E.add(tuple(sorted((x,z))))
        E.add(tuple(sorted((y,z))))
for z in (5,7,9): E.add((3,z))
for z in (6,8,10): E.add((4,z))
N=[set() for _ in V]
for x,y in E:
    N[x].add(y);N[y].add(x)
assert len(E)==18 and sorted(map(len,N)) == [3]*8+[4]*3

def canon(path):
    x=tuple(path)
    return min(x,x[::-1])

states=set()
def explore(path,mask):
    if len(path)==11:
        states.add(canon(path))
        return
    for v in sorted(N[path[-1]]):
        if not (mask >> v)&1:
            explore(path+[v],mask | (1<<v))
for r in range(5,11): explore([r],1<<r)
assert len(states)==222

adj={p:set() for p in states}
for p in states:
    for order in (p,p[::-1]):
        for i in range(9):
            if order[-1] not in N[order[i]]: continue
            q=canon(order[:i+1]+(order[-1],)+order[i+1:-1][::-1])
            assert q in states and q!=p
            adj[p].add(q)
assert len(adj)==222 and all(len(v)==4 for v in adj.values())
assert all(p in adj[q] for p in states for q in adj[p])
assert sum(map(len,adj.values()))//2==444
hist=Counter()
for root in states:
    dist={root:0}; todo=deque([root])
    while todo:
        u=todo.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v]=dist[u]+1;todo.append(v)
    hist[(len(dist),max(dist.values()))]+=1
assert hist == {(222,8):198,(222,9):24},hist
print('POSA_CHECK_OK graph=Herschel graph_vertices=11 graph_edges=18 undirected_hamiltonian_paths=222 posa_edges=444 all_degree=4 components=1 radius=8 diameter=9 ecc8=198 ecc9=24')
