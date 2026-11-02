"""Separate ordered-block construction, uniqueness, and circular orbit test."""
from itertools import permutations,combinations,product
from math import factorial

def partitions_blocks(labels):
    if not labels:
        yield ()
    else:
        for a in labels:
            rest=tuple(x for x in labels if x!=a)
            for bs in partitions_blocks(rest):yield ((a,),)+bs
            for b in rest:
                left=tuple(x for x in rest if x!=b)
                for bs in partitions_blocks(left):yield ((a,b),)+bs

def matrix(q,blocks,bits):
    mat=[[0]*q for _ in range(q)]
    for j,B in enumerate(blocks):
        for x in B:
            for K in blocks[j+1:]:
                for y in K:mat[x][y]=1
        if len(B)==1:mat[B[0]][B[0]]=bits[j]
        else:
            x,y=B;mat[x][y]=mat[y][x]=bits[j]
            mat[x][x]=mat[y][y]=1-bits[j]
    return mat

for q in range(1,6):
    mats=set();codes=set()
    for B in partitions_blocks(tuple(range(q))):
        for bits in product((0,1),repeat=len(B)):
            m=matrix(q,B,bits)
            code=frozenset((a,b,c) for a in range(q) for b in range(q) for c in range(q) if m[a][b] and not m[b][c])
            # Direct forbidden-prefix test and cardinality, not inferred from a formula.
            assert len(code)==(q**3-q)//3
            assert {x[:2] for x in code}.isdisjoint({x[1:] for x in code})
            mats.add(tuple(sum(m,[]))); codes.add(tuple(sorted(code)))
    p0,p1=0,1
    for _ in range(q):p0,p1=p1,2*p1+p0
    # After q steps: p0=P_q and p1=P_(q+1)
    assert len(mats)==factorial(q)*p1
    assert len(codes)==factorial(q)*(p1-p0)
    print('q=%d structured_partitions=%d distinct_codes=%d' %(q,len(mats),len(codes)))
print('ORDERED_BLOCK_CHECK_OK')
