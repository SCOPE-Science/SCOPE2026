#!/usr/bin/env python3
"""Exact algebraic verification of a six-state EBV/dysplasia model."""
import sympy as s
N,D,I,H,C,V=s.symbols('N D I H C V')
a1,a2,a3,a4,a5,d1,d2,d3,d4,d5,d6,alpha,beta,gamma,mu,e=s.symbols('a1 a2 a3 a4 a5 d1 d2 d3 d4 d5 d6 alpha beta gamma mu e', positive=True)
lam=s.symbols('lam')
vars=s.Matrix([N,D,I,H,C,V])
f=s.Matrix([a1-(d1+alpha)*N,(a2-d2)*D+alpha*N-beta*D*V,(a3-gamma-d3)*I+beta*D*V,(a4-mu-d4)*H+gamma*I,(a5-d5)*C+mu*H,e*a3*I-d6*V])
N0=a1/(d1+alpha)
D0=alpha*N0/(d2-a2)
E0={N:N0,D:D0,I:0,H:0,C:0,V:0}
assert all(s.cancel(x.subs(E0))==0 for x in f)
E02={N:a1/d1,D:0,I:0,H:0,C:0,V:0}
f02=[s.factor(x.subs(E02)) for x in f]
assert f02==[-a1*alpha/d1,a1*alpha/d1,0,0,0,0]
J=f.jacobian(vars).subs(E0)
char=s.factor((lam*s.eye(6)-J).det())
q=d2-a2;k=d3+gamma-a3;h=d4+mu-a4;c=d5-a5;m=d6
quad=(lam+k)*(lam+m)-beta*D0*e*a3
expected=(lam+d1+alpha)*(lam+q)*(lam+h)*(lam+c)*quad
assert s.cancel(char-expected)==0
R=s.cancel(beta*e*a3*D0/(k*m))
assert s.factor(quad-(lam**2+(k+m)*lam+k*m*(1-R)))==0
w={a1:1,a2:1,a3:1,a4:1,a5:1,d1:2,d2:2,d3:2,d4:2,d5:2,d6:2,alpha:1,beta:20,gamma:1,mu:1,e:1}
assert s.simplify(R.subs(w))==s.Rational(5,3)
assert s.simplify(N0.subs(w))==s.Rational(1,3)
assert s.simplify(D0.subs(w))==s.Rational(1,3)
wchar=s.factor(char.subs(w))
assert wchar==(lam+3)*(lam+1)**2*(lam+2)*(3*lam**2+12*lam-8)/3
assert -2+s.sqrt(s.Rational(20,3))>0
# Below-threshold witness gives an exact stable block with all other rates unchanged.
wlow=dict(w); wlow[beta]=5
assert s.simplify(R.subs(wlow))==s.Rational(5,12)
assert all(s.cancel(x.subs(E0).subs(w))==0 for x in f)
print('VERIFY_OK')
