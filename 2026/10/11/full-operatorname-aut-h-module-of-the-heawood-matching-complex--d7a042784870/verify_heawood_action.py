#!/usr/bin/env python3
"""Reconstruct the rational homology character of the Fano incidence matching complex.

Uses only the Python standard library. All computations are deterministic.
"""
from collections import Counter
from itertools import permutations

N = 7
D = (0, 1, 3)
LINES = tuple(frozenset((j+d) % N for d in D) for j in range(N))
EDGES = tuple(sorted((p, 7+j) for p in range(N) for j,L in enumerate(LINES) if p in L))
assert len(EDGES) == 21
assert len(set(LINES)) == 7
assert all(sum(p in L for L in LINES) == 3 for p in range(N))
assert all(len(LINES[i] & LINES[j]) == 1 for i in range(7) for j in range(i+1,7))
INDEX = {e:i for i,e in enumerate(EDGES)}

FACES = [[] for _ in range(7)]
def visit(start, face, covered):
    for i in range(start, len(EDGES)):
        u,v = EDGES[i]
        vertex_mask = (1<<u) | (1<<v)
        if vertex_mask & covered:
            continue
        f = face | (1<<i)
        FACES[f.bit_count()-1].append(f)
        visit(i+1, f, covered | vertex_mask)
visit(0,0,0)
assert tuple(map(len,FACES)) == (21,168,644,1218,1050,336,24)
ALL_FACES = tuple(f for level in FACES for f in level)
assert len(ALL_FACES) == 3461

# Exact finite-field boundary ranks. Columns are represented by arbitrary-precision
# integers, so XOR is Gaussian elimination over the field of two elements.
RANKS=[]
for k in range(1,7):
    lower = {f:i for i,f in enumerate(FACES[k-1])}
    pivots = {}
    for face in FACES[k]:
        col=0
        bits=face
        while bits:
            one = bits & -bits
            col ^= 1 << lower[face ^ one]
            bits ^= one
        while col:
            row = col.bit_length()-1
            if row in pivots:
                col ^= pivots[row]
            else:
                pivots[row] = col
                break
    RANKS.append(len(pivots))
assert tuple(RANKS) == (20,148,496,722,312,24)
assert tuple(len(FACES[k]) - RANKS[k-1] - RANKS[k] for k in range(1,6)) == (0,0,0,16,0)
assert len(FACES[0])-1-RANKS[0] == 0 and len(FACES[6])-RANKS[5] == 0

# The unique bipartition of the connected incidence graph permits either
# preserving the seven point vertices or exchanging the two colour classes.
line_index = {L:j for j,L in enumerate(LINES)}
PRES=[]
for p in permutations(range(7)):
    transformed=[frozenset(p[x] for x in L) for L in LINES]
    if all(L in line_index for L in transformed):
        PRES.append(tuple(p) + tuple(7+line_index[L] for L in transformed))
assert len(PRES)==168
DUAL = tuple(7+(-i)%7 for i in range(7)) + tuple((-j)%7 for j in range(7))
SWAP=[tuple(DUAL[x] for x in p) for p in PRES]
GROUP=PRES+SWAP
assert len(GROUP)==336 and len(set(GROUP))==336
assert all({tuple(sorted((p[u],p[v]))) for u,v in EDGES} == set(EDGES) for p in GROUP)
ID=tuple(range(14))
def compose(g,h): return tuple(g[h[i]] for i in range(14))
def order(g):
    x=ID
    for k in range(1,49):
        x=compose(g,x)
        if x==ID: return k
    raise AssertionError('unbounded order')

def signed_trace(g):
    edge_map=[INDEX[tuple(sorted((g[u],g[v])))] for u,v in EDGES]
    answer=-1  # the reduced degree-minus-one generator
    for dim,faces in enumerate(FACES):
        accum=0
        for face in faces:
            indices=[i for i in range(21) if face & (1<<i)]
            targets=[edge_map[i] for i in indices]
            if sum(1<<j for j in targets)!=face:
                continue
            inversions=sum(targets[i]>targets[j] for i in range(len(targets)) for j in range(i+1,len(targets)))
            accum+=(-1)**inversions
        answer+=(-1)**dim*accum
    return answer

