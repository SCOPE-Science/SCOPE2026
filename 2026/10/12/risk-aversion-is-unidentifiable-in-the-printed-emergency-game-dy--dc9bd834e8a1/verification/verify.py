#!/usr/bin/env python3
"""Exact payoff-level risk-response checks for a tripartite emergency game."""
import sympy as sp
x, z, lam = sp.symbols('x z lam', real=True)
Fm, Fweak, Cm, Rm = sp.symbols('Fm Fweak Cm Rm', real=True)
# On the y=0 face, truthful and ambiguous information payoffs.
truth = -Cm
strong = Rm - (1-z)*Fm
weak = Rm - (1-z)*Fweak
mean = sp.expand(x*strong + (1-x)*weak)
variance = sp.factor(x*(strong-mean)**2 + (1-x)*(weak-mean)**2)
expect_variance = x*(1-x)*(1-z)**2*(Fm-Fweak)**2
assert sp.simplify(variance-expect_variance) == 0
# Mean-variance utilities and the exact TWO-action replicator identity.
truth_utility = truth
ambig_utility = mean - lam*variance
replicator = z*(1-z)*(truth_utility-ambig_utility)
risk_slope = sp.factor(sp.diff(replicator,lam))
assert sp.simplify(risk_slope-x*(1-x)*z*(1-z)**3*(Fm-Fweak)**2)==0
# Source's Eq. (18) risk term has one fewer complement factor.
source_Eq18_risk = z*lam*(1-x)*x*(1-z)**2*(Fm-Fweak)**2
source_slope = sp.factor(sp.diff(source_Eq18_risk,lam))
# Source's post-simplification Eq. (21) at y=0.
source_Eq21 = z*(-Cm-Rm+(1-z)*(x*Fm+(1-x)*Fweak))
assert sp.simplify(sp.diff(source_Eq21,lam)) == 0
vals={x:sp.Rational(1,2),z:sp.Rational(1,2),
      Fm:sp.Rational(7,2),Fweak:sp.Rational(4,5)}
assert sp.simplify(risk_slope.subs(vals)) == sp.Rational(729,6400)
assert sp.simplify(source_slope.subs(vals)) == sp.Rational(729,3200)
assert sp.simplify(sp.diff(source_Eq21,lam).subs(vals)) == 0
# For different lambda values the published (lambda-free) update maps coincide
# algebraically at each step, whereas the intended payoff equation separates them.
assert sp.simplify((replicator.subs(lam,2)-replicator.subs(lam,0)).subs(vals)) == sp.Rational(729,3200)
print('VERIFY_OK')
