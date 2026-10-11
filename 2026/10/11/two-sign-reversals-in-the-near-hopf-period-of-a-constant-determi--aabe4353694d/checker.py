"""Symbolic checks for the constant-determinant Selkov Hopf expansion.

Requires sympy. Run: python checker.py
"""
import sympy as s

K, mu = s.symbols('K mu', positive=True, real=True)
a = K*(1-K-mu)/2
b = s.sqrt(K*(1+K+mu)/2)
x, y, q, v = s.symbols('x y q v', real=True)
fx = -x+a*y+x*x*y
fy = b-a*y-x*x*y
assert s.simplify((fx+fy)-(b-x)) == 0
A = s.Matrix([fx,fy]).jacobian([x,y]).subs({x:b,y:b/K})
assert s.simplify(A.det()-K)==0
assert s.simplify(s.trace(A)-mu)==0
# The exact coordinate map: q=x+y-b-b/K, v=b-x.
d = 2*b-b/K
osc = s.expand((-fx).subs({x:b-v,y:b/K+q+v}, simultaneous=True))
target = -K*q+mu*v+2*b*q*v+d*v**2-q*v**2-v**3
assert s.simplify(osc-target)==0

w, B, D, t = s.symbols('w B D t',real=True, nonzero=True)
Q1=s.cos(t)
Q2=D/s.Integer(2)+D/s.Integer(6)*s.cos(2*t)+B/(3*w)*s.sin(2*t)
R=2*B*w*(Q1*s.diff(Q2,t)+Q2*s.diff(Q1,t))+2*D*w**2*s.diff(Q1,t)*s.diff(Q2,t)-w**2*Q1*s.diff(Q1,t)**2-w**3*s.diff(Q1,t)**3
# Fourier projections at the resonant fundamental.
C=s.simplify(s.integrate(s.expand_trig(s.expand(R))*s.cos(t),(t,0,2*s.pi))/s.pi)
S=s.simplify(s.integrate(s.expand_trig(s.expand(R))*s.sin(t),(t,0,2*s.pi))/s.pi)
assert s.simplify(C-(4*B**2+4*D**2*w**2-3*w**2)/12)==0
assert s.simplify(S+w*(2*B*D-3*w**2)/4)==0

b0=s.sqrt(K*(1+K)/2)
d0=b0*(2*K-1)/K
omega=s.sqrt(K)
mu2=s.simplify((S/w).subs({w:omega,B:b0,D:d0}, simultaneous=True))
nu2=s.simplify((-C/(2*w)).subs({w:omega,B:b0,D:d0}, simultaneous=True))
assert s.simplify(mu2-(1+2*K-2*K**2)/4)==0
assert s.simplify(nu2+(2*K-1)*(4*K**2+3*K-2)/(24*omega))==0
period_slope=s.factor(-nu2/(omega*mu2))
assert s.simplify(period_slope-(2*K-1)*(4*K**2+3*K-2)/(6*K*(1+2*K-2*K**2)))==0
kstar=(s.sqrt(41)-3)/8
assert 0<float(kstar)<0.5
assert s.simplify((4*K**2+3*K-2).subs(K,kstar))==0
for kv,expected in [(s.Rational(3,10),1),(s.Rational(46,100),-1),(s.Rational(55,100),1)]:
 assert s.sign(period_slope.subs(K,kv))==expected
print('VERIFY_OK')
