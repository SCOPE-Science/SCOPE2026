"""Exact symbolic checks for a quadratic coefficient-sum extremum.

Usage: python verify.py  (requires sympy)
"""
import sympy as sp

I = sp.I
r = sp.sqrt(3)
zeta = (1 + I*r)/2
eta = sp.conjugate(zeta)
lam = sp.Rational(1,2) - I/(2*r)
assert [sp.simplify(lam*zeta**k + sp.conjugate(lam)*eta**k) for k in range(3)] == [1,1,0]

z = sp.symbols("z")
p = (2+4*z-z**2)/(3*r)
assert sp.simplify(p.subs(z,zeta)-(r+I)/2) == 0
assert sp.simplify(p.subs(z,eta)-(r-I)/2) == 0

t = sp.symbols("t", real=True)
unit = sp.exp(I*t)
q = 2+4*unit-unit**2
modsq = sp.simplify(sp.expand_trig(sp.expand_complex(q*sp.conjugate(q))))
assert sp.trigsimp(modsq - (27-8*(sp.cos(t)-sp.Rational(1,2))**2)) == 0

# Two boundary stationarity constraints: Re(K_plus*c) and Re(K_minus*c).
Kplus = sp.simplify(I*zeta*(2*zeta-1)*sp.conjugate(p.subs(z,zeta)))
Kminus = sp.simplify(I*eta*(2*eta-1)*sp.conjugate(p.subs(z,eta)))
assert sp.simplify(Kplus-(-sp.Rational(3,2)-I*r/2)) == 0
assert sp.simplify(Kminus-(sp.Rational(3,2)-I*r/2)) == 0
u,v=sp.symbols('u v',real=True)
eqs=[sp.expand_complex(sp.re(K*(u+I*v))).expand() for K in (Kplus,Kminus)]
mat=sp.Matrix([[sp.diff(eq,u),sp.diff(eq,v)] for eq in eqs])
assert sp.simplify(mat.det()) != 0
assert sp.solve(eqs,(u,v)) == {u:0,v:0}
assert sp.simplify((sp.Rational(2,1)/r)**2-sp.Rational(4,3)) == 0
print('PASS: exact interpolation, sharp modulus, contacts, and rigidity')
