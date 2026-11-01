"""Reproducibility checks for right-prism Steiner-root threshold."""
from fractions import Fraction
from math import pi, tan
import random
import sympy as s
import numpy as np

p,q,u,z,delta=s.symbols('p q u z delta',real=True)
r=s.Rational(3,2)*(p-4)
qstar=s.factor(-r*r-2*r)
F=s.Rational(4,3)*z**3+(u+p)*z**2+2*(u+q)*z+q*u
B=z*z+2*z+q
A=s.expand(F-u*B)
assert s.expand(A.subs(q,-z*z-2*z)+s.Rational(2,3)*z*z*(z-r)) == 0
assert s.simplify(F.subs(q,qstar)/(z-r)-(s.Rational(4,3)*z*z+(u-8+3*p)*z+u*(s.Rational(3,2)*p-4)))==0
u_star=s.factor(-s.diff(A,z).subs({q:qstar,z:r})/s.diff(B,z).subs({q:qstar,z:r}))
assert s.factor(F.subs({q:qstar,u:u_star,z:r}))==0
assert s.factor(s.diff(F,z).subs({q:qstar,u:u_star,z:r}))==0
assert s.factor(s.diff(F,z,2).subs({q:qstar,u:u_star,z:r}))!=0
assert s.simplify(s.discriminant(s.div(F.subs(q,qstar),z-r,z)[0],z)-((u-(p-s.Rational(8,3)))**2+s.Rational(8,9)*(3*p-8)**2))==0
D=s.discriminant(F,z)
Dshift=s.Poly(s.factor(D.subs({q:qstar+delta,u:u_star})),delta)
assert Dshift.degree()==3
assert s.factor(Dshift.nth(0))==0
assert s.factor(Dshift.nth(3))==-s.Rational(128,3)
assert s.factor(Dshift.nth(1))==-3*(p-4)**2*(27*p*p-176*p+288)**3/(4*(3*p-10)**4)
Qpoly=1593*p**4-21888*p**3+112768*p*p-258048*p+221184
assert s.factor(Dshift.nth(2))==Qpoly/(3*p-10)**2
# Machine-checkable rational pi bound using Machin's identity and alternating arctan series.
def arctan_bounds(n, m):
    x=Fraction(1,n)
    terms=[(-1)**k*x**(2*k+1)/(2*k+1) for k in range(m+1)]
    t=sum(terms[:-1]); v=t+terms[-1]
    return min(t,v),max(t,v)
aL,aU=arctan_bounds(5,18)
bL,bU=arctan_bounds(239,5)
piL=16*aL-4*bU
piU=16*aU-4*bL
lo=Fraction(3141592,10**6); hi=Fraction(3141593,10**6)
assert lo<piL<piU<hi, (float(piL),float(piU))
assert s.Rational(s.factor(Qpoly.subs(p,s.Rational(3141592,10**6))))<-14
# On p in (3,4), termwise |Q'| <= 2618624 < 3 million.
assert (4*1593*4**3+3*21888*4**2+2*112768*4+258048)<3000000
# Hence Q(pi) < -14+3 < 0, and all coefficients in D(q*+delta,u*) negative.
assert (27*p*p-176*p+288).as_poly(p).discriminant()<0
assert abs(float(qstar.subs(p,s.pi))-0.917279901395842)<1e-12
assert 0<float(u_star.subs(p,s.pi))<1
q0=float(3*s.pi*s.pi/32)
assert float(qstar.subs(p,s.pi))<q0<1
for n in range(3,25):
    qn=pi/(n*tan(pi/n))
    if n<=6: assert qn<float(qstar.subs(p,s.pi))
    else: assert qn>float(qstar.subs(p,s.pi))

# Exact rational separation of the regular hexagon and heptagon from q*.
def sin_bounds(x):
    y=sum(((-1)**k*x**(2*k+1)/s.factorial(2*k+1) for k in range(4)),Fraction(0))
    return y,y+x**9/Fraction(362880)
def cos_bounds(x):
    y=sum(((-1)**k*x**(2*k)/s.factorial(2*k) for k in range(4)),Fraction(0))
    return y,y+x**8/Fraction(40320)
def quotient_bounds(n):
    xl=piL/n; xh=piU/n
    sl,_=sin_bounds(xl); _,su=sin_bounds(xh)
    _,cu=cos_bounds(xl); cl,_=cos_bounds(xh)
    tlo=sl/cu; thi=su/cl
    return piL/(n*thi),piU/(n*tlo)
ql6,qu6=quotient_bounds(6)
ql7,qu7=quotient_bounds(7)
qs_of=lambda x: -24+15*x-Fraction(9,4)*x*x
assert qu6<qs_of(piL)<qs_of(piU)<ql7

rng=random.Random(32577)
qcut=float(qstar.subs(p,s.pi))
witness=float(u_star.subs(p,s.pi))
for qv in [0.0001,0.01,0.1,0.5,0.8,0.905,0.90689968,qcut-1e-10]:
    for uv in [0.001,0.1,witness,1,2,10,100]:
        roots=np.roots([4/3,uv+pi,2*(uv+qv),qv*uv])
        assert max(abs(x.imag) for x in roots)<1e-7,(qv,uv,roots)
        assert max(x.real for x in roots)<0
for qv in [qcut+1e-8,0.92,0.925,0.93,0.95,0.99,1]:
    roots=np.roots([4/3,witness+pi,2*(witness+qv),qv*witness])
    assert max(abs(x.imag) for x in roots)>1e-5,(qv,roots)
for _ in range(1000):
    qv=qcut*rng.random()
    uv=10**rng.uniform(-3,4)
    roots=np.roots([4/3,uv+pi,2*(uv+qv),qv*uv])
    assert max(abs(x.imag) for x in roots)<0.0001,(qv,uv,roots)
print('PASS symbolic factorization / discriminant / rational pi certificate / regular polygon threshold / 1063 root tests')
print('q*=',float(qstar.subs(p,s.pi)),'u*=',witness,'q0=',q0)
