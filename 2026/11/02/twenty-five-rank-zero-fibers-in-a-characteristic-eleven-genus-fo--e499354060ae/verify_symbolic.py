#!/usr/bin/env python3
"""Exact independent symbolic certificate for a genus-four cyclic trigonal pencil."""
import sympy as S
x, a, z = S.symbols('x a z')
p = 11
f = x**5 + a*x**2 + 1
P = lambda h, v: S.Poly(h, v, modulus=p)
red = lambda h,v: P(h,v).as_expr()
F3, F7 = (S.Poly(S.expand(f**e), x) for e in (3, 7))
coeff = lambda poly, i: red(poly.coeff_monomial(x**i), a)
A = [coeff(F7, k) for k in (10,21,32)]
B = [coeff(F3, k) for k in (10,9,8)]
assert [red(c,a) for c in A] == [red(c,a) for c in (-a**5-1, -3*a**3,-4*a)]
assert [red(c,a) for c in B] == [3,3*a**2,0]
T = red(sum(A[i]*B[i]**p for i in range(3)),a)
assert T == red(2*a**25-3*a**5-3,a)
D = S.discriminant(f,x)
assert red(D,a) == red(-2*(a**5+5),a)
assert P(S.gcd(P(T,a),P(D,a)).as_expr(),a) == P(1,a)
assert S.gcd(P(T,a), P(S.diff(T,a),a)).degree()==0
Q = P(2*z**5-3*z-3,z)
F = P(z**4+2*z**3+4*z**2-3*z-2,z)
assert Q == P(2*(z-2)*F.as_expr(),z)
assert S.gcd(F,P(S.diff(F.as_expr(),z),z)).degree()==0
# Modular exponentiation in F_11[z]/(F) rules out any degree-1 or degree-2 factors.
assert S.gcd(F, P(S.rem(S.Poly(z,z,modulus=p)**121-S.Poly(z,z,modulus=p),F),z)).degree()==0
Frobenius_remainder = S.rem(S.Poly(z,z,modulus=p)**121-S.Poly(z,z,modulus=p),F)
assert Frobenius_remainder == P(-5*z**3+4*z**2+3*z+1,z)
assert P(T-2*(a**5-2)*F.as_expr().subs(z,a**5),a).is_zero
assert S.factor_list(T,modulus=p)[1] == [(a**5-2,1),(a**20+2*a**15+4*a**10-3*a**5-2,1)]
print('SYMBOLIC_CERTIFICATE_OK')
print('Cartier coefficients A=',A,'B=',B)
print('Stable scalar T=',T)
print('Discriminant=',red(D,a))
print('Quartic modular remainder=',Frobenius_remainder)
print('F11 polynomial factors of T=',S.factor_list(T,modulus=p)[1])
