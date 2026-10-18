#!/usr/bin/env python3
"""Independent cochain-row F2 rank verification by subset-mask enumeration."""
from itertools import combinations

def graph_neighbors(kind):
    G = [0]*16
    for i in range(16):
        ai,bi=divmod(i,4)
        for j in range(16):
            if i==j:continue
            aj,bj=divmod(j,4)
            dx,dy=(ai-aj)%4,(bi-bj)%4
            if kind=='Shrikhande':
                # Isomorphic Cayley presentation via (x,y) -> (x+y,2x+3y) modulo four.
                # This invertible matrix has determinant one modulo four.
                # The six original differences become precisely these six.
                yes = dx!=0 and dy!=0 and dx!=dy
            else:
                yes = (ai==aj or bi==bj)
            if yes:G[i] |= 1<<j
    assert all(x.bit_count()==6 for x in G)
    assert all((G[i]&G[j]).bit_count()==2 for i in range(16) for j in range(i+1,16))
    if kind=='Shrikhande':
        # Every neighborhood of this alternative presentation induces a six-cycle.
        for u in range(16):
            W=[v for v in range(16) if (G[u]>>v)&1]
            assert all(sum((G[v]>>w)&1 for w in W)==2 for v in W)
    return G

def all_faces(kind):
    N=graph_neighbors(kind)
    facets=[((1<<16)-1) & ~(N[v] | (1<<v)) for v in range(16)]
    assert len(set(facets))==16 and all(x.bit_count()==9 for x in facets)
    by_dimension=[[] for d in range(9)]
    for mask in range(1,1<<16):
        if any((mask & facet)==mask for facet in facets):
            by_dimension[mask.bit_count()-1].append(mask)
    return by_dimension

def coboundary_rank(F,d):
    # Rank of the transpose of C_d -> C_{d-1}, over F2.
    if d==0:return 1
    lower=F[d-1]; upper=F[d]
    # Assemble transposed boundary rows directly from codimension-one inclusions.
    rows=[0]*len(lower)
    lower_id={m:i for i,m in enumerate(lower)}
    for upper_idx,face in enumerate(upper):
        b=face
        while b:
            atom=b&-b
            rows[lower_id[face^atom]]^=1<<upper_idx
            b-=atom
    pivots={}
    for row in rows:
        while row:
            lead=(row&-row).bit_length()-1
            if lead in pivots:row ^= pivots[lead]
            else:pivots[lead]=row;break
    return len(pivots)

checks={
    'Shrikhande':((16,120,528,1292,1728,1296,576,144,16),(1,15,105,423,869,848,448,128,16)),
    'Rook':((16,120,560,1332,1728,1296,576,144,16),(1,15,105,453,879,848,448,128,16)),
}
for kind in checks:
    F=all_faces(kind)
    f=tuple(map(len,F))
    ranks=tuple(coboundary_rank(F,d) for d in range(9))
    betti=tuple(f[d]-ranks[d]-(ranks[d+1] if d<8 else 0) for d in range(9))
    assert (f,ranks)==checks[kind]
    print(kind,'f',f,'ranks',ranks,'reduced_F2_betti',betti)
print('PASS')
