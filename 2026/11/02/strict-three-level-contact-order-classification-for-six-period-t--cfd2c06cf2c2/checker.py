"""Exact algebra checks for temporal SIS contact-order classification.

Requires sympy. Execute: python checker.py. These checks complement the
human-readable proof; a finite test alone does not establish an infinite theorem.
"""
from itertools import combinations
import sympy as sp

u, v = sp.symbols('u v', positive=True)
z = sp.Symbol('z')
X = sp.Matrix([[u, v, 0], [v, u, 0], [0, 0, u]])
Y = sp.Matrix([[u, 0, 0], [0, u, v], [0, v, u]])

def product(word):
    p = sp.eye(3)
    for c in word:
        p = p * (X if c == 'X' else Y)
    return p

G, M, A = (product(w) for w in ('XXXYYY', 'XXYXYY', 'XYXYXY'))

def same(a, b):
    assert sp.expand(a - b) == 0

TG = 3*u**2*(u**2+v**2)*(u**2+3*v**2)
TM = u**2*(3*u**4+12*u**2*v**2+5*v**4)
TA = 3*u**2*(u**4+4*u**2*v**2+v**4)
D = u**6*(u**2-v**2)**6
for mat, expected in ((G, TG), (M, TM), (A, TA)):
    same(sp.trace(mat), expected)
    same(mat.det(), D)

same(sp.trace(G)-sp.trace(M), 4*u**2*v**4)
same(sp.trace(M)-sp.trace(A), 2*u**2*v**4)
KGM = u**2*(u**4+3*u**2*v**2-v**4)
KMA = u**2*(u**4+3*u**2*v**2-sp.Rational(5,2)*v**4)
same(G.charpoly(z).as_expr()-M.charpoly(z).as_expr(),
     -4*u**2*v**4*z*(z-KGM))
same(M.charpoly(z).as_expr()-A.charpoly(z).as_expr(),
     -2*u**2*v**4*z*(z-KMA))
same(TM/sp.Integer(3)-KGM, u**2*(u**2*v**2+sp.Rational(8,3)*v**4))
same(TA/sp.Integer(3)-KMA, u**2*(u**2*v**2+sp.Rational(7,2)*v**4))

words = [''.join('X' if j in inds else 'Y' for j in range(6))
         for inds in combinations(range(6), 3)]
def dihedral(word):
    return {w[i:]+w[:i] for w in (word, word[::-1]) for i in range(6)}
seen = set()
orbits = {}
for word in words:
    if word in seen:
        continue
    orbit = dihedral(word)
    seen |= orbit
    orbits[min(orbit)] = orbit
assert sorted(map(len, orbits.values())) == [2, 6, 12]
assert set(orbits) == {'XXXYYY', 'XXYXYY', 'XYXYXY'}
assert seen == set(words)
# Exact characteristic polynomial, not a floating-point root comparison.
for canon, orbit in orbits.items():
    expected = product(canon).charpoly(z).as_expr()
    for word in orbit:
        same(product(word).charpoly(z).as_expr(), expected)

params = {u: sp.Rational(4,5), v: sp.Rational(149,500)}
pivot = {u: sp.Rational(4,5), v: sp.Rational(3,10)}
vector = sp.Matrix([sp.Rational(5,4), sp.Rational(3,2), 1])
assert (X*Y*vector).subs(pivot) == vector
# Every coordinate strictly shrinks if transmission is reduced from 3/10.
assert all(e > 0 for e in (vector-X*Y*vector).subs(params))
cert = (sp.eye(3)-M).det().subs(params)
assert cert == -sp.Rational(667551319210915426403604273201,
                            931322574615478515625000000000000)
assert cert < 0
print('PASS: symbolic characteristic-polynomial identities, 20 schedules,'
      ' three dihedral classes, and exact invasion-threshold witness.')
