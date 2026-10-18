"""Standalone numerical and symbolic diagnostics for the sharp Pianka pooling bound.

The analytic theorem is proved in RESULT.md; finite tests here are not a proof.
Standard Python is sufficient. SymPy is used only if already installed.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import product
from math import sqrt, isfinite
from random import Random

getcontext().prec = 65
one = Decimal(1)
a = Decimal(2) ** (one / Decimal(3))
s = (Decimal(2) - a*a) / (a*a - one)
h = (Decimal(2)*s).sqrt()
K = (one - one/a) * (Decimal(2) - a*a).sqrt()
drop = h / (Decimal(2) + h*h).sqrt() - h / (Decimal(4) + h*h).sqrt()
assert abs(drop - K) < Decimal('1e-55'), (drop, K)
assert Decimal('.13251412') < K < Decimal('.13251414')

def overlap(p, q):
    a = sum(x*y for x, y in zip(p,q))
    b = sum(x*x for x in p)
    c = sum(x*x for x in q)
    return a / sqrt(b*c)

def schoener(p, q):
    ps = sum(p)
    qs = sum(q)
    return sum(min(x/ps,y/qs) for x,y in zip(p,q))

def pool(p):
    return [p[0]+p[1], *p[2:]]

# Finite exact-grid comparison and independent floating normalization check.
num = 0
for p in product(range(4), repeat=3):
    if not any(p):
        continue
    for q in product(range(4), repeat=3):
        if not any(q):
            continue
        decrease = overlap(p,q) - overlap(pool(p), pool(q))
        assert decrease <= float(K) + 2.e-14, (p,q,decrease)
        assert schoener(pool(p),pool(q))+2.e-14 >= schoener(p,q), (p,q)
        num += 1
assert num == (4**3-1)**2
rng = Random(20261016)
random_checks = 0
for dimension in (3,4,6,12):
    for j in range(2500):
        p = [rng.random() if rng.random()<0.85 else 0.0 for _ in range(dimension)]
        q = [rng.random() if rng.random()<0.85 else 0.0 for _ in range(dimension)]
        if not any(p) or not any(q):
            continue
        assert overlap(p,q)-overlap(pool(p),pool(q)) <= float(K)+2.e-13
        assert schoener(pool(p),pool(q))+2.e-13 >= schoener(p,q)
        random_checks+=1

# Converse extreme: disjoint single-category uses become identical after pooling.
assert overlap([1,0,0],[0,1,0]) == 0
assert overlap([1,0],[1,0]) == 1

try:
    import sympy as sp
except ImportError:
    print('SymPy not installed; symbolic diagnostics skipped')
else:
    x = sp.symbols('x', positive=True)
    g = x/sp.sqrt(1+x*x)-x/sp.sqrt(2+x*x)
    gp = (1+x*x)**sp.Rational(-3,2)-2*(2+x*x)**sp.Rational(-3,2)
    assert sp.simplify(sp.diff(g,x)-gp) == 0
    z=2**sp.Rational(2,3)
    station=(2-z)/(z-1)
    assert sp.simplify((2+station)/(1+station)-z) == 0
    assert sp.simplify(g.subs(x,sp.sqrt(station))-(1-2**(-sp.Rational(1,3)))*sp.sqrt(2-z)) == 0
    print('Symbolic derivative, stationary point, and radical maximum verified')
print('Decimal extremal identity verified; K =', K)
print('Grid pairs checked:',num)
print('Deterministic random vectors checked:', random_checks)
print('All finite diagnostic checks passed')
