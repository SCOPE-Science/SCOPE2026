#!/usr/bin/env python3
"""Exact algebra and representative finite replays for a scalar startup positivity classification.

Requires Python 3.10+ and SymPy 1.12+. Finite checks do not replace the proof.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
import sympy as s

checks=0

def check(a):
    global checks
    assert a
    checks+=1

k,z=s.symbols('k z',real=True)
D=(3-k)*(1+k)
a0=(1-3*k)/(3-k)
a1=-4*(1-k)/(3-k)
b0=2*k*k/D
b1=4*k/D
b2=2/D
A=4*(1-k*k-k*z)/(D+2*z)
B=((1-3*k)*(1+k)+2*k*k*z)/(D+2*z)
Delta=s.factor(A*A-4*B)
za=(1-k*k)/k
zb=(3*k-1)*(1+k)/(2*k*k)
zc=(1+k)/(2*(1-k))
check(s.cancel((1+z*b2)*A+(a1+z*b1))==0)
check(s.cancel((1+z*b2)*B-(a0+z*b0))==0)
check(s.factor(Delta-4*(1+k)**3*((1+k)-2*(1-k)*z)/(D+2*z)**2)==0)
check(s.factor(zb-za-(1+k)**2*(2*k-1)/(2*k*k))==0)
check(s.factor(zc-zb-(1+k)*(2*k-1)**2/(2*k*k*(1-k)))==0)
check(s.factor(s.diff(zb,k)-(1-k)/k**3)==0)
check(s.factor(s.diff(za,k)+(1+k*k)/k**2)==0)
check(s.factor(A.subs(z,za))==0)
check(s.factor(B.subs(z,zb))==0)
check(s.factor(Delta.subs(z,zc))==0)
check(A.subs({k:s.Rational(1,2),z:s.Rational(3,2)})==0)
check(B.subs({k:s.Rational(1,2),z:s.Rational(3,2)})==0)

with localcontext() as ctx:
    ctx.prec=100
    def dec(v):
        if isinstance(v,Fraction):
            return Decimal(v.numerator)/Decimal(v.denominator)
        return Decimal(v)
    def coefficients(kk,zz):
        dd=(3-kk)*(1+kk)
        return (dec(4*(1-kk*kk-kk*zz)/(dd+2*zz)),
                dec(((1-3*kk)*(1+kk)+2*kk*kk*zz)/(dd+2*zz)))
    def replay(aa,bb,w,steps=220):
        p=Decimal(1);q=w
        for n in range(2,steps):
            p,q=q,aa*q-bb*p
            yield n,q
    def all_nonnegative(aa,bb,w,steps=220):
        return all(v>=0 for _,v in replay(aa,bb,w,steps))
    for kk in (Fraction(0),Fraction(1,4),Fraction(1,3),Fraction(2,5),Fraction(49,100),Fraction(1,2),Fraction(3,5),Fraction(3,4),Fraction(9,10)):
        cc=(1+kk)/(2*(1-kk))
        aa_z=(1-kk*kk)/kk if kk>0 else None
        bb_z=(3*kk-1)*(1+kk)/(2*kk*kk) if kk>Fraction(1,3) else None
        if kk<=Fraction(1,3):
            half=(cc*Fraction(3,4),)
            allz=()
            single=()
        elif kk<Fraction(1,2):
            allz=(bb_z*Fraction(1,3),bb_z)
            half=((bb_z+cc)/2,bb_z+(cc-bb_z)*Fraction(99,100))
            single=()
        elif kk==Fraction(1,2):
            allz=(cc*Fraction(1,3),cc)
            half=()
            single=()
        else:
            allz=(aa_z*Fraction(1,3),aa_z)
            half=()
            single=((aa_z+bb_z)/2,)
        for zz in allz:
            aa,bb=coefficients(kk,zz)
            check(aa>=0 and bb<=0)
            for w in (Fraction(1,10),Fraction(1),Fraction(10),Fraction(100)):
                check(all_nonnegative(aa,bb,dec(w)))
        for zz in half:
            aa,bb=coefficients(kk,zz)
            check(aa>0 and bb>0)
            disc=aa*aa-4*bb
            check(disc>=0)
            low=(aa-disc.sqrt())/2
            check(low>0)
            check(all_nonnegative(aa,bb,low*Decimal(2)))
            # A starting ratio below the smaller positive root must eventually fail.
            neg=[n for n,v in replay(aa,bb,low/2,1500) if v<0]
            check(bool(neg))
        for zz in single:
            aa,bb=coefficients(kk,zz)
            disc=aa*aa-4*bb
            lam=(aa+disc.sqrt())/2
            check(aa<0 and bb<0 and lam>0)
            check(all_nonnegative(aa,bb,lam,60))
            for scale in (Decimal('0.8'),Decimal('1.2')):
                neg=[n for n,v in replay(aa,bb,scale*lam,2000) if v<0]
                check(bool(neg))
        # Strongly outside the discriminant boundary, every positive start oscillates.
        zz=cc*Fraction(3,2)
        aa,bb=coefficients(kk,zz)
        check(aa*aa-4*bb<0)
        for w in (Decimal('0.1'),Decimal('1'),Decimal('10')):
            check(any(v<0 for _,v in replay(aa,bb,w,500)))
    # A case that can be positive beyond the usual numerical-startup limit only by tuning.
    kk=Fraction(3,4)
    za0=(1-kk*kk)/kk
    zb0=(3*kk-1)*(1+kk)/(2*kk*kk)
    zz=(za0+zb0)/2
    aa,bb=coefficients(kk,zz)
    disc=aa*aa-4*bb
    check(aa<0 and bb<0 and disc>0)
    check(all_nonnegative(aa,bb,(aa+disc.sqrt())/2,80))
    print('ILLUSTRATION', 'kappa',kk,'positive_singleton_interval',(za0,zb0))
print('VERIFY_OK',checks)
