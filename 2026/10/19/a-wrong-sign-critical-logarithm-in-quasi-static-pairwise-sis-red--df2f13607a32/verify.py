#!/usr/bin/env python3
"""Exact symbolic checks for a critical pairwise-SIS asymptotic theorem.

The infinite-time argument is given in RESULT.md; these algebraic
checks validate its critical coefficients without using simulations.
"""
import sympy as sp

n, x, p, gamma = sp.symbols('n x p gamma', positive=True)
b = sp.symbols('b', real=True)
tau = gamma / (n - 1)
p0 = (n - 1) / n
F = x * (tau * n * p - gamma)
G = gamma * (1 - p) + tau * (n - 2) * p - tau * n * p**2 - 2 * tau * (n - 1) * p**2 * x / (1 - x)

def zero(v):
    assert sp.cancel(v) == 0, sp.factor(v)

kappa = (2 * n - 1) / (n - 1)
a = -2 * (n - 1)**3 / (n**2 * (2*n - 1))
A = 2 * (n - 1)**2 / (n * (2*n - 1))
bh = -2 * (n - 1)**3 * (4*n - 3) / (n**2 * (2*n - 1)**3)
bq = 2 * (n - 1)**3 * (2*n**3 - 10*n**2 + 9*n - 2) / (n**3 * (2*n - 1)**3)
Ch = -2 * (n - 1)**2 * (4*n - 3) / (n * (2*n - 1)**3)
Cq = 2 * (n - 1)**2 * (2*n**3 - 10*n**2 + 9*n - 2) / (n**2 * (2*n - 1)**3)
Lh = (4*n - 3) / (2*n - 1)**2
Lq = -(2*n**3 - 10*n**2 + 9*n - 2) / (n * (2*n - 1)**2)

def coeff(formula, k):
    return sp.expand(sp.series(formula, x, 0, k+1).removeO()).coeff(x, k)

zero(G.subs({x: 0, p: p0}))
zero(sp.diff(G, p).subs({x: 0, p: p0}) + gamma*kappa)
zero(sp.diff(G, x).subs({x: 0, p: p0}) + 2*gamma*(n-1)**2/n**2)
for bb, is_center in [(bq, False), (bh, True)]:
    graph = p0 + a*x + bb*x*x
    f = F.subs(p, graph)
    g = G.subs(p, graph)
    zero(coeff(g, 1))
    zero(coeff(f, 2) + gamma*A)
    zero(coeff(g - (sp.diff(graph, x)*f if is_center else 0), 2))
    zero(coeff(f, 3) - gamma*(Ch if is_center else Cq))
zero(bq - bh - 4*(n-1)**6/(n**3*(2*n-1)**3))
zero(-Ch/A - Lh)
zero(-Cq/A - Lq)
zero(Lh - Lq - 2*(n-1)**3/(n*(2*n-1)**2))
assert [sp.simplify(z.subs(n, 3)) for z in (A, Lh, Lq, Lh-Lq)] == [sp.Rational(8,15),sp.Rational(9,25),sp.Rational(11,75),sp.Rational(16,75)]
assert [sp.simplify(z.subs(n, 4)) for z in (Lh, Lq, Lh-Lq)] == [sp.Rational(13,49),-sp.Rational(1,98),sp.Rational(27,98)]
poly = 2*n**3 - 10*n**2 + 9*n - 2
assert poly.subs(n, 3) == -11 and poly.subs(n, 4) == 2
# Since derivative 6*n**2-20*n+9 is increasing for n>=4 and is positive at 4,
# the sign of the quasi-static log coefficient is negative for all integer n>=4.
assert sp.diff(poly, n).subs(n, 4) > 0
assert sp.diff(poly, n, 2).subs(n, 4) > 0
print('PASS: exact critical pairwise-SIS coefficient identities and degree-3/4 boundaries')
