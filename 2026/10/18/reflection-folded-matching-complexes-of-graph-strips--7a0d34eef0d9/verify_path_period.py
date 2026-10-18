#!/usr/bin/env python3
"""Independent finite mod-two homology checks of the path factor in the fold theorem."""
from collections import defaultdict


def rank_gf2(columns):
    piv={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p not in piv:
                piv[p]=x;break
            x^=piv[p]
    return len(piv)


def reduced_betti_path(m):
    by_dim=defaultdict(list)
    for x in range(1,1<<m):
        if x & (x<<1):continue
        by_dim[x.bit_count()-1].append(x)
    maxd=max(by_dim)
    ranks={0:0,maxd+1:0}
    for d in range(1,maxd+1):
        row={x:i for i,x in enumerate(by_dim[d-1])}
        cols=[]
        for face in by_dim[d]:
            bitset=0
            for j in range(m):
                if face>>j & 1:bitset^=1<<row[face^(1<<j)]
            cols.append(bitset)
        ranks[d]=rank_gf2(cols)
    bb={d:len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0) for d in range(maxd+1)}
    bb[0]-=1
    return {d:b for d,b in bb.items() if b}


def main():
    for n in range(2,15):
        m=n-1
        b=reduced_betti_path(m)
        if n%3==2:expected={}
        else:expected={n//3-1:1}
        assert b==expected,(n,b,expected)
        print('PASS n, path factor homology:',n,b)
    print('VERIFY_OK')

if __name__=='__main__':main()
