"""Exact finite-path verification for a centered iid-site nearest-neighbor walk.

Run: python verify.py
Requires sympy >= 1.12. No network or external data is used.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb
import sympy as sp

moments = sp.symbols('M0:8')
half = sp.Rational(1, 2)

def symbolic_moment(r, l):
    return sum((-1)**j * comb(l, j) * moments[r+j] for j in range(l+1))

def symbolic_displacement(n):
    by_destination = defaultdict(lambda: sp.Integer(0))
    for bits in product((0, 1), repeat=n):
        location, departures = 0, {}
        for right in bits:
            r, l = departures.get(location, (0, 0))
            departures[location] = (r+right, l+1-right)
            location += 2*right-1
        weight = sp.Integer(1)
        for r, l in departures.values():
            weight *= symbolic_moment(r, l)
        by_destination[location] += weight
    expectation = sum(location*weight for location, weight in by_destination.items())
    return sp.factor(sp.expand(expectation).subs({moments[0]: 1, moments[1]: half}))

def direct_environment_displacement(n, law):
    """Independent computation: sum conditional Markov chains over frozen site maps."""
    xs = list(range(-n+1, n))
    total = F(0)
    for choices in product(range(len(law)), repeat=len(xs)):
        environment = {x: law[i][0] for x, i in zip(xs, choices)}
        weight = F(1)
        for i in choices:
            weight *= law[i][1]
        if weight == 0:
            continue
        distribution = {0: F(1)}
        for _ in range(n):
            nxt = defaultdict(lambda: F(0))
            for x, px in distribution.items():
                p = environment[x]
                nxt[x+1] += px*p
                nxt[x-1] += px*(1-p)
            distribution = dict(nxt)
        total += weight*sum(x*px for x, px in distribution.items())
    return total

m2, m3 = moments[2], moments[3]
A = -(4*m2-1)*(6*m2-4*m3-1)/4
expected = [sp.Integer(0)]*4 + [A, 2*A]
for n in range(1, 7):
    actual = symbolic_displacement(n)
    assert sp.simplify(actual-expected[n-1]) == 0, (n, actual)

laws = [
    [(F(1,4), F(1,3)), (F(5,8), F(2,3))],
    [(F(3,8), F(2,3)), (F(3,4), F(1,3))],
    [(F(1,4), F(1,2)), (F(3,4), F(1,2))],
]
for law in laws:
    assert sum((p*w for p,w in law), F(0)) == F(1,2)
    s = sum((w*(p-F(1,2))**2 for p,w in law), F(0))
    mu3 = sum((w*(p-F(1,2))**3 for p,w in law), F(0))
    coefficient = 4*s*mu3
    raw3 = sum((w*p**3 for p,w in law), F(0))
    assert sp.Rational(coefficient) == sp.simplify(A.subs({m2: sp.Rational(s+F(1,4)), m3: sp.Rational(raw3)}))
    for n in range(1,7):
        actual = direct_environment_displacement(n, law)
        target = F(0) if n<=4 else coefficient*(1 if n==5 else 2)
        assert actual == target, (law,n,actual,target)
print('PASS: 6 symbolic full-path identities and 18 independent exact-rational Markov calculations')
print('The infinite-renewal velocity conclusion follows analytically, not from these finite tests.')
