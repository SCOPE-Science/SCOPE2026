#!/usr/bin/env python3
"""Independent finite-field test of the binary quadratic constraint on dual triads.
For each odd prime, enumerate all invertible symmetric 2x2 matrices T over F_p,
count projective roots of u^T T u, and independently verify determinant/discriminant.
This is a finite check, not a proof for arbitrary prime powers.
"""
from itertools import product
from collections import Counter

def run(p):
    roots=Counter(); examples={}
    for a,b,c in product(range(p), repeat=3):
        det=(a*c-b*b)%p
        if not det: continue
        count=sum((a+2*b*t+c*t*t)%p==0 for t in range(p))
        count+=(c%p==0)  # infinity point [u0:u1]=[0:1]
        # disc of polynomial in affine t is 4(b^2-ac) nonzero.
        delta=(b*b-a*c)%p
        square=pow(delta,(p-1)//2,p)==1
        expected=2 if square else 0
        assert count==expected, (p,a,b,c,count,expected)
        roots[count]+=1
        examples.setdefault(count,(a,b,c))
    assert set(roots)=={0,2}
    print('FIELD',p,'invertible_symmetric',sum(roots.values()),'zero_roots',roots[0],
          'two_roots',roots[2],'sample_zero',examples[0],'sample_two',examples[2])

if __name__=='__main__':
    for p in (3,5,7,11,13):run(p)
    print('ALL_QUADRATICS_OK')
