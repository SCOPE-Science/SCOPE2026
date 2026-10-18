#!/usr/bin/env python3
"""Self-contained exact/high-precision checks for a two-cycle sharpness witness.
Analytical arguments in RESULT.md prove global completeness; this is auxiliary.
"""
from fractions import Fraction as Q
from decimal import Decimal, localcontext

A,B,C=Q(1,20),Q(1,10),Q(21,200)

def dec(q):
    if not isinstance(q,Q): q=Q(q)
    return Decimal(q.numerator)/Decimal(q.denominator)

def left(x):
    return Decimal(1)-(Decimal(1)-dec(A))*(Decimal(1)-dec(x)/dec(B)).sqrt()

def right(y):
    return dec(C)*((y-dec(B))/(Decimal(1)-dec(B))).sqrt()

def invright(x):
    return dec(B)+(Decimal(1)-dec(B))*(x/dec(C))**2

def D(x):
    return left(x)-invright(x)

def check():
    with localcontext() as ctx:
        ctx.prec=65
        q=[Q(0),B/4,3*B/4,B]
        signs=[-1,1,-1,1]
        assert [int(D(dec(x)).compare(0)) for x in q]==signs
        assert Q(208,245)**2-3*Q(19,40)**2==Q(168613,3841600)
        assert abs(D(dec(0))-dec(-Q(1,20)))<Decimal('1e-60')
        assert abs(D(dec(3*B/4))-dec(-Q(67,1960)))<Decimal('1e-60')
        assert abs(D(dec(B))-dec(Q(41,490)))<Decimal('1e-60')
        roots=[]
        for lo,hi in zip(q[:-1],q[1:]):
            l,h=dec(lo),dec(hi)
            dl=D(l)
            for _ in range(225):
                m=(l+h)/2
                dm=D(m)
                if (dm>0)==(dl>0): l,dl=m,dm
                else: h=m
            x=(l+h)/2; y=invright(x)
            assert dec(0)<x<dec(B)<y<=dec(1)
            assert abs(left(x)-y)<Decimal('1e-60')
            assert abs(right(y)-x)<Decimal('1e-60')
            lp=(dec(1)-dec(A))/(Decimal(2)*dec(B)*(Decimal(1)-x/dec(B)).sqrt())
            rp=dec(C)/(Decimal(2)*(Decimal(1)-dec(B))*((y-dec(B))/(Decimal(1)-dec(B))).sqrt())
            mu=lp*rp
            roots.append((x,y,mu))
        assert roots[0][2]>1 and 0<roots[1][2]<1 and roots[2][2]>1
        assert abs(dec(C)/(2*(dec(B)*(1-dec(B))).sqrt())-dec(Q(7,40)))<Decimal('1e-60')
        assert dec(Q(19,4))>1
        for x,y,mu in roots:
            print('left_point=',x,'right_point=',y,'two_step_multiplier=',mu)
        print('PASS: four exact signs; three bracketed cycles; stability and no-fixed-point inequalities')

if __name__=='__main__': check()
