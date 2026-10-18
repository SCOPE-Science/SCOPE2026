"""Symbolic and quadrature checks of a 4D double-cone Fourier profile.
Requires Python 3, SymPy, and mpmath; the accompanying analytical proof is primary.
"""
import sympy as S
import mpmath as mp
u, s, x = S.symbols('u s x', real=True)
I = S.integrate(S.cos(u*x)*(S.sin(s*(1-x))-s*(1-x)*S.cos(s*(1-x))),(x,0,1))
N = (u*u-s*s)*S.sin(s)+2*s*(S.cos(u)-S.cos(s))
formula = s*s*N / (s*s-u*u)**2
branch = I.args[-1][0] if isinstance(I,S.Piecewise) else I
assert S.trigsimp(S.factor(branch-formula)) == 0
assert S.simplify(S.diff(N,s).subs({u:3*S.pi,s:S.pi})) == -8*S.pi**2
assert S.simplify(S.diff(N,u).subs({u:3*S.pi,s:S.pi})) == 0
assert S.simplify(S.diff(N,u,2).subs({u:3*S.pi,s:S.pi})) == 2*S.pi
assert S.simplify(I.subs({u:S.pi,s:S.pi})) == S.pi/4
assert S.simplify(I.subs({u:3*S.pi,s:S.pi})) == 0
J=S.simplify(S.integrate((1-x)**3*S.cos(u*x),(x,0,1)))
assert S.simplify(J.subs(u,0)) == S.Rational(1,4)
mp.mp.dps=45
f=lambda a,b: mp.quad(lambda z:mp.cos(a*z)*(mp.sin(b*(1-z))-b*(1-z)*mp.cos(b*(1-z))),[0,1])
for b in [mp.mpf('0.05'),mp.mpf('0.6'),mp.mpf('1.5'),mp.mpf('2.5'),mp.pi-mp.mpf('0.05')]:
 for a in [mp.mpf('0'),mp.mpf('0.5'),mp.mpf('2.3'),mp.pi,2*mp.pi,3*mp.pi,5*mp.pi]:
  q=f(a,b)
  assert q > 0,(a,b,q)
  if abs(a*a-b*b)>mp.mpf('0.01'):
   nn=(a*a-b*b)*mp.sin(b)+2*b*(mp.cos(a)-mp.cos(b))
   pred=b*b*nn/(b*b-a*a)**2
   assert abs(q-pred)<mp.mpf('1e-35'),(a,b,q,pred)
assert abs(f(3*mp.pi,mp.pi))<mp.mpf('1e-39')
assert abs(f(mp.pi,mp.pi)-mp.pi/4)<mp.mpf('1e-39')
for alpha in (20,60,100):
 def g(a,b): return (a*a-b*b)*mp.sin(b)+2*b*(mp.cos(a)-mp.cos(b))
 a=mp.mpf('3')*mp.pi-mp.mpf('12')*mp.pi/alpha**2
 b=mp.pi+mp.mpf('18')*mp.pi/alpha**4
 # Use the analytic implicit derivative b'(a)=-N_u/N_s in the constrained stationarity equation.
 Nu=lambda aa,bb:2*aa*mp.sin(bb)-2*bb*mp.sin(aa)
 Ns=lambda aa,bb: (aa*aa-bb*bb)*mp.cos(bb)-2*bb*mp.sin(bb)+2*(mp.cos(aa)-mp.cos(bb))+2*bb*mp.sin(bb)
 aa,bb=mp.findroot((lambda a,b:g(a,b),lambda a,b:a*Ns(a,b)-alpha**2*b*Nu(a,b)),(a,b),tol=mp.mpf('1e-37'))
 kap2=aa*aa+alpha**2*bb*bb
 assert bb>mp.pi and aa<3*mp.pi
 assert kap2 < mp.pi**2*(alpha**2+9)
 assert abs((kap2-mp.pi**2*(alpha**2+9))*alpha**2/mp.pi**2 +36)<mp.mpf('2')
print('PASS: exact integral, pole limits, implicit derivatives, 35 positivity quadratures, 3 asymptotic optimizers')
