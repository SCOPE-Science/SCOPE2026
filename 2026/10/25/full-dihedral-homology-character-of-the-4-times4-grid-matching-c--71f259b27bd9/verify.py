#!/usr/bin/env python3
"""Exact integral chains and rational dihedral characters for a finite grid matching complex.

Requires only Python 3.9+ standard library. All computations are exact integers.
"""
from collections import defaultdict, deque
from itertools import combinations

SIZE = 4
EDGE_LIST = []
for row in range(SIZE):
    for col in range(SIZE):
        if row + 1 < SIZE:
            EDGE_LIST.append(tuple(sorted(((row,col),(row+1,col)))))
        if col + 1 < SIZE:
            EDGE_LIST.append(tuple(sorted(((row,col),(row,col+1)))))
EDGE_LOOKUP = {e:i for i,e in enumerate(EDGE_LIST)}
EDGE_VERTEX_MASKS = [sum(1<<(SIZE*r+c) for r,c in e) for e in EDGE_LIST]
assert len(EDGE_LIST)==24

FACES = defaultdict(list)
FACES[0]=[0]
def enumerate_from(face,used,last):
    for e in range(last+1,24):
        if used & EDGE_VERTEX_MASKS[e]:
            continue
        nxt=face|(1<<e)
        FACES[nxt.bit_count()].append(nxt)
        enumerate_from(nxt,used|EDGE_VERTEX_MASKS[e],e)
enumerate_from(0,0,-1)
assert tuple(len(FACES[k]) for k in range(9))==(1,24,224,1044,2593,3388,2150,552,36)
ALL_FACES=set().union(*[set(v) for v in FACES.values()])
assert len(ALL_FACES)==10012

# An explicit elementary matching: successive toggles on currently unmatched faces.
ACTIVE=set(ALL_FACES)
PAIRED={}
for toggle in range(24):
    found=[]
    for f in sorted(ACTIVE,key=lambda x:(x.bit_count(),x)):
        upper=f|(1<<toggle)
        if not f & (1<<toggle) and upper in ACTIVE:
            found.append((f,upper))
    for lower,upper in found:
        assert lower in ACTIVE and upper in ACTIVE
        ACTIVE.remove(lower)
        ACTIVE.remove(upper)
        PAIRED[lower]=upper
        PAIRED[upper]=lower
CRITICAL=defaultdict(list)
for f in ACTIVE:
    CRITICAL[f.bit_count()].append(f)
for items in CRITICAL.values():
    items.sort()
assert set(CRITICAL)=={5,6}
assert len(CRITICAL[5])==10 and len(CRITICAL[6])==6
assert len(PAIRED)==9996

# Acyclicity of the ENTIRE oriented augmented face-poset Hasse graph.
ARCS=defaultdict(list)
INDEG={f:0 for f in ALL_FACES}
arc_total=0
for k in range(1,9):
    for upper in FACES[k]:
        for e in range(24):
            if not upper & (1<<e):
                continue
            lower=upper^(1<<e)
            if PAIRED.get(lower)==upper:
                start,end=lower,upper
            else:
                start,end=upper,lower
            ARCS[start].append(end)
            INDEG[end]+=1
            arc_total+=1
assert arc_total==47968
queue=deque(x for x,d in INDEG.items() if d==0)
processed=0
while queue:
    x=queue.popleft()
    processed+=1
    for y in ARCS[x]:
        INDEG[y]-=1
        if INDEG[y]==0:
            queue.append(y)
assert processed==10012
print('EXHAUSTIVE_MORSE_ACYCLICITY',len(ALL_FACES),arc_total)

# Standard oriented simplicial integral boundary.
BOUNDARY_CACHE={}
def boundary(face):
    if face not in BOUNDARY_CACHE:
        out={}
        index=0
        for e in range(24):
            if face & (1<<e):
                out[face^(1<<e)]=1 if index%2==0 else -1
                index+=1
        BOUNDARY_CACHE[face]=out
    return BOUNDARY_CACHE[face]

def add_to(target,source,factor=1):
    for key,value in source.items():
        new=target.get(key,0)+factor*value
        if new:
            target[key]=new
        else:
            target.pop(key,None)

def chain_boundary(chain):
    out={}
    for face,coeff in chain.items():
        add_to(out,boundary(face),coeff)
    return out

