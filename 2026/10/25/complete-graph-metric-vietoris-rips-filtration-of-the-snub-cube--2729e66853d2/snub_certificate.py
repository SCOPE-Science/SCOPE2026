#!/usr/bin/env python3
"""Exact combinatorial and Forman-Morse verification for the snub-cube graph Rips filtration.

Only the Python standard library is required. Coordinates used for graph construction
are rational approximations in a certified open distance gap; all subsequent work
is integer and combinatorial.
"""
from fractions import Fraction
from itertools import permutations, product
from collections import Counter, deque, defaultdict
import heapq

# Rational point in the open interval bracketing the real root of t^3+t^2+t=1.
t = Fraction(543689, 1000000)
base = (Fraction(1), t, 1/t)
points = []
for p in permutations(range(3)):
    parity = sum(p[i] > p[j] for i in range(3) for j in range(i+1,3)) % 2
    for signs in product((-1, 1), repeat=3):
        if sum(a == 1 for a in signs) % 2 == parity:
            points.append(tuple(signs[i]*base[p[i]] for i in range(3)))
assert len(points) == len(set(points)) == 24

# The squared edge threshold 7/2 is strictly between the first two distance shells.
# Their numerical positions are about 2.591 and 5.182; exact comparisons below
# use rational arithmetic and do not rely on rounding.
G = [0]*24
sqdist = lambda u,v: sum((a-b)**2 for a,b in zip(u,v))
for i in range(24):
    for j in range(i+1,24):
        d2 = sqdist(points[i],points[j])
        if d2 < Fraction(7,2):
            G[i] |= 1 << j
            G[j] |= 1 << i
assert all(x.bit_count() == 5 for x in G)
assert sum(x.bit_count() for x in G)//2 == 60

# Certify that perturbation from the exact root to t cannot change edge ordering:
# interval rational endpoints bracket root and every squared distance stays on
# the same side of 7/2 throughout, by interval bounds of |coordinate differences|.
lo, hi = Fraction(543688, 1000000), Fraction(543690, 1000000)
assert lo**3+lo**2+lo-1 < 0 < hi**3+hi**2+hi-1

def interval_coord(sign, i):
    if i == 0: return (Fraction(sign),Fraction(sign))
    if i == 1: return ((lo,hi) if sign>0 else (-hi,-lo))
    return ((1/hi,1/lo) if sign>0 else (-1/lo,-1/hi))

# Enumerate the symbolic coordinate patterns separately from their evaluated values.
patterns=[]
for p in permutations(range(3)):
    parity=sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))%2
    for signs in product((-1,1),repeat=3):
        if sum(x==1 for x in signs)%2 == parity:
            patterns.append(tuple((signs[i],p[i]) for i in range(3)))
assert len(patterns)==24
for i in range(24):
 for j in range(i+1,24):
    low,high=Fraction(0),Fraction(0)
    for (sa,a),(sb,b) in zip(patterns[i],patterns[j]):
        aa=interval_coord(sa,a);bb=interval_coord(sb,b)
        dlow=aa[0]-bb[1];dhigh=aa[1]-bb[0]
        mn=Fraction(0) if dlow<=0<=dhigh else min(dlow**2,dhigh**2)
        mx=max(dlow**2,dhigh**2)
        low+=mn;high+=mx
    assert (high<Fraction(7,2)) if (G[i]>>j)&1 else (low>Fraction(7,2))

# Shortest-path distances by integer breadth-first search.
dist=[]
for root in range(24):
    row=[-1]*24;row[root]=0;q=deque([root])
    while q:
        v=q.popleft();nei=G[v]
        while nei:
            b=nei & -nei;nei-=b;w=b.bit_length()-1
            if row[w]<0: row[w]=row[v]+1;q.append(w)
    assert min(row)>=0
    dist.append(row)
assert max(max(row) for row in dist)==4

def faces_at_scale(r):
    allowed=[sum(1<<j for j in range(24) if j!=i and dist[i][j]<=r) for i in range(24)]
    faces=set()
    def extend(mask,candidates):
        if mask:faces.add(mask)
        while candidates:
            b=candidates&-candidates;candidates-=b
            v=b.bit_length()-1
            extend(mask|b,candidates&allowed[v])
    extend(0,(1<<24)-1)
    return faces

