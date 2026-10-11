#!/usr/bin/env python3
"""Exact self-contained combinatorial certificate for Q4 total three-cut complex."""
from itertools import combinations, permutations, product
from collections import Counter, defaultdict, deque
from math import comb

N=16
FULL=(1<<N)-1
EDGES={(a,b) for a in range(N) for b in range(a+1,N) if (a^b).bit_count()==1}
ADJ=[0]*N
for a,b in EDGES:
    ADJ[a]|=1<<b
    ADJ[b]|=1<<a
assert len(EDGES)==32
IND3=[]
for a,b,c in combinations(range(N),3):
    if not (ADJ[a] & ((1<<b)|(1<<c))) and not (ADJ[b] & (1<<c)):
        IND3.append((1<<a)|(1<<b)|(1<<c))
assert len(IND3)==208
FACETS=[FULL ^ S for S in IND3]
# Build face poset from 208 facets without any precomputed data.
faces={0}
for f in FACETS:
    s=f
    while s:
        faces.add(s)
        s=(s-1)&f
assert len(faces)==64671
vec=Counter(f.bit_count()-1 for f in faces if f)
assert tuple(vec[d] for d in range(13))==(16,120,560,1820,4368,8008,11440,12870,11440,8008,4368,1444,208)
# Sequential matching by the first still available coordinate; empty face excluded.
unpaired=faces-{0}
match_up={}; match_down={}; stages=[]
for v in range(N):
    m=1<<v; ct=0
    for s in sorted(unpaired):
        t=s|m
        if not (s&m) and t in unpaired:
            unpaired.remove(s);unpaired.remove(t)
            match_up[s]=t;match_down[t]=s;ct+=1
    stages.append(ct)
assert stages==[32078,84,40,36,10,10,6,6,0,0,0,0,0,0,0,0]
assert len(match_up)==32270
assert len(unpaired)==130
assert Counter(s.bit_count()-1 for s in unpaired)=={0:1,10:129}
# Exhaustively check acyclicity of the entire Forman oriented Hasse diagram:
# unmatched covers high --> low; matching edges low --> high.
indeg={s:0 for s in faces if s}; edges=0
for s in faces:
    if s==0:continue
    t=s
    while t:
        b=t&-t;t-=b
        low=s^b
        if low==0:continue
        if match_up.get(low)==s:
            indeg[s]+=1
        else:
            indeg[low]+=1
        edges+=1
assert edges>0
q=deque(s for s,deg in indeg.items() if deg==0)
processed=0
while q:
    s=q.popleft();processed+=1
    if s in match_up:
        t=match_up[s];indeg[t]-=1
        if indeg[t]==0:q.append(t)
    t=s
    while t:
        bit=t&-t;t-=bit
        low=s^bit
        if low==0 or match_up.get(low)==s:continue
        indeg[low]-=1
        if indeg[low]==0:q.append(low)
assert processed==len(faces)-1,(processed,len(faces)-1)
# Independent Alexander-dual low-dimensional enumerator:
# L={S: independence_number(G[S])<=2}; bipartite => |S|<=4.
L2=0;L3=0;L_DUAL={0}
for v in range(N): L_DUAL.add(1<<v)
for a,b in combinations(range(N),2):L_DUAL.add((1<<a)|(1<<b))
for v in combinations(range(N),3):
    if any((a,b) in EDGES for a,b in combinations(v,2)):
        L2+=1;L_DUAL.add(sum(1<<a for a in v))
for v in combinations(range(N),4):
    if all(any((a,b) in EDGES for a,b in combinations(t,2)) for t in combinations(v,3)):
        L3+=1;L_DUAL.add(sum(1<<a for a in v))
assert (L2,L3)==(352,376)
assert len(L_DUAL)==865
assert L3-L2+comb(N,2)-N+1==129
# Second count from 2-matchings, induced four-cycles, edge-containing triples.
E=len(EDGES);num_sq=sum((a^b).bit_count()==2 for a,b in combinations(range(N),2))//2
assert num_sq==24
assert L2==E*(N-2)-N*comb(4,2)
assert L3==comb(E,2)-N*comb(4,2)-num_sq

# Character of Aut(Q4)=(C2)^4 \rtimes S4 on the top rational homology.
def perm_vertices(p,flip):
    return tuple(flip ^ sum(((x>>i)&1)<<p[i] for i in range(4)) for x in range(N))
def signed_type(p,flip):
    seen=set();pos=[];neg=[]
    for i in range(4):
        if i in seen:continue
        cyc=[];j=i
        while j not in seen:
            seen.add(j);cyc.append(j);j=p[j]
        parity=sum((flip>>u)&1 for u in cyc)%2
        (neg if parity else pos).append(len(cyc))
    return (tuple(sorted(pos,reverse=True)),tuple(sorted(neg,reverse=True)))
def trace_rep(perm):
    visited=set();orbits=[]
    for u in range(N):
        if u in visited:continue
        orbit=0;x=u
        while x not in visited:
            visited.add(x);orbit|=1<<x;x=perm[x]
        orbits.append(orbit)
    # Alternating invariant face sum; empty face contributes -1.
    # Uses full face set to avoid any assumption about topology.
    val=-1
    for r in range(1,len(orbits)+1):
        coeff=(-1)**(r+1)
        for items in combinations(orbits,r):
            mask=0
            for s in items:mask|=s
            if mask in faces:val+=coeff
    # Independent equivariant Alexander-dual character computation:
    # All hypercube automorphisms act evenly on its 16 vertices.
    dual_sum=1
    for r in range(1,len(orbits)+1):
        coeff=(-1)**r
        for items in combinations(orbits,r):
            mask=0
            for s in items:mask|=s
            if mask in L_DUAL:dual_sum+=coeff
    assert val==dual_sum,(perm,val,dual_sum)
    return val
classes=defaultdict(set);num={}
for p in permutations(range(4)):
    for flip in range(16):
        ty=signed_type(p,flip)
        val=trace_rep(perm_vertices(p,flip))
        classes[ty].add(val);num[ty]=num.get(ty,0)+1
assert len(classes)==20
assert all(len(v)==1 for v in classes.values())
assert classes[((1,1,1,1),())]=={129}
# Character inner product ensures legitimate dimension distribution; dimension of invariants integer.
traces={k:next(iter(v)) for k,v in classes.items()}
assert sum(num[k]*traces[k] for k in traces)%384==0
print('VERIFY_OK')
print('independent_triples',len(IND3),'simplices',len(faces)-1,'f_vector',*[vec[d] for d in range(13)])
print('Morse_pairs',len(match_up),'critical_0',1,'critical_10',129,'Hasse_incidences',edges,'acyclic_vertices',processed)
print('Alexander_dual',N,comb(N,2),L2,L3,'squares',num_sq)
print('B4-character twenty signed-cycle classes:')
for ty in sorted(classes, key=lambda x:(x[0],x[1])):
    print('%s|%s|%s|%s'%(','.join(map(str,ty[0])) or '-',','.join(map(str,ty[1])) or '-',num[ty],traces[ty]))
