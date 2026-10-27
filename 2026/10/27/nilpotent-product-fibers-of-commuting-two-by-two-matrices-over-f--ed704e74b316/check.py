#!/usr/bin/env python3
"""Exhaustive matrix-product fiber check for small prime and nonprime finite fields."""
from collections import Counter
from fractions import Fraction
from itertools import product


def operations(q):
    if q == 4:
        def add(a, b): return a ^ b
        def mul(a, b):
            r = 0
            while b:
                if b & 1:
                    r ^= a
                b >>= 1
                a <<= 1
                if a & 4:
                    a ^= 7  # X^2 = X+1, so F4 = F2[X]/(X^2+X+1).
            return r
        def neg(a): return a
    else:
        def add(a, b): return (a + b) % q
        def mul(a, b): return a * b % q
        def neg(a): return -a % q
    return add, mul, neg


def check(q):
    add, mul, neg = operations(q)
    def mm(A, B):
        a,b,c,d=A; e,f,g,h=B
        return (add(mul(a,e),mul(b,g)), add(mul(a,f),mul(b,h)),
                add(mul(c,e),mul(d,g)), add(mul(c,f),mul(d,h)))
    def isnil(C):
        a,b,c,d=C
        return add(a,d)==0 and add(mul(a,d),neg(mul(b,c)))==0
    Z=(0,0,0,0)
    M=list(product(range(q),repeat=4))
    fib=Counter(); commuting=0
    for A in M:
        for B in M:
            C=mm(A,B)
            if C==mm(B,A):
                commuting+=1
                if isnil(C):fib[C]+=1
    assert commuting==q**6+q**5-q**3,(q,commuting)
    assert fib[Z]==q*q*(3*q*q-2),(q,fib[Z])
    nonzero=[C for C in M if C!=Z and isnil(C)]
    assert len(nonzero)==q*q-1,(q,len(nonzero))
    assert all(fib[C]==2*q*(q-1) for C in nonzero),(q,fib)
    total=sum(fib.values())
    assert total==5*q**4-2*q**3-4*q*q+2*q,(q,total)
    print(f'q={q}: commuting={commuting} nilproduct={total} zerofiber={fib[Z]} nonzero_nils={len(nonzero)} conditional={Fraction(total,commuting)}')

for q in (2,3,4,5):check(q)
print('VERIFY_OK')
