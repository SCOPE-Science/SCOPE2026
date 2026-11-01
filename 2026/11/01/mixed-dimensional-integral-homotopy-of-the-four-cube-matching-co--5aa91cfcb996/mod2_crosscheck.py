#!/usr/bin/env python3
"""Independent exact mod-2 simplicial boundary-rank check on the tesseract matching complex."""

V = range(16)
E = [(i,j) for i in V for j in range(i+1,16) if (i^j).bit_count()==1]
assert len(E)==32
masks = [(1<<i)|(1<<j) for i,j in E]
res=[]
def visit(edge,used,selected):
    if edge==32:
        res.append(selected)
        return
    visit(edge+1,used,selected)
    if not used & masks[edge]:visit(edge+1,used|masks[edge],selected|(1<<edge))
visit(0,0,0)
levels=[[f for f in res if f.bit_count()==k] for k in range(9)]
assert [len(x) for x in levels]==[1,32,400,2496,8256,14208,11648,3712,272]
print('faces:', [len(x) for x in levels]); del res
ranks={}
for k in range(1,9):
    rows={f:i for i,f in enumerate(levels[k-1])}
    pivots={}
    for top in levels[k]:
        boundary=0
        bits=top
        while bits:
            bit=bits & -bits;bits ^= bit
            boundary ^= (1<<rows[top^bit])
        while boundary:
            pivot=boundary.bit_length()-1
            if pivot in pivots: boundary ^= pivots[pivot]
            else:
                pivots[pivot]=boundary
                break
    ranks[k]=len(pivots)
    print('rank boundary',k,'=',ranks[k])
assert all(len(levels[k])-(ranks.get(k,0)+ranks.get(k+1,0))==0 for k in (1,2,3,4,7,8))
assert len(levels[5])-ranks[5]-ranks[6]==1
assert len(levels[6])-ranks[6]-ranks[7]==130
print('reduced mod-2 Betti: b4=1 b5=130; other b=0')
print('MOD2_CHECK_PASS')
