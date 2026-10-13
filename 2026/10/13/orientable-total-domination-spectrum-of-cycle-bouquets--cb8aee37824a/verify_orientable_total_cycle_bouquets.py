"""Finite, exhaustive cross-check of the cycle-bouquet orientation polynomial.
All checks use independently generated oriented edges and brute-force TD-sets.
"""
from collections import Counter
from itertools import product
from math import prod

def bouquet(lengths):
    edges=[]; nxt=1
    for length in lengths:
        vs=[0]+list(range(nxt,nxt+length-1))
        nxt += length-1
        edges.extend((vs[i],vs[(i+1)%length]) for i in range(length))
    return nxt,edges

def gamma_of_orientation(n,edges,bits):
    ins=[0]*n
    for (a,b),w in zip(edges,bits):
        if w:a,b=b,a
        ins[b] |= 1<<a
    if any(x==0 for x in ins):return None
    for size in range(1,n+1):
        for s in range(1,1<<n):
            if s.bit_count()!=size:continue
            if all(s & ins[v] for v in range(n)):
                return size
    assert False

def expected(lengths):
    b=sum(x-3 for x in lengths)
    out=Counter()
    for cyc in product((0,1),repeat=len(lengths)):
        if not any(cyc):continue
        count=prod(2 if flag else length-1 for flag,length in zip(cyc,lengths))
        out[b+2+sum(cyc)]+=count
    return out

if __name__=='__main__':
    for lengths in [(3,), (4,), (3,3), (3,4), (4,4), (3,5), (3,3,3), (3,4,5)]:
        n,edges=bouquet(lengths)
        found=Counter()
        for bits in product((0,1),repeat=len(edges)):
            gamma=gamma_of_orientation(n,edges,bits)
            if gamma is not None:found[gamma]+=1
        want=expected(lengths)
        assert found==want,(lengths,found,want)
        print('lengths=',lengths,'vertices=',n,'orientations=',2**len(edges),'valid=',sum(found.values()),'spectrum=',dict(sorted(found.items())))
    print('VERIFY_OK')
