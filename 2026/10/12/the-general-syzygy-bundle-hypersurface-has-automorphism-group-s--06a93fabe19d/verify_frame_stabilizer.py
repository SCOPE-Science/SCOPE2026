from itertools import permutations
import sympy as sp

x,y,z = sp.symbols('x y z')
pts = [sp.Matrix([1,0,0]), sp.Matrix([0,1,0]), sp.Matrix([0,0,1]), sp.Matrix([1,1,1])]
q1 = x*y - x*z
q2 = x*y - y*z

def normalize_projective(v):
    vals = list(map(sp.simplify, v))
    for a in vals:
        if a != 0:
            return tuple(sp.simplify(t/a) for t in vals)
    raise ValueError('zero vector')

def matrix_for_perm(perm):
    qs = [pts[i] for i in perm]
    B = sp.Matrix.hstack(qs[0], qs[1], qs[2])
    c = B.inv() * qs[3]
    if any(ci == 0 for ci in c):
        raise AssertionError('not a projective frame')
    return sp.Matrix.hstack(c[0]*qs[0], c[1]*qs[1], c[2]*qs[2])

def coeffs(poly):
    P = sp.Poly(sp.expand(poly), x,y,z)
    return sp.Matrix([
        P.coeff_monomial(x*x), P.coeff_monomial(y*y), P.coeff_monomial(z*z),
        P.coeff_monomial(x*y), P.coeff_monomial(x*z), P.coeff_monomial(y*z)
    ])

Bq = sp.Matrix.hstack(coeffs(q1), coeffs(q2))
seen = set()
for perm in permutations(range(4)):
    M = matrix_for_perm(perm)
    assert M.det() != 0
    for j,p in enumerate(pts):
        assert normalize_projective(M*p) == normalize_projective(pts[perm[j]])
    # Pull back the two pencil generators; each must stay in their span.
    X = M * sp.Matrix([x,y,z])
    for q in (q1, q2):
        tr = sp.expand(q.subs({x:X[0], y:X[1], z:X[2]}, simultaneous=True))
        c = coeffs(tr)
        assert Bq.row_join(c).rank() == 2
    key = tuple(normalize_projective(M.reshape(9,1)))
    seen.add(key)

assert Bq.rank() == 2
assert len(seen) == 24
print('frame_points=4')
print('pencil_dimension=2')
print('permutations_verified=24')
print('distinct_projective_transformations=24')
print('pencil_preservation=ok')
print('VERIFY_OK')
