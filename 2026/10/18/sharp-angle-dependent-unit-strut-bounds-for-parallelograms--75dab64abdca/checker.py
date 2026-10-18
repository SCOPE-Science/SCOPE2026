"""Reproducible arithmetic and geometric consistency checks for the unit-strut parallelogram theorem.
Run: python checker.py (Python >=3.9, mpmath and sympy installed).
Finite tests supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt
import random
import sympy as S
import mpmath as mp
mp.mp.dps = 70

z = S.symbols('z', real=True)
assert S.expand(z*(5-4*z)-1 - (1-z)*(4*z-1)) == 0
assert S.factor((1-z)*(1-4*z)) == (z-1)*(4*z-1)

# The inclusion conditions are exact polynomial comparisons in rational data.
def algebraic(c, a, b):
    c,a,b = map(F,(c,a,b)); ss = 1-c*c
    if not (c < 1 and a > 0 and b > 0 and a <= 2 and b <= 2):
        return False
    if a < 2*c or b < 2*c:
        return False
    if a*a + 4*ss*b*b < 4 or b*b + 4*ss*a*a < 4:
        return False
    if c == F(1,2) and a == 1 and b == 1:
        return False
    return True

def geometric(c,a,b):
    c,a,b = map(lambda v: mp.mpf(str(v.numerator))/v.denominator if isinstance(v,F) else mp.mpf(str(v)),(c,a,b))
    s = mp.sqrt(1-c*c)
    A = mp.matrix([0,0]); B = mp.matrix([a,0]); C = mp.matrix([a+b*c,b*s]); D = mp.matrix([b*c,b*s])
    vs = [A,B,C,D]
    for i in range(4):
        U,V = vs[i],vs[(i+1)%4]
        e=V-U
        ell=mp.sqrt(e[0]**2+e[1]**2)
        if ell>2+mp.mpf('1e-55'):
            return False
        h=mp.sqrt(max(mp.mpf('0'),1-ell**2/4))
        # For a counterclockwise polygon, the left normal points into the body.
        W=(U+V)/2 + h*mp.matrix([-e[1]/ell,e[0]/ell])
        lam=(W[0]-c*W[1]/s)/a
        mu=W[1]/(b*s)
        tol=mp.mpf('1e-43')
        if not (-tol<=lam<=1+tol and -tol<=mu<=1+tol):
            return False
        if any(mp.norm(W-Z)<tol for Z in vs):
            return False
    return True

CVALS=[F(0),F(3,5),F(4,5),F(5,13),F(12,13)]
vals=[F(v,5) for v in range(1,11)] + [F(1),F(2)]
cnt=0
for c,a,b in product(CVALS, vals, vals):
    got=geometric(c,a,b)
    want=algebraic(c,a,b)
    assert got==want,(c,a,b,got,want)
    cnt+=1
# Exact exceptional cases: algebraic closed inequalities alone would include a forbidden vertex witness.
for c,a,b in [(F(1,2),F(1),F(1)),(F(3,5),F(6,5),F(1)),(F(3,5),F(1),F(6,5)),(F(4,5),F(8,5),F(1))]:
    assert not algebraic(c,a,b)
    assert not geometric(c,a,b)
# Nonvertex sharp rhombi on each open side of the transition.
for c in [F(0),F(3,5),F(4,5)]:
    cc=mp.mpf(c.numerator)/c.denominator
    ell=2/mp.sqrt(5-4*cc*cc) if c<F(1,2) else 2*cc
    assert geometric(c,ell,ell)
# Exact lower bound for all rational feasible pairs, testing many parameter cells.
checked=0
for c,a,b in product(CVALS, vals, vals):
    if not algebraic(c,a,b): continue
    cc=mp.mpf(c.numerator)/c.denominator
    lower=(4/mp.sqrt(5-4*cc*cc) if cc<=mp.mpf('.5') else 4*cc)
    aa=mp.mpf(a.numerator)/a.denominator
    bb=mp.mpf(b.numerator)/b.denominator
    assert aa+bb+mp.mpf('1e-45')>=lower
    checked+=1
print('PASS: symbolic identities; %d exact-predicate vs geometric-witness tests; %d exact feasible lower-bound cells; 4 vertex/boundary cases; 3 sharp valid rhombi.'%(cnt,checked))
