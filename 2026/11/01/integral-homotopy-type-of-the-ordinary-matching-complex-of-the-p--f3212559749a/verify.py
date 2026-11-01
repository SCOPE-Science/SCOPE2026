#!/usr/bin/env python3
"""Exact finite verification of the ordinary matching complex of the pentagonal prism.

Uses only Python's standard library.  Bitmask vertices are graph edges; all
nonempty faces, Hasse incidences, matching pairs, gradient paths and signed
Morse boundary coefficients are constructed directly from the graph.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from fractions import Fraction
from itertools import combinations

N = 5
VERTICES = range(2 * N)
EDGES = tuple(sorted({tuple(sorted((s*N+i,s*N+(i+1)%N)))
                      for s in (0,1) for i in range(N)} |
                     {(i,N+i) for i in range(N)}))
assert len(EDGES) == 15
assert len(set(EDGES)) == 15
E = len(EDGES)


def faces_by_independent_ends():
    faces = set()
    for mask in range(1,1<<E):
        used = 0
        valid = True
        for j,(u,v) in enumerate(EDGES):
            if mask & (1<<j):
                b=(1<<u)|(1<<v)
                if used&b:
                    valid=False
                    break
                used |= b
        if valid: faces.add(mask)
    return faces

FACES = faces_by_independent_ends()
assert len(FACES) == 341
assert dict(sorted(Counter(m.bit_count()-1 for m in FACES).items())) == {
    0:15,1:75,2:145,3:95,4:11
}

# Independent face construction using a recursive matching extension.
RECURSIVE = set()
def add_edges(pos,used,mask):
    if pos == E:
        if mask: RECURSIVE.add(mask)
        return
    add_edges(pos+1,used,mask)
    u,v=EDGES[pos]
    b=(1<<u)|(1<<v)
    if used&b == 0:
        add_edges(pos+1,used|b,mask|(1<<pos))
add_edges(0,0,0)
assert FACES == RECURSIVE

# Canonical 15-stage toggle matching; all choices are deterministic.
remaining=set(FACES)
PAIRS=[]
for j in range(E):
    bit = 1<<j
    stage=[(f,f|bit) for f in sorted(remaining)
           if not(f&bit) and (f|bit) in remaining]
    for low,up in stage:
        assert low in remaining and up in remaining
        assert up.bit_count()==low.bit_count()+1
        remaining.remove(low)
        remaining.remove(up)
    PAIRS.extend(stage)
CRITICAL=frozenset(remaining)
assert len(PAIRS)==165
assert Counter(m.bit_count()-1 for m in CRITICAL)=={0:1,2:5,3:5}

LOW_UP={a:b for a,b in PAIRS}
UP_LOW={b:a for a,b in PAIRS}
assert len(LOW_UP)==len(UP_LOW)==len(PAIRS)
assert all(a not in UP_LOW for a in LOW_UP)

# Full directed Hasse graph (1,020 incidences).
arrows=defaultdict(list)
indeg={f:0 for f in FACES}
incidences=0
for upper in FACES:
    for i in range(E):
        if not upper&(1<<i):continue
        lower=upper^(1<<i)
        if lower==0:continue
        assert lower in FACES
        if LOW_UP.get(lower)==upper:
            origin,dest=lower,upper
        else:
            origin,dest=upper,lower
        arrows[origin].append(dest)
        indeg[dest]+=1
        incidences+=1
assert incidences==1020
queue=deque(f for f in sorted(FACES) if indeg[f]==0)
processed=0
while queue:
    f=queue.popleft()
    processed+=1
    for g in arrows[f]:
        indeg[g]-=1
        if indeg[g]==0:queue.append(g)
assert processed==len(FACES),"Gradient Hasse graph contains a cycle"


def signed_boundary(mask):
    b=[j for j in range(E) if mask>>j & 1]
    return [(mask^(1<<j),(-1)**h) for h,j in enumerate(b)]

# Gradient path formula, separately in each degree, with acyclicity above
# providing termination. A k-face matched downward has zero k-projection.
@lru_cache(None)
def descend(face):
    if face in CRITICAL:return {face:1}
    if face in UP_LOW:return {}
    u=LOW_UP[face]
    bd=dict(signed_boundary(u))
    epsilon=bd[face]
    result=defaultdict(int)
    for f,coefficient in bd.items():
        if f==face:continue
        for c,mult in descend(f).items():
            result[c]-=epsilon*coefficient*mult
    return {c:v for c,v in result.items() if v}


def morse_boundary(degree):
    rows=sorted(x for x in CRITICAL if x.bit_count()==degree)
    cols=sorted(x for x in CRITICAL if x.bit_count()==degree+1)
    mat=[]
    for r in rows:
        line=[]
        for c in cols:
            tot=0
            for f,sign in signed_boundary(c):
                tot+=sign*descend(f).get(r,0)
            line.append(tot)
        mat.append(line)
    return rows,cols,mat

rows,cols,BOUNDARY=morse_boundary(3)
EXPECTED=[[-1,1,0,0,0],
          [1,0,0,-1,0],
          [0,1,0,-1,0],
          [0,0,1,1,-1],
          [-1,0,-1,0,1]]
assert BOUNDARY==EXPECTED
assert len(rows)==len(cols)==5


def rank_rational(matrix):
    if not matrix:return 0
    A=[[Fraction(x) for x in row] for row in matrix]
    R,C=len(A),len(A[0]);r=0
    for c in range(C):
        pivot=next((i for i in range(r,R) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        scalar=A[r][c]
        A[r]=[x/scalar for x in A[r]]
        for i in range(R):
            if i!=r and A[i][c]:
                scalar=A[i][c]
                A[i]=[x-scalar*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==R:break
    return r

assert rank_rational(BOUNDARY)==3
# The displayed 3x3 minor has determinant -1: Smith factors all unity.
def det3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
          - a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
          + a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))
assert det3([[BOUNDARY[i][j] for j in (0,1,2)] for i in (0,1,3)])==-1

# Independent simplicial chain ranks modulo different primes.
# Each column is the boundary of a simplex; sparse modular pivot elimination.
def sparse_mod_rank(dim,p):
    pivots={}
    for upper in sorted(f for f in FACES if f.bit_count()==dim+1):
        x={f:(sgn%p) for f,sgn in signed_boundary(upper)}
        if dim==1:
            # 0-simplices all retained, no augmentation row.
            pass
        while x:
            k=min(x)
            if k not in pivots:
                inv=pow(x[k],-1,p)
                pivots[k]={t:(v*inv)%p for t,v in x.items() if v%p}
                break
            val=x[k]; vec=pivots[k]
            for t,v in vec.items():
                z=(x.get(t,0)-val*v)%p
                if z:x[t]=z
                else:x.pop(t,None)
    return len(pivots)

for p in (2,3,5,7):
    ranks={k:sparse_mod_rank(k,p) for k in (1,2,3,4)}
    # C_0..C_4 dimensions: 15,75,145,95,11.
    # d1 has rank 14; d2 rank61; d3 rank82; d4 rank11 (if b2=b3=2).
    assert ranks == {1:14,2:61,3:82,4:11},(p,ranks)

print('VERIFY_OK graph_vertices=10 graph_edges=15 faces=341',
      'fvector=(15,75,145,95,11)',
      'incidences=1020 matched_pairs=165',
      'critical=(1_0,5_2,5_3)',
      'acyclic_Hasse_nodes=341',
      'Morse_boundary_rank=3 unit_minor=-1',
      'reduced_homology=(H2=Z2,H3=Z2)',
      'modular_direct_checks=4')
print('MORSE_D3',BOUNDARY)
print('CRITICAL_0',sorted(x for x in CRITICAL if x.bit_count()==1))
print('CRITICAL_2',rows)
print('CRITICAL_3',cols)
