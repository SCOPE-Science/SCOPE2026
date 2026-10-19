"""Reproduce exact polynomial identities for the two-parameter Sprott H equilibrium-index theorem.
Run: python sprott_h_checker.py (requires SymPy). These checks support the accompanying analytic Routh argument.
"""
import sympy as sp

L = sp.Symbol('lambda')
a, b, t = sp.symbols('a b t', positive=True, real=True)
x, y, z = sp.symbols('x y z', real=True)
F = sp.Matrix([-y + z*z, x + a*y, x - b*z])
E = sp.Matrix([-b*b/a, b*b/a**2, -b/a])
assert all(sp.cancel(v)==0 for v in F.subs(dict(zip((x,y,z), E))))
J = F.jacobian((x,y,z)).subs(dict(zip((x,y,z), E)))
P = sp.expand(J.charpoly(L).as_expr())
Q = L**3 + (b-a)*L**2 + (1-a*b+2*b/a)*L-b
assert sp.cancel(P-Q)==0
D = sp.expand((b-a)*(1-a*b+2*b/a)+b)
assert sp.cancel(D.subs(b,a*t)-a*(a*a*t*(1-t)+2*t*t-1))==0
AH2 = (1-2*t*t)/(t*(1-t))
BH2 = sp.factor(t*t*AH2)
assert sp.factor(sp.diff(BH2,t)) == (2*t-1)*(2*t*t-2*t-1)/(t-1)**2
assert BH2.subs(t, sp.Rational(1,2)) == sp.Rational(1,2)
assert sp.simplify((1-a*b+2*b/a).subs(b,a*t).subs(a,sp.sqrt(AH2))-t/(1-t))==0
assert sp.simplify((b-a).subs(b,a*t).subs(a,sp.sqrt(AH2)) + (1-t)*sp.sqrt(AH2))==0

# Floating-root samples are optional corroboration, not an exhaustive proof.
for av,bv in [(1,.5),(.5,1),(.75,.3),(3,.2),(1,1),(2,1),(1,.8)]:
    roots = sp.nroots(Q.subs({a:av,b:bv}))
    index=sum(complex(v).real>1e-9 for v in roots)
    u=bv/av
    predicted=3 if 0<u<2**(-.5) and av*av<(1-2*u*u)/(u*(1-u)) else 1
    assert index==predicted, (av,bv,index,predicted)
print('Exact symbolic identities and seven supplementary spectral examples passed.')
