#!/usr/bin/env python3
"""Exact exhaustive dodecahedral Hamilton-cycle switch graph certificate.
Uses only the Python standard library. Run: python verify_cycle_dfs.py
"""
from collections import deque, Counter
from itertools import combinations

N=20
E=tuple(sorted({tuple(sorted((i,(i+1)%10))) for i in range(10)}|
                {tuple(sorted((i,10+i))) for i in range(10)}|
                {tuple(sorted((10+i,10+(i+2)%10))) for i in range(10)}))
assert len(E)==30
adj=[set() for _ in range(N)]
for u,v in E: adj[u].add(v);adj[v].add(u)
assert all(len(x)==3 for x in adj)
index={e:i for i,e in enumerate(E)}
def make_mask(path):
    ans=0
    for i in range(N):
        e=tuple(sorted((path[i],path[(i+1)%N])))
        ans|=1<<index[e]
    return ans
cycles=[]
def dfs(path,used):
    if len(path)==N:
        if path[0] in adj[path[-1]] and path[1]<path[-1]:
            cycles.append(make_mask(path))
        return
    v=path[-1]
    for w in sorted(adj[v]):
        if not (used>>w)&1:
            dfs(path+[w],used|(1<<w))
dfs([0],1)
cycles=sorted(cycles)
assert len(cycles)==30 and len(set(cycles))==30

def distance(source):
    d=[-1]*N;d[source]=0;q=deque([source])
    while q:
        v=q.popleft()
        for w in adj[v]:
            if d[w]<0: d[w]=d[v]+1;q.append(w)
    return d
ant=[]
for v in range(N):
    far=[w for w,d in enumerate(distance(v)) if d==5]
    assert len(far)==1,(v,far)
    ant.append(far[0])
assert all(ant[ant[v]]==v for v in range(N))
assert all(tuple(sorted((ant[u],ant[v]))) in index for u,v in E)

def conjugate(mask):
    new=0
    for i,(u,v) in enumerate(E):
        if (mask>>i)&1:
            new|=1<<index[tuple(sorted((ant[u],ant[v])))]
    return new
ci={c:i for i,c in enumerate(cycles)}
partner=[ci[conjugate(c)] for c in cycles]
assert all(partner[i]!=i and partner[partner[i]]==i for i in range(30))

def simple_cycle_mask(mask):
    verts=set();local={v:set() for v in range(N)}
    for i,(u,v) in enumerate(E):
        if (mask>>i)&1:
            local[u].add(v);local[v].add(u);verts.update((u,v))
    if not verts or any(len(local[v])!=2 for v in verts):return False
    reached=set();q=[min(verts)]
    while q:
        v=q.pop()
        if v in reached:continue
        reached.add(v);q.extend(local[v]-reached)
    return reached==verts

R=[set() for _ in range(30)]
differences=Counter()
for i,j in combinations(range(30),2):
    x=cycles[i]^cycles[j]
    differences[x.bit_count()]+=1
    if x.bit_count()==8 and simple_cycle_mask(x):
        R[i].add(j);R[j].add(i)
assert sum(map(len,R))==120
assert all(len(s)==4 for s in R)
assert all(i not in R[i] and all(i in R[j] for j in R[i]) for i in range(30))
assert all(sum(1 for k in R[i] if k in R[j])==0 for i in range(30) for j in R[i])

def bfs(A,start):
    d={start:0};q=deque([start])
    while q:
        v=q.popleft()
        for w in A[v]:
            if w not in d:d[w]=d[v]+1;q.append(w)
    return d
assert max(max(bfs(R,v).values()) for v in range(30))==4
assert all(len(bfs(R,v))==30 for v in range(30))
color={0:0};q=deque([0])
while q:
    v=q.popleft()
    for w in R[v]:
        if w not in color: color[w]=1-color[v];q.append(w)
        else:assert color[w]!=color[v]
assert len(color)==30 and Counter(color.values())==Counter({0:15,1:15})
assert all(color[partner[i]]==1-color[i] for i in range(30))

orbits=sorted({tuple(sorted((i,partner[i]))) for i in range(30)})
assert len(orbits)==15
orbit_of={v:t for t,orb in enumerate(orbits) for v in orb}
Q=[set() for _ in range(15)]
multi=Counter()
for i in range(30):
    for j in R[i]:
        if i<j:
            u,v=sorted((orbit_of[i],orbit_of[j]))
            assert u!=v
            Q[u].add(v);Q[v].add(u);multi[(u,v)]+=1
assert len(multi)==30 and all(c==2 for c in multi.values())
assert all(len(s)==4 for s in Q)
assert all(len(bfs(Q,v))==15 for v in range(15))
triangles=[(i,j,k) for i in range(15) for j in Q[i] if j>i for k in Q[i]&Q[j] if k>j]
assert len(triangles)==10
assert all(sum(i in t for t in triangles)==2 for i in range(15))
assert all(sum((i in t and j in t) for t in triangles)==1 for i in range(15) for j in Q[i] if i<j)

P=[set() for _ in range(10)]
for a,b in combinations(range(10),2):
    if len(set(triangles[a])&set(triangles[b]))==1:
        P[a].add(b);P[b].add(a)
assert all(len(s)==3 for s in P)
assert sum(map(len,P))==30
assert len(bfs(P,0))==10
assert all(len(P[a]&P[b])==0 for a,b in combinations(range(10),2) if b in P[a])
assert all(len(P[a]&P[b])==1 for a,b in combinations(range(10),2) if b not in P[a])
# This (10,3,0,1) characterization uniquely identifies the Petersen graph.
# Every triangle node corresponds to one Petersen vertex, each Q node to an edge.
# For a quotient edge Q[u]-Q[v], its unique common triangle witnesses edge incidence.
# The color of the original vertex supplies the two sheets of Q x K_2.
for i in range(30):
    for j in range(30):
        if i==j:continue
        expect=orbit_of[j] in Q[orbit_of[i]] and color[i]!=color[j]
        assert (j in R[i])==expect

# Minimality: any symmetric difference has even cardinality and forms a disjoint
# union of simple cycles. The base graph has no 4- or 6-cycle.
assert all(not simple_cycle_mask((1<<a)|(1<<b)|(1<<c)|(1<<d)) for a,b,c,d in combinations(range(30),4))
# No 6-cycle: path search from each first vertex with a canonical min condition.
def count_simple_cycles(k):
    found=set()
    def go(path):
        if len(path)==k:
            if path[0] in adj[path[-1]]:
                ed=tuple(sorted(tuple(sorted((path[i],path[(i+1)%k]))) for i in range(k)))
                found.add(ed)
            return
        for w in adj[path[-1]]:
            if w not in path:go(path+[w])
    for v in range(N):go([v])
    return len(found)
assert count_simple_cycles(4)==0 and count_simple_cycles(6)==0
assert differences[8]==60
assert all(s>=8 for s in differences)
assert differences==Counter({8:60,10:60,12:30,14:120,16:75,18:60,20:30})
print('DFS_EXHAUSTIVE_PASS cycles=30 eight_switches=60 degree=4 diameter=4')
print('ANTIPODAL_QUOTIENT_PASS orbits=15 edges=30 triangles=10 derived_Petersen=10')
print('CANONICAL_DOUBLE_COVER_PASS 30 vertices 60 edges Petersen_line_double_cover')
print('SHARP_THRESHOLD_PASS lower_bound=8 connected_at=8')
