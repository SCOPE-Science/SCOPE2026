"""Independent finite symbolic corroboration of tangent-developable identities.

All calculations are over prime fields. This script checks representative
identities and not the proof for arbitrary degrees.
"""
import sympy as sp
from math import comb

t, s, u, Y, Z = sp.symbols('t s u Y Z')
for p in (2, 3, 5, 7):
    for d in range(3, 12):
        for i in range(2,d+1):
            q = sp.Poly(sp.expand((u-s)**i+i*s*(u-s)**(i-1)),s,u,modulus=p)
            # linear tangent displacement cancels in every characteristic
            linear = q.coeff_monomial(s*u**(i-1))
            assert linear == 0
        assert (sp.Poly(sp.expand((u-s)**2+2*s*(u-s)-u*u+s*s),s,u,modulus=p)).is_zero
        if p!=2:
            assert (sp.Poly(sp.expand((u-s)**3+3*s*(u-s)**2-u**3+3*u*s*s-2*s**3),s,u,modulus=p)).is_zero
# char3 twisted cubic quartic substitution and cubic Jacobian equations
x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3')
F=x0*x0*x3*x3+x1**3*x3+x0*x2**3
v={x0:1,x1:t+s,x2:t*t+2*s*t,x3:t**3+3*s*t*t}
assert sp.Poly(sp.expand(F.subs(v)),t,s,modulus=3).is_zero
j0=2*x0*x3*x3+x2**3
j3=2*x0*x0*x3+x1**3
assert sp.Poly(sp.expand(sp.diff(F,x0)-j0),x0,x1,x2,x3,modulus=3).is_zero
assert sp.Poly(sp.expand(sp.diff(F,x3)-j3),x0,x1,x2,x3,modulus=3).is_zero
assert sp.Poly(sp.diff(F,x1),x0,x1,x2,x3,modulus=3).is_zero
assert sp.Poly(sp.diff(F,x2),x0,x1,x2,x3,modulus=3).is_zero
# compare complete intersection of cubics (3,3) with formula for d=3, p=3
for n in range(8,22):
    from math import comb as C
    hf=C(n+3,3)-2*C(n,3)+C(n-3,3)
    assert hf == 9*n-9
# Hilbert polynomials by filtered associated graded O(-4j)
for d in range(3,12):
    for m in (2,3):
        for n in range(10,20):
            h=sum(d*n-4*j+1 for j in range(m))
            assert h == m*d*n+m-2*m*(m-1)
print('VERIFY_OK: tangent coordinate identities mod 2/3/5/7 for d=3..11; char3 quartic and cubic Jacobian; filtered Hilbert polynomials')
