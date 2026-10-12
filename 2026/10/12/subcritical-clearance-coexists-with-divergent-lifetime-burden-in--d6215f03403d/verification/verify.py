#!/usr/bin/env python3
"""Exact matrix checks for a positive multi-order SEIATR model; no simulation proof."""
import sympy as sp
z=sp.symbols('z')
b,d,beta,sig,p,theta,kappa,ri,ra,rt=sp.symbols('b d beta sig p theta kappa ri ra rt',positive=True)
KE=sig+d;KI=kappa+ri+d;KA=ra+d;KT=rt+d
D=sp.diag(KE,KI,KA)
C=sp.Matrix([[0,beta,beta*theta],[p*sig,0,0],[(1-p)*sig,0,0]])
Q=D.inv()*C
R0=beta*sig/KE*(p/KI+theta*(1-p)/KA)
poly=sp.factor((z*sp.eye(3)-Q).det())
assert sp.factor(poly-z*(z**2-R0))==0
rates={b:sp.Integer(2),d:sp.Integer(1),beta:sp.Rational(1,5),sig:sp.Integer(1),p:sp.Rational(1,2),theta:sp.Rational(1,2),kappa:sp.Rational(1,2),ri:sp.Rational(1,2),ra:sp.Rational(1,2),rt:sp.Rational(1,2)}
assert sp.factor(R0.subs(rates))==sp.Rational(1,24)
Dn=D.subs(rates);Cn=C.subs(rates);Qn=Q.subs(rates)
w=(sp.eye(3)-Qn).inv()*sp.ones(3,1)
assert all(x>0 for x in w)
assert (Cn-Dn)*w==-Dn*sp.ones(3,1)
assert Dn==sp.diag(2,2,sp.Rational(3,2))
assert KT.subs(rates)==sp.Rational(3,2)
# Strict positivity of coefficients and an exact Routh-Hurwitz check
A=Cn-Dn
ch=sp.Poly((z*sp.eye(3)-A).det(),z)
a,bcoef,ccoef=ch.all_coeffs()[1:]
assert a>0 and bcoef>0 and ccoef>0 and a*bcoef>ccoef
# The irrational-order case is covered by the proof because scalar kernels and
# their mass identities hold for all real orders in (0,1), not by this program.
print('VERIFY_OK')
