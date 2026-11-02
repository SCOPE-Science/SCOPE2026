#!/usr/bin/env python3
"""Exact ideal-product enumeration for two nonisomorphic eight-element rings.

This program uses only Python's standard library.  It checks all additive
subgroups for multiplicative stability, then multiplies the resulting ideals
using the ring multiplication tables; no structural classification is assumed.
"""
from fractions import Fraction
from itertools import product
from math import comb


def binary_ring():
    # F_2[x,y]/(x,y)^2; element a+bx+cy is the bit mask a+2b+4c.
    add = lambda u,v: u^v
    def mul(u,v):
        a,b,c = u&1,(u>>1)&1,(u>>2)&1
        d,e,f = v&1,(v>>1)&1,(v>>2)&1
        return (a*d%2)+2*((a*e+b*d)%2)+4*((a*f+c*d)%2)
    return add,mul


def mixed_ring():
    # Z_4[t]/(2t,t^2); element a+bt, a mod 4, b mod 2.
    def add(u,v): return ((u%4+v%4)%4)+4*((u//4+v//4)%2)
    def mul(u,v):
        a,b=u%4,u//4
        c,d=v%4,v//4
        return (a*c)%4+4*((a*d+c*b)%2)
    return add,mul


def list_ideals(add,mul):
    elems=list(range(8))
    ideals=[]
    for mask in range(1,1<<8):
        if not mask&1: continue # 0 must be in every ideal
        I=tuple(x for x in elems if mask&(1<<x))
        if any(not(mask&(1<<add(a,b))) for a in I for b in I): continue
        if any(not(mask&(1<<mul(r,a))) for r in elems for a in I): continue
        ideals.append(I)
    return ideals


def count_zero_products(ideals,mul,k):
    zero=0
    for idx in product(range(len(ideals)),repeat=k):
        # I_1 ... I_k=(0) iff every product a_1 ... a_k vanishes.
        values={1} # multiplication identity is coded as element 1
        for j in idx:
            values={mul(x,y) for x in values for y in ideals[j]}
        if values == {0}:
            zero+=1
    return zero


def gaussian(n,j,q):
    # Pascal-type recurrence for Gaussian binomial coefficients.
    arr=[[0]*(n+1) for _ in range(n+1)]
    for a in range(n+1):
        arr[a][0]=arr[a][a]=1
        for b in range(1,a):
            arr[a][b]=arr[a-1][b-1]+q**b*arr[a-1][b]
    return arr[n][j]


def closed_form(q,d,k):
    S=sum(gaussian(d,j,q) for j in range(d+1))
    return S, Fraction((S+1)**k-1-k*(S-1),(S+1)**k)


def main():
    for title,build in [
        ('split-characteristic-2',binary_ring),
        ('mixed-characteristic-4',mixed_ring)
    ]:
        add,mul=build()
        ideals=list_ideals(add,mul)
        assert len(ideals)==6, (title,ideals)
        assert sorted(map(len,ideals))==[1,2,2,2,4,8]
        assert all(mul(x,y)==mul(y,x) for x in range(8) for y in range(8))
        assert all(mul(mul(x,y),z)==mul(x,mul(y,z))
                   for x in range(8) for y in range(8) for z in range(8))
        print(title, 'ideals',len(ideals),'sizes',sorted(map(len,ideals)))
        for k in range(2,6):
            got=count_zero_products(ideals,mul,k)
            S,val=closed_form(2,2,k)
            expected=val*len(ideals)**k
            assert expected.denominator==1 and got==expected.numerator,(k,got,expected)
            print(' k',k,'zero tuples',got,'total',len(ideals)**k,'probability',str(val))
        assert count_zero_products(ideals,mul,2)==27
    for q,d in [(2,1),(2,2),(2,3),(3,2),(5,2)]:
        S,z2=closed_form(q,d,2)
        expected=1-Fraction(2*S-1,(S+1)**2)
        assert z2==expected
        print('parameters',q,d,'proper ideals',S,'zeta2',str(z2))
    for k in range(2,15):
        f=1-Fraction(1,2**k)
        for q,d in [(2,1),(2,2),(2,3),(3,2),(5,2)]:
            S,z=closed_form(q,d,k)
            relation=(z>f)-(z<f)
            want=(-1 if k in (2,3) else 1) if d==1 else (0 if (q,d,k)==(2,2,2) else 1)
            assert relation==want,(q,d,k,z,f)
    print('VERIFY_OK')

if __name__=='__main__': main()
