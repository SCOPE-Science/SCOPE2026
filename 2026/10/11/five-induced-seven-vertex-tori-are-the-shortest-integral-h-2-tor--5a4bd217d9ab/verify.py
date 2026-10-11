#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, deque
from pathlib import Path
import json

FACETS = {
(1,2,3,4),(1,2,3,5),(1,2,4,6),(1,2,5,6),(1,3,4,7),(1,3,5,7),
(1,4,6,8),(1,4,7,9),(1,4,8,9),(1,5,6,10),(1,5,7,11),(1,5,10,11),
(1,6,8,12),(1,6,10,12),(1,7,9,13),(1,7,11,13),(1,8,9,12),(1,9,12,14),
(1,9,13,14),(1,10,11,14),(1,10,12,14),(1,11,13,14),(2,3,4,10),
(2,3,5,15),(2,3,10,15),(2,4,6,13),(2,4,10,16),(2,4,13,14),(2,4,14,16),
(2,5,6,9),(2,5,9,12),(2,5,12,15),(2,6,9,11),(2,6,11,13),(2,7,8,12),
(2,7,8,14),(2,7,10,15),(2,7,10,16),(2,7,12,15),(2,7,14,16),(2,8,9,11),
(2,8,9,12),(2,8,11,14),(2,11,13,14),(3,4,7,12),(3,4,10,12),(3,5,7,17),
(3,5,14,15),(3,5,14,16),(3,5,16,17),(3,6,8,12),(3,6,8,16),(3,6,10,12),
(3,6,10,15),(3,6,14,15),(3,6,14,16),(3,7,8,12),(3,7,8,17),(3,8,16,17),
(4,5,8,11),(4,5,8,13),(4,5,11,17),(4,5,13,14),(4,5,14,16),(4,5,16,17),
(4,6,8,13),(4,7,9,15),(4,7,12,15),(4,8,9,11),(4,9,11,17),(4,9,15,17),
(4,10,12,17),(4,10,16,17),(4,12,15,17),(5,6,9,10),(5,7,11,17),
(5,8,10,11),(5,8,10,13),(5,9,10,13),(5,9,12,14),(5,9,13,14),
(5,12,14,15),(6,7,11,13),(6,7,11,17),(6,7,13,16),(6,7,14,16),
(6,7,14,17),(6,8,13,16),(6,9,10,15),(6,9,11,17),(6,9,15,17),
(6,14,15,17),(7,8,14,17),(7,9,10,13),(7,9,10,15),(7,10,13,16),
(8,10,11,14),(8,10,13,16),(8,10,14,17),(8,10,16,17),(10,12,14,17),
(12,14,15,17)
}
V = tuple(range(1,18))

def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
Q = sorted(FACETS)
assert (len(V),len(E),len(T),len(Q)) == (17,119,204,102)
EI = {e:i for i,e in enumerate(E)}
TI = {t:i for i,t in enumerate(T)}
TSET = set(T)
QSET = set(Q)

cert = json.loads(Path(__file__).with_name('certificate.json').read_text(encoding='utf-8'))
assert cert['schema_version'] == 1
assert cert['triangle_order'] == [list(t) for t in T]
B = cert['kernel_basis']
L = cert['left_inverse']
assert len(B)==204 and all(len(r)==102 for r in B)
assert len(L)==102 and all(len(r)==204 for r in L)
EXPECTED = [tuple(s) for s in cert['expected_supports']]

# Integral boundary matrices.
d2 = [[0]*204 for _ in range(119)]
for j,(a,b,c) in enumerate(T):
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        d2[EI[e]][j] = s

d3 = [[0]*102 for _ in range(204)]
for j,(a,b,c,d) in enumerate(Q):
    for t,s in [((b,c,d),1),((a,c,d),-1),((a,b,d),1),((a,b,c),-1)]:
        d3[TI[t]][j] = s

