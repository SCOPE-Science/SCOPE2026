#!/usr/bin/env python3
"""Exact coefficient and local-variation checks for the spiral-angle Hankel problem.

Requires SymPy.  All identities are algebraic or exact Taylor coefficients;
finite numerical evaluations below are sanity checks, not the proof.
"""
import sympy as sp

r, phi, beta = sp.symbols('r phi beta', real=True)
I = sp.I
x = -sp.exp(I*phi)
t = sp.cos(beta)*sp.exp(-I*beta)
c1 = 2*r
c2 = 2*(r**2+(1-r**2)*x)
c3 = 2*(r**3 + 2*r*(1-r**2)*x-r*(1-r**2)*x**2)
H = t**2 * (6*c1*c3-4*c2**2+t*c1**2*c2-t**2*c1**4)/144
F = sp.expand_complex(H*sp.conjugate(H))
base = {r:sp.Rational(1,2),phi:0,beta:0}
assert sp.simplify(H.subs(base)) == -sp.Rational(1,8)
expected = {
 (r,r):-sp.Rational(1,9),
 (r,phi):0,
 (r,beta):0,
 (phi,phi):-sp.Rational(3,512),
 (phi,beta):-sp.Rational(5,768),
 (beta,beta):-sp.Rational(29,384),
}
for (a,b),want in expected.items():
    got = sp.simplify(sp.diff(F,a,b).subs(base))
    assert got == want,(a,b,got,want)
phi_prime = sp.simplify(-expected[(phi,beta)]/expected[(phi,phi)])
assert phi_prime == -sp.Rational(10,9)
f2 = sp.simplify((expected[(beta,beta)] - expected[(phi,beta)]**2/expected[(phi,phi)])/2)
assert f2 == -sp.Rational(59,1728)
m2 = sp.simplify(4*f2)
assert m2 == -sp.Rational(59,432)

B=(17*(1+sp.cos(2*beta))+2*sp.cos(beta))/(144*(1+sp.sec(beta)**2))
b2=sp.simplify(sp.diff(B,beta,2).subs(beta,0)/2)
assert b2 == -sp.Rational(53,288)
gap=sp.simplify(m2-b2)
assert gap == sp.Rational(41,864)

# Check the explicit lower-bound family, fixing r=1/2 and
# the phase phi(beta)=(-10/9)*beta. Its squared modulus has
# the same second-order coefficient as the global optimum.
witness=sp.simplify(F.subs({r:sp.Rational(1,2),phi:-sp.Rational(10,9)*beta}))
assert sp.simplify(witness.subs(beta,0)) == sp.Rational(1,64)
assert sp.simplify(sp.diff(witness,beta).subs(beta,0)) == 0
assert sp.simplify(sp.diff(witness,beta,2).subs(beta,0)/2) == -sp.Rational(59,1728)

# Numeric demonstration, not used for the infinite/asymptotic proof.
bs=sp.Rational(1,10)
vm=sp.N(sp.sqrt(witness.subs(beta,bs)),18)
vb=sp.N(B.subs(beta,bs),18)
assert vm>vb
print('zero_angle_extremal_H=-1/8')
print('curvature_rr=-1/9; curvature_phiphi=-3/512')
print('angular_slope=-10/9')
print('sharp_quadratic_term=-59/432')
print('displayed_bound_quadratic_term=-53/288')
print('deficit_gap_quadratic_coefficient=41/864')
print('beta_0.1_witness=',vm)
print('beta_0.1_displayed_bound=',vb)
print('EXACT_CHECKS_PASSED')
