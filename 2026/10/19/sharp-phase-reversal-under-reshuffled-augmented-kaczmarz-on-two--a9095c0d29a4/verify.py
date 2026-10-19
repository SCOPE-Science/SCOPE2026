"""Exact symbolic verification of a phase-resolved covariance identity."""
import sympy as s
p=s.symbols('p',real=True)
q=1-p
M=s.Matrix([[q,-q],[p,q]])
C=s.Matrix([p,-p])
D=s.simplify((M-s.eye(2))*C)
H=(2-p)*(4-3*p)*(5*p*p-8*p+4)
Si=s.Matrix([[2-p,-p],[-p,2*p]])/(4-3*p)
S0=s.Matrix([[p*(8-28*p+32*p*p-11*p**3),-2*p*p*(2*p-1)*(2-p)],[-2*p*p*(2*p-1)*(2-p),4*p*p*(p*p-2*p+2)]])/H
N=M*M
assert s.simplify(Si-M*Si*M.T-C*C.T)==s.zeros(2)
assert s.simplify(S0-N*S0*N.T-D*D.T)==s.zeros(2)
V1=s.factor((M*S0*M.T+C*C.T)[0,0]); V0=s.factor(S0[0,0]); Vi=s.factor(Si[0,0]);
assert s.simplify(V1-p*(8-12*p+4*p*p+p**3)/H)==0
assert s.simplify(Vi-V0-4*(1-p)*(1-(1-p)**2+4*(1-p)**3)/H)==0
assert s.simplify(Vi-V1-4*(1-p)**2*(p*p-6*p+4)/H)==0
assert s.limit(V0/p,p,0)==s.Rational(1,4)
assert s.limit(V1/p,p,0)==s.Rational(1,4)
assert s.limit(Vi,p,0)==s.Rational(1,2)
assert s.factor((s.eye(2)-M).det())==p
for t in [s.Rational(1,100),s.Rational(1,4),s.Rational(3,4),s.Rational(4,5),s.Rational(9,10)]:
  assert H.subs(p,t)>0
  assert (Vi-V0).subs(p,t)>0
  assert (Vi-V1).subs(p,t)>0 if t < 3-s.sqrt(5) else (Vi-V1).subs(p,t)<0
print('PASS exact symbolic covariance, both phase laws, signs, asymptotics')
