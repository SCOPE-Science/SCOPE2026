#!/usr/bin/env python3
"""Exact symbolic checks for the six-compartment information--SIRS equilibrium."""
from fractions import Fraction
import sympy as sp

U,M,Z,S,I,R = sp.symbols('U M Z S I R')
b1,b2,mu1,mu2,gamma,eta,K,beta,eps = sp.symbols(
    'b1 b2 mu1 mu2 gamma eta K beta eps', positive=True)
v=b2/(1-K*I)
inc=beta*(1+M)/(1+Z)*S*I
F=sp.Matrix([
 mu1-b1*U*M-v*U*Z-mu1*U,
 (b1*U-mu1)*M,
 (v*U-mu1)*Z,
 eps*(mu2-inc+eta*R-mu2*S),
 eps*(inc-(gamma+mu2)*I),
 eps*(gamma*I-(eta+mu2)*R),
])
exact={b1:sp.Rational(2),b2:sp.Rational(3,2),mu1:1,mu2:sp.Rational(1,4),
       gamma:sp.Rational(1,4),eta:sp.Rational(3,4),K:sp.Rational(1,2),beta:sp.Rational(4,3)}
state={U:sp.Rational(1,2),M:sp.Rational(1,4),Z:sp.Rational(1,4),
       S:sp.Rational(3,8),I:sp.Rational(1,2),R:sp.Rational(1,8)}
assert all(sp.cancel(x.subs(exact).subs(state))==0 for x in F)
assert sum(state[x] for x in (U,M,Z))==1
assert sum(state[x] for x in (S,I,R))==1

# Four-dimensional dynamics, with q = M+Z, z = Z and S = 1-I-R.
q,z,i,r=sp.symbols('q z i r')
H=sp.Matrix([
(1-q)*(b1*(q-z)+b2/(1-K*i)*z)-mu1*q,
(b2/(1-K*i)*(1-q)-mu1)*z,
eps*((beta*(1+q-z)/(1+z)*(1-i-r)-(gamma+mu2))*i),
eps*(gamma*i-(eta+mu2)*r),
])
redstate={q:sp.Rational(1,2),z:sp.Rational(1,4),i:sp.Rational(1,2),r:sp.Rational(1,8)}
assert all(sp.cancel(x.subs(exact).subs(redstate))==0 for x in H)
J=H.jacobian([q,z,i,r])
J_expected=sp.Matrix([[-1,0,sp.Rational(1,6),0],[-sp.Rational(1,2),0,sp.Rational(1,6),0],
[eps/5,-2*eps/5,-2*eps/3,-2*eps/3],[0,0,eps/4,-eps]])
assert all(sp.simplify(x)==0 for x in J.subs(exact).subs(redstate)-J_expected)
lam=sp.symbols('lam')
char=sp.expand(J_expected.charpoly(lam).as_expr())
expected=lam**4+(1+5*eps/3)*lam**3 + (sp.Rational(17,10)*eps+sp.Rational(5,6)*eps**2)*lam**2 + (eps/30+sp.Rational(13,15)*eps**2)*lam +eps**2/30
assert sp.expand(char-expected)==0
full_char=sp.factor(F.jacobian([U,M,Z,S,I,R]).subs(exact).subs(state).charpoly(lam).as_expr())
assert sp.factor(full_char-(lam+1)*(lam+eps/4)*expected)==0

# General characteristic/Schur complement identity.
a,c,d,A,h,f,g,t,e = sp.symbols('a c d A h f g t e',positive=True)
B=A+h
Jgeneral=sp.Matrix([[-a,0,d,0],[-c,0,d,0],[e*A,-e*B,-e*f,-e*f],[0,0,e*g,-e*t]])
P=sp.factor(Jgeneral.charpoly(lam).as_expr())
Fnum=sp.factor((lam+e*f)*lam*(lam+a)*(lam+e*t)
              +e**2*f*g*lam*(lam+a)
              +e*d*(h*lam+B*(a-c))*(lam+e*t))
assert sp.factor(P-Fnum)==0
assert sp.factor(P.subs(lam,0)-e**2*d*B*t*(a-c))==0
assert sp.simplify((h*lam+B*(a-c))/(lam*(lam+a))
   -B*(a-c)/(a*lam)-(c*B-a*A)/(a*(lam+a)))==0

# Exact finite-parameter samples, two distinct timescale choices each.
trials=[
 (sp.Rational(3,2),sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1,3),
  sp.Rational(1,4),sp.Rational(1,2),sp.Rational(1,2)),
 (sp.Rational(2),sp.Rational(1),sp.Rational(3,4),sp.Rational(1,2),
  sp.Rational(1,3),sp.Rational(2,3),sp.Rational(3,5)),
 (sp.Rational(4),sp.Rational(1),sp.Rational(4,5),sp.Rational(4,5),
  sp.Rational(1,5),sp.Rational(1,2),sp.Rational(4,5)),
]
# Each tuple contains b1,mu1, b2/b1,K,gamma,mu2,eta.
num_samples=0
for b1v,mu1v,rv,Kv,gv,m2v,etav in trials:
 iv=(1-rv)/Kv
 tv=etav+m2v
 sv=1-iv*(1+gv/tv)
 if sv<=0:continue
 uv=mu1v/b1v;Qv=1-uv
 p=sp.Rational(1)
 mv=(1+Qv-p)/(1+p);zv=(p*(1+Qv)-1)/(1+p)
 betav=(gv+m2v)/sv
 ps={b1:b1v,mu1:mu1v,b2:rv*b1v,K:Kv,
     gamma:gv,mu2:m2v,eta:etav,beta:betav}
 xs={U:uv,M:mv,Z:zv,S:sv,I:iv,R:gv*iv/tv}
 assert all(sp.cancel(x.subs(ps).subs(xs))==0 for x in F)
 for ev in [sp.Rational(1,10),sp.Rational(1,1),sp.Rational(10,1)]:
  mat=J.subs(ps).subs({q:Qv,z:zv,i:iv,r:gv*iv/tv,eps:ev})
  coeff=list(sp.Poly(mat.charpoly(lam).as_expr(),lam).all_coeffs())
  a1,a2,a3,a4=coeff[1:]
  assert all(v>0 for v in coeff)
  assert a1*a2>a3
  assert a1*a2*a3 >a3*a3+a1*a1*a4
  num_samples+=1
print('PASS: exact equilibrium, Jacobian, transfer identity, characteristic polynomial and',num_samples,'rational Hurwitz samples')
