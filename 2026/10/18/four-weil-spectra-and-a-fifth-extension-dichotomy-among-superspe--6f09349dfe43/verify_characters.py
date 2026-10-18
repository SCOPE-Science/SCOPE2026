#!/usr/bin/env python3
"""Exact tame-character and cyclotomic-product checks for a trigonal genus-five curve.

No computer algebra packages or finite-field databases are used.
"""
from math import comb, gcd

PHI15 = [1, -1, 0, 1, -1, 1, 0, -1, 1]

def reduce_phi(v):
    v = list(v)
    if len(v) < 9:
        v += [0] * (9-len(v))
    for k in range(len(v)-1, 7, -1):
        c = v[k]
        if c:
            for i in range(9):
                v[k-8+i] -= c*PHI15[i]
    return tuple(v[:8])

def add(a, b):
    return tuple(x+y for x,y in zip(a,b))

def mul(a,b):
    v = [0]*15
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            v[i+j] += x*y
    return reduce_phi(v)

ZERO=(0,)*8
ONE=(1,)+(0,)*7

def poly_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def poly_pow(a,n):
    z=[1]
    for _ in range(n): z=poly_mul(z,a)
    return z

def expected(r):
    g=gcd(r,15)
    if g==15:
        return poly_pow([1,1],10)
    if g==1:
        return [1,0,0,0,0,-1,0,0,0,0,1]
    if g==3:
        return [1,0,0,0,0,2,0,0,0,0,1]
    if g==5:
        return poly_pow([1,-1,1],5)
    raise AssertionError(r)

def main():
    basis = [(i,j) for j in (1,2) for i in range(5)
             if 3*i+2-2*j >= 0 and -3*i-4+7*j >= 0 and 2-j >= 0]
    assert basis == [(0,1),(1,1),(1,2),(2,2),(3,2)],basis
    e={((3*(i+1)-2*j)%15) for i,j in basis}
    assert e=={1,2,4,5,8},e
    chars=e|{(-x)%15 for x in e}
    assert chars=={1,2,4,5,7,8,10,11,13,14}
    powers=[reduce_phi([1])]
    t=reduce_phi([0,1])
    for i in range(14): powers.append(mul(powers[-1],t))
    assert mul(powers[1],powers[14])==ONE
    counts={1:0,3:0,5:0,15:0}
    for r in range(15):
        coef=[ONE]
        for k in sorted(chars):
            z=powers[(r*k)%15]
            new=[ZERO for _ in range(len(coef)+1)]
            for i,cell in enumerate(coef):
                new[i]=add(new[i],cell)
                new[i+1]=add(new[i+1],mul(cell,z))
            coef=new
        observed=[v[0] for v in coef]
        assert all(not any(v[1:]) for v in coef),(r,coef)
        assert observed==expected(r),(r,observed,expected(r))
        counts[gcd(r,15)]+=1
    assert counts=={1:8,3:4,5:2,15:1},counts
    print('HOLOMORPHIC_BASIS',basis)
    print('H1_CHARACTERS',sorted(chars))
    print('POLYNOMIALS_ALL_15_OK',counts)
    for g in [15,1,3,5]: print('gcd',g,'L_COEFFICIENTS_ASCENDING',expected(g))
    print('VERIFY_CHARACTERS_OK')

if __name__=='__main__': main()
