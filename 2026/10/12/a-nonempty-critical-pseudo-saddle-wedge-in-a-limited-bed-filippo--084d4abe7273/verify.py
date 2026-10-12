#!/usr/bin/env python3
import sympy as sp
from fractions import Fraction

mu,nu,h0,h1,b,Lam,Ic=sp.symbols('mu nu h0 h1 b Lam Ic', positive=True)
q=mu+nu
D=h1-h0
r0=q+h0
r1=q+h1
beta=r1
Ic0=sp.simplify(b*(r1-beta)/(beta-r0))
assert Ic0==0
Sc2_source=((b+Ic)*r0+b*D)*Ic/((b+Ic)*(beta-r0)-b*D)
Sc2=sp.simplify(Sc2_source)
assert sp.simplify(Sc2-(r0*Ic/D+b*r1/D))==0
Ss=(Lam-q*Ic)/mu
expr=sp.factor(mu*D*(Ss-Sc2))
expected=Lam*D-mu*b*r1-Ic*(q*D+mu*r0)
assert sp.simplify(expr-expected)==0
Icdag=sp.simplify((Lam*D-mu*b*r1)/(q*D+mu*r0))

# Exact witness.
vals={
 mu:sp.Rational(1,10), nu:sp.Rational(3,5), h0:sp.Rational(1,5),
 h1:sp.Integer(2), b:sp.Rational(1,10), Lam:sp.Integer(8), Ic:sp.Integer(5)
}
qv=sp.simplify(q.subs(vals)); Dv=sp.simplify(D.subs(vals)); r0v=sp.simplify(r0.subs(vals)); r1v=sp.simplify(r1.subs(vals))
assert (qv,Dv,r0v,r1v)==(sp.Rational(7,10),sp.Rational(9,5),sp.Rational(9,10),sp.Rational(27,10))
Icdv=sp.simplify(Icdag.subs(vals)); Sc2v=sp.simplify(Sc2.subs(vals)); Ssv=sp.simplify(Ss.subs(vals))
assert Icdv==sp.Rational(1597,150)
assert Sc2v==sp.Rational(53,20)
assert Ssv==45
assert sp.Integer(5)<Icdv and Ssv>Sc2v
# Normal components at the witness point.
S=sp.Integer(45); Icv=sp.Integer(5); betav=r1v
X1=sp.simplify(Icv*(betav*S/(S+Icv)-r1v))
H2=h0.subs(vals)+Dv*b.subs(vals)/(b.subs(vals)+Icv)
X2=sp.simplify(Icv*(betav*S/(S+Icv)-qv-H2))
assert X1<0 and X2>0
assert Ssv+Icv < Lam.subs(vals)/mu.subs(vals)
Fs=sp.simplify(-mu.subs(vals)*(Ssv-(Lam.subs(vals)-qv*Icv)/mu.subs(vals)))
assert Fs==0
print('VERIFY_OK')
print('Ic_dagger',Icdv)
print('Sc2',Sc2v,'Ss',Ssv)
print('normal_components',X1,X2)
