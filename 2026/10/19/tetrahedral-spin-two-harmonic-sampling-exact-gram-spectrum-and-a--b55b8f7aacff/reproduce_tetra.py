"""Independent exact checks of tetrahedral Hessian sampling.

Requires Python 3 and SymPy. No input files are used.
"""
from fractions import Fraction as F
from math import factorial as fac

import sympy as S


def legendre_derivative(n, r):
    # Rodrigues formula, expanded in powers of x before differentiating.
    x = F(-1, 3)
    return sum(
        F((-1)**j * fac(2*n-2*j), 2**n * fac(j) * fac(n-j) * fac(n-2*j-r))
        * x**(n-2*j-r)
        for j in range((n-r)//2+1)
    )


def spectrum(d, q, r, u):
    return (
        d + F(4,3)*q - F(32,9)*r + F(32,27)*u,
        d - 4*q - F(32,9)*r - F(32,27)*u,
        d + F(28,9)*q + F(160,27)*r + F(32,81)*u,
    )


def exact_low_degrees():
    tight = (1, None)
    for n in range(25):
        d = F((n-1)*n*(n+1)*(n+2), 2)
        values = spectrum(d, *(legendre_derivative(n,r) for r in (2,3,4)))
        assert min(values) >= 0
        rank = sum(k for k,a in zip((2,3,3),values) if a)
        assert rank == ([0,0,5,6][n] if n < 4 else 8)
        if n < 5:
            print(n, tuple(str(a) for a in values), 'rank', rank)
        if n >= 4:
            tight = min(tight, (min(values)/d, n))
    assert tight[0] >= F(1,25)
    print('minimum of all 63 ratios and its degree:', tight)


def gram_factorization():
    d,q,r,u,h = S.symbols('D Q R U h')
    verts = [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]
    def frame(v):
        a,b,c = v
        w1 = S.Matrix([a,-b,0])/S.sqrt(2)
        w2 = S.Matrix([a,b,-2*c])/S.sqrt(6)
        return S.Matrix(v)/S.sqrt(3), (((1,w1),(-1,w2)), ((1,w1+w2),(-1,w1),(-1,w2)))

    # Coefficient of s^2 t^2 times 2!2! in the two-line expansion:
    # P((v+s*a)·(w+t*b)). Any curvature correction is pure trace.
    def entry(v,w,terms,other):
        return S.expand(sum(
            i*j*(2*q*g*g+4*r*x*y*g+u*x*x*y*y)
            for i,a in terms for j,b in other
            for x,y,g in [(a.dot(w),v.dot(b),a.dot(b))]
        ))

    v,first = frame(verts[0])
    blocks = [d*S.eye(2)]
    for vv in verts[1:]:
        w,second = frame(vv)
        blocks.append(S.Matrix([[entry(v,w,a,b) for b in second] for a in first]))

    A,B,C = spectrum(d,q,r,u)
    for k in range(4):
        ft = sum((c*block for c,block in zip(([(1,*v)[k] for v in verts]), blocks)), S.zeros(2))
        expected = (h-A)**2 if k == 0 else (h-B)*(h-C)
        assert S.expand(ft.charpoly(h).as_expr()-expected) == 0
    print('all four character blocks have the claimed characteristic polynomial')


def tail():
    # Monotone bounds for normalized derivatives at n>=25, from the correctly
    # twice-differentiated ODE L P''''-6x P'''+(n(n+1)-6)P''=0.
    n = 25
    assert F(9,8)*(1+F(2,n)) <= F(5,4)
    assert F(9,8)*(F(3,2)*(1+F(1,n))+F(5,3*n)) <= F(15,8)
    assert F(9,8)*(F(5,4)*(1+F(1,n))+F(15,4*n)) <= F(5,3)
    assert F(1,1)-F(1,2*n) >= F(50,51)**2
    assert F(1,2)*(1-F(1,n)) >= F(12,25)
    for q,r,u in [(F(4,3),F(32,9),F(32,27)),(4,F(32,9),F(32,27)),(F(28,9),F(160,27),F(32,81))]:
        # Replace n by 25 in the monotonically decreasing bound.
        bound = F(51,50)*F(25,12)*F(1,5)*(q*F(5,4*n*n)+r*F(15,8*n)+u*F(5,3))
        assert bound < 1
        print('tail relative error bound:', bound)


if __name__ == '__main__':
    exact_low_degrees()
    gram_factorization()
    tail()
