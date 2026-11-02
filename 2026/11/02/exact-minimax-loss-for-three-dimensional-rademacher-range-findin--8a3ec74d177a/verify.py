"""Exact-arithmetic checks for the three-dimensional sign-sketch projection theorem.
Run: python verify.py  (requires sympy).  No external data required.
"""
from itertools import combinations, product
from sympy import Matrix, Rational, eye, simplify

U = [Matrix(v) for v in ((1, 1, 1), (1, 1, -1), (1, -1, 1), (-1, 1, 1))]
V = [Matrix([1 if k == i else s if k == j else 0 for k in range(3)])
     for i in range(3) for j in range(i + 1, 3) for s in (-1, 1)]
assert sum((v * v.T for v in U), Matrix.zeros(3)) == 4 * eye(3)
assert sum((v * v.T for v in V), Matrix.zeros(3)) == 4 * eye(3)
assert all(Matrix.hstack(*(U[i] for i in t)).det() != 0 for t in combinations(range(4), 3))


def direct_residual(A, indices):
    ids = sorted(set(indices))
    if len(ids) >= 3:
        return Rational(0)
    Y = A * Matrix.hstack(*(U[i] for i in ids))
    B = (Y.T * Y).inv()
    R = A - Y * B * Y.T * A
    return (R.T * R).trace().cancel()


def predicted(A, ell):
    G = A.T * A
    T = G.trace()
    Ginv = G.inv()
    singleton = sum((T - (u.T * G**2 * u)[0] / (u.T * G * u)[0]
                     for u in U), Rational(0))
    pair = sum((2 / (v.T * Ginv * v)[0] for v in V), Rational(0))
    return ((singleton + (2**ell - 2)*pair) / 4**ell).cancel(), singleton, pair


def exhaustive(A, ell):
    accum = Rational(0)
    byset = {}
    for word in product(range(4), repeat=ell):
        key = tuple(sorted(set(word)))
        if key not in byset:
            byset[key] = direct_residual(A, key)
        accum += byset[key]
    return (accum / 4**ell).cancel()


MATRICES = [
    eye(3),
    2*eye(3),
    Matrix.diag(1, 2, 3),
    Matrix([[1, 1, 0], [0, 1, 2], [1, 0, 1]]),
    Matrix([[2, 1, -1], [1, 1, 0], [-1, 2, 1]]),
    Matrix([[3, 0, 1], [1, 2, 0], [0, -1, 2]]),
]

number_of_comparisons = 0
for A in MATRICES:
    assert A.det() != 0
    G = A.T * A
    T = G.trace()
    for ell in range(1, 6):
        actual = exhaustive(A, ell)
        formula, s1, s2 = predicted(A, ell)
        assert actual == formula, (A, ell, actual, formula)
        bound = (Rational(2**(ell+1), 1) - Rational(4,3)) * T / 4**ell
        assert actual <= bound, (A,ell,actual,bound)
        assert (actual == bound) == (G == T/3 * eye(3))
        assert s1 <= 8*T/3
        assert s2 <= 2*T
        number_of_comparisons += 6

for ell in range(1, 9):
    p1 = Rational(4,4**ell)
    p2 = Rational(6*(2**ell-2),4**ell)
    p3 = 1-p1-p2
    assert p1 >= 0 and p2 >= 0 and p3 >= 0
    risk_identity = predicted(eye(3),ell)[0]
    sharp = (Rational(2**(ell+1),1) - Rational(4,3))*3/4**ell
    assert risk_identity == sharp == (2*p1+p2)

print(f'PASS: {number_of_comparisons} exact-rational checks over {len(MATRICES)} invertible matrices and five sketch lengths; 8 exact rank-distribution checks')
