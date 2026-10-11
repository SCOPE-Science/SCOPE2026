#!/usr/bin/env python3
from itertools import combinations
from collections import Counter, defaultdict, deque

FACETS = {
    (1, 2, 3, 4),
    (1, 2, 3, 5),
    (1, 2, 4, 6),
    (1, 2, 5, 6),
    (1, 3, 4, 7),
    (1, 3, 5, 7),
    (1, 4, 6, 8),
    (1, 4, 7, 9),
    (1, 4, 8, 9),
    (1, 5, 6, 10),
    (1, 5, 7, 11),
    (1, 5, 10, 11),
    (1, 6, 8, 12),
    (1, 6, 10, 12),
    (1, 7, 9, 13),
    (1, 7, 11, 14),
    (1, 7, 13, 15),
    (1, 7, 14, 15),
    (1, 8, 9, 12),
    (1, 9, 12, 16),
    (1, 9, 13, 16),
    (1, 10, 11, 17),
    (1, 10, 12, 17),
    (1, 11, 14, 17),
    (1, 12, 16, 17),
    (1, 13, 15, 16),
    (1, 14, 15, 16),
    (1, 14, 16, 17),
    (2, 3, 4, 12),
    (2, 3, 5, 15),
    (2, 3, 12, 15),
    (2, 4, 6, 14),
    (2, 4, 12, 18),
    (2, 4, 14, 18),
    (2, 5, 6, 13),
    (2, 5, 13, 15),
    (2, 6, 9, 14),
    (2, 6, 9, 17),
    (2, 6, 13, 17),
    (2, 7, 10, 13),
    (2, 7, 10, 16),
    (2, 7, 12, 15),
    (2, 7, 12, 18),
    (2, 7, 13, 15),
    (2, 7, 16, 18),
    (2, 8, 9, 14),
    (2, 8, 9, 17),
    (2, 8, 11, 17),
    (2, 8, 11, 18),
    (2, 8, 14, 18),
    (2, 10, 11, 16),
    (2, 10, 11, 17),
    (2, 10, 13, 17),
    (2, 11, 16, 18),
    (3, 4, 7, 16),
    (3, 4, 12, 13),
    (3, 4, 13, 16),
    (3, 5, 7, 17),
    (3, 5, 15, 17),
    (3, 6, 10, 12),
    (3, 6, 10, 18),
    (3, 6, 12, 15),
    (3, 6, 15, 17),
    (3, 6, 17, 18),
    (3, 7, 16, 18),
    (3, 7, 17, 18),
    (3, 9, 10, 13),
    (3, 9, 10, 18),
    (3, 9, 13, 16),
    (3, 9, 16, 18),
    (3, 10, 12, 13),
    (4, 5, 13, 15),
    (4, 5, 13, 18),
    (4, 5, 14, 17),
    (4, 5, 14, 18),
    (4, 5, 15, 17),
    (4, 6, 8, 11),
    (4, 6, 11, 14),
    (4, 7, 9, 10),
    (4, 7, 10, 16),
    (4, 8, 9, 17),
    (4, 8, 11, 17),
    (4, 9, 10, 15),
    (4, 9, 15, 17),
    (4, 10, 15, 16),
    (4, 11, 14, 17),
    (4, 12, 13, 18),
    (4, 13, 15, 16),
    (5, 6, 10, 18),
    (5, 6, 13, 18),
    (5, 7, 11, 12),
    (5, 7, 12, 17),
    (5, 10, 11, 16),
    (5, 10, 14, 16),
    (5, 10, 14, 18),
    (5, 11, 12, 16),
    (5, 12, 16, 17),
    (5, 14, 16, 17),
    (6, 8, 11, 15),
    (6, 8, 12, 15),
    (6, 9, 11, 14),
    (6, 9, 11, 15),
    (6, 9, 15, 17),
    (6, 13, 17, 18),
    (7, 9, 10, 13),
    (7, 11, 12, 14),
    (7, 12, 14, 15),
    (7, 12, 17, 18),
    (8, 9, 12, 14),
    (8, 11, 15, 18),
    (8, 12, 14, 15),
    (8, 14, 15, 18),
    (9, 10, 15, 18),
    (9, 11, 12, 14),
    (9, 11, 12, 16),
    (9, 11, 15, 18),
    (9, 11, 16, 18),
    (10, 12, 13, 17),
    (10, 14, 15, 16),
    (10, 14, 15, 18),
    (12, 13, 17, 18)
}
V = tuple(range(1,19))

def faces(k):
    return sorted({tuple(sorted(c)) for f in FACETS for c in combinations(f,k)})

E = faces(2)
T = faces(3)
assert (len(V),len(E),len(T),len(FACETS)) == (18,139,242,121)
ESET,TSET=set(E),set(T)

# Every triangular face is in two tetrahedra, as expected for a closed 3-manifold.
inc=Counter()
for f in FACETS:
    for t in combinations(f,3):
        inc[tuple(sorted(t))]+=1
