#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, deque

FACETS=[(1,2,4),(1,2,6),(1,3,4),(1,3,7),(1,5,6),(1,5,7),
        (2,3,5),(2,3,7),(2,4,5),(2,6,7),(3,4,6),(3,5,6),
        (4,5,7),(4,6,7)]
FACETS=[tuple(sorted(f)) for f in FACETS]
FSET=set(FACETS)
EDGES=sorted({tuple(sorted(e)) for f in FACETS for e in combinations(f,2)})
EI={e:i for i,e in enumerate(EDGES)}

def rank2(rows,n):
    a=list(rows); r=0
    for c in range(n):
        p=next((i for i in range(r,len(a)) if (a[i]>>c)&1),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for i in range(len(a)):
            if i!=r and ((a[i]>>c)&1): a[i]^=a[r]
        r+=1
    return r

def nullbasis(rows,n):
    a=list(rows); r=0; piv=[]
    for c in range(n):
        p=next((i for i in range(r,len(a)) if (a[i]>>c)&1),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        for i in range(len(a)):
            if i!=r and ((a[i]>>c)&1): a[i]^=a[r]
        piv.append(c); r+=1
    free=[c for c in range(n) if c not in piv]
    out=[]
    for f in free:
        x=1<<f
        for i,c in enumerate(piv):
            if (a[i]>>f)&1: x|=1<<c
        out.append(x)
    return out

def span(bs):
    s=[0]
    for b in bs: s += [x^b for x in s]
    return s

def compose(p,q):
    return tuple(p[q[i]-1] for i in range(7))

def cycle_perm(cycles):
    p={i:i for i in range(1,8)}
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]): p[a]=b
    return tuple(p[i] for i in range(1,8))

def perm_mask(mask,p):
    y=0
    for i,(a,b) in enumerate(EDGES):
        if (mask>>i)&1:
            e=tuple(sorted((p[a-1],p[b-1])))
            y |= 1<<EI[e]
    return y

def canon_cycle(seq):
    n=len(seq); cand=[]
    for s in (seq,list(reversed(seq))):
        for k in range(n): cand.append(tuple(s[k:]+s[:k]))
    return min(cand)

assert len(EDGES)==21 and len(FACETS)==14
inc={e:[] for e in EDGES}
for fi,f in enumerate(FACETS):
    for e in combinations(f,2): inc[tuple(sorted(e))].append(fi)
assert all(len(v)==2 for v in inc.values())

tri_rows=[]
for f in FACETS:
    m=0
    for e in combinations(f,2): m ^= 1<<EI[tuple(sorted(e))]
    tri_rows.append(m)
assert rank2(tri_rows,21)==13
Z=span(nullbasis(tri_rows,21))
assert len(Z)==256
cob=[]
for v in range(1,8):
    cob.append(sum(1<<i for i,e in enumerate(EDGES) if v in e))
assert rank2(cob,21)==6
B=set(span(cob[:6])); assert len(B)==64

# Four cohomology cosets and their complete edge-support weight enumerators.
unassigned=set(Z); cosets=[]
while unassigned:
    z=min(unassigned); C={z^b for b in B}; cosets.append(C); unassigned-=C
assert len(cosets)==4
zero=next(C for C in cosets if 0 in C)
nonzero=[C for C in cosets if 0 not in C]
def enum(C): return dict(sorted(Counter(x.bit_count() for x in C).items()))
assert enum(zero)=={0:1,6:7,10:21,12:35}
assert all(enum(C)=={6:7,8:7,10:21,12:21,14:8} for C in nonzero)
assert all(min(x.bit_count() for x in C)==6 for C in nonzero)
assert all(sum(x.bit_count()==6 for x in C)==7 for C in nonzero)

# Dual graph and its six-cycles.
adj={i:set() for i in range(14)}; fpedge={}
for e,fs in inc.items():
    a,b=fs; adj[a].add(b); adj[b].add(a); fpedge[frozenset((a,b))]=e
assert all(len(adj[i])==3 for i in adj)
# bipartition 7+7, and every same-side pair has one common neighbor: the Fano incidence graph.
color={0:0}; q=deque([0])
while q:
    v=q.popleft()
    for w in adj[v]:
        if w not in color: color[w]=1-color[v]; q.append(w)
        else: assert color[w]!=color[v]
parts=[[v for v in adj if color[v]==c] for c in (0,1)]
assert sorted(map(len,parts))==[7,7]
for P in parts:
    for a,b in combinations(P,2): assert len(adj[a]&adj[b])==1

cycles=set()
for s in range(14):
    stack=[(s,[s])]
    while stack:
        v,path=stack.pop()
        if len(path)==6:
            if s in adj[v]: cycles.add(canon_cycle(path))
            continue
        for w in adj[v]:
            if w not in path: stack.append((w,path+[w]))
assert len(cycles)==28

def cmask(c):
    m=0
    for a,b in zip(c,c[1:]+c[:1]): m |= 1<<EI[fpedge[frozenset((a,b))]]
    return m
cmasks={cmask(list(c)) for c in cycles}
weight6={z for z in Z if z.bit_count()==6}
assert cmasks==weight6 and len(cmasks)==28
assert {x for x in zero if x.bit_count()==6}==set(cob)
# Thus the seven trivial six-cycles are exactly the boundaries of the seven dual faces.
cls={}
for i,C in enumerate([zero]+nonzero):
    for x in C: cls[x]=i
assert Counter(cls[x] for x in cmasks)==Counter({0:7,1:7,2:7,3:7})

# Published generators for action 7^4; their generated group has order 42.
g1=cycle_perm([(1,2,3,4,5,6,7)])
g2=cycle_perm([(1,3,2,6,4,5)])
G={tuple(range(1,8))}; front=list(G)
while front:
    a=front.pop()
    for g in (g1,g2):
        h=compose(g,a)
        if h not in G: G.add(h); front.append(h)
assert len(G)==42
for p in G:
    assert {tuple(sorted(p[v-1] for v in f)) for f in FACETS}==FSET
rem=set(cmasks); orbits=[]
while rem:
    x=next(iter(rem)); orb={perm_mask(x,p) for p in G}; assert orb<=cmasks
    orbits.append(orb); rem-=orb
assert sorted(map(len,orbits))==[7,21]
essential=next(o for o in orbits if len(o)==21)
facial=next(o for o in orbits if len(o)==7)
assert all(cls[x]!=0 for x in essential)
assert all(cls[x]==0 for x in facial)
assert Counter(cls[x] for x in essential)==Counter({1:7,2:7,3:7})

print('VERIFY_OK')
print('f_vector=7,21,14 H1_F2_dim=2')
print('zero_coset=1+7t6+21t10+35t12')
print('each_nonzero_coset=7t6+7t8+21t10+21t12+8t14')
print('dual_graph=Heawood six_cycles=28 facial=7 essential=21')
print('essential_class_split=7,7,7 map_group_order=42 orbit_sizes=7,21')
