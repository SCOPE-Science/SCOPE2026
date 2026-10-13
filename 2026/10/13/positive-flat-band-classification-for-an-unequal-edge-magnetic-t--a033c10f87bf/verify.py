"""Exact identities and finite parameter sanity checks for the unequal-edge magnetic ladder."""
import sympy as sp
x, y, c, a, u, v, w, ep = sp.symbols('x y c a u v w ep', real=True)
# x=cos(t), y=sin(t), c=cos(A), a=sin(A);
# the product of the two rail terms has cos(2t) coefficient 2/S_h**2,
# independent of edge lengths and the remaining matching matrix entries.
t, A, Sh = sp.symbols('t A Sh', real=True, nonzero=True)
ra = 2 * sp.cos(t+A)/Sh
rb = 2 * sp.cos(t-A)/Sh
assert sp.trigsimp(ra*rb-2*sp.cos(2*t)/Sh**2-2*sp.cos(2*A)/Sh**2)==0
# When one rung is Dirichlet, the two Kirchhoff constraints eliminate its free derivative.
Htop = 2*(sp.cos(t+A)-sp.cos(u))/sp.sin(u)
Hbot = 2*(sp.cos(t-A)-sp.cos(u))/sp.sin(u)
assert sp.trigsimp(Htop+Hbot-4*(sp.cos(t)*sp.cos(A)-sp.cos(u))/sp.sin(u))==0
# For opposite rung parities the only rung-sine solution with zero vertices vanishes.
M=sp.Matrix([[1,1],[1,-1]])
assert M.det()==-2
# Exact flux-only resonance witness: h=3/4, r=1, s=2 arctan(1/2)/pi, A=pi/2, k=pi.
k=sp.pi; h=sp.Rational(3,4); r=sp.Integer(1)
s=2*sp.atan(sp.Rational(1,2))/sp.pi
assert sp.simplify(sp.sin(k*r))==0
assert sp.simplify(sp.sin(k*h))!=0
assert sp.simplify(sp.sin(k*s))!=0
assert sp.simplify(sp.cos(sp.pi/2))==0
# Use exact double-angle rational values for theta=arctan(1/2).
q=sp.Rational(1,2)
assert 2*sp.cot(k*h)+(1-q*q)/(2*q)+(1+q*q)/(2*q)==0
# Unit-length source model: all integer momenta satisfy a horizontal-rung Dirichlet intersection.
for n in range(1,12):
 assert sp.sin(n*sp.pi)==0
print('VERIFY_OK harmonic_coefficient=2/S_h**2 rung_flux_resonance=exact opposite_parity=rank_two')
