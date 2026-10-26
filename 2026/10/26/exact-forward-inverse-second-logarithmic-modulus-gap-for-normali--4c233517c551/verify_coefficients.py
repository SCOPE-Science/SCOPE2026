"""Standalone exact checks of the convex logarithmic coefficient formulas.

Run with Python 3 and sympy: python verify_coefficients.py
This code supplements, rather than proves, the analytic extremal argument.
"""
import random
from fractions import Fraction
import sympy as S

z,w,u,v=S.symbols('z w u v')
a2=u
a3=u**2+v/3
f=z+a2*z**2+a3*z**3
p=S.series(1+z*S.diff(f,z,2)/S.diff(f,z),z,0,3).removeO()
p_expected=1+2*u*z+(2*u**2+2*v)*z**2
assert S.simplify(p-p_expected)==0
# Composition of f and its formal inverse through degree three.
inverse=w-a2*w**2+(2*a2**2-a3)*w**3
assert S.expand(f.subs(z,inverse)-w).coeff(w,2)==0
assert S.expand(f.subs(z,inverse)-w).coeff(w,3)==0
gamma2=S.expand(a3/2-a2**2/4)
Gamma2=S.expand(3*a2**2/4-a3/2)
assert S.simplify(gamma2-(u**2/4+v/6))==0
assert S.simplify(Gamma2-(u**2/4-v/6))==0
assert S.simplify((gamma2+Gamma2)-u**2/2)==0
assert S.simplify((gamma2-Gamma2)-v/3)==0
R=S.Rational(2,5)
for sign in (1,-1):
    U=S.sqrt(R)
    V=sign*S.Rational(3,5)
    vals=[S.simplify(q.subs({u:U,v:V})) for q in (gamma2,Gamma2)]
    assert vals==([S.Rational(1,5),0] if sign==1 else [0,S.Rational(1,5)])
for j in range(0,101):
    r=Fraction(j,100)
    bound=min(r/2,(1-r)/3)
    for sign in (1,-1):
        V=sign*min(Fraction(3,2)*r,1-r)
        A=Fraction(r,4)
        B=V/6
        delta=abs(A+B)-abs(A-B)
        assert delta==sign*bound
rng=random.Random(201626)
for _ in range(500):
    r=rng.random()
    phase=rng.uniform(-3.141592653589793,3.141592653589793)
    mag=rng.random()*(1-r)
    from cmath import exp
    U=(r**0.5)*exp(1j*rng.uniform(-3.141592653589793,3.141592653589793))
    V=mag*exp(1j*phase)
    val=abs(abs(U*U/4+V/6)-abs(U*U/4-V/6))
    assert val<=min(r/2,(1-r)/3)+1e-12
print('VERIFY_OK symbolic_identities=6 exact_signed_conditional_extremizers=202 random_interior_tests=500')
