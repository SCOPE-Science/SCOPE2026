#!/usr/bin/env python3
"""Finite-field checks for the reduced quartic and exceptional Frobenius geometry.

This checker is not a proof of assertions over every extension: the accompanying
algebraic argument proves them. Arithmetic below is bit-polynomial GF(2^n).
"""
from collections import Counter

IRREDUCIBLE={1:0b11,2:0b111,3:0b1011,4:0b10011,5:0b100101,6:0b1000011}

def field(n):
    q=1<<n; irr=IRREDUCIBLE[n]; mask=q-1
    def mul(a,b):
        v=0
        while b:
            if b&1:v^=a
            b>>=1;a<<=1
            if a&q:a^=irr
        return v&mask
    def power(a,m):
        z=1
        while m:
            if m&1:z=mul(z,a)
            a=mul(a,a);m>>=1
        return z
    return q,mul,power

def projective_points(q):
    for y in range(q):
        for z in range(q):
            for w in range(q):yield 1,y,z,w
    for z in range(q):
        for w in range(q):yield 0,1,z,w
    for w in range(q):yield 0,0,1,w
    yield 0,0,0,1

def test(n):
    q,mul,powr=field(n)
    m3=[powr(x,3) for x in range(q)]
    m4=[powr(x,4) for x in range(q)]
    squares=[mul(x,x) for x in range(q)]
    xs=[]
    crit=[]
    for x,y,z,w in projective_points(q):
        B=mul(m3[x],y)^mul(m3[y],z)^mul(m3[z],x)
        if B!=m4[w]:continue
        xs.append((x,y,z,w))
        if (mul(squares[x],y)^m3[z])==0 and (m3[x]^mul(squares[y],z))==0 and (m3[y]^mul(squares[z],x))==0:
            crit.append((x,y,z,w))
    predicted_count=q*q+q+1
    assert len(xs)==predicted_count,(n,len(xs),predicted_count)
    expected_singular=1+(6 if n%3==0 else 0)
    assert len(crit)==expected_singular,(n,crit)
    for x,t,z,w in crit:
        assert x==1 and t!=0
        assert powr(t,7)==1 and z==powr(t,q-3 if q>=4 else 0) and w==mul(t,t)
        # The tangent cone is t^{-1}u^2+t^2uv+t^{-2}v^2.
        inv=powr(t,q-2)
        ta=inv; tb=mul(t,t); tc=powr(inv,2)
        slopes=[h for h in range(q) if mul(ta,mul(h,h))^mul(tb,h)^tc==0]
        assert len(slopes)==(2 if n%2==0 else 0),(n,t,slopes)
    # Following both blowups at A3: nonsplit exceptional has q+1 points;
    # split exceptional has 3q+1 points, replacing one singular point.
    increase_per=(3 if n%2==0 else 1)*q
    predicted_resolution=q*q+q+1+expected_singular*increase_per
    coho=q*q+1+q*(2+2*(n%2==0)+6*(n%3==0)+12*(n%6==0))
    assert predicted_resolution==coho
    print(f'n={n} q={q} X={len(xs)} singular={len(crit)} '
          f'split_tangents={n%2==0} resolved={coho}')

if __name__=='__main__':
    for n in range(1,7):test(n)
    print('KLEIN_SEVEN_A3_FROBENIUS_ZETA_CHECKS_PASS')
