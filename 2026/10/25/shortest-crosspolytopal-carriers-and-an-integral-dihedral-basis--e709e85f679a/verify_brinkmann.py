"""Exact finite certificate for the Brinkmann independence-complex theorem.
Run: python verify_brinkmann.py. Requires networkx and sympy.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import product
from math import gcd
import networkx as nx
from sympy import Matrix

def verts(f):return [i for i in range(21) if f>>i&1]

ED={0:[2,5,7,13],1:[3,6,7,8],2:[4,8,9],3:[5,9,10],4:[6,10,11],5:[11,12],6:[12,13],7:[15,20],8:[14,16],9:[15,17],10:[16,18],11:[17,19],12:[18,20],13:[14,19],14:[17,18],15:[18,19],16:[19,20],17:[20]}
G=nx.Graph();G.add_nodes_from(range(21))
for a,ns in ED.items(): G.add_edges_from((a,b) for b in ns)
assert (len(G),G.number_of_edges())==(21,42)
assert set(dict(G.degree()).values())=={4}
adj=[sum(1<<j for j in G.neighbors(i)) for i in range(21)]
faces=[]; fv=Counter()
def rec(f,pool):
    if f:faces.append(f);fv[f.bit_count()-1]+=1
    while pool:
        v=(pool&-pool).bit_length()-1;pool^=1<<v
        rec(f|1<<v,pool&~adj[v])
rec(0,(1<<21)-1)
assert [fv[d] for d in range(len(fv))]==[21,168,658,1344,1400,665,106]
assert len(faces)==4362
live=set(faces);lo={};up={}
for v in range(21):
    ps=[(f,f|1<<v) for f in live if not (f>>v&1) and f|1<<v in live]
    for a,b in ps:
        if a in live and b in live:live.remove(a);live.remove(b);lo[a]=b;up[b]=a
assert len(lo)==2176
assert Counter(f.bit_count()-1 for f in live)=={0:1,4:8,5:1}
ids={f:i for i,f in enumerate(faces)};links=[[] for f in faces];deg=[0]*len(faces);incidences=0
for f in faces:
    if f.bit_count()==1:continue
    for v in verts(f):
        sub=f^(1<<v)
        if lo.get(sub)==f:a,b=sub,f
        else:a,b=f,sub
        links[ids[a]].append(ids[b]);deg[ids[b]]+=1;incidences+=1
q=deque(i for i,d in enumerate(deg) if d==0);visited=0
while q:
    i=q.popleft();visited+=1
    for j in links[i]:
        deg[j]-=1
        if deg[j]==0:q.append(j)
assert (incidences,visited)==(19418,4362)
crit4=sorted(x for x in live if x.bit_count()==5);crit5=next(x for x in live if x.bit_count()==6)
ci={f:i for i,f in enumerate(crit4)}
@lru_cache(None)
def proj(f):
    if f in ci:return {ci[f]:1}
    if f in up:return {}
    assert f in lo
    top=lo[f];vs=verts(top);p=next(i for i,v in enumerate(vs) if top^(1<<v)==f)
    ans=Counter()
    for i,v in enumerate(vs):
        if i==p:continue
        for k,a in proj(top^(1<<v)).items():ans[k]-=(-1)**(p+i)*a
    return {k:a for k,a in ans.items() if a}
row=Counter()
for i,v in enumerate(verts(crit5)):
    for k,a in proj(crit5^(1<<v)).items():row[k]+=(-1)**i*a
morse=[row[k] for k in range(8)]
assert morse==[1,-2,1,1,-1,-1,1,-1]
E=sorted(tuple(sorted(e)) for e in G.edges())
compat=[]
for i,(a,b) in enumerate(E):
    compat.append(sum(1<<j for j,(c,d) in enumerate(E) if j>i and len({a,b,c,d})==4 and not((adj[a]|adj[b])&((1<<c)|(1<<d)))))
matchings=[]
def enumer(pool,picks):
    if len(picks)==5:matchings.append(tuple(picks));return
    while pool:
        i=(pool&-pool).bit_length()-1;pool^=1<<i
        enumer(pool&compat[i],picks+[i])
enumer((1<<42)-1,[])
assert len(matchings)==21

def parity(a):return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))
def sphere(pairs):
    z=Counter()
    for bits in product((0,1),repeat=5):
        vs=[pairs[k][bits[k]] for k in range(5)]
        z[sum(1<<v for v in vs)]+=(-1)**sum(bits)*parity(vs)
    return {f:c for f,c in z.items() if c}
def coords(z):
    x=[0]*8
    for f,c in z.items():
        assert f.bit_count()==5
        for k,a in proj(f).items():x[k]+=c*a
    return tuple(x[j]-x[0]*morse[j] for j in range(1,8))
def act(z,p):
    out=Counter()
    for f,c in z.items():
        vs=[p[v] for v in verts(f)]
        out[sum(1<<v for v in vs)]+=c*parity(vs)
    return {f:c for f,c in out.items() if c}
zs=[sphere([E[j] for j in m]) for m in matchings]
for z in zs:
    boundary=Counter()
    for f,c in z.items():
        assert f.bit_count()==5
        for j,v in enumerate(verts(f)):
            boundary[f^(1<<v)]+=c*(-1)**j
    assert not any(boundary.values())
    assert gcd(*coords(z))==1
ms=list(nx.algorithms.isomorphism.GraphMatcher(G,G).isomorphisms_iter())
assert len(ms)==14
rot=[];refs=[]
for p in ms:
    parts=[];vis=set()
    for a in range(21):
        if a in vis:continue
        b=a;length=0
        while b not in vis:vis.add(b);b=p[b];length+=1
        parts.append(length)
    if sorted(parts)==[7,7,7]:rot.append(tuple(p[i] for i in range(21)))
    if sorted(parts)==[1,1,1]+[2]*9:refs.append(tuple(p[i] for i in range(21)))
r=min(rot);s=min(refs)
assert r==(1,2,3,4,5,6,0,8,9,10,11,12,13,7,15,16,17,18,19,20,14)
assert s==(0,6,5,4,3,2,1,13,12,11,10,9,8,7,20,19,18,17,16,15,14)
assert all(r[r[r[r[r[r[r[i]]]]]]]==i for i in range(21))
assert all(s[s[i]]==i for i in range(21))
assert all(s[r[s[i]]]==next(j for j in range(21) if r[j]==i) for i in range(21))
lookup={tuple(E[j] for j in m):i for i,m in enumerate(matchings)}
seen=set();orbit_reports=[]
for i,m in enumerate(matchings):
    if i in seen:continue
    z=zs[i];rows=[];idxs=[]
    for k in range(7):
        rows.append(coords(z))
        support=tuple(sorted(tuple(sorted(E[j])) for j in matchings[i])) if k==0 else support
        idxs.append(lookup[support]);seen.add(lookup[support])
        support=tuple(sorted(tuple(sorted((r[a],r[b]))) for a,b in support))
        z=act(z,r)
    assert len(set(idxs))==7
    A=Matrix(rows);det=int(A.det());rank=A.rank()
    signs=[]
    for z0 in [zs[i]]:
        z=z0
        for k in range(7):
            b=coords(act(z,s));hit=[(j,e) for j,x in enumerate(rows) for e in (-1,1) if b==tuple(e*t for t in x)]
            assert len(hit)==1;signs.append(hit[0]);z=act(z,r)
    orbit_reports.append((i,rank,det,signs,idxs))
assert sorted((rank,abs(det)) for _,rank,det,_,_ in orbit_reports)==[(6,0),(7,1),(7,1)]
assert sum(all(sgn==1 for _,sgn in signs) for _,rank,det,signs,_ in orbit_reports)==2
assert len(seen)==21
print('VERIFY_OK_BRINKMANN_INTEGRAL_SHORTEST_SPHERE_ORBITS')
print('GRAPH',len(G),G.number_of_edges(),'AUT',len(ms),'IND_F',tuple(fv[d] for d in range(7)))
print('MORSE_PAIRS',len(lo),'CRITICAL',(1,8,1),'HASSE',incidences,'ACYCLIC',visited)
print('SIGNED_MORSE_D5',morse,'INTEGRAL_H4_RANK',7)
print('TEN_VERTEX_CROSSPOLYTOPE_SPHERES',len(matchings),'THREE_ORBITS',[(a,b,c) for a,b,c,_,_ in orbit_reports])
print('UNIMODULAR_ORBIT_BASIS_COUNT',2,'DIHEDRAL_PERMUTATION_LATTICE_RANK',7)

