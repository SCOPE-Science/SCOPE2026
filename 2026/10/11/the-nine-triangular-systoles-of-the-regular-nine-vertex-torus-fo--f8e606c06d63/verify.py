#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import defaultdict, Counter, deque
from math import gcd

V=tuple(range(1,10))
FACETS={
(1,3,6),(1,3,7),(1,4,6),(1,4,8),(1,5,7),(1,5,8),
(2,3,6),(2,3,8),(2,4,7),(2,4,8),(2,5,6),(2,5,7),
(3,7,9),(3,8,9),(4,6,9),(4,7,9),(5,6,9),(5,8,9)
}
# Published group generators (Koehler--Lutz table of generators).
GENS=[
(2,9,4,5,3,7,8,6,1), # (1,2,9)(3,4,5)(6,7,8)
(4,5,6,7,8,9,1,2,3), # (1,4,7)(2,5,8)(3,6,9)
(1,2,4,5,3,8,6,7,9), # (3,4,5)(6,8,7)
(2,1,6,8,7,3,5,4,9), # (1,2)(3,6)(4,8)(5,7)
(2,1,5,4,3,7,6,8,9), # (1,2)(3,5)(6,7)
]

def compose(p,q):
    # p after q, 1-based images stored in tuple positions 0..8
    return tuple(p[q[i]-1] for i in range(9))

def inv(p):
    r=[0]*9
    for i,x in enumerate(p,1): r[x-1]=i
    return tuple(r)

def image_face(f,p):
    return tuple(sorted(p[x-1] for x in f))

# Check seed orbit reconstruction from the published regular map orbit 136_18.
G={tuple(V)}
front=[tuple(V)]
while front:
    a=front.pop()
    for g in GENS:
        b=compose(g,a)
        if b not in G:
            G.add(b); front.append(b)
assert len(G)==108
assert {image_face((1,3,6),g) for g in G}==FACETS

# Reconstruct all faces.
def faces(k):
    return sorted({tuple(c) for f in FACETS for c in combinations(f,k)})
E=faces(2); T=faces(3)
assert (len(V),len(E),len(T),len(FACETS))==(9,27,18,18)
ESET,TSET=set(E),set(T)

# Surface checks.
inc=Counter(e for t in T for e in combinations(t,2))
assert set(inc.values())=={2} and len(inc)==27
for v in V:
    ledges=[]
    for t in T:
        if v in t:
            q=tuple(x for x in t if x!=v)
            ledges.append(tuple(sorted(q)))
    vs={x for e in ledges for x in e}
    deg=Counter(x for e in ledges for x in e)
    assert len(ledges)==len(vs)==6 and all(deg[x]==2 for x in vs)
assert len(V)-len(E)+len(T)==0

# Contract a deterministic spanning tree of the 1-skeleton.
adj=defaultdict(list)
for a,b in E:
    adj[a].append(b); adj[b].append(a)
for a in adj: adj[a].sort()
TREE=set(); seen={1}; q=deque([1])
while q:
    u=q.popleft()
    for v in adj[u]:
        if v not in seen:
            seen.add(v); q.append(v); TREE.add(tuple(sorted((u,v))))
assert len(TREE)==8
NTE=[e for e in E if e not in TREE]
EI={e:i for i,e in enumerate(NTE)}
assert len(NTE)==19

