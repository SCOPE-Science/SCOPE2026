#!/usr/bin/env python3
"""Independent mod-two boundary-rank cross-check for GP(8,3) carriers.

This does not use the discrete Morse reduction and cannot prove integer
primitivity. It reconstructs ordinary simplicial boundary maps directly.
"""
from itertools import combinations

def egraph():
    return sorted({tuple(sorted(p)) for i in range(8)
        for p in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8))})

def rank_add(x,pivots):
    while x:
        high=x.bit_length()-1
        if high in pivots:x^=pivots[high]
        else:pivots[high]=x;return True
    return False

def rank_columns(cols):
    b={}
    for x in cols:rank_add(x,b)
    return len(b)

def main():
    E=egraph();assert len(E)==24
    vertexmasks=[(1<<a)|(1<<b) for a,b in E]
    available=[]
    for x in range(24):
        available.append(sum(1<<j for j in range(24) if vertexmasks[j]&vertexmasks[x]))
    cells={0}
    for j in range(24):
        cells|={s|(1<<j) for s in cells if not(s&available[j])}
    levels={d:sorted(s for s in cells if s.bit_count()==d+1) for d in range(8)}
    assert [len(levels[d]) for d in range(8)]==[24,228,1096,2826,3816,2444,600,33]

    def matrixcols(d):
        idx={s:j for j,s in enumerate(levels[d-1])}
        for s in levels[d]:
            out=0
            for j in range(24):
                if s>>j&1:out^=1<<idx[s^(1<<j)]
            yield out
    r4=rank_columns(matrixcols(4))
    rowindex={s:j for j,s in enumerate(levels[4])}
    b5={}
    for col in matrixcols(5):rank_add(col,b5)
    assert r4==1935 and len(b5)==1873 and len(levels[4])-r4-len(b5)==8

    paths=[(i,j,vertexmasks[i]|vertexmasks[j]) for i,j in combinations(range(24),2)
           if (vertexmasks[i]&vertexmasks[j]).bit_count()==1]
    assert len(paths)==48
    carrier_vectors=[]
    def walk(pos,used,pairs):
        if len(pairs)==5:
            vec=0
            for bits in range(32):
                m=sum(1<<p[(bits>>i)&1] for i,p in enumerate(pairs))
                vec^=1<<rowindex[m]
            carrier_vectors.append(vec)
            return
        for j in range(pos,len(paths)):
            a,b,used_path=paths[j]
            if not used_path&used:walk(j+1,used|used_path,pairs+[(a,b)])
    walk(0,0,[])
    assert len(carrier_vectors)==912
    # Test each carrier independently modulo the original degree-five boundaries.
    assert all(rank_add(v,dict(b5)) for v in carrier_vectors)
    # Test the span, now allowing carrier columns to enlarge the original image.
    combined=dict(b5)
    for v in carrier_vectors:rank_add(v,combined)
    assert len(combined)==1881
    print('VERIFY_OK_DIRECT_MOD2 M4_DIM_3816 BOUNDARY4_RANK_1935 BOUNDARY5_RANK_1873')
    print('BETTI4_8 EVERY_ONE_OF_912_CARRIERS_NONBOUNDARY OVERALL_CARRIER_SPAN_8')

if __name__=='__main__':main()
