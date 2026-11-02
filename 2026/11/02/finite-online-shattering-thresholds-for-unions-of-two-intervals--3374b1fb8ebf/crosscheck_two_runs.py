#!/usr/bin/env python3
"""Independent tuple-of-strings exhaustive recurrence for n<=8.
No bitset mask or certificate-generation dependencies.
"""
from functools import lru_cache
from itertools import product

def can_shatter_class(n):
    words = [''.join(bits) for bits in product('01', repeat=n)]
    C = frozenset(w for w in words if sum(w[i]=='1' and (i==0 or w[i-1]=='0') for i in range(n)) <= 2)
    @lru_cache(None)
    def dim(H):
        if len(H)<2:return 0
        best=0
        for i in range(n):
            A=frozenset(w for w in H if w[i]=='0')
            B=frozenset(w for w in H if w[i]=='1')
            if A and B:
                z=1+min(dim(A),dim(B))
                if z>best:best=z
        return best
    return len(C),dim(C)

if __name__=='__main__':
    expected=(1,2,3,4,4,5,5,6)
    for n, d in enumerate(expected, 1):
        count, ld=can_shatter_class(n)
        assert ld==d
        print('INDEPENDENT_SET_RECURSION',n,count,ld)
    print('ALTERNATIVE_REPRESENTATION_PASS')
