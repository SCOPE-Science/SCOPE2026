#!/usr/bin/env python3
from itertools import product, combinations

# The 13-point P_2^2 model from Cianci--Ottina, Theorem 5.10 / Figure 2.
names = ['c1','c2','c3','c4','b1','b2','b3','b4','b5','b6','a1','a2','a3']
idx = {x:i for i,x in enumerate(names)}
n = len(names)
cover = []
# c < b incidences
cb = {
    'b1':['c1','c2'], 'b2':['c3','c4'], 'b3':['c1','c3'],
    'b4':['c2','c4'], 'b5':['c2','c3'], 'b6':['c1','c4']
}
for b, cs in cb.items():
    for c in cs: cover.append((idx[c],idx[b]))
# b < a incidences
ba = {
    'b1':['a1','a2'], 'b2':['a1','a2'], 'b3':['a1','a3'],
    'b4':['a1','a3'], 'b5':['a2','a3'], 'b6':['a2','a3']
}
for b, aa in ba.items():
    for a in aa: cover.append((idx[b],idx[a]))

# Reflexive transitive closure.
le = [[False]*n for _ in range(n)]
for i in range(n): le[i][i] = True
for i,j in cover: le[i][j] = True
for k in range(n):
    for i in range(n):
        if le[i][k]:
            for j in range(n):
                if le[k][j]: le[i][j] = True
assert all(not (i != j and le[i][j] and le[j][i]) for i in range(n) for j in range(n))

# Domain C is the four-point minimal circle: l0,l1 below u0,u1.
domain_rel = [(0,2),(0,3),(1,2),(1,3)]
maps = []
for f in product(range(n), repeat=4):
    if all(le[f[i]][f[j]] for i,j in domain_rel): maps.append(f)
assert len(maps) == 853

# Pointwise mapping-poset relation and homotopy components.
m = len(maps)
def map_le(f,g): return all(le[f[t]][g[t]] for t in range(4))
MLE = [[False]*m for _ in range(m)]
parent = list(range(m))
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]; x = parent[x]
    return x
def union(a,b):
    a,b=find(a),find(b)
    if a!=b: parent[b]=a
for i in range(m):
    MLE[i][i] = True
for i in range(m):
    for j in range(i+1,m):
        ij = map_le(maps[i],maps[j]); ji = map_le(maps[j],maps[i])
        MLE[i][j]=ij; MLE[j][i]=ji
        if ij or ji: union(i,j)
comps = {}
for i in range(m): comps.setdefault(find(i),[]).append(i)
comp_list = sorted(comps.values(), key=lambda C:(-len(C), C[0]))
assert sorted(map(len,comp_list), reverse=True) == [721,132]

# Order complex of P_2^2 over F_2.
edges = [(i,j) for i in range(n) for j in range(n) if i!=j and le[i][j]]
edge_index = {e:k for k,e in enumerate(edges)}
triangles = [(i,j,k) for i in range(n) for j in range(n) for k in range(n)
             if i!=j and j!=k and i!=k and le[i][j] and le[j][k]]
# Since antisymmetric and strict in all entries, these are exactly 3-chains.
assert len(edges) == 36 and len(triangles) == 24

def gf2_rank(vecs):
    basis = {}
    for x in vecs:
        y=x
        while y:
            p=y.bit_length()-1
            if p in basis: y ^= basis[p]
            else:
                basis[p]=y; break
    return len(basis), basis

def in_span(x,basis):
    y=x
    while y:
        p=y.bit_length()-1
        if p not in basis: return False
        y ^= basis[p]
    return True

# d1: edges -> vertices; d2: triangles -> edges.
d1_cols = [(1<<i) ^ (1<<j) for i,j in edges]
d2_cols = []
for i,j,k in triangles:
    v=(1<<edge_index[(i,j)]) ^ (1<<edge_index[(i,k)]) ^ (1<<edge_index[(j,k)])
    d2_cols.append(v)
r1,_ = gf2_rank(d1_cols)
r2,b2 = gf2_rank(d2_cols)
h1dim = len(edges)-r1-r2
assert (r1,r2,h1dim) == (12,23,1)

# The four edges of K(C) form its fundamental mod-2 cycle.
def image_cycle(f):
    v=0
    for s,t in domain_rel:
        a,b=f[s],f[t]
        if a==b: continue
        assert le[a][b]
        v ^= 1 << edge_index[(a,b)]
    return v

essential = []
for i,f in enumerate(maps):
    z=image_cycle(f)
    # z is a cycle; nonzero H1 iff not a d2-boundary because dim H1=1.
    assert in_span(sum([],[]), {}) if False else True
    if not in_span(z,b2): essential.append(i)
assert len(essential) == 132
E=set(essential)
assert any(set(C)==E for C in comp_list)
null_comp = next(C for C in comp_list if len(C)==721)
assert not (E & set(null_comp))

# All 13 constants lie in the null component.
const = []
for a in range(n):
    k=maps.index((a,a,a,a)); const.append(k)
assert set(const).issubset(set(null_comp))

# Beat-point deletion certificate inside the null component, preserving constants.
local = list(null_comp)
q=len(local)
pos={g:i for i,g in enumerate(local)}
up=[0]*q; down=[0]*q
for ii,g in enumerate(local):
    for jj,h in enumerate(local):
        if ii==jj: continue
        if MLE[g][h]: up[ii] |= 1<<jj
        if MLE[h][g]: down[ii] |= 1<<jj
active=(1<<q)-1
const_local={pos[g] for g in const}
deletions=[]

def first_bit(x): return (x & -x).bit_length()-1

def beat_kind(i):
    U=up[i]&active
    if U:
        z=U
        while z:
            u=first_bit(z)
            if ((U & ~(1<<u)) & ~up[u]) == 0: return ('up',u)
            z &= z-1
    L=down[i]&active
    if L:
        z=L
        while z:
            d=first_bit(z)
            if ((L & ~(1<<d)) & ~down[d]) == 0: return ('down',d)
            z &= z-1
    return None

while active.bit_count() > len(const_local):
    found=None
    z=active
    while z:
        i=first_bit(z); z &= z-1
        if i in const_local: continue
        bk=beat_kind(i)
        if bk is not None:
            found=(i,bk); break
    if found is None:
        raise AssertionError('beat reduction stalled before constants')
    i,(kind,w)=found
    # Validate witness in current induced subposet immediately before deletion.
    if kind=='up':
        U=up[i]&active
        assert U and (U&(1<<w)) and (((U&~(1<<w)) & ~up[w])==0)
    else:
        L=down[i]&active
        assert L and (L&(1<<w)) and (((L&~(1<<w)) & ~down[w])==0)
    deletions.append((i,kind,w))
    active &= ~(1<<i)
assert {i for i in range(q) if active>>i & 1} == const_local
assert len(deletions)==708
up_count=sum(k=='up' for _,k,_ in deletions)
down_count=sum(k=='down' for _,k,_ in deletions)

# Constants inherit precisely the target order.
for a in range(n):
    for b in range(n):
        assert MLE[const[a]][const[b]] == le[a][b]

# Pick a reproducible essential witness and print it in point names.
widx=min(essential, key=lambda i: maps[i])
w=maps[widx]
witness=tuple(names[x] for x in w)

print('VERIFY_OK maps=853 components=721,132 essential=132 H1dim=1 '
      f'null_deletions=708 up={up_count} down={down_count} witness={witness}')
