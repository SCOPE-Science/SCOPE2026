#!/usr/bin/env python3
"""Exact checks for the reflection-symmetric quadratic flow theorem."""
import sympy as s
x,y,z,a,t,r,phi=s.symbols('x y z a t r phi',real=True)
F=s.Matrix([x*(1-y),z,-y-a*z+x**2])
L=(z**2+(1-y)**2)/2+(x**2-1)*(1-y)
DL=s.factor(s.Matrix([s.diff(L,v) for v in (x,y,z)]).dot(F))
assert s.expand(DL-(2*x**2*(1-y)**2-a*z**2))==0
for eq in [(0,0,0),(1,1,0),(-1,1,0)]:
 assert [s.simplify(f.subs(dict(zip((x,y,z),eq)))) for f in F]==[0,0,0]
# The harmonic boundary family has constant x and solves the ODE at a=0.
path=s.Matrix([0,r*s.cos(t+phi),-r*s.sin(t+phi)])
res=s.simplify(s.diff(path,t)-F.subs({x:0,y:path[1],z:path[2],a:0}))
assert list(res)==[0,0,0]
# The nonzero equilibrium characteristic polynomial is independent of sign.
lam=s.symbols('lam')
for sig in [-1,1]:
 J=F.jacobian([x,y,z]).subs({x:sig,y:1,z:0})
 assert s.expand(J.charpoly(lam).as_expr()-(lam**3+a*lam**2+lam+2))==0
# Invariant-zero-set branches and the critical mean-balance equation.
assert s.factor(F[2].subs({x:0,z:0})) == -y
assert s.simplify(F[2].subs({y:1,z:0})-(x**2-1)) == 0
assert s.simplify(F[2].subs(a,0)-(x**2-y)) == 0
assert s.simplify(F[0]/x-(1-y))==0
# On the symmetry plane the characteristic equation is lam^2+a*lam+1.
J0=F.jacobian([x,y,z]).subs({x:0,y:0,z:0})
assert s.factor(J0.charpoly(lam).as_expr())==(lam-1)*(lam**2+a*lam+1)
print('PASS: exact Lyapunov identity, invariant-set branches, three equilibria, harmonic family, spectra')
