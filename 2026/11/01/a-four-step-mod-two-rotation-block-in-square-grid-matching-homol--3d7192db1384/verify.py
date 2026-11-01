#!/usr/bin/env python3
"""Exact, standalone finite-chain verification for the 3 by 3 grid matching complex.
Requires Python 3, standard library only. No external data or services.
"""
from collections import deque

N = 3
edges = []
for i in range(N):
    for j in range(N):
        if i+1 < N:
            edges.append(((i,j),(i+1,j)))
        if j+1 < N:
            edges.append(((i,j),(i,j+1)))
assert len(edges)==12

# All matchings, including the empty face (bitmask zero).
faces = set()
def generate(matching, eligible):
    faces.add(matching)
    for pos,e in enumerate(eligible):
        endpoints=set(edges[e])
        rest=[k for k in eligible[pos+1:] if endpoints.isdisjoint(edges[k])]
        generate(matching | (1<<e),rest)
generate(0,list(range(12)))
face_by_size={s:sorted(f for f in faces if f.bit_count()==s) for s in range(5)}
assert [len(face_by_size[s]) for s in range(5)]==[1,12,44,56,18]

def facets(f):
    x=f
    while x:
        bit=x&-x
        yield f^bit
        x^=bit

# Canonical matching via successive vertex toggles, on augmented face poset.
remaining=set(faces)
paired_down={}
paired_up={}
for v in range(12):
    bit=1<<v
    pairs=[(f,f|bit) for f in sorted(remaining)
           if not f&bit and f|bit in remaining]
    for lower,upper in pairs:
        assert lower in remaining and upper in remaining
        remaining.remove(lower)
        remaining.remove(upper)
        paired_down[lower]=upper
        paired_up[upper]=lower
assert len(paired_down)==63
assert len(remaining)==5 and all(x.bit_count()==3 for x in remaining)
# Check the directed alternating-face graph on lower paired faces has no cycle.
followers={f:[] for f in paired_down}
indegree={f:0 for f in paired_down}
for f,u in paired_down.items():
    for other in facets(u):
        if other!=f and other in paired_down:
            followers[f].append(other)
            indegree[other]+=1
ready=deque(f for f in paired_down if indegree[f]==0)
seen=0
while ready:
    f=ready.pop();seen+=1
    for other in followers[f]:
        indegree[other]-=1
        if indegree[other]==0:
            ready.append(other)
assert seen==63, (seen,len(paired_down))
# Augmented discrete Morse complex has exactly five critical 2-cells,
# hence reduced integral homology H2=Z^5, all other reduced groups zero.

id_edge={tuple(sorted(e)):k for k,e in enumerate(edges)}
def edge_perm(f):
    return [id_edge[tuple(sorted((f(*u),f(*v))))] for u,v in edges]
identity=lambda i,j:(i,j)
rot=lambda i,j:(j,2-i)
rot2=lambda i,j:(2-i,2-j)
axis=lambda i,j:(2-i,j)
diag=lambda i,j:(j,i)
ops=[identity,rot,rot2,axis,diag]

def perm_mask(x,p):
    new=0
    while x:
        b=x&-x
        k=b.bit_length()-1
        new|=1<<p[k]
        x^=b
    return new

def inversion_sign(seq):
    inv=sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))
    return 1 if inv%2==0 else -1

# The reduced Hopf trace formula includes the augmented empty simplex term -1.
traces=[]
for fun in ops:
    p=edge_perm(fun)
    val=-1
    for s in range(1,5):
        for face in face_by_size[s]:
            if perm_mask(face,p)!=face:
                continue
            seq=[p[k] for k in range(12) if face & (1<<k)]
            val+=((-1)**(s-1))*inversion_sign(seq)
    traces.append(val)
assert traces==[5,1,1,-1,1],traces

