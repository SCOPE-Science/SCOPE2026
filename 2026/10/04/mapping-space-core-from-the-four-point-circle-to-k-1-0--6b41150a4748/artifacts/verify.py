#!/usr/bin/env python3
from itertools import product
from collections import defaultdict, deque

names = [f'c{i}' for i in range(1,5)] + [f'b{i}' for i in range(1,9)] + [f'a{i}' for i in range(1,5)]
idx = {x:i for i,x in enumerate(names)}
n = len(names)
cover = []
for b, cs in {
    'b1':['c1','c3'],'b7':['c1','c3'],
    'b2':['c2','c4'],'b8':['c2','c4'],
    'b4':['c1','c2'],'b5':['c1','c2'],
    'b3':['c3','c4'],'b6':['c3','c4'],
}.items():
    for c in cs: cover.append((idx[c],idx[b]))
for a, bs in {
    'a1':['b1','b2','b3','b4'],
    'a2':['b1','b2','b5','b6'],
    'a3':['b3','b5','b7','b8'],
    'a4':['b4','b6','b7','b8'],
}.items():
    for b in bs: cover.append((idx[b],idx[a]))
le = [[False]*n for _ in range(n)]
for i in range(n): le[i][i] = True
for x,y in cover: le[x][y] = True
for k in range(n):
    for i in range(n):
        if le[i][k]:
            for j in range(n):
                if le[k][j]: le[i][j] = True

# Four-point circle C has two minima (coordinates 0,1) below two maxima (coordinates 2,3).
def isotone(f):
    return le[f[0]][f[2]] and le[f[0]][f[3]] and le[f[1]][f[2]] and le[f[1]][f[3]]

maps = [f for f in product(range(n), repeat=4) if isotone(f)]
assert len(maps) == 1288
# Independent exact count: choose the two lower images first and then either upper image
# independently from their common upper set.
count2 = 0
for x,y in product(range(n), repeat=2):
    u = sum(1 for z in range(n) if le[x][z] and le[y][z])
    count2 += u*u
assert count2 == len(maps)
M = len(maps)

def mle(f,g):
    return all(le[f[t]][g[t]] for t in range(4))

# Comparability graph components.
parent=list(range(M)); rank=[0]*M
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]; x=parent[x]
    return x
def union(a,b):
    a,b=find(a),find(b)
    if a==b:return
    if rank[a]<rank[b]: a,b=b,a
    parent[b]=a
    if rank[a]==rank[b]:rank[a]+=1

upmask=[0]*M; downmask=[0]*M
for i in range(M):
    fi=maps[i]
    for j in range(i+1,M):
        fj=maps[j]
        ij=mle(fi,fj); ji=mle(fj,fi)
        if ij or ji:
            union(i,j)
        if ij:
            upmask[i] |= 1<<j; downmask[j] |= 1<<i
        if ji:
            upmask[j] |= 1<<i; downmask[i] |= 1<<j
comps=defaultdict(list)
for i in range(M): comps[find(i)].append(i)
components=sorted(comps.values(), key=lambda c:(-len(c), c[0]))
sizes=[len(c) for c in components]
assert sizes == [1024,64,64]+[17]*8, sizes

def bits(mask):
    while mask:
        lsb=mask & -mask
        yield lsb.bit_length()-1
        mask ^= lsb

def unique_minimal_upper(i, active):
    U=upmask[i] & active
    if not U:return None
    mins=[]
    for u in bits(U):
        # u is minimal in strict upper set iff no other active strict upper lies below u.
        if not (downmask[u] & U): mins.append(u)
        if len(mins)>1:return None
    return mins[0] if len(mins)==1 else None

def unique_maximal_lower(i, active):
    L=downmask[i] & active
    if not L:return None
    maxs=[]
    for d in bits(L):
        if not (upmask[d] & L): maxs.append(d)
        if len(maxs)>1:return None
    return maxs[0] if len(maxs)==1 else None

def reduce_component(comp):
    active=0
    for i in comp: active |= 1<<i
    dels=[]
    while True:
        changed=False
        for i in comp:
            if not ((active>>i)&1): continue
            u=unique_minimal_upper(i,active)
            if u is not None:
                active &= ~(1<<i); dels.append(('up',i,u)); changed=True; break
            d=unique_maximal_lower(i,active)
            if d is not None:
                active &= ~(1<<i); dels.append(('down',i,d)); changed=True; break
        if not changed: break
    core=list(bits(active))
    return core,dels

def is_crown8(core):
    if len(core)!=8:return False
    S=set(core)
    # covers internal to core
    cover_edges=[]
    minima=[]; maxima=[]
    for x in core:
        below=[y for y in core if y!=x and mle(maps[y],maps[x])]
        above=[y for y in core if y!=x and mle(maps[x],maps[y])]
        if not below:minima.append(x)
        if not above:maxima.append(x)
    if len(minima)!=4 or len(maxima)!=4:return False
    for x in minima:
        for y in maxima:
            if mle(maps[x],maps[y]): cover_edges.append((x,y))
    if len(cover_edges)!=8:return False
    deg={x:0 for x in core}
    adj={x:[] for x in core}
    for x,y in cover_edges:
        deg[x]+=1;deg[y]+=1;adj[x].append(y);adj[y].append(x)
    if any(deg[x]!=2 for x in core):return False
    seen={core[0]};q=[core[0]]
    while q:
        x=q.pop()
        for y in adj[x]:
            if y not in seen:seen.add(y);q.append(y)
    return len(seen)==8

core_sizes=[]; total_up=total_down=0
for ci,comp in enumerate(components):
    core,dels=reduce_component(comp)
    core_sizes.append(len(core))
    ups=sum(k=='up' for k,_,_ in dels); downs=len(dels)-ups
    total_up += ups; total_down += downs
    if ci==0:
        assert len(core)==16 and len(dels)==1008 and ups==248 and downs==760, (len(core),ups,downs)
        constant_indices={i for i,f in enumerate(maps) if f[0]==f[1]==f[2]==f[3]}
        assert set(core)==constant_indices
        const_by_value={maps[i][0]:i for i in core}
        assert set(const_by_value)==set(range(n))
        for x in range(n):
            for y in range(n):
                assert mle(maps[const_by_value[x]],maps[const_by_value[y]]) == le[x][y]
    elif ci in (1,2):
        assert len(core)==8 and len(dels)==56 and ups==24 and downs==32, (ci,len(core),ups,downs)
        assert is_crown8(core)
    else:
        assert len(core)==1 and len(dels)==16 and ups==9 and downs==7, (ci,len(core),ups,downs)
assert core_sizes == [16,8,8]+[1]*8
assert total_up==368 and total_down==880, (total_up,total_down)
assert sum(core_sizes)==40
print('VERIFY_OK maps=1288 components=11 sizes=1024,64,64,17x8 deletions=1248 up=368 down=880 core=40')
