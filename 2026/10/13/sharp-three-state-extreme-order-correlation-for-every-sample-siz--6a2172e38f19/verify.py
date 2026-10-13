"""Symbolic and exact finite diagnostics for the stated three-state theorem.

Run: python verify.py
Requires: SymPy as in requirements.txt.
The proof of the infinite statement is in RESULT.md; finite checks are diagnostic.
"""
from fractions import Fraction
from itertools import product
import sympy as sp


def main():
    a,b,t,z,x,r=sp.symbols('a b t z x r')
    d=b-a
    h=d**2-a
    EL=a+d*t
    EU=1-b+d*t
    EL2=a+d*t*t
    EU2=1-b+d*t*t
    ELU=a*(1+t*t)+t*(b-2*a)
    vl=sp.expand(EL2-EL**2)
    vu=sp.expand(EU2-EU**2)
    cov=sp.expand(ELU-EL*EU)
    assert sp.expand(cov-(a*b+h*t*(1-t)))==0
    V0=(3*a+b-(a+b)**2)/4
    L0=d*(1-a-b)
    K=d*(1-d)
    P=sp.expand((V0+K*(sp.Rational(1,4)-z))**2-L0**2*(sp.Rational(1,4)-z))
    assert sp.expand(vl*vu-P.subs(z,t*(1-t)))==0
    assert sp.expand(P.subs(z,0)-a*b*(1-a)*(1-b))==0
    assert sp.expand(sp.diff(P,z).subs(z,0)+2*a*d*(1-b)*(1+d))==0
    H=sp.expand(2*h*P-(a*b+h*z)*sp.diff(P,z))
    assert sp.diff(H,z,2)==0
    assert sp.expand(H.subs(z,0)-2*a*b*(1-b)*(h+a*b))==0
    B=(1-x-sp.Rational(1,2)*r*(10*x*x-11*x+3)
         -sp.Rational(1,2)*r*r*(17*x**3-15*x*x+4*x)
         -sp.Rational(1,2)*r**3*(12*x**4-8*x**3)
         -2*r**4*x**5)
    assert sp.expand(H.subs(z,sp.Rational(1,4)).subs({a:r*x*x,b:r*x*x+x})-r*x**5*B)==0

    checks=0
    for n in range(4,8):
        aa=Fraction(1,3**n)
        bb=Fraction(2**n,3**n)
        dd=bb-aa
        hh=dd**2-aa
        bound=((aa+bb)**2-aa)/(3*aa+bb-(aa+bb)**2)
        for tt in [Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(2,5)]:
            values=(Fraction(0),tt,Fraction(1))
            draws=list(product(range(3),repeat=n))
            denom=len(draws)
            min_vals=[values[min(v)] for v in draws]
            max_vals=[values[max(v)] for v in draws]
            m1=sum(min_vals,Fraction(0))/denom
            m2=sum(max_vals,Fraction(0))/denom
            m11=sum((v*v for v in min_vals),Fraction(0))/denom
            m22=sum((v*v for v in max_vals),Fraction(0))/denom
            m12=sum((q*v for q,v in zip(min_vals,max_vals)),Fraction(0))/denom
            assert m1 == aa+dd*tt
            assert m2 == 1-bb+dd*tt
            assert m11 == aa+dd*tt*tt
            assert m22 == 1-bb+dd*tt*tt
            assert m12 == aa*(1+tt*tt)+tt*(bb-2*aa)
            assert m12-m1*m2 == aa*bb+hh*tt*(1-tt)
            corr_squared=(m12-m1*m2)**2/((m11-m1*m1)*(m22-m2*m2))
            assert corr_squared <= bound*bound
            assert (corr_squared==bound*bound)==(tt==Fraction(1,2))
            checks+=8
    for n in range(4,40):
        aa=Fraction(1,3**n);bb=Fraction(2**n,3**n)
        dd=bb-aa; rr=aa/(dd*dd)
        assert 0 < dd <= Fraction(7,27) < Fraction(1,3)
        assert 0 < rr <= Fraction(27,49) < Fraction(3,5)
        # This is finite confirmation; the proof uses monotone ratios in n.
        checks+=4
    print('PASS: 7 symbolic identities,',checks,'exact rational diagnostics')

if __name__=='__main__':
    main()
