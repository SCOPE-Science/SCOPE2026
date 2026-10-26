#!/usr/bin/env python3
"""Standalone finite checks of the stated rare-synergy phase diagram.
All critical sign tests use exact rational arithmetic; limits are inspected at high precision.
Finite checks are NOT offered as proof of asymptotic statements.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext

D=F(2,5); K=F(3,2)

def value(n,L,c,x):
    p=c/L**n
    assert 0<p<1
    return K*(p*(1+D*x)**n + (1-p)*(1-D*x)**n)-1

def bisect(n,L,c,lo,hi,prec=110):
    with localcontext() as ctx:
        ctx.prec=prec
        d=lambda f: Decimal(f.numerator)/Decimal(f.denominator)
        delta,kappa,Ld,cd=map(d,(D,K,L,c))
        p=cd/Ld**n
        def v(x): return kappa*(p*(1+delta*x)**n+(1-p)*(1-delta*x)**n)-1
        a,b=map(d,(lo,hi)); fa=v(a); fb=v(b)
        assert fa*fb<0, ('bracket',n,L,c,fa,fb)
        for _ in range(600):
            m=(a+b)/2; fm=v(m)
            if fm==0: return m
            if fm*fa>0: a,fa=m,fm
            else: b,fb=m,fm
        return (a+b)/2


def main():
    nvalues=[24,48,96]
    cases=[(F(6,5),F(1)),(F(7,5),F(1)),(F(7,5),F(1,3)),(F(7,5),F(2,3)),(F(8,5),F(1))]
    for L,c in cases:
        for n in nvalues:
            at0=value(n,L,c,F(0)); atmid=value(n,L,c,F(1,2)); at1=value(n,L,c,F(1))
            assert at0>0
            if L==F(6,5):
                xstar=(L-1)/D
                assert value(n,L,c,xstar-F(1,5))<0 and at1>0
                low=bisect(n,L,c,F(0),F(1,5))
                high=bisect(n,L,c,xstar-F(1,5),F(1))
            else:
                assert atmid<0
                low=bisect(n,L,c,F(0),F(1,2))
                if L==F(7,5) and c>=F(2,3):
                    assert at1>0
                    high=bisect(n,L,c,F(1,2),F(1))
                else:
                    assert at1<0
                    high=None
            with localcontext() as ctx:
                ctx.prec=80
                k=Decimal(K.numerator)/K.denominator
                delta=Decimal(D.numerator)/D.denominator
                predlo=k.ln()/delta
                loerr=abs(low*Decimal(n)-predlo)
                if high is not None and L==F(6,5):
                    Ld=Decimal(L.numerator)/L.denominator
                    cd=Decimal(c.numerator)/c.denominator
                    target=(Ld-1)/delta-Ld/(delta*Decimal(n))*(k*cd).ln()
                    hierr=abs(high-target)
                elif high is not None and L==F(7,5) and c==F(1):
                    target=Decimal(1)-(1+delta)/(delta*Decimal(n))*(k).ln()
                    hierr=abs(high-target)
                elif high is not None and L==F(7,5) and c==F(2,3):
                    target=Decimal(1)-k*(1+delta)/delta*(1-delta)**n/Decimal(n)
                    hierr=abs(high-target)
                else: hierr=None
            print('L',L,'c',c,'n',n,'low',str(low)[:28], 'hi',str(high)[:28] if high else 'none', 'scaled_low_err',str(loerr)[:13], 'high_error',str(hierr)[:13])
    # Strictly convex for n>=2, because f'' is positive as an exact rational sum.
    n=20; L=F(6,5); c=F(1); p=c/L**n
    for x in [F(0),F(1,5),F(2,5),F(3,5),F(4,5),F(1)]:
        second=K*n*(n-1)*D**2*(p*(1+D*x)**(n-2)+(1-p)*(1-D*x)**(n-2))
        assert second>0
    # The finite-n full-cooperation threshold follows algebraically from f_n(1)=0.
    for n in [10,20,40]:
        L=1+D
        pcrit=(1/K-(1-D)**n)/((1+D)**n-(1-D)**n)
        assert 0<pcrit<1
        assert K*(pcrit*(1+D)**n+(1-pcrit)*(1-D)**n)-1==0
        print('n',n,'pcrit',str(float(pcrit)))
    # Explicit extremely rare-synergy example: exact root bracketing for n=96.
    n=96; L=F(6,5); c=F(1)
    assert value(n,L,c,F('0.01053'))>0 and value(n,L,c,F('0.01055'))<0
    assert value(n,L,c,F('0.48735'))<0 and value(n,L,c,F('0.48736'))>0
    print('Exact n=96 rational root brackets verified; synergy probability=',float(c/L**n))
    print('All finite exact-rational sign/identity and high-precision checks passed.')

if __name__=='__main__': main()
