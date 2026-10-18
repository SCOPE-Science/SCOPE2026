"""Exact, standalone cross-check of quaternion-group rank-weighted Fourier profiles.

Requires Python 3 and SymPy. Run: python checker.py
Mathematical proof is in RESULT.md; these finite calculations corroborate it.
"""
from itertools import product
from sympy import I, sqrt, Matrix, symbols, simplify, S

E = Matrix.eye(2)
A = Matrix([[I, 0], [0, -I]])
B = Matrix([[0, 1], [-1, 0]])
C = A * B
assert A * A == -E and B * B == -E and C * C == -E
assert A * B == C and B * A == -C

V = symbols('v0:4')
block = V[0] * E - V[1] * A - V[2] * B - V[3] * C
assert simplify(block.det() - sum(x*x for x in V)) == 0

complex_u = [
    (1, 0, 0, 0), (1, 0, 0, 0), (1, 1, 0, 0), (0, 0, 0, 0),
    (1, 1, 1, 1), (0, 0, 0, 0), (1, 1, 1, 1), (1, 1, 1, 1),
]
complex_v = [
    (1, 0, 0, 0), (0, 0, 0, 0), (1, I, 0, 0), (1, I, 0, 0),
    (1, 1, 1, I * sqrt(3)), (1, 1, I * sqrt(2), 0), (1, I, 0, 0), (0, 0, 0, 0),
]
real_u = [
    (1, 0, 0, 0), (1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 0, 0),
    (1, 1, 1, 1), (1, 1, 2, 0), (1, 1, 1, 1), (1, 1, 1, 1),
]
real_v = [
    (1, 0, 0, 0), (0, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0),
    (1, 1, 1, 0), (0, 0, 0, 0), (1, 0, 0, 0), (0, 0, 0, 0),
]

expected = {
    'complex': (8, 4, 4, 2, 3, 2, 3, 1),
    'real': (8, 4, 6, 2, 5, 3, 5, 1),
}


def check(u, v):
    # The group ordering is (1,i,j,k,-1,-i,-j,-k).
    f = tuple(simplify((x+y)/S(2)) for x,y in zip(u,v)) + tuple(
        simplify((x-y)/S(2)) for x,y in zip(u,v))
    support = sum(x != 0 for x in f)
    chars = tuple(
        simplify(u[0] + p*u[1] + q*u[2] + p*q*u[3])
        for p,q in product((1,-1), repeat=2))
    a = sum(x != 0 for x in chars)
    # Fourier matrices are defined with adjoints; rank does not depend on 1/8.
    F = simplify(v[0]*E - v[1]*A - v[2]*B - v[3]*C)
    rho = (E, A, B, C, -E, -A, -B, -C)
    direct = Matrix.zeros(2)
    for value, representation in zip(f, rho):
        direct += value * representation.conjugate().transpose()
    assert direct.applyfunc(simplify) == F.applyfunc(simplify)
    r = F.rank()
    assert simplify(F.det() - sum(z*z for z in v)) == 0
    return support, a + 2*r, a, r


for field, rows in [('complex', (complex_u, complex_v)), ('real', (real_u, real_v))]:
    for t, (u,v) in enumerate(zip(*rows), 1):
        actual = check(u,v)
        assert actual[:2] == (t, expected[field][t-1]), (field,t,actual)
        if field == 'real':
            assert all(simplify(S(z).as_real_imag()[1]) == 0 for z in (*u,*v))
        print(field, t, 'rank-weighted Fourier support', actual[1],
              'abelian blocks', actual[2], 'nonabelian block rank', actual[3])

# The four-point Walsh elementary support lemma, exhaustively over possible
# pairs of characters and using their +/-1 ratio, is checked symbolically.
characters = [tuple(1 if ((alpha and (idx in (1,3))) + (beta and (idx in (2,3)))) % 2 == 0 else -1 for idx in range(4))
              for alpha,beta in product((0,1),repeat=2)]
for j in range(4):
    assert all(c*c == 1 for c in characters[j])
    for k in range(j+1,4):
        ratios=[characters[j][m]*characters[k][m] for m in range(4)]
        assert ratios.count(1)==2 and ratios.count(-1)==2
print('All sixteen witness computations and structural character identities passed.')
