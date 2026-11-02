"""Exact symbolic checks supporting the weighted-Dulac phase portrait."""
from fractions import Fraction
import sympy as S

r,z,mu=S.symbols('r z mu',positive=True,real=True)
alpha=S.symbols('alpha',real=True)
P=21*r**4-125*r**2+400*z**2+100
fr=-mu*r*P/21
fz=-z-r**2/S.Integer(10)
assert S.factor(P-(r**2-5)*(21*r**2-20)-400*z**2)==0
assert S.factor(P.subs(z,-r**2/S.Integer(10))-25*(r**2-1)*(r**2-4))==0
B=S.Integer(1)/r
D=S.diff(B*fr,r)+S.diff(B*fz,z)
D_expected=(S.Rational(15625,1764)*mu-1-4*mu*(r**2-S.Rational(125,84))**2)/r
assert S.factor(D-D_expected)==0
Q=(S.diff(r**alpha*fr,r)+S.diff(r**alpha*fz,z))/r**alpha
Q_expected=-1-mu/S.Integer(21)*(21*(alpha+5)*r**4-125*(alpha+3)*r**2+400*(alpha+1)*z**2+100*(alpha+1))
assert S.simplify(Q-Q_expected)==0
qmin=-S.Rational(25,84)*(289*alpha**2+1734*alpha+3945)/(alpha+5)
u_star=S.Rational(125,42)*(alpha+3)/(alpha+5)
assert S.simplify(qmin-(21*(alpha+5)*u_star**2-125*(alpha+3)*u_star+100*(alpha+1)))==0
assert S.factor(S.diff(qmin,alpha)+S.Rational(25,84)*(17*alpha+35)*(17*alpha+135)/(alpha+5)**2)==0
J=S.Matrix([[S.diff(fr,r), S.diff(fr,z)], [S.diff(fz,r), S.diff(fz,z)]])
J0=J.subs({r:0,z:0})
J1=J.subs({r:1,z:-S.Rational(1,10)})
J2=J.subs({r:2,z:-S.Rational(2,5)})
assert S.simplify(J0[0,0]+100*mu/21)==0
assert S.simplify(J0[1,1]+1)==0
assert S.simplify(J1.det()+50*mu/7)==0
assert S.simplify(J2.det()-200*mu/7)==0
assert S.simplify(J2.trace()+1+344*mu/21)==0
assert Fraction(1764,15625)/Fraction(588,6575)==Fraction(789,625)
print('PASS: exact weighted divergence, radial-power optimality, equilibria and endpoint ratio')
