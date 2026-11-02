#!/usr/bin/env python3
"""Exact checks for the E8 root spherical-harmonic interpolation calculation.

No third-party Python modules are required. All coordinates and spectral
quantities are represented exactly, using integers and rational arithmetic.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb


def root_representatives():
    roots = set()
    for i, j in combinations(range(8), 2):
        for a, b in product((-2, 2), repeat=2):
            r = [0] * 8
            r[i], r[j] = a, b
            roots.add(tuple(r))
    for signs in product((-1, 1), repeat=8):
        if sum(v < 0 for v in signs) % 2 == 0:
            roots.add(tuple(signs))
    assert len(roots) == 240
    assert all(sum(c * c for c in r) == 8 for r in roots)
    assert all(tuple(-v for v in r) in roots for r in roots)
    representatives = sorted(r for r in roots if next(v for v in r if v) > 0)
    assert len(representatives) == 120
    return representatives


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def matrices(reps):
    n = len(reps)
    T = [[dot(a, b) for b in reps] for a in reps]
    assert all(T[i][i] == 8 for i in range(n))
    assert all(T[i][j] in (-4, 0, 4) for i in range(n) for j in range(n) if i != j)
    A = [[int(i != j and abs(T[i][j]) == 4) for j in range(n)] for i in range(n)]
    S = [[(T[i][j] // 4 if i != j else 0) for j in range(n)] for i in range(n)]
    assert all(sum(row) == 56 for row in A)
    assert all(sum(A[i][k]*A[j][k] for k in range(n)) ==
               (56 if i == j else 28 if A[i][j] else 24)
               for i in range(n) for j in range(n))
    assert all(sum(S[i][k]*S[k][j] for k in range(n)) ==
               26*S[i][j] + (56 if i == j else 0)
               for i in range(n) for j in range(n))
    # The raw coordinate representatives constitute a tight frame:
    assert all(sum(r[i]*r[j] for r in reps) == (120 if i == j else 0)
               for i in range(8) for j in range(8))
    return T, A, S


def gegenbauer_at(x, last_degree):
    out = [Fraction(1), 6*x]
    for ell in range(1, last_degree):
        out.append((2*(ell+3)*x*out[-1]-(ell+5)*out[-2])/(ell+1))
    return out[:last_degree+1]


def eigenvalues(ell, w, c):
    if ell % 2:
        return [(1+28*w,8), (1-2*w,112)]
    return [(1+56*w+63*c,1), (1+8*w-9*c,35), (1-4*w+3*c,84)]


def check():
    roots = root_representatives()
    T, A, S = matrices(roots)
    last = 48
    wvals = gegenbauer_at(Fraction(1,2),last)
    cvals = gegenbauer_at(Fraction(0),last)
    expected_ranks = [1,8,35,112,84,112,119,120,120,120,119]
    for ell in range(last+1):
        D = comb(ell+5,5)
        W, V = wvals[ell], cvals[ell]
        assert D > 0 and W.denominator == 1 and V.denominator == 1
        # Independent exact coefficient evaluation by factorization of the
        # generating functions (1-t+t^2)^(-3), (1+t^2)^(-3).
        k, r = divmod(ell, 3)
        Wcheck = ((-1)**k * (k+1) if r == 0 else
                  (-1)**k * 3*comb(k+2,2))
        Vcheck = 0 if ell % 2 else (-1)**(ell//2)*comb(ell//2+2,2)
        assert W == Wcheck and V == Vcheck
        w, c = W/D, V/D
        ev = eigenvalues(ell,w,c)
        assert all(q >= 0 for q, mult in ev)
        rank = sum(mult for q,mult in ev if q != 0)
        assert rank == (expected_ranks[ell] if ell <= 10 else 120)
        # Compare the Gram construction from coordinates to the two/three
        # spectral-class formulas entrywise, without numerical diagonalization.
        for i in range(120):
            for j in range(120):
                raw = T[i][j]
                if i == j:
                    actual = Fraction(1)
                elif raw == 0:
                    actual = c
                else:
                    actual = w if raw == 4 else (-w if ell % 2 else w)
                if ell % 2:
                    predicted = (1 if i == j else 0)+w*S[i][j]
                else:
                    predicted = (1-c if i == j else 0)+(w-c)*A[i][j]+c
                assert actual == predicted
        if ell <= 10:
            print(f'degree={ell}: rank={rank}; eigenvalues={ev}')
    # Exact base of the all-degrees analytic positivity bound:
    assert Fraction(comb(12+5,5),(12+6)**2) > Fraction(413,24)
    assert Fraction(comb(11+5,5),(11+6)**2) > Fraction(14,3)
    # For every integer l>=0, D_l/(l+6)^2 is strictly increasing since
    # (l+6)^3-(l+1)(l+7)^2=3*l*l+45*l+167>0.
    print('E8_INTERPOLATION_CHECK_OK')

if __name__ == '__main__':
    check()