def rank_mod_p(A,p):
    A=[[x%p for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        pivot=next((i for i in range(r,m) if A[i][c]),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[(x-q*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

# rank(d2)=102 over Q: the mod-3 rank is a lower bound, while the
# certified 102-dimensional kernel below is an upper bound.
assert rank_mod_p(d2,3) == 102

# Check d2 B = 0 and L B = I. Therefore B is an integral basis of ker d2:
# for an integral cycle x=Bc over Q, c=Lx is automatically integral.
for i in range(119):
    for j in range(102):
        assert sum(d2[i][k]*B[k][j] for k in range(204)) == 0
for i in range(102):
    for j in range(102):
        assert sum(L[i][k]*B[k][j] for k in range(204)) == (1 if i==j else 0)

# Express d3 in the integral cycle basis and verify B H = d3.
H = [[sum(L[i][k]*d3[k][j] for k in range(204)) for j in range(102)] for i in range(102)]
for i in range(204):
    for j in range(102):
        assert sum(B[i][k]*H[k][j] for k in range(102)) == d3[i][j]

def det_bareiss(A):
    A=[row[:] for row in A]
    n=len(A)
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            sw=next((i for i in range(k+1,n) if A[i][k]),None)
            if sw is None: return 0
            A[k],A[sw]=A[sw],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-A[i][k]*A[k][j])//prev
        for i in range(k+1,n): A[i][k]=0
        for j in range(k+1,n): A[k][j]=0
        prev=pivot
    return sign*A[n-1][n-1]

assert abs(det_bareiss(H)) == 2
# Thus H_2 = Z^102 / H Z^102 is a group of order two.

# Find the unique nonzero F2 functional on this order-two quotient.
def left_null_vector_mod2(H):
    # Solve H^T lambda = 0 over F2 by bit RREF.
    rows=[]
    n=len(H)
    for j in range(n):
        bits=0
        for i in range(n):
            if H[i][j]&1: bits |= 1<<i
        rows.append(bits)
    piv=[]; r=0
    for c in range(n):
        p=next((i for i in range(r,n) if (rows[i]>>c)&1),None)
        if p is None: continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(n):
            if i!=r and ((rows[i]>>c)&1): rows[i]^=rows[r]
        piv.append(c); r+=1
    assert r==101
    free=[c for c in range(n) if c not in piv]
    assert len(free)==1
    x=1<<free[0]
    for k in range(r-1,-1,-1):
        p=piv[k]
        if (rows[k]&x).bit_count()&1: x ^= 1<<p
    lam=[(x>>i)&1 for i in range(n)]
    assert any(lam)
    assert all(sum(lam[i]*H[i][j] for i in range(n))%2==0 for j in range(n))
    return lam

lam = left_null_vector_mod2(H)
# Pull the detector back to triangle chains through L.
wtri=[sum(lam[i]*L[i][j] for i in range(102))%2 for j in range(204)]
assert sum(wtri)==11

# Exhaust all supports through size seven. A supported integral representative
# of the nonzero torsion class would reduce mod two to a cycle with detector 1,
# so absence of such a mod-two cycle is a rigorous lower bound.
triangle_masks=[sum(1<<(v-1) for v in t) for t in T]
cols=[]
for j in range(204):
    bits=0
    for i in range(119):
        if d2[i][j]&1: bits ^= 1<<i
    if wtri[j]: bits |= 1<<119
    cols.append(bits)
TARGET=1<<119

def span_contains(vecs,target):
    piv={}
    for v in vecs:
        x=v
        while x:
            p=x.bit_length()-1
            if p in piv: x^=piv[p]
            else:
                piv[p]=x; break
    x=target
    while x:
        p=x.bit_length()-1
        if p in piv: x^=piv[p]
        else: return False
    return True

counts={}
supports=[]
for k in range(1,8):
    cnt=0
    for S in combinations(V,k):
        mask=sum(1<<(v-1) for v in S)
        vecs=[cols[j] for j,m in enumerate(triangle_masks) if not (m & ~mask)]
        if span_contains(vecs,TARGET):
            cnt+=1
            if k==7: supports.append(S)
    counts[k]=cnt
assert [counts[k] for k in range(1,8)] == [0,0,0,0,0,0,5]
assert supports == EXPECTED

# Verify that each minimum support is an induced orientable closed surface,
# compute an integral fundamental cycle, and detect the nonzero H2 class.
def induced(S,dim):
    ss=set(S)
    source={2:E,3:T,4:Q}[dim]
    return [x for x in source if set(x)<=ss]

def fundamental_chain(S):
    tris=induced(S,3)
    edges=induced(S,2)
    tets=induced(S,4)
    assert (len(edges),len(tris),len(tets)) == (21,14,0)
    edge_inc=defaultdict(list)
    for i,(a,b,c) in enumerate(tris):
        for e,coef in [((b,c),1),((a,c),-1),((a,b),1)]:
            edge_inc[e].append((i,coef))
    assert len(edge_inc)==21 and all(len(v)==2 for v in edge_inc.values())
    # Each vertex link is one cycle, excluding pseudomanifold singularities.
    for v in S:
        link_edges=[]
        for tri in tris:
            if v in tri:
                link_edges.append(tuple(sorted(x for x in tri if x!=v)))
        link_vertices=set(x for e in link_edges for x in e)
        deg=defaultdict(int); adj=defaultdict(set)
        for a,b in link_edges:
            deg[a]+=1; deg[b]+=1; adj[a].add(b); adj[b].add(a)
        assert link_vertices and all(deg[x]==2 for x in link_vertices)
        start=next(iter(link_vertices)); vis={start}; dq=deque([start])
        while dq:
            u=dq.popleft()
            for z in adj[u]:
                if z not in vis: vis.add(z); dq.append(z)
        assert vis==link_vertices
    sign={0:1}; dq=deque([0])
    while dq:
        i=dq.popleft(); a,b,c=tris[i]
        for e,ci in [((b,c),1),((a,c),-1),((a,b),1)]:
            p=edge_inc[e]
            j,cj = p[0] if p[1][0]==i else p[1]
            want=-sign[i]*ci*cj
            if j in sign: assert sign[j]==want
            else: sign[j]=want; dq.append(j)
    assert len(sign)==14
    x=[0]*204
    for i,t in enumerate(tris): x[TI[t]]=sign[i]
    assert all(sum(d2[e][j]*x[j] for j in range(204))==0 for e in range(119))
    c=[sum(L[i][j]*x[j] for j in range(204)) for i in range(102)]
    assert sum(lam[i]*c[i] for i in range(102))%2==1
    # chi = 7-21+14=0, and the certified connected orientable closed
    # 2-manifold is therefore a torus.
    assert 7-len(edges)+len(tris)==0
    return x

for S in supports: fundamental_chain(S)

# Absolute seven-vertex lower bound for triangulated tori:
# E=3V and E<=V(V-1)/2 force V>=7.
assert all(3*v > v*(v-1)//2 for v in range(1,7))
assert 3*7 == 7*6//2

print(
    'VERIFY_OK f=17,119,204,102 H2_Z=Z/2 '
    'min_vertex_support=7 carriers7=5 '
    'all_carriers_induced_orientable_tori=yes '
    'all_carriers_nonzero_torsion=yes '
    'support_counts_le7=0,0,0,0,0,0,5 '
    'supports=1-2-4-5-9-11-13;1-2-4-5-9-11-14;'
    '1-4-5-6-9-11-13;1-5-6-8-9-11-13;1-6-8-9-10-11-13'
)
