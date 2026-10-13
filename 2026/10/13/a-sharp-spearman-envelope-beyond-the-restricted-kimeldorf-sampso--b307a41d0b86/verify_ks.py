"""Exact identities and finite diagnostic for a two-term polynomial copula."""
import sympy as sp
import numpy as np

u, v, a, b = sp.symbols('u v a b', real=True)
C = u*v*(1 + a*(1-u)*(1-v) + b*(1-u*u)*(1-v*v))
c = 1 + a*(1-2*u)*(1-2*v) + b*(1-3*u*u)*(1-3*v*v)
assert sp.simplify(sp.diff(C,u,v)-c) == 0
assert sp.simplify(C.subs(v,1)-u) == 0
assert sp.simplify(C.subs(u,1)-v) == 0
assert sp.simplify(C.subs(u,0)) == 0
assert sp.simplify(C.subs(v,0)) == 0

rho = sp.simplify(12*sp.integrate(sp.integrate(C-u*v,(u,0,1)),(v,0,1)))
assert sp.simplify(rho-a/sp.Integer(3)-3*b/sp.Integer(4)) == 0

t = (sp.Integer(9)-sp.sqrt(57))/24
beta = 1-sp.sqrt(57)/19
alpha = -3+7*sp.sqrt(57)/19
candidate = sp.simplify(c.subs({a:alpha,b:beta}))
assert sp.simplify(24*t*t-18*t+1) == 0
assert sp.simplify(2*(1-3*t*t)-sp.Rational(9,4)*(1-2*t)) == 0
assert sp.simplify(beta-1/(2-6*t+6*t*t)) == 0
assert sp.simplify(alpha+6*t*beta) == 0
assert 0 < float(t) < 1/(3**0.5)
assert -1 < float(alpha) < 0
assert float(beta)>0
assert sp.simplify(candidate.subs(v,1)-6*beta*(u-t)**2) == 0
assert sp.simplify(candidate.subs({u:1,v:0})-6*beta*t*t) == 0
assert sp.simplify(candidate.subs({u:0,v:0})-(6*sp.sqrt(57)/19-1)) == 0
assert sp.simplify(sp.diff(candidate.subs(v,1),u).subs(u,t)) == 0
assert sp.simplify(rho.subs({a:alpha,b:beta})-(sp.sqrt(57)-3)/12) == 0
assert sp.simplify(1/(3*(1-2*t))-(sp.sqrt(57)-3)/12) == 0

# Discrete diagnostics do not establish continuum nonnegativity.
xx=np.linspace(0.0,1.0,1601)
aa=1-2*xx
bb=1-3*xx*xx
z=1+float(alpha)*np.outer(aa,aa)+float(beta)*np.outer(bb,bb)
assert z.min()>-2e-12, z.min()
assert abs(float(candidate.subs({u:t,v:1})))<1e-12
assert abs(float(candidate.subs({u:1,v:t})))<1e-12

print('VERIFY_OK')
print('rho_star_exact:',(sp.sqrt(57)-3)/12)
print('rho_star_numeric:',sp.N((sp.sqrt(57)-3)/12,18))
print('alpha_star:',sp.N(alpha,18),'beta_star:',sp.N(beta,18))
print('grid_min:',z.min())
