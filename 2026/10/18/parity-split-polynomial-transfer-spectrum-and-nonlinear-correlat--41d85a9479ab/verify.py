"""Exact symbolic reproduction of the polynomial transfer calculation.
Requires Python 3 and SymPy. Run: python verify.py
"""
import sympy as s

z,d=s.symbols('z d', real=True)
a=s.Rational(1,2)-d
u=lambda t:t-s.Rational(1,2)
g=lambda t:u(t)**2-s.Rational(1,12)
lam=s.expand(2*(d**3+a**3))
beta=s.expand(2*(-d**2+d**3-a**3))

def P(f):
    return s.expand(d*(f.subs(z,d*z)+f.subs(z,1-d*z))+
                    a*(f.subs(z,d+a*z)+f.subs(z,1-d-a*z)))

assert s.simplify(P(s.Integer(1))-1)==0
assert s.simplify(P(u(z)))==0
assert s.simplify(P(g(z))-lam*g(z)-beta*u(z))==0
assert s.simplify(lam-3*(d-s.Rational(1,4))**2-s.Rational(1,16))==0
assert s.integrate(g(z),(z,0,1))==0
assert s.integrate(g(z)**2,(z,0,1))==s.Rational(1,180)
for j in range(1,8):
    odd=u(z)**(2*j-1)
    even=u(z)**(2*j)
    assert s.simplify(P(odd))==0
    poly=s.Poly(P(even),z)
    assert s.simplify(poly.coeff_monomial(z**(2*j))-2*(d**(2*j+1)+a**(2*j+1)))==0

for dv in [s.Rational(1,11),s.Rational(13,100),s.Rational(1,5),s.Rational(1,4),s.Rational(27,100),s.Rational(3,8),s.Rational(7,16)]:
    al=s.Rational(1,2)-dv
    ll=2*(dv**3+al**3)
    pp=g(z)
    for n in range(14):
        # Expected stationary covariance via exact integral of the nth PF iterate.
        cov=s.integrate(s.expand(g(z)*pp),(z,0,1))
        assert s.simplify(cov-ll**n/s.Integer(180))==0, (dv,n,cov)
        pp=s.expand(P(pp).subs(d,dv))

q=s.expand(s.Rational(1,2)+s.Rational(1,2)*(2*z-1)**3)
rho=3*(2*z-1)**2
h=(2*z-1)**6-s.Rational(1,3)
assert q.subs(z,0)==0 and q.subs(z,1)==1
assert s.simplify(s.diff(q,z)-rho)==0
assert s.integrate(rho,(z,0,1))==1
assert s.integrate(h*rho,(z,0,1))==0
assert s.integrate(h*h*rho,(z,0,1))==s.Rational(4,45)
assert s.expand(h-4*g(q))==0
assert lam.subs(d,s.Rational(27,100))==s.Rational(637,10000)
assert lam.subs(d,s.Rational(13,100))==s.Rational(1057,10000)
print('PASS: transfer identities, parity spectrum through degree 14,')
print('7 rational parameter x 14 exact-lag covariance cases, conjugate density and moments.')
