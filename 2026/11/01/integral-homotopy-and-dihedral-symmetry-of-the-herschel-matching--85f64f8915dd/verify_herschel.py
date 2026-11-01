#!/usr/bin/env python3
"""Exact checks for the matching complex of the Herschel graph (stdlib only).

Vertices are 0..10. Each face is a bitmask of graph-edge indices. The
acyclic matching is constructed by successive toggles in edge order.
All integer operations are exact, and no external packages are required.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations
from math import cos, pi

EDGE_NEIGHBORS = {
    0: (1,3,4), 1: (2,5,6), 2: (3,7), 3: (8,9),
    4: (5,9), 5: (10,), 6: (7,10), 7: (8,),
    8: (10,), 9: (10,)
}
EDGES = tuple(sorted((min(u,v), max(u,v))
                     for u, vs in EDGE_NEIGHBORS.items() for v in vs))
assert len(EDGES) == 18 and len(set(EDGES)) == 18
V = tuple(range(11))
ADJ = [{v for a,v in EDGES if a==u} | {a for a,b in EDGES if b==u}
       for u in V]
DEG = [len(a) for a in ADJ]
CONFLICT = [sum(1 << j for j, f in enumerate(EDGES)
                if i != j and (set(e) & set(f)))
            for i,e in enumerate(EDGES)]

# Enumerate all matchings as bitmasks. This is an exhaustive, not sampled, count.
faces = [0]
for i in range(18):
    faces += [m | (1 << i) for m in faces if not CONFLICT[i] & m]
assert len(faces) == len(set(faces)) == 752
F = set(faces) - {0}
FV = Counter(x.bit_count()-1 for x in F)
assert dict(FV) == {0:18, 1:111, 2:280, 3:270, 4:72}

# Greedy toggle matching. The full directed Hasse graph is checked for cycles.
mate = {}
for i in range(18):
    for f in sorted(F, key=lambda x:(x.bit_count(), x)):
        g = f | (1 << i)
        if f in mate or f & (1 << i) or g not in F or g in mate:
            continue
        mate[f], mate[g] = g, f
critical = sorted(F - set(mate), key=lambda x:(x.bit_count(),x))
CR = Counter(x.bit_count()-1 for x in critical)
assert len(mate) == 734 and dict(CR) == {0:1,2:2,3:14}
indeg={f:0 for f in F}
succ={f:[] for f in F}
hasse=0
for g in F:
    for i in range(18):
        if not g & (1 << i): continue
        f=g^(1 << i)
        if not f: continue
        a,b=(f,g) if mate.get(f)==g else (g,f)
        succ[a].append(b); indeg[b]+=1; hasse+=1
queue=deque(f for f in F if indeg[f]==0)
visited=0
while queue:
    f=queue.popleft(); visited+=1
    for g in succ[f]:
        indeg[g]-=1
        if indeg[g]==0: queue.append(g)
assert hasse==2502 and visited==len(F)

# Integer Morse differential from critical 3-cells to critical 2-cells.
def boundary(mask):
    return [(mask ^ (1 << i), -1 if j & 1 else 1)
            for j,i in enumerate(i for i in range(18) if mask & (1 << i))]
C2={f:j for j,f in enumerate(f for f in critical if f.bit_count()==3)}
C3=[f for f in critical if f.bit_count()==4]
@lru_cache(None)
def project(face):
    if face in C2:
        return (1,0) if C2[face]==0 else (0,1)
    higher = mate.get(face)
    if higher is None or higher.bit_count() != face.bit_count()+1:
        return (0,0)
    eps = next(sign for lower,sign in boundary(higher) if lower==face)
    result=[0,0]
    for lower,sign in boundary(higher):
        if lower==face: continue
        rec=project(lower)
        for j in range(2): result[j]-=eps*sign*rec[j]
    return tuple(result)
M=[]
for cell in C3:
    out=[0,0]
    for lower,sign in boundary(cell):
        rec=project(lower)
        for j in range(2):out[j]+=sign*rec[j]
    M.append(tuple(out))
assert len(M)==14 and M[0]==(1,0) and M[3]==(0,-1)
assert M == [(1,0),(-1,1),(-1,1),(0,-1),(-1,1),(0,0),
             (1,-1),(1,0),(1,0),(-1,0),(-1,0),(0,-1),(-1,0),(0,0)]

# Independent mod-p boundary-rank computation (does not use the matching).
by_dim={d:sorted(f for f in F if f.bit_count()-1==d) for d in range(5)}
def rank_mod2(d):
    ix={f:i for i,f in enumerate(by_dim[d-1])}; basis={}
    for cell in by_dim[d]:
        col=sum(1<<ix[lower] for lower,_ in boundary(cell))
        while col:
            pivot=col.bit_length()-1
            if pivot not in basis: basis[pivot]=col; break
            col ^= basis[pivot]
    return len(basis)
def rank_modp(d,p):
    ix={f:i for i,f in enumerate(by_dim[d-1])};basis={}
    for cell in by_dim[d]:
        col={ix[f]:sign%p for f,sign in boundary(cell)}
        while col:
            pivot=max(col)
            if pivot not in basis:
                inv=pow(col[pivot],-1,p)
                basis[pivot]={i:(v*inv)%p for i,v in col.items()};break
            scalar=col[pivot]
            for i,v in basis[pivot].items():
                t=(col.get(i,0)-scalar*v)%p
                if t: col[i]=t
                else: col.pop(i,None)
    return len(basis)
for p in (2,3,5):
    ranks=[rank_mod2(d) if p==2 else rank_modp(d,p) for d in range(1,5)]
    assert ranks==[17,94,186,72], (p,ranks)

# Exhaustively enumerate graph automorphisms from adjacency, without a library.
order_vertices=sorted(V,key=lambda x:(-DEG[x],x))
all_perms=[]
def extend(i, partial, used):
    if i==len(V):
        all_perms.append(tuple(partial[v] for v in V));return
    u=order_vertices[i]
    for v in V:
        if v in used or DEG[u]!=DEG[v]:continue
        if any((x in ADJ[u])!=(partial[x] in ADJ[v]) for x in partial):continue
        partial[u]=v; used.add(v)
        extend(i+1,partial,used)
        used.remove(v);partial.pop(u)
extend(0,{},set())
assert len(all_perms)==len(set(all_perms))==12
id_perm=V
def multiply(a,b): return tuple(a[b[i]] for i in V)
def power(a,k):
    p=id_perm
    for _ in range(k): p=multiply(p,a)
    return p
def order(a):
    for k in range(1,13):
        if power(a,k)==id_perm: return k
    raise AssertionError('order')
r=next(a for a in sorted(all_perms) if order(a)==6)
s=next(a for a in sorted(all_perms) if order(a)==2 and
       multiply(multiply(a,r),a)==power(r,5))
assert len({power(r,k) for k in range(6)} |
           {multiply(s,power(r,k)) for k in range(6)})==12
edge_index={e:i for i,e in enumerate(EDGES)}
def lefschetz_h3(g):
    edge_perm=[edge_index[tuple(sorted((g[u],g[v])))] for u,v in EDGES]
    L=0
    for face in F:
        indexes=[i for i in range(18) if face & (1 << i)]
        im=[edge_perm[i] for i in indexes]
        if set(indexes)!=set(im): continue
        inv=sum(im[a]>im[b] for a in range(len(im)) for b in range(a+1,len(im)))
        L += -1 if ((len(indexes)-1+inv)&1) else 1
    return 1-L
char_rot=[lefschetz_h3(power(r,k)) for k in range(6)]
char_ref=[lefschetz_h3(multiply(s,power(r,k))) for k in range(6)]
assert char_rot==[12,1,-3,-2,-3,1],char_rot
assert char_ref==[0,2,0,2,0,2],char_ref
# Irreducible rational characters of D_6.
mults={}
for rsign in (1,-1):
    for ssign in (1,-1):
        chi=[rsign**k for k in range(6)]+[ssign*rsign**k for k in range(6)]
        numer=sum(a*b for a,b in zip(char_rot+char_ref,chi))
        assert numer%12==0
        mults[f'A({rsign},{ssign})']=numer//12
for j in (1,2):
    chi=[round(2*cos(2*pi*j*k/6)) for k in range(6)]+[0]*6
    numer=sum(a*b for a,b in zip(char_rot+char_ref,chi))
    assert numer%12==0
    mults[f'E{j}']=numer//12
assert mults=={'A(1,1)':1,'A(1,-1)':0,'A(-1,1)':0,
               'A(-1,-1)':1,'E1':3,'E2':2}
assert sum(char_rot+char_ref)==12  # full-group invariant dimension 1
print('Herschel edges:',EDGES)
print('face vector (dimensions 0..4):',[FV[d] for d in range(5)])
print('nonempty faces:',len(F),'matched pairs:',len(mate)//2,
      'critical cells:',dict(sorted(CR.items())),
      'Hasse relations:',hasse,'acyclic:',True)
print('critical 2-faces:',list(C2))
print('critical 3-faces:',C3)
print('Morse d3 columns:',M,'minor columns 1 and 4 determinant: -1')
print('boundary ranks modulo 2,3,5:',[17,94,186,72])
print('homotopy type: wedge of 12 three-spheres')
print('automorphisms:',len(all_perms),'rotation r:',r,'reflection s:',s)
print('homology character rotations:',char_rot,'reflections:',char_ref)
print('rational irreducible multiplicities:',mults)
print('full group quotient reduced rational Betti 3:',sum(char_rot+char_ref)//12)
