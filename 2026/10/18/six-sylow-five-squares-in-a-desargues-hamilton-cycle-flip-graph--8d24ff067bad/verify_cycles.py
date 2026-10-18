#!/usr/bin/env python3
"""Independent Hamilton-tour enumeration on generalized Petersen G(10,3).
No external modules are required. The invariant is the Hamilton-preserving
single alternating-cycle exchange of perfect matching complements.
"""
from collections import Counter, deque

N = 20
edges = set()
for k in range(10):
    for i,j in ((k,(k+1)%10),(k,k+10),(k+10,10+(k+3)%10)):
        edges.add(tuple(sorted((i,j))))
assert len(edges)==30
adj=[set() for _ in range(N)]
for x,y in edges:
    adj[x].add(y)
    adj[y].add(x)
assert all(len(a)==3 for a in adj)

def canonical_edge(a,b):
    return (min(a,b),max(a,b))

# Fix vertex 0 and count each undirected Hamilton cycle exactly once by
# requiring second vertex < last vertex.
tours=set()
def extend(path, visited):
    u=path[-1]
    if len(path)==N:
        if path[0] in adj[u] and path[1]<path[-1]:
            tour=frozenset(canonical_edge(path[i],path[(i+1)%N]) for i in range(N))
            assert len(tour)==N
            tours.add(tour)
        return
    for v in sorted(adj[u]):
        if not ((visited>>v)&1):
            extend(path+[v], visited | (1<<v))

extend([0],1)
assert len(tours)==24, len(tours)
T=sorted(tours,key=lambda c:tuple(sorted(c)))
M=[edges-c for c in T]
assert len({frozenset(x) for x in M})==24

def is_one_cycle(ed):
    deg=Counter(v for x,y in ed for v in (x,y))
    if not deg or any(k!=2 for k in deg.values()):
        return False
    graph={v:set() for v in deg}
    for x,y in ed:
        graph[x].add(y);graph[y].add(x)
    seen={next(iter(graph))};todo=list(seen)
    for x in todo:
        for y in graph[x]:
            if y not in seen:seen.add(y);todo.append(y)
    return len(seen)==len(deg)

flip={10:set(),18:set()}
other=Counter()
for i in range(len(T)):
    for j in range(i+1,len(T)):
        difference=M[i]^M[j]
        if is_one_cycle(difference):
            flip.setdefault(len(difference),set()).add((i,j))
        else:
            other[len(difference)]+=1
assert {k:len(v) for k,v in flip.items()}=={10:84,18:60}
assert dict(other)=={12:60,16:60,20:12}

def structure(ed):
    neigh=[set() for _ in T]
    for x,y in ed:
        neigh[x].add(y);neigh[y].add(x)
    distance=[]
    for s in range(len(T)):
        d={s:0};q=deque([s])
        while q:
            u=q.popleft()
            for v in neigh[u]:
                if v not in d:d[v]=d[u]+1;q.append(v)
        distance.append(d)
    comp_sizes=[];rem=set(range(len(T)))
    while rem:
        i=min(rem);seen={i};todo=[i];rem.remove(i)
        for u in todo:
            for v in neigh[u]&rem:
                seen.add(v);rem.remove(v);todo.append(v)
        comp_sizes.append(len(seen))
    return neigh,distance,sorted(comp_sizes)

n10,d10,c10=structure(flip[10]);n18,d18,c18=structure(flip[18])
assert c10==[24] and c18==[12,12]
assert Counter(map(len,n10))=={7:24}
assert Counter(map(len,n18))=={5:24}
assert all(Counter(di.values())=={0:1,1:7,2:16} for di in d10)
special={(i,j) for i,j in flip[10] if not (n10[i]&n10[j])}
assert len(special)==24
sp,_,sc=structure(special)
assert sc==[4]*6
assert all(len(n)==2 for n in sp)
# Check each special-component induces an actual four-cycle; between
# every two components the remaining edges form one perfect matching.
fibers=[];remaining=set(range(len(T)))
while remaining:
    seed=min(remaining);seen={seed};todo=[seed];remaining.remove(seed)
    for i in todo:
        for j in sp[i]&remaining:
            seen.add(j);todo.append(j);remaining.remove(j)
    fibers.append(seen)
for i,A in enumerate(fibers):
    assert sum((j in n10[a]) for a in A for j in A)//2==4
    for B in fibers[i+1:]:
        cross={(a,b) for a in A for b in B if b in n10[a]}
        assert len(cross)==4
        assert {a for a,b in cross}==A and {b for a,b in cross}==B

print('graph=G(10,3) vertices=20 edges=30')
print('Hamilton_cycles=24')
print('Hamilton_preserving_single_cycle_flips_by_length=10:84,18:60')
print('non_single_cycle_pairs_by_length=12:60,16:60,20:12')
print('10_flip_degree=7 10_flip_edges=84 10_flip_radius=2 10_flip_diameter=2')
print('18_flip_degree=5 18_flip_component_sizes=12,12')
print('exceptional_edges_no_common_neighbor=24')
print('fiber_structure=6C4 inter_fiber_perfect_matchings=15')
print('VERIFY_OK')
