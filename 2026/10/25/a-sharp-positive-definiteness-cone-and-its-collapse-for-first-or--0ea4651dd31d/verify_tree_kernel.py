"""Exact checks for the formulas in the accompanying tree-kernel proof.

Requires Python 3 and SymPy. Finite tests corroborate, but do not prove,
statements about every homogeneous-tree vertex set.
"""
from fractions import Fraction
import sympy as sp

r, s, b, t = sp.symbols("r s b t", positive=True)
q = s**2
F = (1-r**2)/(1-r*t+q*r**2)
g = sp.factor(r*sp.diff(F,r)/F)
assert sp.simplify(sp.diff(g,t)-r*(1-q*r**2)/(1-r*t+q*r**2)**2) == 0
gminus = -2*r*(s+r)/((1+s*r)*(1-r**2))
gplus = 2*r*(s-r)/((1-s*r)*(1-r**2))
assert sp.simplify(g.subs(t,-2*s)-gminus) == 0
assert sp.simplify(g.subs(t,2*s)-gplus) == 0
blower = -(1-s*r)*(1-r**2)/(2*r*(s-r))
bupper = (1+s*r)*(1-r**2)/(2*r*(s+r))
assert sp.simplify(blower.subs(r,1/s)) == 0
assert sp.simplify(bupper.subs(r,1/s)-(q-1)/(q+1)) == 0
assert blower.subs({s:2,r:sp.Rational(1,4)}) == -sp.Rational(15,28)
assert bupper.subs({s:2,r:sp.Rational(1,4)}) == sp.Rational(5,4)

def minor_entry(i,j,Q,R,B):
    alpha=1-R*R-2*B*R*R
    beta=B*(1-R*R)
    return sum(Fraction(1,Q**k)*R**(i+j-2*k)*
               (alpha+beta*(i+j-2*k)) for k in range(min(i,j)+1))

Q=4
R=Fraction(1,2)
B=Fraction(3,5)
alpha=1-R*R-2*B*R*R
beta=B*(1-R*R)
assert alpha == beta == Fraction(9,20)
for i in range(9):
    for j in range(9):
        assert minor_entry(i,j,Q,R,B) == alpha*R**(i+j)*(i+1)*(j+1)

R=Fraction(3,4)
B=Fraction(1,5)
n=6
det=(minor_entry(n,n,Q,R,B)*minor_entry(n+1,n+1,Q,R,B)
     -minor_entry(n,n+1,Q,R,B)**2)
assert det < 0
print("Exact identities, edge thresholds, and direct finite-minor checks: OK")
