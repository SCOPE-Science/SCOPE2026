#!/usr/bin/env python3
"""Exact cyclotomic zero-set validation for determinant-one convolutions."""
from itertools import product

def is_square_nonzero(v,p):
    return v%p in {(j*j)%p for j in range(1,p)}

def check(p,full=True):
    n=p*p
    group=[(a,b,c,d) for a,b,c,d in product(range(n),repeat=4) if (a*d-b*c)%n==1]
    assert len(group)==p**4*(p*p-1)
    import random
    rng=random.Random(11)
    freqs=list(product(range(n),repeat=4)) if full else [tuple(rng.randrange(n) for _ in range(4)) for _ in range(400)]
    for M in freqs:
        co=[0]*n
        a,b,c,d=M
        for x,y,z,w in group:
            co[(a*x+b*y+c*z+d*w)%n]+=1
        actual=all(len({co[r+i*p] for i in range(p)})==1 for r in range(p))
        aa,bb,cc,dd=[v%p for v in M]
        det=(aa*dd-bb*cc)%p
        expected=(not (aa or bb or cc or dd)) or is_square_nonzero(det,p)
        if actual != (not expected):
            raise AssertionError((p,M,actual,expected))
    print(f'SL2_PRIME_SQUARE_CYCLOTOMIC_OK p={p} matrices={len(group)} frequencies={len(freqs)}')
if __name__=='__main__':
    check(3, True)
    check(5, False)