def solver(k):
    """Solve the lower/upper matching incidence block in cardinality k.

    The off-diagonal dependency graph is acyclic by the checked matching.
    Each pivot is the signed simplicial incidence, hence +/-1.
    """
    lowers=sorted(f for f in FACES[k-1]
                  if f in PAIRED and PAIRED[f].bit_count()==k)
    uppers=[PAIRED[f] for f in lowers]
    upper_index={upper:i for i,upper in enumerate(uppers)}
    diagonal=[]
    off_rows=[]
    for i,(lower,upper) in enumerate(zip(lowers,uppers)):
        b=boundary(upper)
        diagonal.append(b[lower])
        used=0
        for e in range(24):
            if lower & (1<<e):
                used|=EDGE_VERTEX_MASKS[e]
        row={}
        for e in range(24):
            if used & EDGE_VERTEX_MASKS[e]:
                continue
            new_upper=lower|(1<<e)
            if new_upper in upper_index:
                j=upper_index[new_upper]
                row[j]=boundary(new_upper)[lower]
        assert row.pop(i)==diagonal[i]
        off_rows.append(row)
    indegrees=[0]*len(lowers)
    for row in off_rows:
        for j in row:
            indegrees[j]+=1
    todo=deque(i for i,d in enumerate(indegrees) if not d)
    order=[]
    while todo:
        i=todo.popleft()
        order.append(i)
        for j in off_rows[i]:
            indegrees[j]-=1
            if indegrees[j]==0:
                todo.append(j)
    assert len(order)==len(lowers)
    def solve(rhs):
        b=[rhs.get(lower,0) for lower in lowers]
        x=[0]*len(lowers)
        for i in reversed(order):
            total=b[i]-sum(coeff*x[j] for j,coeff in off_rows[i].items())
            assert total%diagonal[i]==0
            x[i]=total//diagonal[i]
        assert all(diagonal[i]*x[i]+sum(coeff*x[j] for j,coeff in off_rows[i].items())==b[i]
                   for i in range(len(lowers)))
        return {uppers[i]:value for i,value in enumerate(x) if value}
    return solve,lowers

SOLVE5,LOWERS4=solver(5)
SOLVE6,LOWERS5=solver(6)
SOLVE7,LOWERS6=solver(7)

def include_critical(face,solve):
    chain={face:1}
    correction=solve(boundary(face))
    add_to(chain,correction,-1)
    return chain
INC5=[include_critical(f,SOLVE5) for f in CRITICAL[5]]
INC6=[include_critical(f,SOLVE6) for f in CRITICAL[6]]
for c in INC6:
    b=chain_boundary(c)
    assert all(b.get(lower,0)==0 for lower in LOWERS5)
for c in INC5:
    b=chain_boundary(c)
    assert all(b.get(lower,0)==0 for lower in LOWERS4)

D=[[chain_boundary(INC6[j]).get(CRITICAL[5][i],0) for j in range(6)] for i in range(10)]
EXPECTED_D=[[0,0,0,0,0,0],
            [0,1,0,0,-1,0],
            [0,0,1,0,0,-1],
            [0,0,0,0,0,0],
            [1,0,0,-1,0,0],
            [1,0,0,-1,-1,1],
            [0,0,0,0,0,0],
            [0,0,0,0,0,0],
            [0,1,-1,0,0,0],
            [0,-1,1,0,0,0]]
assert D==EXPECTED_D
for j in range(6):
    rhs={}
    for i in range(10):
        if D[i][j]: add_to(rhs,INC5[i],D[i][j])
    assert chain_boundary(INC6[j])==rhs
# The first two vectors span the kernel, checked using a unimodular rank-four minor.
KERNEL=((1,0,0,1,0,0),(0,1,1,0,1,1))
for vec in KERNEL:
    assert all(sum(D[i][j]*vec[j] for j in range(6))==0 for i in range(10))
# Rows (1,2,4,5), columns (0,1,2,4) give determinant 1.
minor=[[D[i][j] for j in (0,1,2,4)] for i in (1,2,4,5)]
def det4(a):
    from itertools import permutations
    out=0
    for p in permutations(range(4)):
        inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
        prod=1
        for i in range(4):prod*=a[i][p[i]]
        out+=(-1 if inv%2 else 1)*prod
    return out
assert abs(det4(minor))==1
print('INTEGRAL_MORSE_DIFFERENTIAL_RANK_FOUR',10,6,'unimodular_minor',det4(minor))

# The standard two-dimensional top homology can be represented by explicit integral cycles.
TOP_CYCLES=[]
for vec in KERNEL:
    chain={}
    for j,coeff in enumerate(vec):
        if coeff:add_to(chain,INC6[j],coeff)
    assert not chain_boundary(chain)
    TOP_CYCLES.append(chain)

