#!/usr/bin/env python3
from itertools import combinations, product
from collections import defaultdict, deque, Counter

FACETS = {
    (1, 2, 3, 4),
    (1, 2, 3, 5),
    (1, 2, 4, 6),
    (1, 2, 5, 6),
    (1, 3, 4, 7),
    (1, 3, 5, 8),
    (1, 3, 7, 8),
    (1, 4, 6, 9),
    (1, 4, 7, 9),
    (1, 5, 6, 10),
    (1, 5, 8, 10),
    (1, 6, 9, 11),
    (1, 6, 10, 11),
    (1, 7, 8, 12),
    (1, 7, 9, 12),
    (1, 8, 10, 13),
    (1, 8, 12, 13),
    (1, 9, 11, 14),
    (1, 9, 12, 15),
    (1, 9, 14, 15),
    (1, 10, 11, 16),
    (1, 10, 13, 17),
    (1, 10, 16, 18),
    (1, 10, 17, 18),
    (1, 11, 14, 16),
    (1, 12, 13, 15),
    (1, 13, 15, 17),
    (1, 14, 15, 19),
    (1, 14, 16, 19),
    (1, 15, 17, 19),
    (1, 16, 18, 19),
    (1, 17, 18, 19),
    (2, 3, 4, 20),
    (2, 3, 5, 15),
    (2, 3, 15, 20),
    (2, 4, 6, 16),
    (2, 4, 12, 14),
    (2, 4, 12, 16),
    (2, 4, 14, 20),
    (2, 5, 6, 19),
    (2, 5, 9, 15),
    (2, 5, 9, 19),
    (2, 6, 16, 17),
    (2, 6, 17, 19),
    (2, 8, 10, 13),
    (2, 8, 10, 21),
    (2, 8, 11, 13),
    (2, 8, 11, 18),
    (2, 8, 18, 21),
    (2, 9, 10, 13),
    (2, 9, 10, 21),
    (2, 9, 13, 19),
    (2, 9, 15, 21),
    (2, 11, 12, 16),
    (2, 11, 12, 18),
    (2, 11, 13, 19),
    (2, 11, 16, 17),
    (2, 11, 17, 19),
    (2, 12, 14, 18),
    (2, 14, 18, 21),
    (2, 14, 20, 21),
    (2, 15, 20, 21),
    (3, 4, 7, 11),
    (3, 4, 11, 20),
    (3, 5, 8, 17),
    (3, 5, 14, 15),
    (3, 5, 14, 17),
    (3, 6, 7, 11),
    (3, 6, 7, 16),
    (3, 6, 11, 20),
    (3, 6, 12, 18),
    (3, 6, 12, 20),
    (3, 6, 16, 18),
    (3, 7, 8, 19),
    (3, 7, 16, 19),
    (3, 8, 9, 17),
    (3, 8, 9, 19),
    (3, 9, 13, 17),
    (3, 9, 13, 19),
    (3, 10, 12, 14),
    (3, 10, 12, 20),
    (3, 10, 14, 15),
    (3, 10, 15, 20),
    (3, 12, 14, 18),
    (3, 13, 14, 17),
    (3, 13, 14, 21),
    (3, 13, 19, 21),
    (3, 14, 18, 21),
    (3, 16, 18, 19),
    (3, 18, 19, 21),
    (4, 5, 10, 19),
    (4, 5, 10, 21),
    (4, 5, 11, 20),
    (4, 5, 11, 21),
    (4, 5, 19, 20),
    (4, 6, 8, 9),
    (4, 6, 8, 13),
    (4, 6, 13, 16),
    (4, 7, 9, 18),
    (4, 7, 11, 18),
    (4, 8, 9, 18),
    (4, 8, 11, 13),
    (4, 8, 11, 18),
    (4, 10, 12, 14),
    (4, 10, 12, 21),
    (4, 10, 14, 19),
    (4, 11, 13, 21),
    (4, 12, 16, 21),
    (4, 13, 16, 21),
    (4, 14, 19, 20),
    (5, 6, 10, 19),
    (5, 8, 10, 21),
    (5, 8, 17, 21),
    (5, 9, 11, 14),
    (5, 9, 11, 20),
    (5, 9, 14, 15),
    (5, 9, 19, 20),
    (5, 11, 14, 17),
    (5, 11, 17, 21),
    (6, 7, 11, 15),
    (6, 7, 15, 17),
    (6, 7, 16, 17),
    (6, 8, 9, 20),
    (6, 8, 12, 13),
    (6, 8, 12, 20),
    (6, 9, 11, 20),
    (6, 10, 11, 15),
    (6, 10, 15, 19),
    (6, 12, 13, 18),
    (6, 13, 16, 18),
    (6, 15, 17, 19),
    (7, 8, 12, 20),
    (7, 8, 19, 20),
    (7, 9, 10, 12),
    (7, 9, 10, 18),
    (7, 10, 12, 20),
    (7, 10, 18, 20),
    (7, 11, 15, 18),
    (7, 13, 14, 17),
    (7, 13, 14, 20),
    (7, 13, 15, 17),
    (7, 13, 15, 18),
    (7, 13, 18, 20),
    (7, 14, 16, 17),
    (7, 14, 16, 19),
    (7, 14, 19, 20),
    (8, 9, 17, 18),
    (8, 9, 19, 20),
    (8, 17, 18, 21),
    (9, 10, 12, 21),
    (9, 10, 13, 17),
    (9, 10, 17, 18),
    (9, 12, 15, 21),
    (10, 11, 15, 16),
    (10, 14, 15, 19),
    (10, 15, 16, 20),
    (10, 16, 18, 20),
    (11, 12, 15, 16),
    (11, 12, 15, 18),
    (11, 13, 19, 21),
    (11, 14, 16, 17),
    (11, 17, 19, 21),
    (12, 13, 15, 18),
    (12, 15, 16, 21),
    (13, 14, 20, 21),
    (13, 16, 18, 20),
    (13, 16, 20, 21),
    (15, 16, 20, 21),
    (17, 18, 19, 21)
}
PERM = (14, 9, 11, 1, 5, 15, 16, 17, 19, 3, 10, 7, 13, 4, 20, 12, 21, 18, 2, 6, 8)
V = tuple(range(1,22))

