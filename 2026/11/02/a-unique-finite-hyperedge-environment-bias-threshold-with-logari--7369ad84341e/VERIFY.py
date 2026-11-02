"""Standalone reproducibility checks for the frozen-composition game-transition theorem.

Requires Python 3 and SymPy.  These finite checks supplement the analytic proof.
"""
from fractions import Fraction
from math import comb, log
import sympy as S

x, b = S.symbols('x b', real=True, positive=True)
den = 1 - x + x**b
h = x**b / den
N = (b*(b - 1)*(1 - x)**2 + 2*x*(b - (b - 1)*x)
     - b*(b + 1 - (b - 1)*x)*x**b)
Np = (2*(b - 2)*((b - 1)*x - b)
      - b*(b + 1)*x**(b - 1)*(b - (b - 1)*x))
assert S.simplify(S.diff(h, x, 2) - x**(b - 2)*N/den**3) == 0
assert S.simplify(S.diff(N, x) - Np) == 0
assert S.simplify(N.subs(x, 0) - b*(b-1)) == 0
assert S.simplify(N.subs(x, 1) + 2*(b-1)) == 0

p = S.symbols('p')
h2 = p**2/(1-p+p**2)
bias_formulas = {
  2: p*(p-1)*(p**2+2*p-2)/(3*(p**2-p+1)),
  3: -p*(p-3)*(p-1)*(2*p**2-1)/(7*(p**2-p+1)),
}
for g, expected in bias_formulas.items():
    B = sum(S.binomial(g,k)*p**k*(1-p)**(g-k) *
            S.Rational(k*k, g*g-g*k+k*k) if k else S.Integer(0)
            for k in range(g+1))
    assert S.factor(B - h2 - expected) == 0

for beta in (2, 3, 4, 5, 6):
    f = lambda u: Fraction(u.numerator**beta, (u.numerator**beta +
        (u.denominator-u.numerator)*u.denominator**(beta-1)))
    # f(u) = u^beta/(1-u+u^beta), with u in lowest-term fractions.
    for q in (Fraction(1, 5), Fraction(1, 2), Fraction(19, 20)):
        for g in (2, 3, 4, 7):
            B = sum(Fraction(comb(g,k),1)*q**k*(1-q)**(g-k)*f(Fraction(k,g))
                    for k in range(g+1))
            assert Fraction(0) <= B <= Fraction(1)
            assert f(q) >= 0
            # Fully independent direct two-state stationary balance at each K/g.
            for k in range(g+1):
                c=Fraction(k,g)
                pi=f(c)
                assert pi*(1-c) == (1-pi)*c**beta

# Explicit numerical bracketing checks of asymptotic critical-point localization.
for beta in (2, 3, 4, 10, 100, 1000, 10000):
    def n_val(q):
        return (beta*(beta-1)*(1-q)**2
                +2*q*(beta-(beta-1)*q)
                -beta*(beta+1-(beta-1)*q)*q**beta)
    lo, hi = 0.00000001, 0.999999999
    for _ in range(90):
        mid = (lo + hi)/2
        if n_val(mid) > 0:
            lo = mid
        else:
            hi = mid
    r = (lo + hi)/2
    assert n_val(r-1e-5)>0 and n_val(r+1e-5)<0
    assert 0 < r < 1
    if beta >= 100:
        gap=beta*(1-r)-(log(beta)-log(log(beta)))
        assert -0.5 < gap < 0.5
print('PASS: symbolic identities, exact rational fixed-size cases, balance equations, and critical-point brackets')
