#!/usr/bin/env python3
"""Independent exact-cover certificate of the dodecahedral switch structure.
Only Python standard library. Run: python verify_matching_alt.py
"""
from itertools import combinations
from collections import deque,Counter
n=10
edges=set()
for j in range(n):
    edges.add(frozenset((j,(j+1)%n)))
    edges.add(frozenset((j,n+j)))
    edges.add(frozenset((n+j,n+(j+2)%n)))
assert len(edges)==30
neighbors={i:set() for i in range(20)}
for e in edges:
    a,b=tuple(e);neighbors[a].add(b);neighbors[b].add(a)

def all_matchings(available,selected):
    if not available:
        yield frozenset(selected);return
    u=min(available)
    for v in sorted(neighbors[u]&available):
        yield from all_matchings(available-{u,v},selected+[frozenset((u,v))])
M=list(all_matchings(set(range(20)),[]))
assert len(M)==36,(len(M))

def components(edge_collection):
    a={v:set() for v in range(20)}
    for e in edge_collection:
        u,v=tuple(e);a[u].add(v);a[v].add(u)
    left=set(range(20));parts=[]
    while left:
        s=left.pop();component={s};queue=[s]
        for u in queue:
            for v in a[u]-component:
                component.add(v);queue.append(v)
        left-=component
        parts.append(component)
    return parts
cycles=set()
other=0
for matching in M:
    complement=edges-matching
    assert len(complement)==20
    if len(components(complement))==1:cycles.add(frozenset(complement))
    else:other+=1
assert len(cycles)==30 and other==6
C=sorted(cycles,key=lambda es:tuple(sorted(tuple(sorted(x)) for x in es)))
R={i:set() for i in range(30)}
for i,j in combinations(range(30),2):
    d=C[i]^C[j]
    if len(d)!=8:continue
    act=set().union(*d)
    subgraph={x:set() for x in act}
    for e in d:
        a,b=tuple(e);subgraph[a].add(b);subgraph[b].add(a)
    assert all(len(v)==2 for v in subgraph.values())
    reached={next(iter(act))};todo=list(reached)
    while todo:
        for v in subgraph[todo.pop()]:
            if v not in reached: reached.add(v);todo.append(v)
    assert reached==act
    R[i].add(j);R[j].add(i)
assert all(len(s)==4 for s in R.values())
assert sum(map(len,R.values()))==120
# Get antipodes without reference to the cycle-enumeration search.
A={}
for start in neighbors:
    distance={start:0};queue=deque([start])
    while queue:
        u=queue.popleft()
        for v in neighbors[u]:
            if v not in distance:distance[v]=1+distance[u];queue.append(v)
    far=[v for v,d in distance.items() if d==5]
    assert len(far)==1
    A[start]=far[0]
Cnum={c:i for i,c in enumerate(C)}
partner={i:Cnum[frozenset(frozenset((A[a],A[b])) for a,b in (tuple(e) for e in C[i]))] for i in R}
assert all(partner[partner[i]]==i and partner[i]!=i for i in R)
# Quotient under the antipodal involution.
pairs=sorted({tuple(sorted((i,partner[i]))) for i in R})
assert len(pairs)==15
rep={x:j for j,pair in enumerate(pairs) for x in pair}
Q={j:set() for j in range(15)}
for x in R:
    for y in R[x]:
        Q[rep[x]].add(rep[y])
assert all(len(a)==4 for a in Q.values())
triangles=[]
for x,y,z in combinations(range(15),3):
    if y in Q[x] and z in Q[x] and z in Q[y]:triangles.append((x,y,z))
assert len(triangles)==10
T={i:set() for i in range(10)}
for a,b in combinations(range(10),2):
    if set(triangles[a])&set(triangles[b]):
        assert len(set(triangles[a])&set(triangles[b]))==1
        T[a].add(b);T[b].add(a)
assert all(len(s)==3 for s in T.values())
# Explicit backtracking isomorphism to Petersen graph realized as KG(5,2).
S=list(combinations(range(5),2))
P={j:{l for l in range(10) if j!=l and not(set(S[j])&set(S[l]))} for j in range(10)}
assert all(len(s)==3 for s in P.values())

def match(mapping,available):
    if len(mapping)==10:return dict(mapping)
    # Try the next vertex with the maximum number of previously mapped neighbors.
    v=max((j for j in range(10) if j not in mapping),key=lambda x:(len(T[x]&mapping.keys()),-x))
    for w in sorted(available):
        if all(((u in T[v])==(mapping[u] in P[w])) for u in mapping):
            out=match({**mapping,v:w},available-{w})
            if out:return out
    return None
iso=match({},set(range(10)))
assert iso is not None
assert all((v in T[u])==(iso[v] in P[iso[u]]) for u in T for v in T if u!=v)
# Lifting triangles: Q is the line graph of its triangle-intersection graph.
assert all(len([j for j,t in enumerate(triangles) if v in t])==2 for v in Q)
assert all((v in Q[u]) == (bool(set([j for j,t in enumerate(triangles) if u in t]) & set([j for j,t in enumerate(triangles) if v in t]))) for u in Q for v in Q if u!=v)
col={0:0};q=deque([0])
while q:
    a=q.popleft()
    for b in R[a]:
        if b in col: assert col[b]!=col[a]
        else:col[b]=1-col[a];q.append(b)
assert len(col)==30
assert all(col[i]!=col[partner[i]] for i in R)
assert all((j in R[i])==(rep[j] in Q[rep[i]] and col[j]!=col[i]) for i in R for j in R if i!=j)
print('INDEPENDENT_EXACT_COVER_PASS perfect_matchings=36 cycles=30 remaining_2_factors=6')
print('PETERSEN_ISOMORPHISM_PASS quotient_triangles=10 Kneser5_2_verified=1')
print('SHEET_LIFT_PASS 8_switch_graph=double_cover_line_Petersen')
