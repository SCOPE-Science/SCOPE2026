#!/usr/bin/env python3
"""Exact F_3 / F_9 checks for a four-cuspidal sextic family.
No statistical or infinite-proof claims are made by this code.
"""
from itertools import product

# Arithmetic in F_9 = F_3[t]/(t^2+1); encode c0+3*c1.
def add(a,b): return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
def neg(a): return ((-a%3)%3)+3*((-(a//3))%3)
def mul(a,b):
    a0,a1=a%3,a//3; b0,b1=b%3,b//3
    return ((a0*b0-a1*b1)%3)+3*((a0*b1+a1*b0)%3)
def pow9(a,n):
    r=1
    for i in range(n):r=mul(r,a)
    return r

def geom(q):
    plus=(lambda a,b:(a+b)%3) if q==3 else add
    times=(lambda a,b:(a*b)%3) if q==3 else mul
    negation=(lambda a:(-a)%3) if q==3 else neg
    power=(lambda a,n: pow(a,n,3)) if q==3 else pow9
    F=range(q)
    points=[(1,y,z) for y in F for z in F]+[(0,1,z) for z in F]+[(0,0,1)]
    def summ(*v):
        t=0
        for x in v:t=plus(t,x)
        return t
    def scale(a,x):return times(a,x)
    exps=[((6,0,0),1),((0,6,0),1),((0,0,6),1),
          ((4,2,0),None),((0,4,2),None),((2,0,4),None),
          ((2,4,0),None),((0,2,4),None),((4,0,2),None)]
    def poly_eval(x,y,z,a,b,partial=None):
        value=0
        coeffs=[1,1,1,a,a,a,b,b,b]
        for (e,c) in zip((t[0] for t in exps),coeffs):
            if partial is not None:
                deriv=e[partial]%3
                if deriv==0: continue
                c=times(c,deriv)
                ep=list(e); ep[partial]-=1
            else: ep=e
            term=c
            for coord,n in zip((x,y,z),ep):term=times(term,power(coord,n))
            value=plus(value,term)
        return value
    def polynomial(x,y,z,a,b):return poly_eval(x,y,z,a,b)
    def grad(x,y,z,a,b):return tuple(poly_eval(x,y,z,a,b,i) for i in range(3))
    checked=0
    point_distribution={}
    for a,b in product(F,repeat=2):
        s=plus(a,b); d=plus(a,negation(b)); ab=times(a,b)
        disc=plus(power(ab,2),negation(power(s,3)))
        if s==0 or d==0 or disc==0:continue
        sing=[P for P in points if polynomial(*P,a,b)==0 and all(t==0 for t in grad(*P,a,b))]
        expected={(1,sy,sz) for sy in (1,2) for sz in (1,2)}
        assert set(sing)==expected,(q,a,b,sing)
        checked+=1
        count=sum(1 for P in points if polynomial(*P,a,b)==0)
        point_distribution[count]=point_distribution.get(count,0)+1
    assert checked>0
    print(f'F_{q}: {checked} admissible marked parameter pairs; all have exactly four rational singularities at sign points; point counts {point_distribution}')
    if q==3: assert point_distribution=={10:2,4:2}

if __name__=='__main__':
    # symbolic identities in F3 for a representative and direct projective checks.
    geom(3)
    geom(9)
    print('VERIFY_OK')
