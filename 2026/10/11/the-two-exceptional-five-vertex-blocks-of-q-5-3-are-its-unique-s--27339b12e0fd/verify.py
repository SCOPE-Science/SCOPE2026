#!/usr/bin/env python3
from itertools import combinations

# Datta-Upadhyay Example 7, specialized to Q_{5,3}: m=2, n=3.
m,n=2,3
verts=[]
for i in range(1,m+2):
    for j in range(1,n+1): verts.append(('u',i,j))
for i in range(1,m+1):
    for j in range(1,n+1): verts.append(('v',i,j))
vid={v:k for k,v in enumerate(verts)}
def jp(j,a=1): return ((j-1+a)%n)+1
facets=set()
def add(*vs):
    t=tuple(sorted(vid[v] for v in vs))
    assert len(set(t))==3
    facets.add(t)
for i in range(1,m+1):
    for j in range(1,n+1):
        add(('u',i,j),('u',i+1,j),('v',i,j))
        add(('u',i,jp(j)),('u',i+1,jp(j)),('v',i,j))
for i in range(1,m):
    for j in range(1,n+1):
        add(('v',i,j),('v',i+1,j),('u',i+1,j))
        add(('v',i,j),('v',i+1,j),('u',i+1,jp(j)))
for j in range(1,n+1):
    a=((n+2-j-1)%n)+1
    b=((n+1-j-1)%n)+1
    add(('u',m+1,j),('u',1,a),('v',1,a))
    add(('u',m+1,jp(j)),('u',1,a),('v',1,b))
    add(('u',m+1,j),('u',1,a),('v',m,j))
    add(('u',m+1,jp(j)),('u',1,a),('v',m,j))
facets=sorted(facets)
edges=sorted({tuple(sorted(e)) for t in facets for e in combinations(t,2)})
eidx={e:i for i,e in enumerate(edges)}
assert (len(verts),len(edges),len(facets))==(15,45,30)
# closed surface check
edge_degree={e:0 for e in edges}
for t in facets:
    for e in combinations(t,2): edge_degree[tuple(sorted(e))]+=1
assert set(edge_degree.values())=={2}

def rref(rows,ncols):
    rows=[r for r in rows if r]
    piv=[]; rr=0
    for c in range(ncols):
        k=next((k for k in range(rr,len(rows)) if (rows[k]>>c)&1),None)
        if k is None: continue
        rows[rr],rows[k]=rows[k],rows[rr]
        for k2 in range(len(rows)):
            if k2!=rr and ((rows[k2]>>c)&1): rows[k2]^=rows[rr]
        piv.append(c); rr+=1
        if rr==len(rows): break
    return rows[:rr],piv

def nullspace(rows,ncols):
    R,piv=rref(rows,ncols)
    pset=set(piv); free=[c for c in range(ncols) if c not in pset]
    out=[]
    for f in free:
        x=1<<f
        # R rows have pivot p and relation x_p + sum_{c>/?} R_pc x_c = 0.
        for row,p in reversed(list(zip(R,piv))):
            if ((row & x).bit_count() & 1): x ^= 1<<p
        out.append(x)
    # verify
    for x in out:
        assert all(((row & x).bit_count()&1)==0 for row in rows)
    return out

tri_eq=[]
for t in facets:
    mask=0
    for e in combinations(t,2): mask ^= 1<<eidx[tuple(sorted(e))]
    tri_eq.append(mask)
Rtri,Ptri=rref(tri_eq,len(edges))
Zbasis=nullspace(tri_eq,len(edges))
assert len(Rtri)==29 and len(Zbasis)==16

stars=[]
for v in range(len(verts)):
    mask=0
    for k,e in enumerate(edges):
        if v in e: mask ^= 1<<k
    stars.append(mask)
BR,BP=rref(stars,len(edges))
assert len(BR)==14

def reduce_B(x):
    for row,p in zip(BR,BP):
        if (x>>p)&1: x^=row
    return x

