"""Exact algebra checks for three-Picard approximate-proximal stability.

Run with Python 3 and SymPy. These finite computations check algebraic
identities and the displayed example; universal signs use the proof in RESULT.md.
"""
from fractions import Fraction
import sympy as sp

r, c, u, t, z = sp.symbols('r c u t z', real=True)
T4 = 8*c**4 - 8*c**2 + 1
G = r**8 - 2*r**4*T4 - r**2 - 2*r*c
H = 16*u**6 - 32*u**5 + 48*u**4 - 104*u**3 + 72*u**2 - 8*u + 3
P = 1-z+z**2-z**3
assert sp.expand((1+z)*P-(1-z**4)) == 0

resultant = sp.resultant(G, sp.diff(G,c), c)
expected = 65536*r**16*(4*r**6+4*r**4+4*r**2+3)**2*H.subs(u,r**2)
assert sp.factor(resultant-expected) == 0

transformed = sp.cancel((1+t)**6*H.subs(u,t/(1+t)))
assert sp.expand(transformed-(-5*t**6+18*t**5+133*t**4+164*t**3+77*t**2+10*t+3)) == 0
assert H.subs(u,sp.Rational(884,1000)) > 0
assert H.subs(u,sp.Rational(885,1000)) < 0

R = sp.Rational(19,20)
C = sp.Rational(2,3)
q = 1 + G.subs({r:R,c:C})/(1+R*R+2*R*C)
assert sp.cancel(q-sp.Rational(1773279907,1728000000)) == 0
assert q > 1

J = sp.Matrix([[0,-1],[1,0]])
a=sp.Rational(2,3)
b=sp.sqrt(5)/3
F=a*sp.eye(2)+b*J
M=sp.eye(2)-R*F+R**2*F**2-R**3*F**3
assert sp.simplify(M.T*M-q*sp.eye(2)) == sp.zeros(2)
assert sp.simplify(F.T*F-sp.eye(2)) == sp.zeros(2)
assert sp.simplify((sp.eye(2)+R*F).det()) > 1

for cc in [sp.Rational(j,10) for j in range(11)]:
    for rr in [sp.Rational(j,100) for j in (1,20,45,75,90)]:
        assert G.subs({r:rr,c:cc}) < 0
print('VERIFY_OK: geometric-series identity, exact tangency resultant, root uniqueness transform, rational expanding witness, and 55 stable grid points')
