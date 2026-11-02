#!/usr/bin/env python3
"""Exact 60-site two-absorber Krylov classification; Python standard library only."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations

# Explicit abstract icosahedral graph: two poles and two interlaced 5-rings.
V12 = range(12)
base_edges = set()
def put(a,b):
    assert a != b
    base_edges.add(tuple(sorted((a,b))))
for i in range(5):
    a, b = 1+i, 6+i
    for p,q in ((0,a),(11,b),(a,1+(i+1)%5),(b,6+(i+1)%5),
                (a,b),(a,6+(i-1)%5)):
        put(p,q)
assert len(base_edges) == 30
N = [set() for _ in V12]
for a,b in base_edges:
    N[a].add(b);N[b].add(a)
assert all(len(n)==5 for n in N)

# Truncation: a 60-vertex flag (u,v) stands at the u-end of a base edge uv.
flags = sorted((u,v) for u in V12 for v in N[u])
flag_id = {p:i for i,p in enumerate(flags)}
assert len(flags)==60
G = [set() for _ in range(60)]
def link(p,q):
    assert p != q
    G[p].add(q);G[q].add(p)
for u in V12:
    for v,w in combinations(sorted(N[u]),2):
        if w in N[v]:
            link(flag_id[u,v], flag_id[u,w])
for u,v in base_edges:
    link(flag_id[u,v], flag_id[v,u])
assert all(len(g)==3 for g in G)
assert sum(map(len,G))==180

# Every icosahedral automorphism is determined by the image of one vertex
# (12 possibilities), an adjacent neighbor (5), and the link-cycle direction (2).
def link_cycle(v):
    n=sorted(N[v]); ring=[n[0]]
    follow=min(N[ring[0]] & set(n))
    ring.append(follow)
    while len(ring)<5:
        p=next(t for t in N[ring[-1]] & set(n) if t!=ring[-2])
        assert p not in ring
        ring.append(p)
    assert ring[0] in N[ring[-1]]
    return ring

automorphisms=[]
for target in V12:
    cycle=link_cycle(target)
    for start in range(5):
        for orientation in (-1,1):
            p={0:target}
            for i in range(5):
                p[1+i]=cycle[(start+orientation*i)%5]
            for i in range(5):
                a,b=p[1+i],p[1+(i+1)%5]
                other=(N[a] & N[b]) - {target}
                assert len(other)==1
                p[6+i]=next(iter(other))
            missing=set(V12)-set(p.values())
            assert len(missing)==1
            p[11]=next(iter(missing))
            perm=tuple(p[i] for i in V12)
            assert len(set(perm))==12
            assert {tuple(sorted((perm[u],perm[v]))) for u,v in base_edges}==base_edges
            automorphisms.append(tuple(flag_id[perm[u],perm[v]] for u,v in flags))
assert len(set(automorphisms))==120

# Pair-orbit partition certifies that only 23 integer ranks are necessary.
orbits=defaultdict(set)
for a,b in combinations(range(60),2):
    canonical=min(tuple(sorted((p[a],p[b]))) for p in automorphisms)
    orbits[canonical].add((a,b))
assert sum(map(len,orbits.values()))==1770
assert len(orbits)==23
assert Counter(map(len,orbits.values()))==Counter({60:12,120:8,30:3})

# P(A)=0, degree 15, checked on every basis vector by integer arithmetic.
# The input factors are written from constant coefficient upwards.
factors=[(-3,1),(-1,1),(2,1),(-3,-1,1),(-4,1,1),
         (-1,1,1),(1,3,1),(1,7,-2,-3,1)]
poly=[1]
for f in factors:
    new=[0]*(len(poly)+len(f)-1)
    for i,c in enumerate(poly):
        for j,d in enumerate(f):new[i+j]+=c*d
    poly=new
assert len(poly)==16 and poly[-1]==1

def timesA(v):
    w=[0]*60
    for u,x in enumerate(v):
        if x:
            for j in G[u]:w[j]+=x
    return w

def powers(j):
    v=[int(k==j) for k in range(60)]
    out=[]
    for i in range(16):
        out.append(v)
        v=timesA(v)
    assert all(sum(poly[i]*out[i][k] for i in range(16))==0
               for k in range(60))
    return out[:15]

all_power=[powers(j) for j in range(60)]

def exact_rank(columns):
    # Rational column elimination, using no modular-rank heuristic.
    basis={}
    for col in columns:
        v=[Fraction(z) for z in col]
        for pivot in sorted(basis):
            c=v[pivot]
            if c:
                b=basis[pivot]
                for i in range(pivot,60):
                    v[i]-=c*b[i]
        pivot=next((i for i,z in enumerate(v) if z),None)
        if pivot is not None:
            c=v[pivot]
            basis[pivot]=[z/c if i>=pivot else Fraction(0)
                          for i,z in enumerate(v)]
    return len(basis)

assert exact_rank(all_power[0])==15
from collections import deque

def shortest_paths(a,b):
    distances={a:0};ways={a:1};queue=deque([a])
    while queue:
        u=queue.popleft()
        for v in G[u]:
            if v not in distances:
                distances[v]=distances[u]+1;ways[v]=ways[u];queue.append(v)
            elif distances[v]==distances[u]+1:
                ways[v]+=ways[u]
    return distances[b],ways[b]

opposite={}
for a in range(60):
    far=[b for b in range(60) if shortest_paths(a,b)[0]==9]
    assert len(far)==1
    opposite[a]=far[0]
assert all(opposite[opposite[a]]==a for a in range(60))
spokes={tuple(sorted((flag_id[u,v],flag_id[v,u]))) for u,v in base_edges}
special27=(spokes
           | {tuple(sorted((a,opposite[b]))) for a,b in spokes}
           | {tuple(sorted((b,opposite[a]))) for a,b in spokes})
print("special27",len(spokes),len(special27), sorted(special27-spokes)[:5])
assert len(special27)==60

results=[]
for rep,members in sorted(orbits.items()):
    a,b=rep
    rank=exact_rank(all_power[a]+all_power[b])
    results.append((a,b,len(members),rank,*shortest_paths(a,b)))
    print('pair',a,b,'multiplicity',len(members),'rank',rank,'distance/paths',shortest_paths(a,b))
by_rank=Counter()
for a,b,count,rank,distance,ways in results:
    by_rank[rank]+=count
assert by_rank=={15:30,27:60,28:120,29:1560},by_rank
assert all(distance==9 for a,b,count,rank,distance,ways in results if rank==15)
assert sorted((d,count) for a,b,count,r,d,w in results if r==27)==[(1,30),(8,30)]
assert all(distance==5 for a,b,count,rank,distance,ways in results if rank==28)
assert sum(len(members) for rep,members in orbits.items())==1770
for a,b,count,rank,dist,ways in results:
    predicted = (15 if dist==9 else 27 if (a,b) in special27
                 else 28 if dist==5 and ways>1 else 29)
    assert predicted==rank,(a,b,count,rank,dist,ways,predicted)

print('verified pair rank counts:',sorted(by_rank.items()))
print('single absorber rank: 15; two absorber maximum: 29; orbit count: 23')
print('PASS: polynomial identity, exact rational ranks, symmetries, full 1770-pair orbit coverage')
