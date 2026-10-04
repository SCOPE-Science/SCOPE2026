#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter, deque
from fractions import Fraction

V=range(7)
FACETS={frozenset(t) for t in [
(0,1,3),(0,1,5),(0,2,3),(0,2,6),(0,4,5),(0,4,6),
(1,2,4),(1,2,6),(1,3,4),(1,5,6),(2,3,5),(2,4,5),
(3,4,6),(3,5,6)]}
EDGES={frozenset(e) for e in combinations(V,2)}
FACES={frozenset([v]) for v in V} | EDGES | FACETS

def is_simplicial(f):
    for t in FACETS:
        im=frozenset(f[v] for v in t)
        if im not in FACES:
            return False
    return True

def contiguous(f,g):
    for t in FACETS:
        u=frozenset([f[v] for v in t]+[g[v] for v in t])
        if u not in FACES:
            return False
    return True

def rank_q(rows):
    a=[[Fraction(x) for x in r] for r in rows]
    m=len(a); n=len(a[0]) if m else 0
    r=0
    for c in range(n):
        p=next((i for i in range(r,m) if a[i][c]),None)
        if p is None: continue
        a[r],a[p]=a[p],a[r]
        q=a[r][c]
        a[r]=[x/q for x in a[r]]
        for i in range(m):
            if i!=r and a[i][c]:
                q=a[i][c]
                a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
        r+=1
        if r==m: break
    return r

# Pseudomanifold / neighborliness checks.
edge_degrees=Counter()
for t in FACETS:
    for e in combinations(sorted(t),2): edge_degrees[frozenset(e)]+=1
assert set(edge_degrees)==EDGES and set(edge_degrees.values())=={2}
assert len(V)-len(EDGES)+len(FACETS)==0
for v in V:
    link_edges=[]
    for t in FACETS:
        if v in t:
            link_edges.append(frozenset(t-{v}))
    deg=Counter(x for e in link_edges for x in e)
    assert len(link_edges)==6 and set(deg.values())=={2}

# Full 7^7 enumeration.
MAPS=[]
for f in product(V, repeat=7):
    if is_simplicial(f): MAPS.append(f)
assert len(MAPS)==27979
by_image=Counter(len(set(f)) for f in MAPS)
assert by_image==Counter({1:7,2:2646,3:25284,7:42})
for f in MAPS:
    im=frozenset(f)
    if len(im)<7:
        assert im in FACES

# Exact count of the non-automorphism part by surjections onto faces.
assert 7 == 7
assert 2646 == 21*(2**7-2)
assert 25284 == 14*(3**7-3*2**7+3)

AUTOS=[f for f in MAPS if len(set(f))==7]
assert len(AUTOS)==42
AFF={tuple((a*i+b)%7 for i in V) for a in range(1,7) for b in range(7)}
assert set(AUTOS)==AFF

# Every non-automorphism is directly contiguous to a constant at a vertex of its image.
for f in MAPS:
    if f in AFF: continue
    v=min(set(f))
    c=(v,)*7
    assert contiguous(f,c)
# All constants are mutually contiguous because the 1-skeleton is complete.
const=[(v,)*7 for v in V]
for c in const:
    for d in const:
        assert contiguous(c,d)
# Automorphisms are isolated: verify directly against all one-coordinate moves,
# and also verify the star-intersection criterion used in the proof.
idx=set(MAPS)
for a in AUTOS:
    for v in V:
        for y in V:
            if y==a[v]: continue
            g=a[:v]+(y,)+a[v+1:]
            if g in idx:
                assert not contiguous(a,g)
for v in V:
    incident=[t for t in FACETS if v in t]
    inter=set(incident[0])
    for t in incident[1:]: inter &= set(t)
    assert inter=={v}

# Full contiguity components from single-coordinate moves.  Any contiguous pair
# can be factored through such moves by changing vertices one at a time, since
# every hybrid image of a simplex is contained in the original union simplex.
pos={f:i for i,f in enumerate(MAPS)}
adj=[[] for _ in MAPS]
for i,f in enumerate(MAPS):
    for v in V:
        for y in V:
            if y==f[v]: continue
            g=f[:v]+(y,)+f[v+1:]
            j=pos.get(g)
            if j is not None and j>i and contiguous(f,g):
                adj[i].append(j); adj[j].append(i)
seen=set(); sizes=[]
for i in range(len(MAPS)):
    if i in seen: continue
    seen.add(i); q=deque([i]); n=0
    while q:
        x=q.popleft(); n+=1
        for y in adj[x]:
            if y not in seen:
                seen.add(y); q.append(y)
    sizes.append(n)
assert sorted(sizes, reverse=True)==[27937]+[1]*42

# Integral H^1 basis in tree gauge.  Tree edges are (0,i), and non-tree edges
# are the remaining 15 edges.  The two cocycles below span the rank-2 kernel
# of the triangle equations after quotienting by coboundaries.
ALL_EDGES=list(combinations(V,2))
TREE={(0,i) for i in range(1,7)}
NT=[e for e in ALL_EDGES if e not in TREE]
B1={(1,4):1,(2,4):1,(2,5):1,(3,4):1,(3,5):1,(3,6):1}
B2={(1,2):1,(1,6):1,(2,4):-1,(2,5):-1,(3,5):-1,(5,6):1}
def val(co,u,v):
    if u==v:return 0
    if u<v:return co.get((u,v),0)
    return -co.get((v,u),0)
def cocycle(co):
    for a,b,c in FACETS:
        a,b,c=sorted((a,b,c))
        if val(co,b,c)-val(co,a,c)+val(co,a,b)!=0:return False
    return True
assert cocycle(B1) and cocycle(B2)
rows=[]
for t in FACETS:
    a,b,c=sorted(t); row=[]
    for e in NT:
        row.append((1 if e==(b,c) else 0) + (-1 if e==(a,c) else 0) + (1 if e==(a,b) else 0))
    rows.append(row)
assert rank_q(rows)==13

def pullback_matrix(f):
    cols=[]
    for co in (B1,B2):
        pb={(u,v):val(co,f[u],f[v]) for u,v in ALL_EDGES}
        p={0:0}; p.update({i:pb[(0,i)] for i in range(1,7)})
        g={(u,v):pb[(u,v)]-(p[v]-p[u]) for u,v in ALL_EDGES}
        a=g[(1,4)]
        b=g[(1,2)]
        for e in NT:
            assert g[e]==a*B1.get(e,0)+b*B2.get(e,0)
        cols.append((a,b))
    return ((cols[0][0],cols[1][0]),(cols[0][1],cols[1][1]))

MAT_BY_MULT={
1:((1,0),(0,1)),
2:((0,-1),(1,-1)),
3:((1,-1),(1,0)),
4:((-1,1),(-1,0)),
5:((0,1),(-1,1)),
6:((-1,0),(0,-1)),
}
mat_count=Counter()
for f in AUTOS:
    M=pullback_matrix(f); mat_count[M]+=1
    # f(i)=a*i+b, and its H^1 action depends only on a.
    a=(f[1]-f[0])%7
    assert a in range(1,7) and M==MAT_BY_MULT[a]
assert set(mat_count.values())=={7} and len(mat_count)==6

print("VERIFY_OK maps=27979 image_sizes=1:7,2:2646,3:25284,7:42 contiguity=27937+42x1 autos=AGL(1,7) h1_actions=6x7")