def collapse(faces):
    faces=set(faces)
    cnt={x:0 for x in faces};exclusive={x:0 for x in faces}
    for upper in faces:
        m=upper
        while m:
            b=m&-m;m-=b;lower=upper^b
            if lower:
                cnt[lower]+=1;exclusive[lower]^=upper
    heap=[(-x.bit_count(),x) for x in faces if cnt[x]==1]
    heapq.heapify(heap);pairs=[]
    while heap:
        _,x=heapq.heappop(heap)
        if x not in faces or cnt[x]!=1:continue
        y=exclusive[x]
        if y not in faces or cnt[y]!=0:continue
        assert y.bit_count()==x.bit_count()+1 and (x&y)==x
        faces.remove(x);faces.remove(y);pairs.append((x,y))
        for upper in (x,y):
            m=upper
            while m:
                b=m&-m;m-=b;lower=upper^b
                if lower and lower in faces:
                    cnt[lower]-=1;exclusive[lower]^=upper
                    if cnt[lower]==1:
                        heapq.heappush(heap,(-lower.bit_count(),lower))
    return faces,pairs

def connected(vertices, edges):
    adj={v:set() for v in vertices}
    for u,v in edges:
        adj[u].add(v);adj[v].add(u)
    start=next(iter(vertices));seen={start};q=[start]
    for x in q:
        for y in adj[x]:
            if y not in seen:seen.add(y);q.append(y)
    return len(seen)==len(vertices)

def support(mask):
    return [v for v in range(24) if mask>>v&1]

F1=faces_at_scale(1)
assert Counter(x.bit_count()-1 for x in F1)=={0:24,1:60,2:32}
C1,P1=collapse(F1)
assert Counter(x.bit_count()-1 for x in C1)=={0:16,1:20}
V1={support(x)[0] for x in C1 if x.bit_count()==1}
E1=[support(x) for x in C1 if x.bit_count()==2]
assert connected(V1,E1)
assert len(E1)-len(V1)+1==5
print('scale 1: 116 faces; 40 elementary collapses to connected graph (16 vertices, 20 edges); wedge of five circles')

F2=faces_at_scale(2)
assert Counter(x.bit_count()-1 for x in F2)=={0:24,1:156,2:400,3:474,4:264,5:56}
C2,P2=collapse(F2)
assert Counter(x.bit_count()-1 for x in C2)=={0:10,1:24,2:16}
V2={support(x)[0] for x in C2 if x.bit_count()==1}
E2=[support(x) for x in C2 if x.bit_count()==2]
T2=[support(x) for x in C2 if x.bit_count()==3]
assert connected(V2,E2)
for edge in E2:
    assert sum(set(edge).issubset(t) for t in T2)==2
for v in V2:
    edges_link=[];link=set()
    for tri in T2:
        if v in tri:
            a,b=[x for x in tri if x!=v]
            edges_link.append((a,b));link.update([a,b])
    # Connected 2-regular vertex link = a single polygonal circle.
    assert connected(link,edges_link)
    assert all(sum(x in e for e in edges_link)==2 for x in link)
assert len(V2)-len(E2)+len(T2)==2
print('scale 2: 1374 faces; 662 elementary collapses to a closed connected triangulated surface, chi=2; sphere')

F3=faces_at_scale(3)
assert Counter(x.bit_count()-1 for x in F3)=={0:24,1:240,2:1304,3:4218,4:8400,5:10352,6:7800,7:3498,8:872,9:96}
order=[14,0,17,7,6,11,22,21,10,4,2,20,3,19,5,18,9,23,15,16,8,1,13,12]
remaining=set(F3);pairs=[]
for v in order:
    bit=1<<v
    # An acyclic matching is given by greedy vertex toggles in fixed stages.
    for lower in sorted((x for x in remaining if not x&bit),key=lambda x:x.bit_count()):
        upper=lower|bit
        if lower in remaining and upper in remaining:
            remaining.remove(lower);remaining.remove(upper)
            pairs.append((lower,upper))
assert len(pairs)==18399
assert Counter(x.bit_count()-1 for x in remaining)=={0:1,5:5}
# Independently test global acyclicity: a closed V-path is exactly a cycle in
# the graph on matched pairs of a fixed dimension; every pair's outgoing arcs
# run through the other codimension-one faces of its upper cell.
matching=dict(pairs)
indegree={a:0 for a,b in pairs};links={a:[] for a,b in pairs}
for lower,upper in pairs:
    m=upper
    while m:
        b=m&-m;m-=b
        other=upper^b
        if other!=lower and other in matching:
            links[lower].append(other)
            indegree[other]+=1
queue=deque(x for x in indegree if indegree[x]==0);processed=0
while queue:
    x=queue.popleft();processed+=1
    for y in links[x]:
        indegree[y]-=1
        if indegree[y]==0:queue.append(y)
assert processed==len(pairs)==18399
print('scale 3: 36804 faces; global acyclic Morse matching 18399 pairs, 1 vertex and 5 critical dimension-5 cells; wedge of five 5-spheres')
print('scale 0: 24 isolated points. Scale >=4: simplex on all 24 vertices.')
print('PASS: complete homotopy filtration and exact finite Morse certificate')