assert len(inc)==242 and set(inc.values())=={2}

# Contract a deterministic spanning tree of the one-skeleton.
adj=defaultdict(list)
for a,b in E:
    adj[a].append(b); adj[b].append(a)
TREE=set()
seen={1}
q=deque([1])
while q:
    u=q.popleft()
    for v in sorted(adj[u]):
        if v not in seen:
            seen.add(v); q.append(v); TREE.add(tuple(sorted((u,v))))
assert len(TREE)==17 and len(seen)==18
NTE=[e for e in E if e not in TREE]
EI={e:i for i,e in enumerate(NTE)}
assert len(NTE)==122

def triangle_relation(t):
    a,b,c=sorted(t)
    row=[0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI:
            row[EI[e]] += s
    return row

R=[triangle_relation(t) for t in T]

def rref_mod(A,p,track_rows=False):
    A=[[(x%p) for x in row] for row in A]
    m,n=len(A),len(A[0])
    ids=list(range(m))
    r=0; pivcols=[]
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
                z=A[i][c]
                A[i]=[(a-z*b)%p for a,b in zip(A[i],A[r])]
        pivcols.append(c); r+=1
        if r==m:
            break
    return r,A,pivcols,(ids[:r] if track_rows else None)

def bareiss_det(A):
    A=[row[:] for row in A]
    n=len(A)
    sign=1; prev=1
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

# A maximal minor of determinant 25 and a rank drop of two mod 5
# force Smith factors 5,5 after 120 unit factors.
r2,_,_,rows2=rref_mod(R,2,track_rows=True)
assert r2==122
det=bareiss_det([R[i] for i in rows2])
assert abs(det)==25
r5,RR,pivcols,_=rref_mod(R,5)
assert r5==120
free=[j for j in range(len(NTE)) if j not in pivcols]
assert len(free)==2

# Basis of mod-5 cocycles, which gives exact coordinates because
# the integral quotient has just been proved to be (Z/5)^2.
COCYCLES=[]
for f in free:
    v=[0]*len(NTE); v[f]=1
    for i,c in enumerate(pivcols):
        v[c]=(-RR[i][f])%5
    assert all(sum(a*b for a,b in zip(row,v))%5==0 for row in R)
    COCYCLES.append(v)

def oriented_triangle_chain(t):
    a,b,c=t
    x=[0]*len(NTE)
    for u,v in [(a,b),(b,c),(c,a)]:
        e=tuple(sorted((u,v)))
        if e in EI:
            x[EI[e]] += 1 if (u,v)==e else -1
    return x

def coord(t):
    x=oriented_triangle_chain(t)
    return tuple(sum(a*b for a,b in zip(x,w))%5 for w in COCYCLES)

cliques=[
    c for c in combinations(V,3)
    if all(tuple(sorted(e)) in ESET for e in combinations(c,2))
]
empty=[c for c in cliques if c not in TSET]
assert (len(cliques),len(empty))==(619,377)
assert all(coord(c)!=(0,0) for c in empty)

# Unoriented class pairs {x,-x}. There are 12 possible nonzero pairs.
def canon_sign(v):
    neg=tuple((-x)%5 for x in v)
    return min(v,neg)

pair_counts=Counter(canon_sign(coord(c)) for c in empty)
assert len(pair_counts)==12
pair_profile=sorted(pair_counts.values())
assert pair_profile==[11,15,15,17,19,30,33,39,45,49,52,52]
assert sum(pair_profile)==377

# Projective order-five directions: six lines in F_5^2.
def proj(v):
    vals=[]
    for a in range(1,5):
        vals.append(tuple((a*x)%5 for x in v))
    return min(vals)

direction_counts=Counter(proj(coord(c)) for c in empty)
assert len(direction_counts)==6
direction_profile=sorted(direction_counts.values())
assert direction_profile==[50,50,60,64,71,82]

# Every nonzero integral class is represented: each of the 12 sign-pairs occurs,
# and reversing a triangle changes x to -x.
all_nonzero={(a,b) for a in range(5) for b in range(5) if (a,b)!=(0,0)}
represented=set()
for c in empty:
    v=coord(c); represented.add(v); represented.add(tuple((-x)%5 for x in v))
assert represented==all_nonzero

print(
    "VERIFY_OK f=18,139,242,121 H1_Z=Z5^2 "
    "graph_triangles=619 facial3=242 empty3=377 "
    "all_empty3_nonzero=yes simple_integral_1_systole=3 minimizers=377 "
    "all_nonzero_H1_classes_hit=yes nonzero_classes=24 "
    "unoriented_class_pairs=12 pair_profile=11,15,15,17,19,30,33,39,45,49,52,52 "
    "projective_directions=6 direction_profile=50,50,60,64,71,82 "
    "maximal_minor_absdet=25 rank_mod5=120"
)
