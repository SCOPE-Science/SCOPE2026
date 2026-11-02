"""Exact rational verification of cycle-space projection constants on wheel graphs.

Requires only Python 3 standard library. The proof uses a cyclic reduction and
signed-dual certificates; these computations check all tabulated certificates
and the finite Laurent-polynomial identity used for arbitrarily large wheels.
"""
from fractions import Fraction as F


def diff(x):
    """D e_j = e_(j+1) - e_j, with cyclic indices."""
    return [x[(i - 1) % len(x)] - x[i] for i in range(len(x))]


def adjdiff(x):
    return [x[(i + 1) % len(x)] - x[i] for i in range(len(x))]


def unit(n):
    return [F(i == 0) for i in range(n)]


def shift(x, j):
    n = len(x)
    return [x[(i - j) % n] for i in range(n)]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def norm(x):
    return sum(abs(a) for a in x)


def primal(n):
    if n == 3:
        return [F(-1, 4), F(0), F(1, 4)]
    if n == 4:
        return [F(-1, 6), F(0), F(1, 6), F(1, 3)]
    if n == 5:
        return [F(-1, 4), F(-1, 8), F(0), F(1, 8), F(1, 4)]
    return [F(-3, 10)] + [F(0)] * (n - 2) + [F(3, 10)]


def expected(n):
    return {3:F(3,2), 4:F(5,3), 5:F(7,4)}.get(n, F(9,5))


def small_dual(n):
    if n == 3:
        A, B, den = 1, 1, 2
        arrays = [[-1,0,1], [1,-1,-1], [1,1,1], [-1,1,0]]
    elif n == 4:
        A, B, den = 4, 5, 9
        arrays = [[-4,-4,4,4], [4,-4,-4,-4], [5,5,5,5], [-5,5,3,-3]]
    elif n == 5:
        A, B, den = 5, 7, 12
        arrays = [[-5,-5,0,5,5], [5,-5,-5,-5,-5], [7,7,7,7,7],[-7,7,6,0,-6]]
    else:
        assert n == 6
        A, B, den = 2, 3, 5
        arrays = [[-2,-2,0,0,2,2], [2,-2,-2,-2,-2,-2], [3]*6,[-3,3,3,1,-1,-3]]
    return F(A, den), F(B, den), [[F(x,den) for x in row] for row in arrays]


# Laurent-polynomial coefficients of 5 times each dual vector. A term
# with exponent j contributes at cyclic index j modulo n.
LAURENT = [
    {0:-2,1:-2,2:-2,3:-1,-4:1,-3:2,-2:2,-1:2},
    {0:2,1:-2,2:-2,3:-2,-3:-2,-2:-2,-1:-2},
    {0:3,1:3,2:3,-2:3,-1:3},
    {0:-3,1:3,2:3,3:1,-2:-1,-1:-3},
]


def polynomial_shift(p, k):
    return {i+k:x for i,x in p.items()}


def polynomial_add(*terms):
    out = {}
    for weight, poly in terms:
        for k,v in poly.items():
            out[k] = out.get(k,0) + weight*v
    return {k:v for k,v in out.items() if v}


def polynomial_Dt(poly):
    return polynomial_add((1,polynomial_shift(poly,-1)),(-1,poly))


def universal_dual(n):
    q = []
    for terms in LAURENT:
        row = [F(0)]*n
        for j,v in terms.items():
            row[j % n] += F(v,5)
        q.append(row)
    return F(2,5), F(3,5), q


def verify_dual(n, la, lb, q):
    assert la+lb == 1
    assert all(abs(x)<=la for row in q[:2] for x in row)
    assert all(abs(x)<=lb for row in q[2:] for x in row)
    a, b, c, d = q
    coef = [a[i]+adjdiff(b)[i]-adjdiff(c)[i]-adjdiff(adjdiff(d))[i] for i in range(n)]
    assert coef == [0]*n, (n,coef)
    assert c[0]+d[1]-d[0] == expected(n)
    return 4*n+2


def verify_primal(n):
    u=primal(n)
    v=[a-b for a,b in zip(unit(n),diff(u))]
    A=norm(u)+norm(diff(u))
    B=norm(v)+norm(diff(v))
    assert A == B == expected(n), (n,A,B)
    # Directly construct all 2n columns and check their range and identity
    # on all n facial cycle vectors (D e_j, e_j).
    cols=[]
    for j in range(n):
        w=shift(u,j)
        cols.append(diff(w)+w)
    for j in range(n):
        w=shift(v,j)
        cols.append(diff(w)+w)
    assert max(norm(z) for z in cols) == expected(n)
    for j in range(n):
        f=diff(shift(unit(n),j))+shift(unit(n),j)
        Pf=[sum(f[k]*cols[k][i] for k in range(2*n)) for i in range(2*n)]
        assert Pf == f
    return 3*n*n + 2


def main():
    # This exact formal Laurent identity has no modulus or n in it.
    S,T,R,H = LAURENT
    identity = polynomial_add((1,S), (1,polynomial_Dt(T)),
                              (-1,polynomial_Dt(R)),
                              (-1,polynomial_Dt(polynomial_Dt(H))))
    assert not identity, identity
    checks=1
    for n in range(3,201):
        la,lb,q=small_dual(n) if n<=6 else universal_dual(n)
        checks+=verify_dual(n,la,lb,q)
        if n<=30:
            checks+=verify_primal(n)
        else:
            u=primal(n)
            v=[a-b for a,b in zip(unit(n),diff(u))]
            assert norm(u)+norm(diff(u)) == norm(v)+norm(diff(v)) == expected(n)
            checks+=2
    print('CHECK_OK', checks, 'exact rational and Laurent identities', 'n=3..200')

if __name__=='__main__':
    main()
