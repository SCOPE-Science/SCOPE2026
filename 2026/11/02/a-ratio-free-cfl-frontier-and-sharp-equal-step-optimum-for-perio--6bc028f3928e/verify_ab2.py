#!/usr/bin/env python3
"""Exact symbolic checks and reproducible rational tests for alternating-step AB2."""
import cmath
from fractions import Fraction
import sympy as sp

r, z, c, d = sp.symbols('r z c d', positive=True)

def step(ratio, scaled_step):
    return sp.Matrix([[1-scaled_step*(1+ratio/2),scaled_step*ratio/2],[1,0]])

H = step(sp.S.One/r,z)
R = step(r,r*z)
P = sp.simplify(R*H)
D = c**2*r/(4*(r+1)**2)
A = 1-c+c**2/2
Pc = sp.simplify(P.subs(z,c/(1+r)))
assert sp.simplify(sp.trace(Pc)-(A+D)) == 0
assert sp.simplify(Pc.det()-D) == 0
assert sp.simplify(1-sp.trace(Pc)+Pc.det()-c*(1-c/2)) == 0
assert sp.simplify(1+sp.trace(Pc)+Pc.det()-(2-c+c**2/2+2*D)) == 0
assert sp.factor((A+c**2/16)**2-4*(c**2/16)) == (3*c-4)**2*(9*c**2-8*c+16)/256
L = 3*A/5
assert sp.factor(L**2-(A+c**2/16)*L+c**2/16) == -(3*c-4)**2*(7*c**2-6*c+12)/800
assert sp.simplify((Pc.subs(r,1)).subs(c,sp.Rational(4,3))-sp.eye(2)/3)==sp.zeros(2)
Q = sp.simplify(H*R).subs(z,c/(1+r))
LQ = Q.applyfunc(lambda t:sp.limit(t/r,r,sp.oo))
assert LQ == sp.Matrix([[-c/2,c/2],[-c/2,c/2]])

def float_rho(ratio,pair_parameter):
    dd=pair_parameter**2*ratio/(4*(1+ratio)**2)
    aa=1-pair_parameter+pair_parameter**2/2
    tr=aa+dd
    discriminant=complex(tr*tr-4*dd,0)
    roots=((tr+cmath.sqrt(discriminant))/2,(tr-cmath.sqrt(discriminant))/2)
    return max(abs(v) for v in roots)

counter=0
rs=[Fraction(1,47),Fraction(1,9),Fraction(1,2),Fraction(1,1),Fraction(4,3),Fraction(7,1),Fraction(97,1)]
cs=[Fraction(1,40),Fraction(1,4),Fraction(4,5),Fraction(1,1),Fraction(4,3),Fraction(3,2),Fraction(199,100),Fraction(2,1),Fraction(201,100),Fraction(4,1)]
for rr in rs:
  for cc in cs:
    rr=sp.Rational(rr.numerator,rr.denominator); cc=sp.Rational(cc.numerator,cc.denominator)
    z0=cc/(1+rr)
    assert sp.trace(P.subs({r:rr,z:z0}))==sp.trace(Pc.subs({r:rr,c:cc}))
    assert sp.factor(Pc.det().subs({r:rr,c:cc}))==sp.factor(D.subs({r:rr,c:cc}))
    observed=float_rho(float(rr),float(cc))
    if cc<2: assert observed <1-1e-9,(rr,cc,observed)
    elif cc==2: assert abs(observed-1)<1e-9
    else: assert observed >1+1e-9
    if cc<2:
        equ=float_rho(1,float(cc))
        assert observed >= equ-1e-10
        if rr!=1: assert observed>equ+1e-8
        assert observed/equ < 5/3+1e-9
    counter+=1

# Verify one-step recurrence directly on a broad rational grid.
for rr in rs:
 for cc in cs[:8]:
    zz=cc/(1+rr)
    pair=step(rr,rr*zz)*step(1/rr,zz)
    for v0,v1 in [(sp.Rational(3,5),sp.Rational(-2,7)),(sp.Rational(7,4),sp.Rational(5,3))]:
        state=sp.Matrix([v0,v1]); first=step(1/rr,zz)*state
        second=step(rr,rr*zz)*first
        assert second==pair*state
        counter+=1

rho_star=float_rho(1,4/3)
rho_extreme=float_rho(1e10,4/3)
assert abs(rho_star-1/3)<1e-7
assert abs(rho_extreme/rho_star-5/3)<2e-7
print(f'VERIFY_OK symbolic=7 phase_matrix_limit=1 rational_checks={counter} sharp_penalty={rho_extreme/rho_star:.9f}')