# F2 boundary map from matching s-faces to matching (s-1)-faces.
idx={s:{f:k for k,f in enumerate(face_by_size[s])} for s in (2,3,4)}
def xor_columns(cols):
    pivots={}
    dependencies=[]
    for i,x in enumerate(cols):
        coeff=1<<i
        while x:
            pivot=x.bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=(x,coeff)
                break
            y,c=pivots[pivot]
            x^=y;coeff^=c
        if not x:
            dependencies.append(coeff)
    return pivots,dependencies

def f2_rank(vecs):
    return len(xor_columns(vecs)[0])

triangles=face_by_size[3]
tetrahedra=face_by_size[4]
columns_2=[sum(1<<idx[2][sub] for sub in facets(face)) for face in triangles]
cycle_generators=xor_columns(columns_2)[1]
assert len(cycle_generators)==23
boundary_3=[sum(1<<idx[3][sub] for sub in facets(face)) for face in tetrahedra]
assert f2_rank(boundary_3)==18
assert f2_rank(columns_2)==33
# Check that all 18 boundaries of tetrahedra are cycles.
for x in boundary_3:
    y=0
    while x:
        b=x&-x
        y^=columns_2[b.bit_length()-1]
        x^=b
    assert y==0

# Build quotient coordinates relative to im(d3), then independent ker(d2) cycles.
def quotient_basis(vectors):
    pivot={}
    basis=[]
    for w in vectors:
        x=w;coordinates=0
        while x:
            k=x.bit_length()-1
            if k not in pivot:
                t=len(basis)
                pivot[k]=(x,coordinates^(1<<t))
                basis.append(w)
                break
            y,c=pivot[k]
            x^=y;coordinates^=c
    return pivot,basis

pivots,canonical=quotient_basis(boundary_3+cycle_generators)
assert len(canonical)==23 and f2_rank(canonical)==23
homology_cycles=canonical[18:]

def coordinates(x):
    out=0
    while x:
        k=x.bit_length()-1
        y,c=pivots[k]
        x^=y;out^=c
    return out

def permute_chain(x,permutation):
    result=0
    while x:
        bit=x&-x
        result^=1<<permutation[bit.bit_length()-1]
        x^=bit
    return result

def homology_matrix(fun):
    pp=edge_perm(fun)
    tri_index=[idx[3][perm_mask(face,pp)] for face in triangles]
    rows=[0]*5
    for col,cycle in enumerate(homology_cycles):
        transformed=permute_chain(cycle,tri_index)
        coefficients=coordinates(transformed)
        assert coefficients>>23==0
        coefficients>>=18
        for row in range(5):
            rows[row]|=((coefficients>>row)&1)<<col
    return rows

I=[1,2,4,8,16]
R=homology_matrix(rot)
D=homology_matrix(diag)
assert R==[28,1,19,11,13],R
assert D==[8,11,13,1,19],D

def act(M,v):
    return sum(((int((row&v).bit_count()%2))<<i) for i,row in enumerate(M))

def mmul(A,B):
    return [sum(((act(A,act(B,1<<j))>>i)&1)<<j for j in range(5)) for i in range(5)]

def mat_rank(A):
    return f2_rank([sum(((v>>j)&1)<<i for i,v in enumerate(A)) for j in range(5)])

assert mmul(mmul(mmul(R,R),R),R)==I
assert mmul(D,D)==I
assert mmul(mmul(D,R),D)==mmul(mmul(R,R),R)
Nmat=[R[i]^I[i] for i in range(5)]
ranks=[]
cur=I
for j in range(1,5):
    cur=mmul(Nmat,cur)
    ranks.append(mat_rank(cur))
assert ranks==[3,2,1,0],ranks
# Five-dimensional nilpotent with rank powers 3,2,1,0 = J4(0) plus J1(0).
print('VERIFY_OK: 131 augmented faces; 63 acyclic pairs; 5 H2 spheres;')
print('D4 rational character:',traces)
print('H2(F2) rotation rows:',R,'diagonal reflection rows:',D)
print('r-I power ranks:',ranks,'=> Jordan J4(1) + J1(1)')
