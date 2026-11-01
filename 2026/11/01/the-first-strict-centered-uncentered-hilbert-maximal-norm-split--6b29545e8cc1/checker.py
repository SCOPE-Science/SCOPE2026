"""Exact finite certificate for strong-type maximal norms on a short graph path.

Requires Python 3 and SymPy.  All spectral inequalities are checked by rational
leading-principal-minor tests, not floating-point eigenvalue comparison.
"""
from itertools import product
from fractions import Fraction
from sympy import Matrix, Rational, symbols, Poly, oo, sqrt, eye, factor


def balls(n, centered, v):
    sets = set()
    for center in range(n):
        if centered and center != v:
            continue
        for radius in range(n):
            b = tuple(j for j in range(n) if abs(j-center) <= radius)
            if v in b:
                sets.add(b)
    return sorted(sets, key=lambda b: (len(b), b))


def matrix_of(bseq, n):
    return Matrix([[Rational(int(j in b), len(b)) for j in range(n)] for b in bseq])


def positive_definite(M):
    # Sylvester's criterion: all leading principal minors strictly positive.
    for k in range(1, M.rows+1):
        if M[:k, :k].det(method="domain-ge") <= 0:
            return False
    return True


def test_case(n, centered, winning, bound, polynomial, isolate, ray):
    choices = [balls(n, centered, j) for j in range(n)]
    expected_size = 1
    for c in choices:
        expected_size *= len(c)
    observed = 0
    strict = 0
    wins = 0
    T = Rational(*bound)
    for seq in product(*choices):
        observed += 1
        A = matrix_of(seq, n)
        H = A.T*A
        if seq in winning:
            wins += 1
            p = factor((symbols('z')*eye(n)-H).det(method="domain-ge"))
            assert factor(p-polynomial) == 0, (n, centered, seq, p)
            # A specific rational test vector certifies a singular value > bound.
            q = Matrix(ray if seq == winning[0] else list(reversed(ray)))
            assert ((A*q).dot(A*q) - T*q.dot(q)) > 0
            # Exact Sturm count: only one root strictly larger than bound.
            z = symbols('z')
            assert Poly(polynomial, z).count_roots(T, oo) == 1
            assert Poly(polynomial, z).count_roots(Rational(*isolate[0]), Rational(*isolate[1])) == 1
        else:
            assert positive_definite(T*eye(n)-H), (n, centered, seq)
            strict += 1
    assert observed == expected_size
    assert wins == len(winning)
    assert strict == expected_size-len(winning)
    print("EXACT_CASE", n, 'centered' if centered else 'uncentered', 'total',observed,'strict',strict,'winning',wins)

z=symbols('z')
P3=((0,1),(1,),(1,2))
q3=Matrix([Rational(19,100),1,Rational(19,100)])
p3=(4*z-1)*(4*z*z-7*z+1)/16
test_case(3,False,[P3],(3,2),p3,((1593,1000),(1594,1000)),q3)
test_case(3,True,[P3],(3,2),p3,((1593,1000),(1594,1000)),q3)

U=((0,1),(1,),(0,1,2),(1,2,3))
C=((0,1),(1,),(1,2,3),(1,2,3))
reversed_balls = lambda seq: tuple(tuple(3-j for j in b[::-1]) for b in seq[::-1])
u_poly=(324*z**4-702*z**3+308*z*z-42*z+1)/324
c_poly=z*(36*z**3-78*z*z+35*z-4)/36
u_ray=Matrix([Rational(3,10),1,Rational(19,100),Rational(9,100)])
c_ray=Matrix([Rational(19,100),1,Rational(19,100),Rational(19,100)])
test_case(4,False,[U,reversed_balls(U)],(13,8),u_poly,((1632,1000),(1633,1000)),u_ray)
test_case(4,True,[C,reversed_balls(C)],(8,5),c_poly,((1603,1000),(1604,1000)),c_ray)
print('CERTIFICATE_OK')
