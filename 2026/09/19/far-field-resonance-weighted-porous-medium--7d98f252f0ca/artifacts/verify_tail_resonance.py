#!/usr/bin/env python3
"""Symbolic checks for the far-field resonance formulas in RESULT.md.

Requires Python 3.11+ and SymPy 1.14+.
"""
import sympy as sp

m, p, sigma, N = sp.symbols("m p sigma N", positive=True)
c = sp.symbols("c", positive=True)
t = sp.symbols("t", real=True)
F = sp.Function("F")(t)

L = sigma*(m - 1) + 2*(p - 1)
alpha = (sigma + 2)/L
beta = (m - p)/L
r = sigma/(p - 1)
q = L/(p - 1)
h = L/(m - p)
D = m*r*(m*r - N + 2)
C = c**(m - 1)*D

checks = {}
checks["alpha_plus_beta_r"] = sp.simplify(alpha + beta*r - 1/(p - 1))
checks["q_equals_diffusive_power"] = sp.simplify(q - ((m - 1)*r + 2))
checks["h_equals_inverse_beta"] = sp.simplify(h - 1/beta)
checks["one_minus_beta_q"] = sp.factor(1 - beta*q - (2*p - 1 - m)/(p - 1))
checks["rate_difference"] = sp.factor(
    (h - q) - L*(2*p - 1 - m)/((m - p)*(p - 1))
)

# Exact logarithmic-coordinate radial diffusion identity.
g = sp.exp(-m*r*t) * F**m
lhs_rad = sp.diff(g, t, 2) + (N - 2)*sp.diff(g, t)
rhs_rad = sp.exp(-m*r*t) * (
    sp.diff(F**m, t, 2)
    + (N - 2 - 2*m*r)*sp.diff(F**m, t)
    + m*r*(m*r - N + 2)*F**m
)
checks["radial_identity"] = sp.simplify(lhs_rad - rhs_rad)

A = sp.simplify(C/(1 - beta*q))
Klog = sp.simplify(C/beta)
checks["nonresonant_balance"] = sp.simplify((1 - beta*q)*A - C)
checks["resonant_balance"] = sp.simplify(beta*Klog - C)

for name, value in checks.items():
    assert value == 0, (name, value)

# Representative exact parameter checks.
def vals(mv, pv, sv, Nv):
    sub = {m: sp.Rational(mv), p: sp.Rational(pv), sigma: sp.Rational(sv), N: sp.Rational(Nv), c: 1}
    return {
        "q": sp.simplify(q.subs(sub)),
        "h": sp.simplify(h.subs(sub)),
        "D": sp.simplify(D.subs(sub)),
        "one_minus_beta_q": sp.simplify((1-beta*q).subs(sub)),
        "Klog": sp.simplify(Klog.subs(sub)),
    }

forced = vals(sp.Rational(5, 2), 2, 1, 2)
forced["A"] = sp.simplify(A.subs({m: sp.Rational(5,2), p: 2, sigma: 1, N: 2, c: 1}))
resonant = vals(3, 2, 1, 2)
harmonic = vals(3, 2, 1, 5)
homogeneous = vals(4, 2, 1, 2)

assert forced["q"] == sp.Rational(7,2) and forced["h"] == 7
assert forced["D"] == sp.Rational(25,4) and forced["A"] == sp.Rational(25,2)
assert resonant["q"] == resonant["h"] == 4
assert resonant["D"] == 9 and resonant["Klog"] == 36
assert harmonic["D"] == 0 and harmonic["Klog"] == 0
assert homogeneous["h"] < homogeneous["q"]

print("all_symbolic_checks_passed=True")
print("forced_example=", forced)
print("resonant_example=", resonant)
print("harmonic_example=", harmonic)
print("homogeneous_example=", homogeneous)
