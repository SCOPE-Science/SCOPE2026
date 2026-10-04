#!/usr/bin/env python3
from collections import defaultdict

PTS=("c1","c2","c3","b1","b2","b3","a1","a2","a3")
I={x:i for i,x in enumerate(PTS)}
COVERS=(
("c1","b1"),("c2","b1"),
("c1","b2"),("c2","b2"),("c3","b2"),
("c2","b3"),("c3","b3"),
("b1","a1"),("b1","a2"),
("b2","a1"),("b2","a3"),
("b3","a2"),("b3","a3"),
)
N=len(PTS)
le=[[False]*N for _ in range(N)]
for i in range(N): le[i][i]=True
for x,y in COVERS: le[I[x]][I[y]]=True
for k in range(N):
    for i in range(N):
        if le[i][k]:
            for j in range(N):
                if le[k][j]: le[i][j]=True

# Exact beat-point check.
for x in range(N):
    upp=[y for y in range(N) if y!=x and le[x][y]]
    low=[y for y in range(N) if y!=x and le[y][x]]
    assert not any(all(le[u][v] for v in upp) for u in upp)
    assert not any(all(le[v][u] for v in low) for u in low)

pred=[[] for _ in range(N)]
for x,y in COVERS: pred[I[y]].append(I[x])
maps=[]
cur=[None]*N
def gen(pos):
    if pos==N:
        m=tuple(cur)
        # independent full-order check, not just cover check
        assert all((not le[i][j]) or le[m[i]][m[j]] for i in range(N) for j in range(N))
        maps.append(m)
        return
    if pred[pos]:
        allowed=[v for v in range(N) if all(le[cur[p]][v] for p in pred[pos])]
    else:
        allowed=range(N)
    for v in allowed:
        cur[pos]=v
        gen(pos+1)
gen(0)
assert len(maps)==12575
assert len(set(maps))==12575

# Independent reverse-direction enumeration: assign maximal points first and
# intersect common lower bounds of already assigned upper covers.
succ=[[] for _ in range(N)]
for x,y in COVERS: succ[I[x]].append(I[y])
maps_rev=[]
cur2=[None]*N
def gen_rev(pos):
    if pos<0:
        m=tuple(cur2)
        assert all((not le[i][j]) or le[m[i]][m[j]] for i in range(N) for j in range(N))
        maps_rev.append(m)
        return
    if succ[pos]:
        allowed=[v for v in range(N) if all(le[v][cur2[q]] for q in succ[pos])]
    else:
        allowed=range(N)
    for v in allowed:
        cur2[pos]=v
        gen_rev(pos-1)
gen_rev(N-1)
assert len(maps_rev)==12575
assert set(maps_rev)==set(maps)

identity=tuple(range(N))
sigma=(2,1,0,5,4,3,8,7,6)
automorphisms=[m for m in maps if len(set(m))==N]
assert automorphisms==[identity,sigma]
assert tuple(sigma[sigma[i]] for i in range(N))==identity

M=len(maps)
# For every coordinate and value, bitset of maps whose coordinate is >= value.
ge=[[0]*N for _ in range(N)]
for coord in range(N):
    for v in range(N):
        bits=0
        for j,m in enumerate(maps):
            if le[v][m[coord]]: bits |= 1<<j
        ge[coord][v]=bits

parent=list(range(M)); sz=[1]*M
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]
        x=parent[x]
    return x
def union(a,b):
    a,b=find(a),find(b)
    if a==b: return
    if sz[a]<sz[b]: a,b=b,a
    parent[b]=a; sz[a]+=sz[b]

ALL=(1<<M)-1
comparable_pairs=0
for i,m in enumerate(maps):
    bits=ALL
    for coord,v in enumerate(m): bits &= ge[coord][v]
    comparable_pairs += bits.bit_count()
    b=bits
    while b:
        lowbit=b & -b
        j=lowbit.bit_length()-1
        if j!=i: union(i,j)
        b-=lowbit

components=defaultdict(list)
for i in range(M): components[find(i)].append(i)
sizes=sorted((len(v) for v in components.values()), reverse=True)
assert sizes==[12573,1,1]
assert comparable_pairs==1235007
singletons=[v[0] for v in components.values() if len(v)==1]
assert {maps[i] for i in singletons}=={identity,sigma}

indices={m:i for i,m in enumerate(maps)}
constant_indices=[indices[tuple([v]*N)] for v in range(N)]
roots={find(i) for i in constant_indices}
assert len(roots)==1
large_root=next(iter(roots))
assert len(components[large_root])==12573
assert all(find(i)==large_root for i,m in enumerate(maps) if m not in (identity,sigma))

# Reversing both domain and target orders preserves the same isotone functions.
for m in maps:
    assert all((not le[j][i]) or le[m[j]][m[i]] for i in range(N) for j in range(N))

print("VERIFY_OK maps=12575 components=12573,1,1 automorphisms=2 comparable_pairs=1235007 constants_large=9")