def tri_boundary_row(t):
    a,b,c=sorted(t)
    row=[0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI: row[EI[e]] += s
    return row
R=[tri_boundary_row(t) for t in T]

# Integral unit-pivot reduction. Every operation used is unimodular.
def unit_reduce(A):
    A=[row[:] for row in A]
    m,n=len(A),len(A[0]); k=0
    while k<min(m,n):
        pos=None
        for i in range(k,m):
            for j in range(k,n):
                if abs(A[i][j])==1:
                    pos=(i,j); break
            if pos: break
        if pos is None: break
        i,j=pos
        A[k],A[i]=A[i],A[k]
        for r in range(m): A[r][k],A[r][j]=A[r][j],A[r][k]
        if A[k][k]==-1: A[k]=[-x for x in A[k]]
        for i in range(m):
            if i!=k and A[i][k]:
                c=A[i][k]
                A[i]=[x-c*y for x,y in zip(A[i],A[k])]
        for j in range(n):
            if j!=k and A[k][j]:
                c=A[k][j]
                for i in range(m): A[i][j]-=c*A[i][k]
        k+=1
    return k,A
rank,RR=unit_reduce(R)
assert rank==17
for i in range(len(RR)):
    for j in range(len(RR[0])):
        if i<17 or j<17:
            assert RR[i][j]==(1 if i==j and i<17 else 0)
assert all(x==0 for row in RR[17:] for x in row[17:])
# Hence Smith form diag(1^17,0,0), so H1 = Z^2.

# Explicit integral cocycles in the contracted graph-cycle basis.
Y1=[0,1,0,1,0,0,0,0,0,1,0,1,-1,0,0,0,1,0,0]
Y2=[-1,-1,0,-1,-1,0,0,-1,0,0,0,0,1,0,0,1,0,0,1]
assert len(Y1)==len(Y2)==19
assert all(sum(a*b for a,b in zip(row,Y1))==0 for row in R)
assert all(sum(a*b for a,b in zip(row,Y2))==0 for row in R)

def path_cycle(vertices):
    # oriented closed path, last vertex need not repeat first
    row=[0]*len(NTE)
    cyc=list(vertices)+[vertices[0]]
    for u,v in zip(cyc,cyc[1:]):
        e=tuple(sorted((u,v)))
        assert e in ESET
        if e in EI:
            row[EI[e]] += 1 if (u,v)==e else -1
    return row

def coord_path(vertices):
    x=path_cycle(vertices)
    return (sum(a*b for a,b in zip(x,Y1)),sum(a*b for a,b in zip(x,Y2)))
# Explicit basis cycles prove surjectivity of the coordinate map H1 -> Z^2.
BASIS_CYCLES=((1,4,7),(1,8,3))
assert coord_path(BASIS_CYCLES[0])==(1,0)
assert coord_path(BASIS_CYCLES[1])==(0,1)

# Enumerate graph triangles and exact homology coordinates.
cliques=[c for c in combinations(V,3) if all(tuple(sorted(e)) in ESET for e in combinations(c,2))]
empty=[c for c in cliques if c not in TSET]
assert len(cliques)==27 and len(empty)==9

def coord_triangle(c):
    a,b,d=sorted(c)
    return coord_path((a,b,d))
coords={c:coord_triangle(c) for c in empty}
assert Counter(coords.values())==Counter({(0,-1):3,(1,0):3,(-1,1):3})
assert all(v!=(0,0) and gcd(abs(v[0]),abs(v[1]))==1 for v in coords.values())

# Exhaust the full simplicial automorphism group independently over all 9! permutations.
AUT=[]
for p0 in permutations(V):
    p=tuple(p0)
    if {image_face(f,p) for f in FACETS}==FACETS:
        AUT.append(p)
AUT=set(AUT)
assert len(AUT)==108 and AUT==G

# Induced H1 action in basis above.
def action_matrix(p):
    c1=coord_path(tuple(p[x-1] for x in BASIS_CYCLES[0]))
    c2=coord_path(tuple(p[x-1] for x in BASIS_CYCLES[1]))
    # row-major tuple representing columns c1,c2: [[c1[0],c2[0]],[c1[1],c2[1]]]
    return (c1[0],c2[0],c1[1],c2[1])
MATS={action_matrix(p) for p in AUT}
assert len(MATS)==12
assert all(a*d-b*c in (-1,1) for a,b,c,d in MATS)
KERNEL={p for p in AUT if action_matrix(p)==(1,0,0,1)}
assert len(KERNEL)==9

# Full automorphism group is transitive on the 9 carriers.
def orbit(S,H):
    return {image_face(S,p) for p in H}
assert len(orbit(empty[0],AUT))==9

# Kernel orbits are the three exact homology directions, size 3 each.
remaining=set(empty); korbits=[]
while remaining:
    rep=min(remaining)
    O=orbit(rep,KERNEL)
    assert O<=set(empty) and len(O)==3
    cv={coords[x] for x in O}
    assert len(cv)==1
    korbits.append((rep,next(iter(cv)),tuple(sorted(O))))
    remaining-=O
assert len(korbits)==3
assert {x[1] for x in korbits}=={(0,-1),(1,0),(-1,1)}

# Image action is transitive on the three unoriented primitive directions.
def unor(v):
    a,b=v
    if a<0 or (a==0 and b<0): a,b=-a,-b
    return (a,b)
DIRECTIONS={unor(v) for v in coords.values()}
assert DIRECTIONS=={(0,1),(1,0),(1,-1)}
def mat_apply(m,v):
    a,b,c,d=m; x,y=v
    return (a*x+b*y,c*x+d*y)
for d0 in DIRECTIONS:
    hit={unor(mat_apply(m,d0)) for m in MATS}
    assert hit==DIRECTIONS

# Published generators induce the expected order-12 hexagonal action.
GEN_MATS=[action_matrix(g) for g in GENS]
assert GEN_MATS==[
    (1,0,0,1),
    (1,0,0,1),
    (-1,-1,1,0),
    (-1,0,0,-1),
    (0,-1,-1,0)
]

print(
    'VERIFY_OK f=9,27,18 H1_Z=Z^2 '
    'graph_triangles=27 facial3=18 empty3=9 '
    'all_empty3_nonzero_primitive=yes simple_integral_1_systole=3 '
    'unoriented_directions=3 carrier_counts=3,3,3 '
    'aut=108 aut_carrier_orbits=9 '
    'H1_action_image=12 H1_action_kernel=9 kernel_carrier_orbits=3,3,3 '
    'smith=1^17,0,0'
)