def transform_vertex(pos,rotation,reflection):
    row,col=pos
    if reflection:
        col=SIZE-1-col
    for _ in range(rotation):
        row,col=col,SIZE-1-row
    return row,col

def transformed_edge_permutation(rotation,reflection):
    return [EDGE_LOOKUP[tuple(sorted(transform_vertex(v,rotation,reflection) for v in edge))]
            for edge in EDGE_LIST]

def act(chain,edge_perm):
    result={}
    for face,coeff in chain.items():
        permuted=[edge_perm[e] for e in range(24) if face & (1<<e)]
        inv=sum(permuted[i]>permuted[j] for i in range(len(permuted)) for j in range(i+1,len(permuted)))
        newface=sum(1<<i for i in permuted)
        assert newface in ALL_FACES
        add_to(result,{newface:1},coeff*(-1 if inv%2 else 1))
    return result

def top_class_coordinates(chain):
    # Subtract a genuine boundary to remove every cell paired upward in cardinality 6.
    correction=SOLVE7(chain)
    newchain=dict(chain)
    for upper,coeff in correction.items():
        add_to(newchain,boundary(upper),-coeff)
    assert all(newchain.get(lower,0)==0 for lower in LOWERS6)
    coords=[newchain.get(c,0) for c in CRITICAL[6]]
    a,b=coords[0],coords[1]
    assert coords==[a,b,b,a,b,b]
    representative={}
    add_to(representative,TOP_CYCLES[0],a)
    add_to(representative,TOP_CYCLES[1],b)
    assert representative==newchain
    return (a,b)

H5={}; H4={}; LEFSCHETZ={}; MATRICES={}
for rotation in range(4):
    for reflection in (0,1):
        perm=transformed_edge_permutation(rotation,reflection)
        matrixcols=[]
        for cycle in TOP_CYCLES:
            shifted=act(cycle,perm)
            assert not chain_boundary(shifted)
            matrixcols.append(top_class_coordinates(shifted))
        mat=((matrixcols[0][0],matrixcols[1][0]),(matrixcols[0][1],matrixcols[1][1]))
        MATRICES[rotation,reflection]=mat
        trace_top=mat[0][0]+mat[1][1]
        H5[rotation,reflection]=trace_top
        # Reduced Lefschetz trace: alternate the signed fixed oriented faces,
        # counting the augmentation (empty simplex) in degree -1 with sign -1.
        tr=-1
        for k in range(1,9):
            for face in FACES[k]:
                indices=[perm[e] for e in range(24) if face & (1<<e)]
                newface=sum(1<<i for i in indices)
                if newface!=face:
                    continue
                inv=sum(indices[i]>indices[j] for i in range(len(indices)) for j in range(i+1,len(indices)))
                tr+=(-1 if inv%2 else 1)*(1 if (k-1)%2==0 else -1)
        LEFSCHETZ[rotation,reflection]=tr
        H4[rotation,reflection]=tr+trace_top

expected_H5={(r,s):(2 if r==0 else -2 if r==2 else 0) for r in range(4) for s in (0,1)}
# Reflection classes have trace zero in the two-dimensional rotation representation.
for r in range(4):
    expected_H5[r,1]=0
assert H5==expected_H5
assert MATRICES[1,0]==((0,1),(-1,0))
assert MATRICES[0,1]==((-1,0),(0,1))
def matmul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
identity=((1,0),(0,1))
R=MATRICES[1,0]; S=MATRICES[0,1]
assert matmul(matmul(R,R),matmul(R,R))==identity
assert matmul(S,S)==identity
assert matmul(matmul(S,R),S)==MATRICES[3,0]
expected_H4={(0,0):6,(1,0):2,(2,0):2,(3,0):2,
             (0,1):0,(1,1):-2,(2,1):0,(3,1):-2}
assert H4==expected_H4
# Check finite irreducible decomposition without relying on a character table.
# Characters A1, A2, B1 and the standard two-dimensional E.
def a1(r,s):return 1
def a2(r,s):return (-1)**s
def b1(r,s):return (-1)**r
def e_char(r,s):return 0 if s else (2 if r==0 else -2 if r==2 else 0)
for r in range(4):
    for s in (0,1):
        assert H4[r,s] == a1(r,s)+2*a2(r,s)+b1(r,s)+e_char(r,s)
        assert H5[r,s] == e_char(r,s)
assert sum(H4.values())//8 == 1 and sum(H5.values()) == 0
print('ALL_EIGHT_DIHEDRAL_CHARACTERS_VERIFIED',H4,H5)
print('DEGREE_FOUR_AND_FIVE_MODULES_AND_QUOTIENT_VERIFIED')
