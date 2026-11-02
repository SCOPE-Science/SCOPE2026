"""Exact symbolic checks for ramification of plane-monomial series on the tricuspidal quartic.
Run: python tricuspidal_verify.py
Requires SymPy. These finite checks supplement, rather than prove, the all-degree theorem.
"""
from itertools import product
import sympy as sp

u = sp.symbols('u')
X, Y, Z = u**2, (u-1)**2, u**2*(u-1)**2


def jet_matrix(m):
    D = 4*m
    C = sp.zeros(3, D+1)
    C[0, 0] = 2*m
    C[0, 1] = 1
    for j in range(D+1):
        C[1, j] = j-2*m
    C[2, D-1] = 1
    C[2, D] = 2*m
    return C


def cusp_tail_dim(m, k):
    C = jet_matrix(m)
    return (4*m-k+1) - C[:, k:].rank()


def test_cusp_linear_series():
    for m in range(2, 11):
        D = 4*m
        assert jet_matrix(m).rank() == 3
        assert cusp_tail_dim(m, 0) == D-2
        assert cusp_tail_dim(m, 1) == D-3
        for k in range(2, D-1):
            assert cusp_tail_dim(m, k) == D-k-1, (m, k)
        assert cusp_tail_dim(m, D-1) == 0
        assert cusp_tail_dim(m, D) == 0


def test_plane_equation():
    P = sp.expand(X**2*Y**2 + X**2*Z**2 + Y**2*Z**2 - 2*X*Y*Z*(X+Y+Z))
    assert P == 0
    for m in range(2, 6):
        C = jet_matrix(m)
        for a in range(m+1):
            for b in range(m+1-a):
                c = m-a-b
                F = sp.Poly(sp.expand(X**a * Y**b * Z**c),u)
                coeff = sp.Matrix([F.nth(j) for j in range(4*m+1)])
                assert C*coeff == sp.zeros(3,1), (m,a,b,c)


def test_wronskian(m):
    funcs = [sp.expand(X**a * Y**b * Z**(m-a-b))
             for a in range(m+1) for b in range(m+1-a)]
    # For m=2 and m=3 the monomials form a basis (no quartic relation).
    assert len(funcs) == 4*m-2
    W = sp.Matrix([[sp.diff(f,u,i) for f in funcs]
                          for i in range(len(funcs))]).det(method='domain-ge')
    W = sp.factor(W)
    expected = u**(4*m-3)*(u-1)**(4*m-3)*(u+1)*(u-2)*(2*u-1)
    assert sp.rem(W,expected,u) == 0
    quotient = sp.cancel(W/expected)
    assert quotient.is_number and quotient != 0, (m,quotient)
    assert sp.degree(W,u) == 2*(4*m-3)+3, (m,sp.degree(W,u))


if __name__ == '__main__':
    test_plane_equation()
    test_cusp_linear_series()
    test_wronskian(2)
    test_wronskian(3)
    print('VERIFY_OK: plane equation, coefficient-jet constraints, cusp dimensions m=2..10, full Wronskians m=2,3')
