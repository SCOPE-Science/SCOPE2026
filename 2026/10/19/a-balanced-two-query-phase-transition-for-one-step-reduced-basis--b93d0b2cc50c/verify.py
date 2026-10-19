#!/usr/bin/env python3
"""Reproduce algebra and direct one-step CG energy checks for the stated model."""
from fractions import Fraction
import sympy as s

x, t = s.symbols('x t', positive=True)
risk = ((x-1)**2/(x**2+t) + (x-t**2)**2/(t*(x**2+t**3)))/(t+1)
q = x**2-t*(t-1)*x+t**2
D = s.diff(risk,x)
D_claim = 2*(x-t)*(x+t)*(x**2+(t-1)*x+t**2)*q/((x**2+t)**2*(x**2+t**3)**2)
assert s.cancel(D-D_claim) == 0
assert s.cancel(risk - (t-2)/(t*(t-1)) - q**2/(t*(t-1)*(x**2+t)*(x**2+t**3))) == 0
assert s.simplify(risk.subs(x,t) - 2*(t-1)**2/(t*(t+1)**2)) == 0
assert s.factor(risk.subs(x,t)-(t-2)/(t*(t-1))) == (t-3)**2/((t-1)*(t+1)**2)

def pcg_energy(T,A,B,first):
    lam=[Fraction(1),T,T,T*T]
    F=[A,A+1/T,A+1/T,A]
    rhs = [Fraction(1) if k in first else Fraction(0) for k in range(4)]
    z=[a*b for a,b in zip(F,rhs)]
    step=sum(rhs[i]*z[i] for i in range(4))/sum(lam[i]*z[i]*z[i] for i in range(4))
    sol=[rhs[i]/lam[i] for i in range(4)]
    err=[sol[i]-step*z[i] for i in range(4)]
    return sum(lam[i]*err[i]*err[i] for i in range(4))

count = 0
for tn in range(2,18):
    for td in range(1,5):
        T=Fraction(tn,td)
        if T<=1:continue
        for an in range(1,13):
            for ad in range(1,9):
                A=Fraction(an,ad)
                theta=T+1/A
                el=(theta-1)**2/(theta**2+T)
                eh=(theta-T*T)**2/(T*T*(theta**2+T**3))
                assert pcg_energy(T,A,None,[0,1]) == el
                assert pcg_energy(T,A,None,[1,3]) == eh
                weighted=el/(T+1)+T*eh/(T+1)
                formula=Fraction(str(0))+(theta-1)**2/((T+1)*(theta**2+T))+(theta-T*T)**2/(T*(T+1)*(theta**2+T**3))
                assert weighted==formula
                count+=3
for tv in [s.Rational(7,2),4,5,10,100]:
    root=tv*(tv-1+s.sqrt((tv-3)*(tv+1)))/2
    assert float(root)>float(tv)
    assert abs(float(risk.subs({t:tv,x:root})-(tv-2)/(tv*(tv-1))))<1e-12
    assert float(root)<float(tv*tv)
    count+=3
print('PASS: 4 symbolic identities, %d exact-rational and root checks.'%count)
