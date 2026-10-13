"""Exact rational verification of a row-selection and rejection-sampling example.

Run with Python 3 and sympy: python verify.py. All comparisons are exact.
"""
from sympy import Matrix, eye, Rational, simplify


def instance(t):
    A = Matrix([[1/t, 0, 0], [1, t, 0], [0, 0, 1]])
    xstar = Matrix([0, 1, 0])
    b = A*xstar
    norms = []
    waits = []
    gains = []
    for i in range(3):
        a = A.row(i).T
        P = eye(3) - a*a.T/(a.dot(a))
        residual_rows = [j for j in range(3) if j != i]
        z = [P*A.row(j).T for j in residual_rows]
        squared = [simplify(v.dot(v)) for v in z]
        F2 = simplify(sum(squared))
        norms.append(F2)
        x0 = a*b[i]/a.dot(a)
        active = [j for j in residual_rows if simplify((A.row(j)*x0)[0]-b[j]) != 0]
        if len(active) == 1:
            j = active[0]
            zj = P*A.row(j).T
            probability = simplify(zj.dot(zj)/F2)
            waits.append(simplify(1/probability))
            nextx = x0 - (((A.row(j)*x0)[0]-b[j])/zj.dot(zj))*zj
            if i in (0, 1):
                assert all(simplify(q) == 0 for q in nextx-xstar)
        else:
            waits.append(None)
        # In these instances the two projected rows are perpendicular,
        # hence the exact least Rayleigh quotient is min(row squared norms)/F2.
        if i in (0, 1):
            assert simplify(z[0].dot(z[1])) == 0
            gains.append(simplify(min(squared)/F2))
        else:
            gains.append(None)
    assert simplify(A.det()-1) == 0
    assert simplify(norms[0]-(1+t*t)) == 0
    assert simplify(norms[1]-(1+1/(1+t*t))) == 0
    assert simplify(norms[2]-(1/t**2+1+t*t)) == 0
    assert norms[0] < norms[1] and norms[0] < norms[2]
    assert simplify(waits[0] - (1+t*t)/t**2) == 0
    assert simplify(waits[1] - (2+t*t)) == 0
    assert simplify(gains[0] - t*t/(1+t*t)) == 0
    assert simplify(gains[1] - 1/(2+t*t)) == 0
    assert simplify(waits[0]*gains[0]-1) == 0
    assert simplify(waits[1]*gains[1]-1) == 0


if __name__ == '__main__':
    for k in range(2, 75):
        instance(Rational(1, k))
    print('VERIFY_OK exact_rational_parameter_cases=73 row_policies=3')
