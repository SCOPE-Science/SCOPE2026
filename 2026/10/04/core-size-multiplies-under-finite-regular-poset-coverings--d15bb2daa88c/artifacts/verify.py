#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict

A=[f'a{i}' for i in range(1,5)]
edges=list(combinations(range(1,5),2))
B=[f'b{i}{j}' for i,j in edges]
matchings=[{(1,2),(3,4)},{(1,3),(2,4)},{(1,4),(2,3)}]
C=[f'c{k}' for k in range(3)]
P=A+B+C
covers=[]
for i in range(1,5):
    for e in edges:
        if i in e:
            covers.append((f'a{i}',f'b{e[0]}{e[1]}'))
for e in edges:
    for k,M in enumerate(matchings):
        if e not in M:
            covers.append((f'b{e[0]}{e[1]}',f'c{k}'))
idx={e:i for i,e in enumerate(covers)}

def rref(rows,n):
    rows=[r for r in rows if r]
    piv=[]; rr=0
    for col in range(n):
        p=next((i for i in range(rr,len(rows)) if (rows[i]>>col)&1),None)
        if p is None: continue
        rows[rr],rows[p]=rows[p],rows[rr]
        for i in range(len(rows)):
            if i!=rr and ((rows[i]>>col)&1): rows[i]^=rows[rr]
        piv.append(col); rr+=1
        if rr==len(rows): break
    return rows[:rr],piv

def rank(rows,n): return len(rref(rows,n)[0])

# Admissibility equations: any two saturated chains from a minimum to a maximum have equal Z2-weight.
constraints=[]
for a in A:
    for c in C:
        mids=[b for b in B if (a,b) in idx and (b,c) in idx]
        for b in mids[1:]:
            b0=mids[0]
            row=0
            for e in [(a,b0),(b0,c),(a,b),(b,c)]: row ^= 1<<idx[e]
            constraints.append(row)
R,piv=rref(constraints,len(covers))
free=[j for j in range(len(covers)) if j not in piv]
z_basis=[]
for f in free:
    v=1<<f
    for row,p in zip(R,piv):
        if (row>>f)&1: v |= 1<<p
    z_basis.append(v)

# Coboundaries of vertex 0-cochains.
cobs=[]
for vtx in P:
    v=0
    for i,(u,w) in enumerate(covers):
        if vtx==u or vtx==w: v |= 1<<i
    cobs.append(v)
base_rank=rank(cobs,len(covers))
z=next(v for v in z_basis if rank(cobs+[v],len(covers))>base_rank)

# The chosen non-coboundary Z2-cocycle represents the nonzero class in H^1(RP2;Z2), hence gives the connected universal double cover.
colored=[covers[i] for i in range(len(covers)) if (z>>i)&1]
E=[(x,g) for x in P for g in (0,1)]
ec=[]
for i,(x,y) in enumerate(covers):
    color=(z>>i)&1
    for g in (0,1): ec.append(((x,g),(y,g^color)))

def closure(nodes, hasse):
    gt={x:set() for x in nodes}
    for u,v in hasse: gt[u].add(v)
    changed=True
    while changed:
        changed=False
        for u in nodes:
            new=set()
            for v in tuple(gt[u]): new |= gt[v]
            if not new <= gt[u]: gt[u]|=new; changed=True
    return gt

def fvector(nodes,hasse):
    gt=closure(nodes,hasse)
    f0=len(nodes)
    f1=sum(len(gt[x]) for x in nodes)
    tris=[(a,b,c) for a in nodes for b in gt[a] for c in gt[b]]
    return (f0,f1,len(tris)),gt,tris

def beat_points(nodes,hasse):
    up={x:[] for x in nodes}; dn={x:[] for x in nodes}
    for u,v in hasse: up[u].append(v); dn[v].append(u)
    # In a finite poset, an up/down beat point is equivalently covered by/covers a unique point.
    return [x for x in nodes if len(up[x])==1 or len(dn[x])==1]

def connected(nodes,hasse):
    adj={x:set() for x in nodes}
    for u,v in hasse: adj[u].add(v);adj[v].add(u)
    seen={nodes[0]}; st=[nodes[0]]
    while st:
        u=st.pop()
        for v in adj[u]:
            if v not in seen: seen.add(v);st.append(v)
    return len(seen)==len(nodes)

def closed_surface_checks(nodes,gt,tris):
    inc=Counter()
    for t in tris:
        for e in combinations(t,2): inc[frozenset(e)]+=1
    if len(inc)!=sum(len(gt[x]) for x in nodes): return False,{}
    if set(inc.values())!={2}: return False,dict(Counter(inc.values()))
    for x in nodes:
        ladj=defaultdict(set)
        for t in tris:
            if x in t:
                y,z=[q for q in t if q!=x]
                ladj[y].add(z);ladj[z].add(y)
        if not ladj or any(len(s)!=2 for s in ladj.values()): return False,dict(Counter(inc.values()))
        start=next(iter(ladj)); seen={start}; st=[start]
        while st:
            q=st.pop()
            for y in ladj[q]:
                if y not in seen:seen.add(y);st.append(y)
        if len(seen)!=len(ladj): return False,dict(Counter(inc.values()))
    return True,dict(Counter(inc.values()))

# Connectivity of double cover.
assert connected(E,ec)
# Hasse-degree preservation, the local fact behind beat-point reflection.
base_up={x:0 for x in P}; base_dn={x:0 for x in P}
for u,v in covers: base_up[u]+=1;base_dn[v]+=1
cover_up={x:0 for x in E}; cover_dn={x:0 for x in E}
for u,v in ec: cover_up[u]+=1;cover_dn[v]+=1
for x in P:
    for g in (0,1):
        assert cover_up[(x,g)]==base_up[x]
        assert cover_dn[(x,g)]==base_dn[x]

pf,pgt,ptris=fvector(P,covers)
ef,egt,etris=fvector(E,ec)
pok,pinc=closed_surface_checks(P,pgt,ptris)
eok,einc=closed_surface_checks(E,egt,etris)
assert len(P)==13 and len(covers)==24 and pf==(13,36,24) and pok
assert len(beat_points(P,covers))==0
assert len(E)==26 and len(ec)==48 and ef==(26,72,48) and eok
assert len(beat_points(E,ec))==0
assert pf[0]-pf[1]+pf[2]==1
assert ef[0]-ef[1]+ef[2]==2
assert len(z_basis)==13 and base_rank==12

print('BASE_POINTS=13')
print('BASE_HASSE_EDGES=24')
print('BASE_F_VECTOR=13,36,24')
print('BASE_EULER=1')
print('BASE_BEAT_POINTS=0')
print('Z2_COCYCLE_DIM=13')
print('Z2_COBBOUNDARY_DIM=12')
print('NONTRIVIAL_COLORING_EDGES='+';'.join(f'{u}>{v}' for u,v in colored))
print('COVER_POINTS=26')
print('COVER_HASSE_EDGES=48')
print('COVER_CONNECTED=1')
print('COVER_F_VECTOR=26,72,48')
print('COVER_EULER=2')
print('COVER_BEAT_POINTS=0')
print('COVER_EDGE_TRIANGLE_INCIDENCE='+str(einc))
print('COVER_VERTEX_LINKS_ARE_CYCLES=1')
print('CORE_SCALE_EXAMPLE=26=2*13')
print('VERIFY_OK')
