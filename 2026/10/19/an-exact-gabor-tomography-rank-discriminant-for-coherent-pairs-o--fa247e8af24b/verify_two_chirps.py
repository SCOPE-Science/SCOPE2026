#!/usr/bin/env python3
"""Exact prime-cyclotomic ambiguity identity check for two quadratic chirps.
The identity is proved symbolically in the accompanying mathematical text.
This program verifies every displacement/modulation for selected prime orders.
No third-party dependencies; Python 3.9+.
"""
from collections import Counter

def vec(p, exponents):
    v=[0]*p
    for e in exponents: v[e%p]+=1
    return v

def equal_cyclo_prime(a,b):
    # At a primitive p-th root, a and b coincide iff a-b is a
    # multiple of 1+t+...+t^(p-1) (p prime; deg < p).
    return len(set(x-y for x,y in zip(a,b)))==1

def gauss_square_norm(p,d):
    e=vec(p,(d*x*x for x in range(p)))
    ce=vec(p,(-d*x*x for x in range(p)))
    v=vec(p, (i+j for i,xi in enumerate(e) for j,xj in enumerate(ce)
               for _ in range(xi*xj)))
    assert equal_cyclo_prime(v, [p]+[0]*(p-1))
    k=(-1 if p%4==3 else 1)
    # Complex conjugate of quadratic Gauss sum equals k times itself.
    assert equal_cyclo_prime(ce, [k*x for x in e])

def check(p,d):
    gauss_square_norm(p,d)
    inv4d=pow(4*d,-1,p)
    count=0
    for a in range(p):
        for b in range(p):
            # Four coefficients of 1, z, conjugate z, z*conjugate z
            # in the self-ambiguity polynomial.
            direct=[
                vec(p,(-b*x for x in range(p))),
                vec(p,(d*x*x-b*x for x in range(p))),
                vec(p,(-d*(x-a)**2-b*x for x in range(p))),
                vec(p,(d*(x*x-(x-a)**2)-b*x for x in range(p))),
            ]
            rhs=[
                ([p]+[0]*(p-1)) if b==0 else [0]*p,
                vec(p,(d*x*x-b*b*inv4d for x in range(p))),
                vec(p,(-d*x*x+b*b*inv4d-a*b for x in range(p))),
                vec(p,([-d*a*a]*p)) if b==(2*d*a)%p else [0]*p,
            ]
            for name,v,w in zip(('1','z','conj(z)','abs(z)^2'),direct,rhs):
                assert equal_cyclo_prime(v,w),(p,d,a,b,name,v,w)
                count+=1
    return count

if __name__=='__main__':
    total=0
    for p in (3,5,7,11,13,17,19):
        for d in (1,2):
            c=check(p,d)
            total+=c
            print(f'PASS p={p} d={d} coefficients={c}')
    print(f'PASS total exact cyclotomic coefficient identities={total}')
    print('Analytic all-prime rank and phase strata proved separately in RESULT.md.')
