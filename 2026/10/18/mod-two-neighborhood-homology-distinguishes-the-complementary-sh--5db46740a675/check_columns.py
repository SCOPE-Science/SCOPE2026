#!/usr/bin/env python3
"""Standalone exact F2 homology verification of the two complementary (16,9,4,6) SRGs."""
from itertools import combinations

def graph(which):
    vertices = [(a,b) for a in range(4) for b in range(4)]
    offsets = {(1,0), (3,0), (0,1), (0,3), (1,1), (3,3)}
    def adjacent(p,q):
        if which == 'Shrikhande':
            return ((p[0]-q[0])%4,(p[1]-q[1])%4) in offsets
        return (p[0]==q[0]) != (p[1]==q[1])
    N=[{j for j in range(16) if j!=i and adjacent(vertices[i],vertices[j])} for i in range(16)]
    assert all(len(s)==6 for s in N)
    assert all(len(N[i] & N[j])==2 for i in range(16) for j in range(i+1,16))
    return N

def faces(which):
    N=graph(which)
    comp=[sorted(set(range(16))-{v}-N[v]) for v in range(16)]
    assert all(len(x)==9 for x in comp)
    F=[set() for _ in range(9)]
    for facet in comp:
        for size in range(1,10):
            F[size-1].update(combinations(facet,size))
    return [sorted(x) for x in F]

def rank2_columns(F, degree):
    if degree==0:return 1  # augmented boundary to the empty simplex
    lower={f:i for i,f in enumerate(F[degree-1])}
    pivots={}
    for face in F[degree]:
        col=0
        for j in range(degree+1):
            col ^= 1 << lower[face[:j]+face[j+1:]]
        while col:
            lead=col.bit_length()-1
            if lead in pivots:col ^= pivots[lead]
            else:pivots[lead]=col;break
    return len(pivots)

expected={
    'Shrikhande': ([16,120,528,1292,1728,1296,576,144,16],[1,15,105,423,869,848,448,128,16],[0,0,0,0,11,0,0,0,0]),
    'Rook': ([16,120,560,1332,1728,1296,576,144,16],[1,15,105,453,879,848,448,128,16],[0,0,2,0,1,0,0,0,0]),
}
for name in ('Shrikhande','Rook'):
    F=faces(name)
    f=[len(s) for s in F]
    ranks=[rank2_columns(F,d) for d in range(9)]
    betti=[f[d]-ranks[d]-(ranks[d+1] if d<8 else 0) for d in range(9)]
    assert (f,ranks,betti)==expected[name]
    print(name,'faces',f,'ranks augmented',ranks,'reduced_F2_betti',betti)
print('PASS')
