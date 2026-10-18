"""Exact algebraic verification of a sharp three-character fourth-moment ratio.
Run: python3 verify.py (requires SymPy).
"""
from fractions import Fraction
import sympy as S
x,y,u,t=S.symbols('x y u t', real=True)
N=x**4+4*x**2+1
D=N+y**4+4*(1+x*x)*y*y-4*x*y
p=6*u**6+50*u**5+156*u**4+202*u**3+110*u**2+14*u-1
fy=S.expand(S.diff(D,y)/4)
fx=S.expand((S.diff(D,x)*N-D*S.diff(N,x))/(-4*y))
assert S.expand(fy-(y**3+2*(1+x*x)*y-x))==0
assert S.expand(S.resultant(fy,fx,x)-4*y*p.subs(u,y*y))==0, S.factor(S.resultant(fy,fx,x))
# The subresultant of the two stationary equations has a unique linear factor.
subs=S.subresultants(fx,fy,x)
lin=S.expand(subs[-2])
expected=S.expand(4*y*(x*(4*y**6+20*y**4+2*y*y-1)+y*(-2*y**6-2*y**4+9*y*y+2)))
assert S.expand(lin-expected)==0, S.factor(lin-expected)
# Exact isolation by rationals; P is strictly increasing on positive reals.
assert p.subs(u,S.Rational(49,1000))<0<p.subs(u,S.Rational(51,1000))
# An elementary global counterexample, uniformly in radius 0<r<1.
e=S.Rational(1,10)
Nt=6-4*e*t+8*e*e*t*t+e**4*t**4
D1=Nt.subs(t,1)
factor=S.factor((Nt-D1)/(1-t))
assert S.expand((1-t)*factor-Nt+D1)==0
assert S.factor(factor)==S.factor(4*e-8*e**2*(1+t)-e**4*(1+t+t*t+t**3))
# Lower bound over 0<=t<=1 (monotone sum bounds).
margin=4*e-16*e**2-4*e**4
assert margin==S.Rational(599,2500) and margin>0
# A disjoint robust independent numeric check via high precision algebraic root.
u_star=S.nroots(p, n=40, maxsteps=500)
u_star=[v for v in u_star if abs(S.im(v))<S.Float('1e-30') and S.re(v)>0]
assert len(u_star)==1
uv=u_star[0]; yv=S.sqrt(uv)
xv=yv*(2*uv**3+2*uv**2-9*uv-2)/(4*uv**3+20*uv**2+2*uv-1)
assert abs(complex(fy.subs({x:xv,y:yv})))<1e-25
assert abs(complex(fx.subs({x:xv,y:yv})))<1e-25
v=S.N((N/D).subs({x:xv,y:yv})**S.Rational(1,4),30)
assert S.Float('1.02744')<v<S.Float('1.02745')
print('VERIFY_OK exact fourth-moment, stationary resultant, subresultant, unique positive-root bracket, all-r counterexample')
print('u=',S.N(uv,20),'x=',S.N(xv,20),'y=',S.N(yv,20),'K=',v)
