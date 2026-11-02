#!/usr/bin/env python3
"""Independent exact-arithmetic regressions for the resonant planar switch.

The proof of the real-parameter theorem is in RESULT.md; rational regressions
provide a separate check of its critical boundaries and predicted itineraries.
"""
from fractions import Fraction as Q
from itertools import product


def F(z, a, b, d):
    x, y = z
    return ((-b*x+y, Q(0)) if x <= 0 else (-a*x+y, -d*x))


def iterate(z, n, a, b, d):
    for _ in range(n):
        z = F(z, a, b, d)
    return z


def check():
    checked = 0
    params = [(Q(p, q), Q(r, s)) for (p,q),(r,s) in product(
        [(1,3),(2,3),(1,1),(3,2),(5,2),(7,1)],
        [(1,4),(1,2),(1,1),(2,1),(5,1)])]
    for a,b in params:
        d = a*b
        for x,y in product(range(-8,9), repeat=2):
            assert iterate((Q(x),Q(y)),5,a,b,d) == (0,0), (a,b,x,y)
            checked += 1
        w=(Q(1),a/2)
        assert iterate(w,4,a,b,d) != (0,0)
        assert iterate(w,5,a,b,d) == (0,0)
        checked+=2
        for c in [-Q(1,7), -Q(3,2), Q(1,7), Q(4,1)]:
            # choose d positive, including strict sides of the resonance
            if a*b-c <= 0:
                continue
            dd=a*b-c
            z=(Q(1),Q(0))
            for n in range(24):
                assert z != (0,0)
                z=F(z,a,b,dd)
                checked+=1
            if c>0:
                for n in range(10):
                    assert iterate((Q(1),Q(0)),2*n,a,b,dd)==(c**n,Q(0))
                    checked+=1
            else:
                for n in range(7):
                    assert iterate((Q(1),Q(0)),2+3*n,a,b,dd)==(c*(-b*c)**n,Q(0))
                    checked+=1
    # A distinct, symbolic matrix-product certificate for the scalar resonance.
    import sympy as S
    A,B,D=S.symbols('a b d', positive=True)
    L=S.Matrix([[-B,1],[0,0]])
    R=S.Matrix([[-A,1],[-D,0]])
    C=S.simplify(L*R*L)
    assert S.simplify(C-(A*B-D)*L)==S.zeros(2)
    # Compute it directly without choosing a sign convention for the matrix factors.
    assert S.simplify(L*R*S.Matrix([1,0])-S.Matrix([A*B-D,0]))==S.zeros(2,1)
    assert S.simplify((L*R*L).subs(D,A*B))==S.zeros(2)
    checked+=3
    print('EXACT_ARITHMETIC_REGRESSION_OK',checked)


if __name__=='__main__':
    check()
