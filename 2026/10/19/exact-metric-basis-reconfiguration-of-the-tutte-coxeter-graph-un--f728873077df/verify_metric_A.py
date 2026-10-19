#!/usr/bin/env python3
"""Exhaustive exact certificate for metric-basis exchange on the Tutte eight-cage.
Uses duads/synthemes, pair-separation bit masks, and S6 orbit reduction.
No external packages or files are required.
"""
from itertools import combinations
from collections import Counter, deque

V = tuple(range(6))
DUADS = tuple(combinations(V, 2))

def factorizations(rem):
    if not rem:
        yield ()
        return
    a = rem[0]
    for b in rem[1:]:
        for rest in factorizations(tuple(x for x in rem if x not in (a,b))):
            yield ((a,b),) + rest

SYNTHEMES = tuple(factorizations(V))
assert len(DUADS) == len(SYNTHEMES) == 15
idx_duad = {x:i for i,x in enumerate(DUADS)}
idx_syntheme = {tuple(sorted(x)):i+15 for i,x in enumerate(SYNTHEMES)}
adj=[set() for _ in range(30)]
for i,p in enumerate(DUADS):
    for j,m in enumerate(SYNTHEMES):
        if p in m:
            adj[i].add(15+j);adj[15+j].add(i)
assert all(len(s)==3 for s in adj)

def distances(s):
    d=[-1]*30; d[s]=0; Q=deque([s])
    while Q:
        u=Q.popleft()
        for v in adj[u]:
            if d[v]<0: d[v]=d[u]+1;Q.append(v)
    assert -1 not in d
    return d
D=[distances(u) for u in range(30)]
assert max(map(max,D))==4
# Each bit represents a distinct unordered pair (u,v).
separation=[0]*30
for u in range(30):
    for v in range(u+1,30):
        j=u*30+v
        for w in range(30):
            if D[w][u]!=D[w][v]:separation[w]|=(1<<j)
full=0
for x in separation:full|=x

def resolved(S):
    x=0
    for s in S:x|=separation[s]
    return x==full
counts={}
for k in range(1,7):
    B=[S for S in combinations(range(30),k) if resolved(S)]
    counts[k]=len(B)
    if B: break
assert counts=={1:0,2:0,3:0,4:0,5:0,6:32460},counts
bases=B
profile=Counter(sum(x<15 for x in S) for S in bases)
assert profile=={2:7470,3:17520,4:7470},profile
ids={S:i for i,S in enumerate(bases)}
n=len(bases)
move=[[] for _ in range(n)]
for i,S in enumerate(bases):
    inside=set(S)
    for u in S:
        for v in range(30):
            if v in inside:continue
            T=tuple(sorted((inside-{u})|{v}))
            j=ids.get(T)
            if j is not None:move[i].append(j)
assert sum(map(len,move))%2==0
m=sum(map(len,move))//2
assert m==403020,m
assert all(len(x)==len(set(x)) for x in move)
assert all(i in move[j] for i,N in enumerate(move) for j in N)
Q=deque([0]);seen={0}
while Q:
    for w in move[Q.popleft()]:
        if w not in seen:seen.add(w);Q.append(w)
assert len(seen)==n
# Adjacent transpositions of the underlying six symbols generate S6.
gens=[]
for a in range(5):
    def perm(x):return a+1 if x==a else (a if x==a+1 else x)
    gen=[]
    for d in DUADS:gen.append(idx_duad[tuple(sorted(perm(x) for x in d))])
    for matching in SYNTHEMES:
        new=tuple(sorted(tuple(sorted(perm(x) for x in e)) for e in matching))
        gen.append(idx_syntheme[new])
    assert sorted(gen)==list(range(30))
    for u in range(30):
        assert {gen[v] for v in adj[u]}==adj[gen[u]]
    gens.append(gen)
# Orbit partition; each basis appears in exactly one orbit, without assumptions
# about a larger automorphism group.
unseen=set(range(n));orbits=[];reps=[]
while unseen:
    start=min(unseen);orbit={start};Q=deque([start])
    while Q:
        i=Q.popleft()
        for g in gens:
            t=ids[tuple(sorted(g[z] for z in bases[i]))]
            if t not in orbit:orbit.add(t);Q.append(t)
    unseen-=orbit
    orbits.append(orbit);reps.append(start)
assert len(orbits)==62
assert Counter(map(len,orbits))=={720:32,360:24,180:2,120:2,90:2}
# Automorphisms preserve graph distance and eccentricity; breadth-first
# searches from one representative in each orbit cover every starting state.
ecc_by_size=Counter();exception=[]
for orbit,start in zip(orbits,reps):
    distances_to=[-1]*n;distances_to[start]=0
    Q=deque([start]);seen_n=1;ecc=0
    while Q:
        u=Q.popleft()
        newdist=distances_to[u]+1
        for v in move[u]:
            if distances_to[v]<0:
                distances_to[v]=newdist;seen_n+=1
                ecc=max(ecc,newdist);Q.append(v)
    assert seen_n==n
    ecc_by_size[ecc]+=len(orbit)
    if ecc==8:exception.append((bases[start],len(orbit)))
assert ecc_by_size=={7:31740,8:720},ecc_by_size
assert len(exception)==1 and exception[0]==((0,1,12,15,21,22),720)
assert len(exception[0][0])==6
# A token slide is a token jump along a cage edge; use the original
# incidence adjacency to filter the fully enumerated jump neighbors.
slide=[[] for _ in bases]
for i,S in enumerate(bases):
    for j in move[i]:
        out=next(x for x in S if x not in bases[j])
        dest=next(x for x in bases[j] if x not in S)
        if dest in adj[out]:slide[i].append(j)
slide_edges=sum(map(len,slide))//2
assert slide_edges==55440,slide_edges
slide_ecc=Counter()
for orb,root in zip(orbits,reps):
    dd=[-1]*n;dd[root]=0;Q=deque([root]);ct=1;mx=0
    while Q:
        u=Q.popleft()
        for v in slide[u]:
            if dd[v]<0:
                dd[v]=dd[u]+1;mx=max(mx,dd[v]);ct+=1;Q.append(v)
    assert ct==n
    slide_ecc[mx]+=len(orb)
assert slide_ecc=={17:3780,18:11040,19:10440,20:7200},slide_ecc
print('METRIC_DIMENSION=6')
print('METRIC_BASES=32460')
print('SPLIT_BY_DUAD_COUNT=2:7470,3:17520,4:7470')
print('TOKEN_JUMP_GRAPH_VERTICES=32460')
print('TOKEN_JUMP_GRAPH_EDGES=403020')
print('TOKEN_JUMP_GRAPH_CONNECTED=1')
print('S6_ORBITS=62;SIZES=720:32,360:24,180:2,120:2,90:2')
print('RADIUS=7;DIAMETER=8;ECCENTRICITIES=7:31740,8:720')
print('ECCENTRICITY_8_SINGLE_S6_ORBIT_REP=(0,1,12,15,21,22)')
print('TOKEN_SLIDE_GRAPH_EDGES=55440;CONNECTED=1')
print('TOKEN_SLIDE_RADIUS=17;DIAMETER=20;ECCENTRICITIES=17:3780,18:11040,19:10440,20:7200')
print('VERIFY_OK')