def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
assert (len(V),len(E),len(T),len(FACETS)) == (21,190,338,169)
ESET, TSET = set(E), set(T)

# Contract a deterministic spanning tree of the one-skeleton.
adj = defaultdict(list)
for a,b in E:
    adj[a].append(b); adj[b].append(a)
TREE=set()
seen={1}
q=deque([1])
while q:
    u=q.popleft()
    for v in sorted(adj[u]):
        if v not in seen:
            seen.add(v); q.append(v)
            TREE.add(tuple(sorted((u,v))))
assert len(TREE)==20

NTE=[e for e in E if e not in TREE]
EI={e:i for i,e in enumerate(NTE)}
assert len(NTE)==170

def triangle_relation(t):
    a,b,c=sorted(t)
    row=[0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI:
            row[EI[e]] += s
    return row

R=[triangle_relation(t) for t in T]

def rref_mod(A,p, track_rows=False):
    A=[[(x%p) for x in row] for row in A]
    m,n=len(A),len(A[0])
    ids=list(range(m))
    r=0
    pivcols=[]
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None:
            continue
        A[r],A[piv]=A[piv],A[r]
        ids[r],ids[piv]=ids[piv],ids[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[(a-q*b)%p for a,b in zip(A[i],A[r])]
        pivcols.append(c)
        r+=1
        if r==m:
            break
    return r,A,pivcols,ids[:r] if track_rows else None

def bareiss_det(A):
    A=[row[:] for row in A]
    n=len(A)
    sign=1
    prev=1
    for k in range(n-1):
        if A[k][k]==0:
            piv=next((i for i in range(k+1,n) if A[i][k]),None)
            if piv is None:
                return 0
            A[k],A[piv]=A[piv],A[k]
            sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            aik=A[i][k]
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*pivot-aik*A[k][j])//prev
            A[i][k]=0
        prev=pivot
    return sign*A[-1][-1]

# A nonzero maximal minor proves rational rank 170.
r2,_,_,rows2 = rref_mod(R,2,track_rows=True)
assert r2==170
minor=[R[i] for i in rows2]
det=bareiss_det(minor)
assert abs(det)==125

# The rank drop modulo five forces at least three invariant factors divisible by five.
r5,RR,pivcols,_ = rref_mod(R,5)
assert r5==167
# The maximal minor bounds the finite quotient order by 125, while the rank drop
# forces divisibility by 5^3. Therefore H1 is exactly (Z/5)^3.

free=[j for j in range(len(NTE)) if j not in pivcols]
assert len(free)==3
COCYCLES=[]
for f in free:
    v=[0]*len(NTE)
    v[f]=1
    for i,c in enumerate(pivcols):
        v[c]=(-RR[i][f])%5
    assert all(sum(a*b for a,b in zip(row,v))%5==0 for row in R)
    COCYCLES.append(v)

def oriented_triangle_chain(order):
    a,b,c=order
    x=[0]*len(NTE)
    for u,v in [(a,b),(b,c),(c,a)]:
        e=tuple(sorted((u,v)))
        s=1 if (u,v)==e else -1
        if e in EI:
            x[EI[e]] += s
    return x

def coord_chain(x):
    return tuple(sum(a*b for a,b in zip(x,w))%5 for w in COCYCLES)

def coord(t):
    return coord_chain(oriented_triangle_chain(t))

cliques=[
    c for c in combinations(V,3)
    if all(tuple(sorted(e)) in ESET for e in combinations(c,2))
]
empty=[c for c in cliques if c not in TSET]
assert (len(cliques),len(empty))==(984,646)
assert all(coord(c)!=(0,0,0) for c in empty)

def canon_sign(v):
    neg=tuple((-x)%5 for x in v)
    return min(v,neg)

def proj(v):
    vals=[tuple((a*x)%5 for x in v) for a in range(1,5)]
    return min(vals)

pair_counts=Counter(canon_sign(coord(c)) for c in empty)
assert len(pair_counts)==40

line_pairs=defaultdict(set)
line_counts=Counter()
for v,n in pair_counts.items():
    L=proj(v)
    line_pairs[L].add(v)
    line_counts[L]+=n

all_lines=set()
for v in product(range(5),repeat=3):
    if v!=(0,0,0):
        all_lines.add(proj(v))
assert len(all_lines)==31
assert set(line_counts)==all_lines
assert Counter(len(s) for s in line_pairs.values())==Counter({1:22,2:9})

# Verify an explicit order-three simplicial symmetry.
pmap={v:PERM[v-1] for v in V}
assert tuple(pmap[pmap[pmap[v]]] for v in V)==V
assert PERM!=V
image_facets={tuple(sorted(pmap[v] for v in f)) for f in FACETS}
assert image_facets==FACETS

def rank_vectors(vs,p=5):
    if not vs:
        return 0
    return rref_mod(vs,p)[0]

# Derive the induced 3x3 action on H1 by three independent triangular cycles.
basis_tris=[]
basis_vecs=[]
for c in cliques:
    v=list(coord(c))
    if v!=[0,0,0] and rank_vectors(basis_vecs+[v],5)>len(basis_vecs):
        basis_tris.append(c); basis_vecs.append(v)
        if len(basis_vecs)==3:
            break
assert len(basis_vecs)==3

def inv3(A,p=5):
    M=[[A[i][j]%p for j in range(3)]+[1 if i==j else 0 for j in range(3)] for i in range(3)]
    for c in range(3):
        piv=next(i for i in range(c,3) if M[i][c])
        M[c],M[piv]=M[piv],M[c]
        inv=pow(M[c][c],-1,p)
        M[c]=[(x*inv)%p for x in M[c]]
        for i in range(3):
            if i!=c and M[i][c]:
                q=M[i][c]
                M[i]=[(a-q*b)%p for a,b in zip(M[i],M[c])]
    return [row[3:] for row in M]

def matmul(A,B,p=5):
    return [[sum(A[i][k]*B[k][j] for k in range(3))%p for j in range(3)] for i in range(3)]

def apply(A,v,p=5):
    return tuple(sum(A[i][j]*v[j] for j in range(3))%p for i in range(3))

B=[[basis_vecs[j][i] for j in range(3)] for i in range(3)]
imgs=[]
for tri in basis_tris:
    image_order=tuple(pmap[v] for v in tri)
    imgs.append(list(coord_chain(oriented_triangle_chain(image_order))))
C=[[imgs[j][i] for j in range(3)] for i in range(3)]
A=matmul(C,inv3(B),5)
I=[[1,0,0],[0,1,0],[0,0,1]]
assert matmul(matmul(A,A,5),A,5)==I

# Check the induced action against every graph triangle.
for tri in cliques:
    lhs=coord_chain(oriented_triangle_chain(tuple(pmap[v] for v in tri)))
    rhs=apply(A,coord(tri))
    assert lhs==rhs

# Projective direction orbits under the order-three symmetry.
remaining=set(all_lines)
orbits=[]
while remaining:
    r=min(remaining)
    orb=set()
    x=r
    for _ in range(3):
        orb.add(proj(x))
        x=apply(A,x)
    assert orb <= all_lines
    orbits.append(sorted(orb))
    remaining-=orb
sizes=sorted(len(o) for o in orbits)
assert sizes==[1]+[3]*10
fixed=[o[0] for o in orbits if len(o)==1][0]
assert line_counts[fixed]==16

triple_totals=[]
for o in orbits:
    vals=[line_counts[x] for x in o]
    assert len(set(vals))==1
    if len(o)==3:
        triple_totals.append(vals[0])
assert sorted(triple_totals)==[2,7,8,19,21,25,26,28,35,39]

double_lines={L for L,s in line_pairs.items() if len(s)==2}
double_orbits=[o for o in orbits if set(o)<=double_lines]
assert len(double_orbits)==3
assert sum(len(o) for o in double_orbits)==9

print(
    "VERIFY_OK f=21,190,338,169 H1_Z=Z5^3 "
    "graph_triangles=984 facial3=338 empty3=646 all_empty3_nonzero=yes "
    "projective_directions=31 all_directions_hit=yes "
    "unoriented_class_pairs_hit=40of62 direction_pair_profile=double9+single22 "
    "order3_symmetry=yes projective_orbits=1+10x3 "
    "fixed_direction_carriers=16 "
    "triple_direction_totals=2,7,8,19,21,25,26,28,35,39 "
    "maximal_minor_det=-125 rank_mod5=167"
)
