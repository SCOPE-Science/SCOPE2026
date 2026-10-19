#!/usr/bin/env python3
"""Finite reproducibility tests for simultaneous additive/multiplicative complete mappings.

Run: python3 verification.py
Requires only Python's standard library.
"""
from itertools import permutations, product


def finite_field(p, d=1, irreducible=None):
    if d == 1:
        return (p, lambda x, y: (x+y) % p, lambda x, y: (x*y) % p)
    if p != 2 or irreducible is None:
        raise ValueError('extension test supports binary fields only')
    q = 1 << d
    def add(x,y): return x ^ y
    def mul(x,y):
        acc = 0
        a = x
        b = y
        while b:
            if b & 1: acc ^= a
            b >>= 1
            a <<= 1
            if a & q: a ^= irreducible
        return acc
    for a in range(1,q):
        assert len({mul(a,b) for b in range(q)}) == q
    return q,add,mul


def ring_mod(n):
    return n, lambda x,y: (x+y)%n, lambda x,y: (x*y)%n


def dual2():
    def mul(a,b):
        return ((a&1)*(b&1)) | (((((a&1)*((b>>1)&1))+(((a>>1)&1)*(b&1)))%2)<<1)
    return (4, lambda x,y: x^y, mul)


def ring_product(A,B):
    na,aa,ma = A;nb,ab,mb=B
    def add(x,y):
        a,i=divmod(x,nb);b,j=divmod(y,nb)
        return aa(a,b)*nb+ab(i,j)
    def mul(x,y):
        a,i=divmod(x,nb);b,j=divmod(y,nb)
        return ma(a,b)*nb+mb(i,j)
    return na*nb,add,mul


def valid(alpha,R):
    n,add,mul=R
    return (len({add(x,alpha[x]) for x in range(n)})==n and
            len({mul(x,alpha[x]) for x in range(n)})==n)


def brute(R):
    n,_,_=R
    if n > 9:raise ValueError('only enumerate at most nine elements')
    return sum(valid(a,R) for a in permutations(range(n)))


def main():
    F2=finite_field(2)
    F3=finite_field(3)
    F4=finite_field(2,2,0b111)
    F8=finite_field(2,3,0b1011)
    F5=finite_field(5)
    bad = [
        ('F2',F2),('F3',F3),('F5',F5),
        ('Z4',ring_mod(4)),('Z6',ring_mod(6)),('Z8',ring_mod(8)),
        ('Z9',ring_mod(9)),('F2[epsilon]/(epsilon^2)',dual2()),
        ('F2 x F2',ring_product(F2,F2)),
        ('F2 x F3',ring_product(F2,F3)),
        ('F2 x F4',ring_product(F2,F4)),
        ('F3 x F3',ring_product(F3,F3)),
    ]
    for name,R in bad:
        count=brute(R)
        print(name, 'simultaneous_permutations', count)
        assert count==0,(name,count)
    for name,R in [('F4',F4),('F8',F8)]:
        count=brute(R)
        print(name, 'simultaneous_permutations',count)
        assert count>0
    for q,poly in [(4,0b111),(8,0b1011),(16,0b10011)]:
        R=finite_field(2,q.bit_length()-1,poly)
        for a in range(2,q):
            alpha=tuple(R[2](a,x) for x in range(q))
            assert len(set(alpha))==q and valid(alpha,R)
    # Two separate one-operation complete maps need not share a witness.
    Rmix=ring_product(F2,F4)
    add_only=tuple(F8[2](2,x) for x in range(8))
    mul_only=tuple((x//4)*4 + F4[2](2,x%4) for x in range(8))
    assert all(Rmix[1](x,y)==(x^y) for x in range(8) for y in range(8))
    assert len(set(add_only))==8 and len({Rmix[1](x,add_only[x]) for x in range(8)})==8
    assert len(set(mul_only))==8 and len({Rmix[2](x,mul_only[x]) for x in range(8)})==8
    assert not valid(add_only,Rmix) and not valid(mul_only,Rmix)
    # Direct-product witnesses, including mixed extension degrees.
    for A,B in [(F4,F4),(F4,F8),(F8,F8)]:
        R=ring_product(A,B)
        nb=B[0]
        alpha=tuple(A[2](2,x//nb)*nb+B[2](2,x%nb) for x in range(R[0]))
        assert len(set(alpha))==R[0] and valid(alpha,R)
    # All scalar witnesses and both permutations over their entire domains.
    # Even without exhaustive enumeration of all permutations, the field-16
    # check verifies the theorem's constructive infinite-family mechanism.
    print('VERIFY_OK: exhaustive 14 rings/fields of order <=9; F4/F8/F16 scalar witnesses; F4xF4, F4xF8, F8xF8 products; independent one-operation witnesses in F2xF4')

if __name__=='__main__':main()
