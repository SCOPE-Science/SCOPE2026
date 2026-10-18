#!/usr/bin/env python3
"""Exact rational certificate for the 14 interval components of the unitary divisor range at exponent -3.
Scientific input: the prime-tail interval theorem, proved in RESULT.md.
No floating point operations, networking, or third-party packages.
"""
from fractions import Fraction as Q
from math import isqrt

SMALL = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
SCALE = 10**30
N = 20000

def zeta_bounds(s):
    floor_sum = sum(SCALE // (k**s) for k in range(1,N+1))
    # For decreasing x^(-s), the remainder lies between the two integrals.
    return (Q(floor_sum, SCALE) + Q(1,(s-1)*(N+1)**(s-1)),
            Q(floor_sum+N, SCALE) + Q(1,(s-1)*N**(s-1)))

def prime_tail_bounds():
    z3lo,z3hi = zeta_bounds(3)
    z6lo,z6hi = zeta_bounds(6)
    P=Q(1)
    for p in SMALL: P *= 1+Q(1,p**3)
    return z3lo/z6hi/P,z3hi/z6lo/P

Tlo,Thi = prime_tail_bounds()
assert Q(1) < Tlo < Thi
# Every endpoint is exactly rational L or T*rational U.

def fuse(parts):
    parts.sort(key=lambda ab:ab[0])
    merged=[]
    included_margin = None
    excluded_margin = None
    for l,u in parts:
        assert l>0 and u>=l
        if merged:
            old_l,old_u=merged[-1]
            # Comparison is decided strictly by the certified zeta bounds.
            if Tlo*old_u >= l:
                slack=Tlo*old_u-l
                included_margin=slack if included_margin is None else min(included_margin,slack)
                if u>old_u:merged[-1]=(old_l,u)
                continue
            assert Thi*old_u < l, 'Insufficient zeta precision'
            slack=l-Thi*old_u
            excluded_margin=slack if excluded_margin is None else min(excluded_margin,slack)
        merged.append((l,u))
    return merged,included_margin,excluded_margin

def calculate(primes):
    components=[(Q(1),Q(1))]
    traces=[]
    for p in primes:
        A=1
        while 1+Q(1,p**(3*A))>Tlo: A+=1
        assert 1+Q(1,p**(3*(A-1)))>Thi if A>1 else True
        nxt=[]
        for l,u in components:
            assert u>=l
            # Powers a>=A, together with omission, form one full interval.
            nxt.append((l,u*(1+Q(1,p**(3*A)))))
            for a in range(1,A):
                c=1+Q(1,p**(3*a))
                nxt.append((l*c,u*c))
        components,im,em=fuse(nxt)
        traces.append((p,A,len(nxt),len(components)))
    return components,traces

components,trace=calculate(reversed(SMALL))
reverse_components,trace2=calculate(SMALL)
assert components==reverse_components, 'Order of exact Euler factors changed result'
assert len(components)==14
assert components[0][0]==1
assert all(Thi*u < components[i+1][0] for i,(l,u) in enumerate(components[:-1]))
# Global upper bound is exactly zeta(3)/zeta(6).
P=Q(1)
for p in SMALL:P*=1+Q(1,p**3)
assert components[-1][1]==P
assert all(u>=l for l,u in components)

print('TAIL_BOUNDS',format(float(Tlo),'.15f'),format(float(Thi),'.15f'))
print('TRACE_DESCENDING',trace)
print('TRACE_ASCENDING',trace2)
print('COMPONENTS',len(components))
for i,(l,u) in enumerate(components,1):
    print('%02d %s %s %.12f %.12f'%(i,l,u,float(l),float(u*(Tlo+Thi)/2)))
print('VERIFY_OK')
