#!/usr/bin/env python3
"""Standalone exact integer verifier for the octahedral matching-complex theorem.
Only Python's standard library is used. The complex is the ordinary matching complex.
"""
from collections import Counter, deque
from itertools import combinations, permutations

VERTICES = range(6)
EDGES = tuple((a,b) for a,b in combinations(VERTICES,2) if a//2 != b//2)
EDGE_ID = {e:i for i,e in enumerate(EDGES)}
SIMPLICES = {
    k: tuple(s for s in combinations(range(12), k)
             if len({v for ei in s for v in EDGES[ei]}) == 2*k)
    for k in (1,2,3)
}
F0, F1, F2 = (SIMPLICES[k] for k in (1,2,3))
assert tuple(map(len,(F0,F1,F2))) == (12,30,8)
INDEX1 = {e:i for i,e in enumerate(F1)}

# Free edges of the 2-dimensional matching complex (each is in a unique face).
incidence = Counter(x for f in F2 for x in combinations(f,2))
assert len(incidence) == 24
assert set(incidence.values()) == {1}
REMOVED = {tuple(face[:2]): tuple(face) for face in F2}
assert len(REMOVED) == 8
SURVIVING = tuple(e for e in F1 if e not in REMOVED)
assert len(SURVIVING) == 22

# The surviving 1-skeleton is a connected graph on twelve vertices.
adjacency = {i: [] for i in range(12)}
for a,b in SURVIVING:
    adjacency[a].append(b)
    adjacency[b].append(a)
parent = {0: None}
queue = deque([0])
while queue:
    a = queue.popleft()
    for b in sorted(adjacency[a]):
        if b not in parent:
            parent[b] = a
            queue.append(b)
assert len(parent) == 12
TREE = frozenset(tuple(sorted((a,b))) for a,b in parent.items() if b is not None)
CHORDS = tuple(e for e in SURVIVING if e not in TREE)
assert len(TREE) == 11 and len(CHORDS) == 11
CHORD_INDEX = {e:i for i,e in enumerate(CHORDS)}


def tree_path(start, target):
    # Return signed oriented edges for the unique tree path.
    pred = {start: None}
    q = deque([start])
    while q and target not in pred:
        x = q.popleft()
        for y in sorted(adjacency[x]):
            e = tuple(sorted((x,y)))
            if e in TREE and y not in pred:
                pred[y] = x
                q.append(y)
    assert target in pred
    v=target; reverse=[]
    while pred[v] is not None:
        u=pred[v]
        reverse.append((tuple(sorted((u,v))),1 if u<v else -1))
        v=u
    return [(edge,sign) for edge,sign in reversed(reverse)]

# Oriented fundamental cycles, positive on their unique chords.
CYCLES=[]
for u,v in CHORDS:
    c=Counter({(u,v):1})
    for edge,sign in tree_path(v,u): c[edge]+=sign
    CYCLES.append({e:z for e,z in c.items() if z})

def boundary1(chain):
    b=Counter()
    for (u,v),coef in chain.items():
        b[v]+=coef; b[u]-=coef
    return {x:z for x,z in b.items() if z}
assert all(not boundary1(c) for c in CYCLES)


def reduce_removed(chain):
    """Integral quotient by the 8 triangle boundaries, as free collapses."""
    out=Counter()
    for (u,v),coef in chain.items():
        if (u,v) in REMOVED:
            a,b,c=REMOVED[(u,v)]
            assert (u,v)==(a,b)
            out[(a,c)]+=coef
            out[(b,c)]-=coef
        else:
            out[(u,v)]+=coef
    reduced={e:z for e,z in out.items() if z}
    assert set(reduced).issubset(SURVIVING)
    return reduced


def signature(positions):
    return -1 if sum(x>y for i,x in enumerate(positions) for y in positions[i+1:])%2 else 1

# All octahedral symmetries: permutations of antipodal coordinate pairs,
# together with independent swaps within pairs. The 4 antipodal face pairs
# identify the rotation subgroup with S4.
BODY_DIAGONALS=((1,1,1),(1,1,-1),(1,-1,1),(1,-1,-1))

def image_body_diagonal(p,mask,diag):
    out=[0,0,0]
    for i in range(3):
        out[p[i]]=diag[i]*(-1 if mask & (1<<i) else 1)
    if out[0]<0:out=[-t for t in out]
    return BODY_DIAGONALS.index(tuple(out))

def cycle_shape(p):
    unseen=set(range(len(p)))
    sizes=[]
    while unseen:
        i=min(unseen); j=i; length=0
        while j in unseen:
            unseen.remove(j);length+=1;j=p[j]
        sizes.append(length)
    return tuple(sorted(sizes,reverse=True))

CHAR_S4={
 '(4)': {(1,1,1,1):1,(2,1,1):1,(2,2):1,(3,1):1,(4,):1},
 '(1111)': {(1,1,1,1):1,(2,1,1):-1,(2,2):1,(3,1):1,(4,):-1},
 '(31)': {(1,1,1,1):3,(2,1,1):1,(2,2):-1,(3,1):0,(4,):-1},
 '(211)': {(1,1,1,1):3,(2,1,1):-1,(2,2):-1,(3,1):0,(4,):1},
 '(22)': {(1,1,1,1):2,(2,1,1):0,(2,2):2,(3,1):-1,(4,):0},
}
GROUP={}
CHARACTER={}
for p in permutations(range(3)):
    for mask in range(8):
        g=tuple(2*p[i//2] + ((i%2) ^ ((mask>>(i//2)) & 1)) for i in range(6))
        assert len(set(g))==6
        emap=tuple(EDGE_ID[tuple(sorted((g[a],g[b])))] for a,b in EDGES)
        c0=sum(emap[i]==i for i in range(12))
        c1=c2=0
        for simplex in F1:
            mapped=tuple(emap[i] for i in simplex)
            if set(mapped)==set(simplex):c1+=signature(mapped)
        for simplex in F2:
            mapped=tuple(emap[i] for i in simplex)
            if set(mapped)==set(simplex):c2+=signature(mapped)
        chi=1-c0+c1-c2
        det=signature(p)*((-1)**mask.bit_count())
        body_map=tuple(image_body_diagonal(p,mask,d) for d in BODY_DIAGONALS)
        shape=cycle_shape(body_map)
        GROUP[g]=(emap,shape,det,(c0,c1,c2))
        CHARACTER[g]=chi
assert len(GROUP)==48


def act_one(simplex,g,emap):
    u,v=simplex
    a,b=emap[u],emap[v]
    return (tuple(sorted((a,b))), 1 if a<b else -1)

# Check the group action directly on H_1 using fundamental cycles of the
# 22-edge collapsed graph, independent of the Lefschetz trace formula.
MATRICES={}
for g,(emap,shape,det,chain_traces) in GROUP.items():
    matrix=[[0]*11 for _ in range(11)]
    for j,cycle in enumerate(CYCLES):
        mapped=Counter()
        for edge,coef in cycle.items():
            e,sign=act_one(edge,g,emap)
            mapped[e]+=coef*sign
        assert not boundary1({e:z for e,z in mapped.items() if z})
        collapsed=reduce_removed(mapped)
        assert not boundary1(collapsed)
        for i,chord in enumerate(CHORDS): matrix[i][j]=collapsed.get(chord,0)
    assert sum(matrix[i][i] for i in range(11)) == CHARACTER[g]
    MATRICES[g]=matrix

# Verify all 48*48 representation multiplication laws over integers.
def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(11)) for j in range(11)] for i in range(11)]
for g in GROUP:
    for h in GROUP:
        gh=tuple(g[h[i]] for i in range(6))
        assert matmul(MATRICES[g],MATRICES[h]) == MATRICES[gh]

