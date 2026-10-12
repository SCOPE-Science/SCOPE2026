#!/usr/bin/env python3
"""Independent explicit size and no-overlap check for a 9-ary length-6 code."""
from itertools import product
from collections import Counter

def build():
    A=tuple(range(2)); B=tuple(range(2,9))
    L={1:{(x,) for x in A}}
    R={1:{(x,) for x in B}}
    P2={x+y for x in L[1] for y in R[1]}
    # Reserve two pairs for R2, put the other twelve in L2.
    R[2]={(0,2),(0,3)}
    L[2]=P2-R[2]
    for k in (3,4,5):
        P={x+y for j in range(1,k) for x in L[j] for y in R[k-j]}
        L[k]=P
        R[k]=set()
    C={x+y for j in range(1,6) for x in L[j] for y in R[6-j]}
    return L,R,C

def run():
    L,R,C=build()
    ls=tuple(len(L[i]) for i in range(1,6)); rs=tuple(len(R[i]) for i in range(1,6))
    assert ls == (2,12,88,640,4656),ls
    assert rs == (7,2,0,0,0),rs
    assert len(C)==33872,len(C)
    # Fully independent of the partition theorem: construct each set of overlaps directly.
    prefixes={c[:i] for c in C for i in range(1,6)}
    suffixes={c[-i:] for c in C for i in range(1,6)}
    assert prefixes.isdisjoint(suffixes),min(prefixes & suffixes)
    # Restricted family: R2..R5 empty; then recursion forces Lk=A B^(k-1), so |C|=a(9-a)^5.
    restricted={a:a*(9-a)**5 for a in range(1,9)}
    assert max(restricted.values())==33614 and restricted[2]==33614
    assert len(C)-max(restricted.values())==258
    print(f'VERIFY_OK q=9 n=6 size={len(C)} L={ls} R={rs} prefix_suffix_disjoint=yes restricted_max={max(restricted.values())} gap=258')
if __name__=='__main__':run()
