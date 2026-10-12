#!/usr/bin/env python3
"""Standalone exact symbolic checks for a two-filter SIRM stability theorem."""
import sympy as s

lam, t, A, b, C, D = s.symbols("lam t A b C D", positive=True)
P = s.expand((lam**2 + A*lam + C)*(lam+b)*(1+t*lam)+D)
a4,a3,a2,a1,a0 = (s.expand(P.coeff(lam,j)) for j in (4,3,2,1,0))
assert s.simplify(a4-t) == 0
assert s.simplify(a3-(1+(A+b)*t)) == 0
assert s.simplify(a2-(A+b+(C+A*b)*t)) == 0
assert s.simplify(a1-(C+A*b+C*b*t)) == 0
assert s.simplify(a0-(C*b+D)) == 0

D2 = s.expand(a3*a2-a4*a1)
D3 = s.expand(a3*a2*a1-a4*a1*a1-a3*a3*a0)
assert s.factor(D2-((A+b)+(A+b)**2*t+A*(A*b+C+b*b)*t*t)) == 0
V = A*(A*b+C+b*b)
assert s.factor(D3-(V*(1+b*t)*(1+A*t+C*t*t)-D*(1+(A+b)*t)**2)) == 0
K = V*(1+b*t)*(1+A*t+C*t*t)/(1+(A+b)*t)**2
H = C*b*(A+b)*t**3+3*C*b*t**2+(2*C-A*A-b*b)*t-(A+b)
assert s.factor(s.diff(K,t)/K - H/((1+b*t)*(1+A*t+C*t*t)*(1+(A+b)*t))) == 0

# Reconstruct the complete feedback Jacobian determinant independently.
h,delta,k,ainf = s.symbols('h delta k ainf', positive=True)
J = s.Matrix([[-A,-delta,-k,0], [h,0,0,0], [0,0,-b,ainf], [0,1/t,0,-1/t]])
Pj = s.factor(t*(lam*s.eye(4)-J).det())
assert s.factor(Pj-P.subs({C:delta*h,D:ainf*k*h})) == 0

# Full five-equation positive endemic witness, with exact rational numbers.
mu=s.Rational(1,10)
beta=s.Integer(1)
gamma=s.Rational(99,10)
p0=s.Rational(1,20)
sigma=s.Integer(1)
u0=s.Rational(9,4)
u2=s.Integer(2)
aa=s.Integer(10)
bb=s.Integer(1)
LL=s.Integer(10)
S=s.Integer(10)
I=s.Rational(1,10)
R=s.Rational(899,10)
M=s.Integer(1)
Q=s.Rational(1,10)
v=sigma*(p0+u0*M/(1+u2*M))
vp=sigma*u0/(1+u2*M)**2
assert v == s.Rational(4,5) and vp == s.Rational(1,4)
assert LL-(mu+v+beta*I)*S == 0
assert beta*S*I-(gamma+mu)*I == 0
assert v*S+gamma*I-mu*R == 0
assert aa*Q-bb*M == 0
assert I-Q == 0
R0=beta*LL/((gamma+mu)*(mu+sigma*p0))
assert R0 == s.Rational(20,3)
Aw=mu+v+beta*I
Cw=(gamma+mu)*beta*I
Dw=aa*beta*I*S*vp
assert (Aw,bb,Cw,Dw)==(1,1,1,s.Rational(5,2))
W={A:Aw,b:bb,C:Cw,D:Dw}
poly=s.expand(D3.subs(W))
assert s.factor(poly-(6*t**3-8*t**2-8*t+1)/2) == 0
assert poly.subs(t,0) == s.Rational(1,2)
assert poly.subs(t,1) == -s.Rational(9,2)
assert poly.subs(t,3) == s.Rational(67,2)
lo1=s.Rational(11326,100000)
hi1=s.Rational(11327,100000)
lo2=s.Rational(196785,100000)
hi2=s.Rational(196786,100000)
assert poly.subs(t,lo1)>0 and poly.subs(t,hi1)<0
assert poly.subs(t,lo2)<0 and poly.subs(t,hi2)>0

# Reproduce the full endemic spectrum polynomial at tau=1 and tau=3.
Sg,Ig,Mg,Qg=s.symbols('Sg Ig Mg Qg')
ve=sigma*(p0+u0*Mg/(1+u2*Mg))
F=[LL-(mu+ve+beta*Ig)*Sg,
   beta*Sg*Ig-(gamma+mu)*Ig,
   aa*Qg-bb*Mg,
   (Ig-Qg)/t]
Jfull=s.Matrix(F).jacobian([Sg,Ig,Mg,Qg]).subs({Sg:S,Ig:I,Mg:M,Qg:Q})
assert s.factor(t*(lam*s.eye(4)-Jfull).det()-P.subs(W)) == 0
print('VERIFY_OK')
