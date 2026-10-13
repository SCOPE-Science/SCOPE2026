#!/usr/bin/env python3
"""Exact rational checks accompanying the four-cycle optimization proof.

No external dependencies. These checks supplement, not replace, the universal
Rayleigh-quotient argument in RESULT.md.
"""
from fractions import Fraction as F
from itertools import permutations


def laplacian(q, a, r, b):
    L = [[F(0) for _ in range(4)] for _ in range(4)]
    for i, j, w in [(0, 1, q), (1, 2, a), (2, 3, r), (3, 0, b)]:
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    return L


def matvec(L, v):
    return [sum(L[i][j] * v[j] for j in range(4)) for i in range(4)]


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def det4(A):
    total = F(0)
    for p in permutations(range(4)):
        inversions = sum(p[i] > p[j] for i in range(4) for j in range(i+1,4))
        term = F(-1) if inversions % 2 else F(1)
        for i in range(4):
            term *= A[i][p[i]]
        total += term
    return total


def verify_spectrum(L, spectrum):
    # Both sides are monic degree-four polynomials; five evaluations suffice.
    for x in [F(-2), F(-1), F(0), F(1), F(2)]:
        matrix = [[(x if i == j else F(0))-L[i][j]
                   for j in range(4)] for i in range(4)]
        product = F(1)
        for lam in spectrum:
            product *= x-lam
        assert det4(matrix) == product


def test_inner(h):
    assert 0 < h <= 3
    t = h*h
    D = h*h + 2*h + 5
    q = (h+1)/(h*D)
    a = b = F(2)/D
    r = (h+1)/D
    gap = F(4)/D
    assert t*q+a+r+b == 1
    assert min(q,a,r,b) > 0
    u = [F(1),F(1),F(-1),F(-1)]
    v = [h,-h,F(-1),F(1)]
    alpha = (3-h)*(h+1)/16
    beta = F(1,4)
    assert alpha >= 0 and beta > 0
    assert dot(u,v) == sum(u) == sum(v) == 0
    assert 4*alpha+2*(h*h+1)*beta == D/4
    assert 4*alpha+(h-1)**2*beta == 1
    assert 4*beta == 1 and 4*h*h*beta == t
    L = laplacian(q,a,r,b)
    assert matvec(L,u) == [gap*xi for xi in u]
    assert matvec(L,v) == [gap*xi for xi in v]
    fourth = 2*(h+1)**2/(h*D)
    assert sum(L[i][i] for i in range(4)) == 2*gap+fourth
    assert fourth > gap
    verify_spectrum(L, [F(0),gap,gap,fourth])


def test_boundary(s):
    assert 0 <= s <= F(1,15)
    q = s
    a = b = F(3,10)-3*s
    r = F(2,5)-3*s
    assert min(q,a,b,r) >= 0
    assert 9*q+a+b+r == 1
    L = laplacian(q,a,r,b)
    v = [F(3),F(-3),F(-1),F(1)]
    assert matvec(L,v) == [x/5 for x in v]
    eigenvalues = [F(1,5), F(3,5)-6*s, F(6,5)-10*s]
    assert all(ev >= F(1,5) for ev in eigenvalues)
    assert sum(L[i][i] for i in range(4)) == sum(eigenvalues)
    verify_spectrum(L,[F(0)]+eigenvalues)
    assert eigenvalues[1] == F(1,5) if s == F(1,15) else eigenvalues[1] > F(1,5)


def test_outer(t):
    assert t > 9
    q = F(0);a = b = F(3,10);r = F(2,5)
    assert t*q+a+b+r == 1
    L = laplacian(q,a,r,b)
    v = [F(3),F(-3),F(-1),F(1)]
    assert matvec(L,v) == [x/5 for x in v]
    verify_spectrum(L,[F(0),F(1,5),F(3,5),F(6,5)])


if __name__ == '__main__':
    H = [F(1,10), F(1,4), F(1,2), F(2,3), F(1), F(6,5), F(3,2), F(2), F(5,2), F(11,4), F(299,100), F(3)]
    for h in H:
        test_inner(h)
    for i in range(41):
        test_boundary(F(i,600))  # 0 through 1/15 inclusive
    for t in [F(10),F(12),F(20),F(100),F(10000)]:
        test_outer(t)
    print('VERIFY_OK: 12 interior/endpoint parameter certificates, 41 transition points, 5 exterior budgets')
