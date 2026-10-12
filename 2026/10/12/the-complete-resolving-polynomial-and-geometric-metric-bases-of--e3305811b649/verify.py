#!/usr/bin/env python3
"""Exact finite-field, distance-signature and symmetry checks for the Pappus graph.

Requires only Python 3.9+ standard library. Point vertices are indices 0..8
in lexicographic order (x,y); line vertices are indices 9..17 in order (m,b).
The retained directions are y = m*x+b over F_3, m in {0,1,2}.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

F = (0,1,2)
P = tuple(product(F,F))
L = tuple(product(F,F))
N = 18
MASK = (1 << N) - 1
idxp = {p:i for i,p in enumerate(P)}
idxl = {a:9+i for i,a in enumerate(L)}
A = [set() for _ in range(N)]
for i,(x,y) in enumerate(P):
    for j,(m,b) in enumerate(L):
        if (y-m*x-b)%3==0:
            A[i].add(9+j); A[9+j].add(i)
assert all(len(neighbors)==3 for neighbors in A)
assert sum(map(len,A))//2==27

# Breadth-first distances independently of the coordinate distance formulas.
D=[]
for u in range(N):
    du=[N+1]*N; du[u]=0; todo=[u]
    for v in todo:
        for w in A[v]:
            if du[w]==N+1:
                du[w]=du[v]+1; todo.append(w)
    assert len(todo)==N
    D.append(tuple(du))
assert max(max(row) for row in D)==4
assert all(Counter(row)=={0:1,1:3,2:6,3:6,4:2} for row in D)

def coordinate_distance(i,j):
    if i<9 and j<9:
        if i==j:return 0
        return 4 if P[i][0]==P[j][0] else 2
    if i>=9 and j>=9:
        if i==j:return 0
        return 4 if L[i-9][0]==L[j-9][0] else 2
    if i>=9:i,j=j,i
    x,y=P[i];m,b=L[j-9]
    return 1 if (y-m*x-b)%3==0 else 3
assert all(D[i][j]==coordinate_distance(i,j) for i in range(N) for j in range(N))

# Each pair of vertices must be distinguished by at least one selected vertex.
# For opposite bipartition sides this follows from distance parity; we still
# construct every condition, without exploiting that shortcut.
requirements=[]
for u,v in combinations(range(N),2):
    distinguishing=sum(1<<z for z in range(N) if D[u][z]!=D[v][z])
    requirements.append(distinguishing)
assert len(requirements)==153

def mask_resolves(mask):
    return all(mask & req for req in requirements)

def signature_resolves(mask):
    sel=[v for v in range(N) if (mask>>v)&1]
    sig={tuple(coordinate_distance(u,v) for v in sel) for u in range(N)}
    return len(sig)==N

# Independent formulations agree over every single subset, not a sample.
poly=Counter()
bases=[]
for mask in range(MASK+1):
    b1=mask_resolves(mask)
    b2=signature_resolves(mask)
    assert b1==b2,(mask,b1,b2)
    if b1:
        poly[mask.bit_count()]+=1
        if mask.bit_count()==4:bases.append(mask)
expected={4:216,5:2808,6:13500,7:29232,8:42894,9:48440,
          10:43740,11:31824,12:18564,13:8568,14:3060,
          15:816,16:153,17:18,18:1}
assert dict(poly)==expected,(poly,expected)
assert sum(poly.values())==243834
assert 2**18-sum(poly.values())==18310
assert len(bases)==216

# Coordinate-free in spirit: the finite-field criterion is the theorem's
# geometric characterization of the 4-vertex bases.
def geometric_basis(S):
    if len(S)!=4:return False
    p=[v for v in S if v<9]
    ls=[v-9 for v in S if v>=9]
    if len(p)!=2 or len(ls)!=2:return False
    x1,y1=P[p[0]];x2,y2=P[p[1]]
    if x1==x2:return False
    inv=lambda z: pow(z%3,-1,3)
    slope=((y2-y1)*inv(x2-x1))%3
    intercept=(y1-slope*x1)%3
    m1,b1=L[ls[0]];m2,b2=L[ls[1]]
    if m1==m2:return False
    if (m1==slope)+(m2==slope)!=1:return False
    par_b=b1 if m1==slope else b2
    if par_b==intercept:return False
    xmeet=((b2-b1)*inv(m1-m2))%3
    return xmeet in (x1,x2)

geometric={sum(1<<v for v in S) for S in combinations(range(N),4)
           if geometric_basis(S)}
assert len(geometric)==216
assert geometric==set(bases)
assert sum(1 for s in bases if (s & 0x1ff).bit_count()!=2)==0

# The 108 collineations preserving the three omitted vertical fibres:
# x'=a*x+b, y'=c*x+d*y+e (a,d nonzero); induced action on lines
# m'=(c+d*m)/a, b'=d*b+e-m'*b. Compose with point/line duality
# p(x,y)->line(x,-y), line(m,b)->point(m,-b).
def affine_perm(a,d,b,c,e):
    z=[]
    for x,y in P:
        z.append(idxp[((a*x+b)%3,(c*x+d*y+e)%3)])
    for m,k in L:
        mp=((c+d*m)*pow(a,-1,3))%3
        kp=(d*k+e-mp*b)%3
        z.append(idxl[(mp,kp)])
    return tuple(z)

def dual(v):
    if v<9:
        x,y=P[v];return idxl[(x,-y%3)]
    m,b=L[v-9];return idxp[(m,-b%3)]

group=set()
for a,d in product((1,2),repeat=2):
    for b,c,e in product(F,repeat=3):
        z=affine_perm(a,d,b,c,e)
        group.add(z)
        group.add(tuple(dual(w) for w in z))
assert len(group)==216
for z in group:
    assert set(z)==set(range(N))
    assert all((z[v] in A[z[u]])==(v in A[u]) for u in range(N) for v in range(N))

# Orbit sizes and the two distinct induced-edge types.
unseen=set(bases)
orbits=[]
while unseen:
    representative=min(unseen)
    orbit={sum(1<<z[v] for v in range(N) if representative>>v &1)
           for z in group}
    assert orbit <= set(bases)
    unseen-=orbit
    incidences={sum(1 for u in range(9) if (s>>u)&1
                    for v in A[u] if (s>>v)&1) for s in orbit}
    assert len(incidences)==1
    orbits.append((len(orbit),next(iter(incidences)),representative))
assert sorted((length,inc) for length,inc,_ in orbits)==[(108,0),(108,1)]
print('VERIFY_OK Pappus=AG(2,3)_minus_vertical 18_vertices 27_edges diameter=4 sphere=1,3,6,6,2')
print('VERIFY_OK masks=262144 BFS_and_F3_distance_signatures_agree=true resolving=243834 nonresolving=18310')
print('VERIFY_OK metric_dimension=4 metric_bases=216 all_exact_geometric_criterion=true')
print('VERIFY_OK polynomial='+','.join('%d:%d'%(k,poly[k]) for k in sorted(poly)))
print('VERIFY_OK automorphism_group=216 two_orbits=108,108 incidence_internal_edges=0,1')
