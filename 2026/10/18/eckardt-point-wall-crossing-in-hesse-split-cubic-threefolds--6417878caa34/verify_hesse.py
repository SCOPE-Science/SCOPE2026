"""Exact symbolic checks for the Hesse-split cubic threefold Eckardt-point classification.

Requires Python 3 and SymPy. These identities support the accompanying
mathematical proof; they do not replace its exhaustive rank case split.
"""
import sympy as s

x, y, z, lam, k = s.symbols('x y z lam k')
A = x**3 + y**3 + z**3 + lam*x*y*z
H = s.hessian(A, (x, y, z))
assert s.expand(H.det() + 6*lam**2*A - 8*(lam**3 + 27)*x*y*z) == 0

# The invariant of Bonifant--Milnor's Hesse form x^3+y^3+z^3=3kxyz.
J = (k*(k**3+8)/(4*(k**3-1)))**3
j_lambda = lam**3 * (216-lam**3)**3 / (lam**3+27)**3
assert s.factor(1728*J.subs(k, -lam/3) - j_lambda) == 0

# Algebraic cube roots of unity, represented exactly.
omega = (-1+s.sqrt(-3))/2
roots = [s.Integer(1), omega, s.conjugate(omega)]
for r in roots:
    assert s.simplify(r**3-1) == 0

# All nine inflection points are explicitly on A_lam, of Hessian rank two.
for L in [s.Integer(0), s.Integer(3), s.Integer(6)]:
    for r in roots:
        for q in [(1,-r,0),(1,0,-r),(0,1,-r)]:
            subs = dict(zip((x,y,z),q)); subs[lam]=L
            assert s.simplify(A.subs(subs)) == 0
            assert H.subs(subs).rank() == 2

# Exactly three base rank-one points for each of the two exceptional forms.
for q in [(1,0,0),(0,1,0),(0,0,1)]:
    subs = dict(zip((x,y,z),q)); subs[lam]=0
    assert A.subs(subs)==1 and H.subs(subs).rank()==1
for r in roots:
    q = [1,r,s.expand(r**2)]
    subs=dict(zip((x,y,z),q)); subs[lam]=6
    assert s.simplify(A.subs(subs)-9)==0
    assert H.subs(subs).rank()==1

# For lam=0 the diagonal Hessian has rank one exactly on the 3 axes.
# For lam != 0, rank-one points cannot lie on a coordinate hyperplane:
# two appropriate principal 2-by-2 minors then force the other two coordinates zero.
# These are EXACT off-principal minors enforcing the rank-one equations:
assert s.factor(H.extract([0,1],[0,2]).det() + lam*(lam*y*z-6*x**2)) == 0
assert s.factor(H.extract([0,1],[1,2]).det() - lam*(lam*x*z-6*y**2)) == 0
assert s.factor(H.extract([1,2],[0,2]).det() + lam*(lam*x*y-6*z**2)) == 0
# Multiplying those equations at xyz != 0 gives lam^3=216.
assert s.expand((lam*x*z)*(lam*y*z)*(lam*x*y) -
                (6*y**2)*(6*x**2)*(6*z**2) -
                (lam**3-216)*(x*y*z)**2) == 0

# Smoothness singular parameter: A_(-3) has a singular [1:1:1].
assert A.subs({x:1,y:1,z:1,lam:-3})==0
assert all(s.diff(A,t).subs({x:1,y:1,z:1,lam:-3})==0 for t in (x,y,z))
print('PASS: exact Hessian identity, modular invariant, nine flexes, exceptional rank-one points and smoothness boundary')
