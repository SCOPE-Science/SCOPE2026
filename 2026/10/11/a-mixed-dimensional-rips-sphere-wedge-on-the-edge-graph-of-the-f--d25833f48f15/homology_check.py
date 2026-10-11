#!/usr/bin/env python3
"""Independent mod-2 ranks from complete simplicial boundary matrices."""
from verify import FACES
from collections import defaultdict
by_degree = defaultdict(list)
for mask in FACES:by_degree[mask.bit_count()-1].append(mask)
ranks={}
for q in range(1,8):
    low=by_degree[q-1]
    idx={face:j for j,face in enumerate(low)}
    piv={}
    for face in by_degree[q]:
        col=0
        x=face
        while x:
            bit=x&-x
            x-=bit
            col ^= 1 << idx[face^bit]
        while col:
            h=col.bit_length()-1
            if h in piv:col ^= piv[h]
            else:piv[h]=col;break
    ranks[q]=len(piv)
for q in range(8):
    b=len(by_degree[q])-ranks.get(q,0)-ranks.get(q+1,0)
    expected={0:1,3:1,5:8}.get(q,0)
    assert b == expected,(q,b,expected)
print('HOMOLOGY_OK', 'ranks',ranks)
