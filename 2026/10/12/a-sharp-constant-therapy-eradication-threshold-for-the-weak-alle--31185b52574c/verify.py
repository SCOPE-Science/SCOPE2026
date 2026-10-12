#!/usr/bin/env python3
import sympy as sp

x,K,c,r,g = sp.symbols("x K c r g", positive=True)
phi = (1-x/K)*x/(x+c)
dphi = sp.factor(sp.diff(phi,x))
expected = (K*c-x**2-2*c*x)/(K*(x+c)**2)
assert sp.simplify(dphi-expected) == 0

xstar = sp.sqrt(c*(K+c))-c
phistar = sp.simplify(phi.subs(x,xstar))
target = (sp.sqrt(K+c)-sp.sqrt(c))**2/K
assert sp.simplify(phistar-target) == 0

poly = r*x**2-K*(r-g)*x+g*K*c
disc = sp.factor(sp.discriminant(poly,x))
assert sp.simplify(disc-K*(K*(g-r)**2-4*c*g*r)) == 0

# Exact normalized/source-ratio example: K=2, c=1, r=3/25.
vals = {K:sp.Integer(2), c:sp.Integer(1), r:sp.Rational(3,25)}
gc = sp.simplify((r*target).subs(vals))
assert sp.simplify(gc-sp.Rational(3,25)*(2-sp.sqrt(3))) == 0

g_hi = sp.Rational(1,25)
assert sp.simplify(g_hi-gc) > 0
assert g_hi < sp.Rational(3,25)
disc_hi = sp.simplify(disc.subs(vals).subs(g,g_hi))
assert disc_hi < 0

g_lo = sp.Rational(1,50)
assert sp.simplify(gc-g_lo) > 0
roots_lo = [sp.simplify(z) for z in sp.solve(poly.subs(vals).subs(g,g_lo),x)]
expected_roots = [(sp.Integer(5)-sp.sqrt(13))/6,(sp.Integer(5)+sp.sqrt(13))/6]
assert all(sp.simplify(a-b)==0 for a,b in zip(roots_lo,expected_roots))

q = sp.symbols("q", positive=True)
ratio = (sp.sqrt(1+q)-sp.sqrt(q))**2
ratio_alt = 1/(sp.sqrt(1+q)+sp.sqrt(q))**2
assert sp.simplify(ratio-ratio_alt) == 0
assert sp.simplify(ratio.subs(q,sp.Rational(1,2))-(2-sp.sqrt(3))) == 0

print("VERIFY_OK")
print("dphi", dphi)
print("xstar", xstar)
print("phistar", phistar)
print("gc_K2_c1_r3_25", gc)
print("disc_g_1_25", disc_hi)
print("roots_g_1_50", roots_lo)
