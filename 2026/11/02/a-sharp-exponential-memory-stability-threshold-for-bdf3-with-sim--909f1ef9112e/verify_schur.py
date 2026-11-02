#!/usr/bin/env python3
"""Exact symbolic positivity certificate for an exponential-memory BDF3 tail.

Requires Python 3 and SymPy; NumPy is optional for supplementary eigenvalue tests.
Every parameter-domain assertion in the polynomial proof is exact over Q.
"""
import sympy as S

q, mu, v, z, h, X, Y = S.symbols('q mu v z h X Y', real=True)
B = 23 - 16*q + 5*q*q
k = 12*mu*(1-q)*v/(q*B)  # k = mu * beta * theta
D = 11+6*mu
P = S.factor(D*z**4-(18+D*q+S.Rational(23,2)*k*q)*z**3
             +(9+18*q+8*k*q*q)*z**2
             -(2+9*q+S.Rational(5,2)*k*q**3)*z+2*q)
P_at_one = S.factor(P.subs(z,1))
assert S.simplify(P_at_one-6*mu*(1-q)*(1-v)) == 0
H = S.cancel((1-h)**4*P.subs(z,(1+h)/(1-h)))
C = [S.factor(S.Poly(H,h).coeff_monomial(h**i)*B) for i in range(5)]
assert all(S.simplify(C[i].subs(v,0)) != 0 for i in range(5))
D2 = S.factor(C[3]*C[2]-C[4]*C[1])
D3 = S.factor(C[3]*C[2]*C[1]-C[4]*C[1]**2-C[3]**2*C[0])
checks = C+[D2,D3]
for j,F in enumerate(checks):
    transformed = S.together(F.subs({q:X/(1+X),v:Y/(1+Y)}))
    numerator, denominator = transformed.as_numer_denom()
    # Denominator: powers of 1+X and 1+Y, positive in the domain.
    denominator = S.factor(denominator)
    assert not denominator.has(mu)
    # The rational substitution gives only positive powers of 1+X, 1+Y.
    factorization = S.factor_list(denominator)
    assert factorization[0] > 0
    for factor, exponent in factorization[1]:
        assert exponent > 0 and (S.simplify(factor-(1+X)) == 0 or
                                 S.simplify(factor-(1+Y)) == 0), (j,factor)
    pol = S.Poly(S.expand(numerator),X,Y,mu,domain='QQ')
    coeffs=pol.coeffs()
    assert coeffs and all(c>=0 for c in coeffs)
    # Strict positivity at X,Y,mu >0 follows from at least one positive monomial.
    assert any(c>0 for c in coeffs)
    print(f'certificate {j}: {len(coeffs)} nonnegative rational monomial coefficients; '
          f'min={min(coeffs)}, maxdeg={pol.total_degree()}')
# At the exact threshold v=1, H_0 vanishes and the remaining cubic is
# strictly Hurwitz: C_1,C_2,C_3,C_4 and C_3*C_2-C_4*C_1 stay positive.
assert S.simplify(C[0].subs(v,1)) == 0
for j in (1,2,3,4,5):
    expr = checks[j].subs(v,1)
    num, den = S.together(expr.subs(q,X/(1+X))).as_numer_denom()
    assert S.factor(den).is_positive is not False
    fac = S.factor_list(S.factor(den))
    assert fac[0]>0
    assert all(fac1==X+1 and exp>0 for fac1,exp in fac[1])
    coefs=S.Poly(S.expand(num),X,mu,domain='QQ').coeffs()
    assert coefs and all(c>=0 for c in coefs) and any(c>0 for c in coefs)
print('PASS: five exact positive-coefficient boundary certificates, simple unit root and Hurwitz cubic')
# Algebraic identities for exponential kernel's stationary quadrature.
W = q*B/(12*(1-q))
assert S.simplify(W-(S.Rational(23,12)*q+S.Rational(7,12)*q**2+q**3/(1-q)))==0
# q=1/4 gives the explicit stable-but-continuously-unstable parameter witness.
assert S.simplify(W.subs(q,S.Rational(1,4))-S.Rational(103,192))==0
# The exact discrete growth multiplier polynomial has Schur spectral radius < 1
# when v<1, equals 1 at v=1, and has a real root >1 when v>1.
# Boundary root is simple: C_1(v=1)>0 by certificate 1.
assert S.simplify(S.diff(P,z).subs(z,1).subs(v,1)) != 0
print('PASS: exact quartic characteristic identity, seven strict Hurwitz positivity certificates, and witness quadrature identity')
try:
 import numpy as np
 for Q,U,V in [(0.25,1.0,0.80),(0.5,0.1,0.5),(0.8,10.0,0.98),(0.25,1.0,1.05)]:
  f=S.Poly(P.subs({q:Q,mu:U,v:V}),z)
  roots=np.roots([float(c) for c in f.all_coeffs()])
  assert (max(abs(roots))<1) if V<1 else (max(abs(roots))>1)
 print('PASS: four independent floating-point spectral sanity checks (supplementary only)')
except ImportError:
 print('NumPy absent; optional floating-point spectral sanity checks skipped')