def cup(a,b):
    # Alexander-Whitney cup on increasing vertex order, evaluated on the mod-2 fundamental 2-cycle.
    s=0
    for x,y,z in facets:
        s ^= ((a>>eidx[(x,y)])&1) & ((b>>eidx[(y,z)])&1)
    return s

# Exhaust all 2^16 cocycles, not merely sampled candidates.
classes={}
cur=0; prev=0
for mask in range(1<<len(Zbasis)):
    if mask==0:
        z=0
    else:
        gray=mask^(mask>>1); diff=gray^prev; bit=(diff&-diff).bit_length()-1
        cur ^= Zbasis[bit]; prev=gray; z=cur
    key=reduce_B(z)
    d=classes.setdefault(key,{'count':0,'minw':10**9,'mins':[],'q':None})
    d['count']+=1
    w=z.bit_count()
    if w<d['minw']: d['minw']=w; d['mins']=[z]
    elif w==d['minw']: d['mins'].append(z)
    q=cup(z,z)
    if d['q'] is None: d['q']=q
    else: assert d['q']==q
assert len(classes)==4
assert all(d['count']==(1<<14) for d in classes.values())
zero=reduce_B(0)
nonzero=[(k,d) for k,d in classes.items() if k!=zero]
profile=sorted((d['minw'],len(d['mins']),d['q']) for k,d in nonzero)
assert profile==[(5,1,1),(5,1,1),(10,1,0)]

# Identify w1 by the surface Wu identity <w1 cup x,[K]> = <x cup x,[K]> for all x in H^1.
keys=[k for k in classes]
wus=[]
for w in keys:
    if all(cup(w,x)==cup(x,x) for x in keys): wus.append(w)
assert len(wus)==1
w1=wus[0]
assert w1!=zero and classes[w1]['minw']==10 and classes[w1]['q']==0

# Extract the two unique weight-5 representatives and the unique w1 representative.
weight5=[]
for k,d in nonzero:
    if d['minw']==5: weight5.append(d['mins'][0])
assert len(weight5)==2
z1,z2=weight5
# The weight-10 class is their sum; uniqueness is already certified by exhaustive class enumeration.
assert reduce_B(z1^z2)==w1
assert (z1^z2)==classes[w1]['mins'][0]

def support(z):
    return {edges[i] for i in range(len(edges)) if (z>>i)&1}
def labels_of_vertices(S):
    return {verts[v] for e in S for v in e}
S1,S2=map(support,(z1,z2))
carriers=[labels_of_vertices(S1),labels_of_vertices(S2)]
expected=[
    {('u',1,1),('u',2,1),('u',3,1),('v',1,1),('v',2,1)},
    {('u',1,3),('u',2,3),('u',3,3),('v',1,2),('v',2,2)},
]
assert {frozenset(c) for c in carriers}=={frozenset(c) for c in expected}
# Each minimum support itself is a simple five-cycle in the primal 1-skeleton.
for S in (S1,S2):
    deg={v:0 for e in S for v in e}
    for a,b in S: deg[a]+=1;deg[b]+=1
    assert len(S)==5 and len(deg)==5 and set(deg.values())=={2}
assert S1.isdisjoint(S2)

def fmt_vertex(v): return f"{v[0]}{v[1]}{v[2]}"
def fmt_support(S):
    return ','.join(sorted(f"{fmt_vertex(verts[a])}-{fmt_vertex(verts[b])}" for a,b in S))
ss=sorted([fmt_support(S1),fmt_support(S2)])
print('VERIFY_OK')
print('f_vector=15,45,30')
print('rank_triangle_cocycle_equations=29')
print('rank_coboundaries=14')
print('H1_F2_dimension=2')
print('cocycles_exhausted=65536')
print('nonzero_profile=(5,1,1),(5,1,1),(10,1,0)  # (minimum_support,minimizer_count,cup_square)')
print('w1_profile=(10,1,0)')
print('weight5_support_A='+ss[0])
print('weight5_support_B='+ss[1])
print('w1_is_disjoint_union_of_weight5_supports=yes')
print('source_G4_carriers_match_weight5_vertex_carriers=yes')
