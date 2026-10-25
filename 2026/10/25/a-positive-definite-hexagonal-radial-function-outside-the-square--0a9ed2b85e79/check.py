"""Exact symbolic identities and supplementary numerical tests for the hexagonal radial example."""
from fractions import Fraction
import cmath
import sympy as s

x, y, z, Q, p = s.symbols('x y z Q p', real=True)
b = s.Rational(13, 20)
c = s.Rational(1, 6)
qxy = x*x-x*y+y*y
pxy = x*x*y*y*(x-y)**2
D = z*z*(z*z+Q)**2+p
N = 2*z*z*(Q+3*z*z)
f = N/D
rays = [(1,0),(1,-1),(0,-1),(-1,0),(-1,1),(0,1)]
proj = [a*x+d*y for a,d in rays]
cones = sum(1/((z+s.I*proj[j])*(z+s.I*proj[(j+1)%6])) for j in range(6))
assert s.cancel(cones - f.subs({Q:qxy,p:pxy})) == 0
assert s.expand(4*qxy**3-27*pxy-(x+y)**2*(2*x-y)**2*(x-2*y)**2) == 0

g = f-b*s.diff(f,z)+c*s.diff(f,z,2)
P = (30*Q**5+181*Q**4-9*Q**3*p+420*Q**3-201*Q**2*p+714*Q**2
     +Q*p**2-859*Q*p+742*Q+36*p**2-747*p+297)/15
assert s.cancel(g.subs(z,1) - P/D.subs(z,1)**3)==0
assert s.simplify(P.subs(p,4*Q**3/27) - (Q+3)**3*(16*Q**4-540*Q**3+4590*Q**2+12015*Q+8019)/10935)==0
H=39*Q**4+1192*Q**3-35622*Q**2-92424*Q-57249
assert s.simplify(s.discriminant(P,p)+(Q+3)**2*H/225)==0
u=s.symbols('u')
assert s.expand(H.subs(Q,u+21)) == (39*u**4+4468*u**3+142668*u**2+1433184*u+916416)
assert s.discriminant(16*Q**2-540*Q+4590,Q)==-2160
T=s.symbols('T',real=True)
square=8*z*z/(z*z+T)**2
square_new=s.factor((square-b*s.diff(square,z)+c*s.diff(square,z,2)).subs(z,1))
assert s.cancel(square_new - 4*(T-11)*(T-9)/(15*(T+1)**4))==0
assert s.factor(square_new.subs(T,10))==-s.Rational(4,219615)
# Direct (non-symbolic) evaluation of the six cone integrals versus the rational formula.
for xv,yv in [(0,0),(1.2,-0.7),(-3.1,2.0),(7.5,1.25)]:
    lam=1+0j
    direct=sum(1/((lam+1j*(a*xv+d*yv))*(lam+1j*(aa*xv+dd*yv)))
               for (a,d),(aa,dd) in zip(rays, rays[1:]+rays[:1]))
    qq=xv*xv-xv*yv+yv*yv
    pp=xv*xv*yv*yv*(xv-yv)**2
    rational=2*lam*lam*(qq+3*lam*lam)/(lam*lam*(lam*lam+qq)**2+pp)
    assert abs(direct-rational)<1e-10
print('PASS: cone identity, hexagonal invariant, rational Fourier numerator, global-positivity certificate, and square negative band')