# Full ten-class character and 10 rational irreducible multiplicities.
classes=Counter((shape,det,CHARACTER[g]) for g,(_,shape,det,_) in GROUP.items())
assert len(classes)==10
EXPECTED={
 ((1,1,1,1),1):(1,11),((1,1,1,1),-1):(1,-5),
 ((2,1,1),1):(6,-1),((2,1,1),-1):(6,-1),
 ((2,2),1):(3,-1),((2,2),-1):(3,-1),
 ((3,1),1):(8,-1),((3,1),-1):(8,1),
 ((4,),1):(6,1),((4,),-1):(6,1)
}
assert {(shape,det):(count,chi) for (shape,det,chi),count in classes.items()} == EXPECTED
MULTIPLICITIES={}
for lam,table in CHAR_S4.items():
    for parity in (0,1):
        inner=sum(CHARACTER[g]*table[shape]*(det**parity)
                  for g,(_,shape,det,_) in GROUP.items())
        assert inner % 48 == 0
        MULTIPLICITIES[(lam,parity)] = inner//48
assert {k:v for k,v in MULTIPLICITIES.items() if v} == {
 ('(31)',1):1,('(211)',0):1,('(211)',1):1,('(22)',1):1
}
assert sum(v*CHAR_S4[lam][(1,1,1,1)] for (lam,p),v in MULTIPLICITIES.items()) ==11
assert sum(CHARACTER[g] for g in GROUP) ==0
central=tuple(i^1 for i in range(6))
assert CHARACTER[central]==-5
assert (11+CHARACTER[central])//2==3
assert (11-CHARACTER[central])//2==8

if __name__=='__main__':
    print('f_vector=12,30,8; free_edges=8; residual_edges=22; tree=11; H1_rank=11')
    for (shape,det),(count,chi) in sorted(EXPECTED.items()):
        print('S4_cycle_type=',shape,'det=',det,'class_size=',count,'H1_trace=',chi)
    print('irreducible_multiplicities=',MULTIPLICITIES)
    print('48 integer homology actions and 2304 multiplication identities verified')
    print('VERIFY_OK')
