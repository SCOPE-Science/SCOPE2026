#!/usr/bin/env python3
"""Numerical and exact-channel checks for a ternary-input two-BSC model.

Run with Python 3.11+; uses only the standard library. The analytic
claims in the accompanying proof do not depend on these finite tests.
"""
from decimal import Decimal, localcontext
from fractions import Fraction


def channel(p):
    a = (1-p)**2
    b = p*(1-p)
    c = p**2
    return ((a,b,b,c),(b,a,c,b),(c,b,b,a))


def entropy(v):
    return -sum(x*x.ln() for x in v if x > 0)


def values(t, beta):
    b = (1-t*t)/4
    s = (1+t*t)/4
    return s-t*t*beta/2, b+t*(1+t)*beta/2, b-t*(1-t)*beta/2


def derivative(t, beta):
    u,v,w = values(t,beta)
    return t*t*u.ln()-t*(1+t)*v.ln()/2+t*(1-t)*w.ln()/2


def curvature(t, beta):
    u,v,w = values(t,beta)
    return -t**4/(2*u)-t*t*(1+t)**2/(4*v)-t*t*(1-t)**2/(4*w)


def optimum(t):
    low, high = Decimal(0), Decimal(1)
    assert derivative(t,low)>0 and derivative(t,high)<0
    for _ in range(350):
        mid=(low+high)/2
        if derivative(t,mid)>0:
            low=mid
        else:
            high=mid
    return (low+high)/2


def output_entropy(t,beta):
    u,v,w=values(t,beta)
    return entropy((u,v,w,u))


def check():
    with localcontext() as ctx:
        ctx.prec=85
        one=Decimal(1)
        z=Decimal(0)
        fractions=(Fraction(0),Fraction(1,10),Fraction(1,4),
                   Fraction(2,5),Fraction(49,100),Fraction(1,2))
        for p in fractions:
            rows=channel(p)
            assert all(sum(row)==1 for row in rows)
            assert all(sorted(row)==sorted(rows[0]) for row in rows)
            for beta in (Fraction(0),Fraction(1,7),Fraction(1,3),Fraction(2,3),Fraction(1)):
                masses=((1-beta)/2,beta,(1-beta)/2)
                out=[sum(masses[i]*rows[i][j] for i in range(3)) for j in range(4)]
                t=one-2*Decimal(p.numerator)/Decimal(p.denominator)
                bd=Decimal(beta.numerator)/Decimal(beta.denominator)
                exact=[Decimal(x.numerator)/Decimal(x.denominator) for x in out]
                u,v,w=values(t,bd)
                assert max(abs(x-y) for x,y in zip(exact,(u,v,w,u)))<Decimal('1e-75')
                if p!=0 and p!=Fraction(1,2):
                    pd=Decimal(p.numerator)/Decimal(p.denominator)
                    conditional=entropy(channel(pd)[0])
                    h2=-(pd*pd.ln()+(one-pd)*(one-pd).ln())
                    assert abs(conditional-2*h2)<Decimal('1e-75')
        print('EXACT_CHANNEL_ROWS_AND_MIXTURES_OK')
        ln2=Decimal(2).ln()
        for pstr in ('0.1','0.25','0.3','0.4','0.45','0.49'):
            p=Decimal(pstr);t=one-2*p
            beta=optimum(t)
            gain=(output_entropy(t,beta)-output_entropy(t,z))/ln2
            assert gain>0 and 0<beta<1 and curvature(t,beta)<0
            b=p*(one-p);s=((one-p)**2+p*p)/2
            assert abs(derivative(t,z)-t*t*(s/b).ln())<Decimal('1e-65')
            assert abs(derivative(t,one)-t*((one-t)/(one+t)).ln())<Decimal('1e-65')
            h=Decimal('1e-14')
            numeric=(output_entropy(t,beta+h)-output_entropy(t,beta-h))/(2*h)
            assert abs(numeric)<Decimal('1e-12')
            print(f'p={pstr} middle_probability={beta:.12f} gain_bits={gain:.12g}')
        for tstr in ('0.1','0.05','0.025','0.0125'):
            t=Decimal(tstr)
            beta=optimum(t)
            gain=(output_entropy(t,beta)-output_entropy(t,z))/ln2
            assert beta>0 and gain>0
            print(f't={tstr} beta_over_t2={beta/t**2:.12f} gain_over_t6={gain/t**6:.12f}')
        print('ASYMPTOTIC_LIMIT_PREDICTIONS',f'beta/t2 -> 1, gain/t6 -> {1/ln2:.12f}')
        print('VERIFY_OK')


if __name__=='__main__':
    check()
