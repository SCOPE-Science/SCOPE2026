#!/usr/bin/env python3
"""Exact witness checks for nonlinear environmental-transmission equilibria.

Requires sympy (tested with sympy 1.13 or later). This program checks
algebraic calculations and a finite exact witness; the all-parameter
asymptotic theorem is proved in RESULT.md, not by numerical experiments.
"""
from fractions import Fraction as F
import sympy as sp

z = sp.symbols('z', positive=True)
alpha = sp.symbols('alpha', positive=True)
h = sp.symbols('h', positive=True)
y = sp.symbols('y', positive=True)
G = z**3/(z**3+1)
D = 2 + z/8 + G
S = 4/(z/4 + 2 + alpha*G - sp.Rational(1,2)/D)
V = S/D
Q = sp.factor(S/4 + V/8 + (alpha*S+V)*G/z - 6)
assert sp.simplify((2-z*0) - 2) == 0

# The underlying six-compartment vector field: all stationarity
# equations except the exposed compartment vanish identically.
E = 3*z
R = z + V/2
C = z
Sdot = 4 - S*z/4 - S + V/2 - alpha*S*G - S
Vdot = S - V*z/8 - 2*V - V*G
Idot = E - 3*z
Rdot = z + V/2 - R
Cdot = z - C
Edot = S*z/4 + V*z/8 - 2*E + alpha*S*G + V*G
for expr in (Sdot,Vdot,Idot,Rdot,Cdot, Edot-z*Q):
    assert sp.cancel(expr) == 0, str(expr)

Q1000 = sp.factor(Q.subs(alpha,1000))
N, Den = sp.fraction(Q1000)
P = sp.Poly(N, z)
assert P.count_roots(0, sp.oo) == 2
assert all(c>0 for c in sp.Poly(Den,z).all_coeffs())
checks = {
    F(1,20): F(-126151613366,3104393127041),
    F(1,10): F(158652899714,17920019921),
    F(1,3): F(6000306,1101019),
    F(1,1): F(-84874,42173),
}
for x, expected in checks.items():
    q = Q1000.subs(z,sp.Rational(x.numerator,x.denominator))
    assert q == sp.Rational(expected.numerator,expected.denominator), (x,q)
assert checks[F(1,20)] < 0 < checks[F(1,10)]
assert checks[F(1,3)] > 0 > checks[F(1,1)]

# Two distinct singular scales: low-infection and high-infection branches.
low_limit = sp.simplify(sp.limit(Q.subs({alpha:h**(-2),z:h*y}),h,0,dir='+'))
assert sp.simplify(low_limit - (sp.Rational(16,7)*y**2-sp.Rational(37,7))) == 0
high_limit = sp.simplify(sp.limit(Q.subs(alpha,h**(-1)),h,0,dir='+'))
assert sp.simplify(high_limit-(4/z-6)) == 0

# The source's reproduction number at the disease-free state.
S0=sp.Rational(16,7); V0=sp.Rational(8,7)
Rc=(S0/4+V0/8)/6
assert Rc == sp.Rational(5,42)
assert sp.simplify((6*(1-Rc)/S0)-sp.Rational(37,16)) == 0

print('PASS: six stationary-field identities, four exact sign values,')
print('two positive roots by exact Sturm count, both singular limits,')
print('disease-free reproduction number and small-root coefficient.')
print('Positive roots (illustration):',sp.nroots(N,maxsteps=150))