def orbit_trace(g):
    # A fixed matching is a union of edge cycles. In the reduced Lefschetz
    # sum, each selected edge cycle contributes a factor -1, irrespective
    # of its length. This is independent of the simplex-orientation routine.
    edge_map=[INDEX[tuple(sorted((g[u],g[v])))] for u,v in EDGES]
    unseen=set(range(21)); cycle_vertex_masks=[]
    while unseen:
        start=min(unseen); cyc=[]; x=start
        while x in unseen:
            unseen.remove(x);cyc.append(x);x=edge_map[x]
        assert x==start
        cover=0
        valid=True
        for i in cyc:
            u,v=EDGES[i];mask=(1<<u)|(1<<v)
            if mask&cover:
                valid=False;break
            cover|=mask
        if valid: cycle_vertex_masks.append(cover)
    def total(j,used):
        if j==len(cycle_vertex_masks):return 1
        result=total(j+1,used)
        mask=cycle_vertex_masks[j]
        if not (used&mask):result-=total(j+1,used|mask)
        return result
    return -total(0,0)

CHAR=[signed_trace(g) for g in GROUP]
assert all(a==orbit_trace(g) for a,g in zip(CHAR,GROUP))
COUNT=Counter(("preserve" if i<168 else "swap",order(g),CHAR[i]) for i,g in enumerate(GROUP))
EXPECTED={
 ('preserve',1,16):1,('preserve',2,0):21,('preserve',3,1):56,
 ('preserve',4,0):42,('preserve',7,2):48,
 ('swap',2,4):28,('swap',6,1):56,('swap',8,0):84,
}
assert dict(COUNT)==EXPECTED

# Eight Sylow-seven subgroups of the colour-preserving automorphism group.
def power(g,n):
    x=ID
    for _ in range(n):x=compose(g,x)
    return x
SYLOWS=list({frozenset(power(g,k) for k in range(7)) for g in PRES if order(g)==7})
assert len(SYLOWS)==8 and all(len(H)==7 for H in SYLOWS)
STEINBERG=[]
for g in GROUP:
    inv=tuple(g.index(i) for i in range(14))
    fixed=sum(frozenset(compose(g,compose(h,inv)) for h in H)==H for H in SYLOWS)
    STEINBERG.append(fixed-1)
EIGHT=[x-1-y for x,y in zip(CHAR,STEINBERG)]
TRIVIAL=[1]*336
inner=lambda X,Y: sum(a*b for a,b in zip(X,Y))//336 if sum(a*b for a,b in zip(X,Y))%336==0 else None
assert [[inner(X,Y) for Y in (TRIVIAL,STEINBERG,EIGHT)] for X in (TRIVIAL,STEINBERG,EIGHT)] == [[1,0,0],[0,1,0],[0,0,1]]
assert CHAR[0]==16 and STEINBERG[0]==7 and EIGHT[0]==8
EXPECTED_PARTS={
 ('preserve',1):(16,7,8),('preserve',2):(0,-1,0),
 ('preserve',3):(1,1,-1),('preserve',4):(0,-1,0),
 ('preserve',7):(2,0,1),('swap',2):(4,1,2),
 ('swap',6):(1,1,-1),('swap',8):(0,-1,0),
}
for i,g in enumerate(GROUP):
    key=('preserve' if i<168 else 'swap',order(g))
    assert (CHAR[i],STEINBERG[i],EIGHT[i])==EXPECTED_PARTS[key]
print('VERIFY_OK')
print('f_vector',tuple(map(len,FACES)))
print('GF2_boundary_ranks',tuple(RANKS))
print('full_character_types',sorted(COUNT.items()))
print('module_dimensions',1,7,8)
