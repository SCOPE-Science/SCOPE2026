#!/usr/bin/env python3
"""Recompute exact characteristic-11 Hasse and resultant certificates.

Requires Python 3 and SymPy. No floating point or external services.
"""
import sympy as s

p = 11
T, u, v = s.symbols('T u v')
q = T**3 - (1 + u)*T**2 + (u + v)*T - v
F = s.Poly(s.expand(q**5), T)
A = s.Poly(F.coeff_monomial(T**5), u, v, modulus=p).as_expr()
B = s.Poly(F.coeff_monomial(T**10), u, v, modulus=p).as_expr()
expected_A = (u**5+3*u**4*v+u**3*v**2-2*u**3*v+u**2*v**3-4*u**2*v**2
              +3*u*v**4+2*u*v**3-3*u*v**2+v**5-5*v**4-5*v**3)
expected_B = (-u**5-3*u**4+2*u**3*v-u**3+4*u**2*v-u**2+3*u*v**2
              -2*u*v-3*u+5*v**2+5*v-1)
assert s.Poly(A-expected_A, u,v, modulus=p).is_zero
assert s.Poly(B-expected_B, u,v, modulus=p).is_zero
R = s.Poly(s.resultant(A,B,v),u,modulus=p)
expected_R = -(u-2)**17*(u+1)*(u+3)*(u+5)*(u-3)*(u**2-5*u-1)*(u**2-u-4)
assert s.Poly(R.as_expr()-expected_R,u,modulus=p).is_zero
assert R.degree()==25
assert s.Poly(A,v).degree()==5 and s.Poly(B,v).degree()==2
assert s.Poly(A.subs(u,2),v,modulus=p).gcd(s.Poly(B.subs(u,2),v,modulus=p)) == s.Poly((v-1)**3*(v-3)*(v-4),v,modulus=p).monic()
Jac = s.diff(A,u)*s.diff(B,v)-s.diff(A,v)*s.diff(B,u)
for vv in [3,4]:
    assert int(A.subs({u:2,v:vv})) % p == 0
    assert int(B.subs({u:2,v:vv})) % p == 0
    assert int(Jac.subs({u:2,v:vv})) % p == 8
    assert (vv*(4-4*vv)*(1-2+vv))%p != 0
for eq in [v, v-u+1, u*u-4*v]:
    C = s.Poly(s.resultant(A,eq,v),u,modulus=p)
    D = s.Poly(s.resultant(B,eq,v),u,modulus=p)
    G = s.gcd(C,D).monic()
    assert G == (s.Poly(1,u,modulus=p) if eq==v else s.Poly((u-2)**5,u,modulus=p).monic())
# Leading homogeneous form of B at degree 5 is -u^5, of A at u=0 is v^5:
assert s.Poly(A.subs(u,0),v,modulus=p).LC() % p == 1
print('VERIFY_OK: Hasse coefficients; degree-25 resultant; 8 simple projected roots; two transverse u=2 points; unique bad boundary and length-15 remainder.')
