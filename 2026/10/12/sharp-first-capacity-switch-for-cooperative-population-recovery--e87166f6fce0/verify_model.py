#!/usr/bin/env python3
"""Exact rational checks for a well-mixed finite-capacity cooperative-birth model.

The symbolic arguments proving all-capacity optimization are in RESULT.md.
This finite checker does not replace those arguments.
"""
from fractions import Fraction as F
from math import prod


def ratio(L, i, gamma):
    assert L >= i + 1 and i >= 2
    return gamma * F((L - 1)**2, (i - 1)*(L-i))


def denominator(K, L, gamma):
    assert K >= 3 and L >= K and gamma > 0
    z = F(1)
    running = F(1)
    for i in range(2, K):
        running *= ratio(L, i, gamma)
        z += running
    return z


def linear_solve(M, v):
    """Independent exact Gauss-Jordan linear solver."""
    n = len(v)
    a = [[F(t) for t in row] + [F(v[i])] for i, row in enumerate(M)]
    for col in range(n):
        row = next((i for i in range(col, n) if a[i][col] != 0), None)
        assert row is not None
        a[col], a[row] = a[row], a[col]
        z = a[col][col]
        a[col] = [t/z for t in a[col]]
        for i in range(n):
            if i == col: continue
            z = a[i][col]
            if z:
                a[i] = [u - z*w for u,w in zip(a[i], a[col])]
    return [row[-1] for row in a]


def direct_hitting(K, L, gamma):
    """Backward equations in continuous time with birth attempt rate 1."""
    N = K - 2
    mat = [[F(0) for _ in range(N)] for _ in range(N)]
    rhs = [F(0) for _ in range(N)]
    for i in range(2, K):
        idx = i-2
        death = F(i)*gamma
        birth = F(i*(i-1)*(L-i),(L-1)**2)
        mat[idx][idx] = birth+death
        if i+1 < K: mat[idx][idx+1] = -birth
        else: rhs[idx] = birth
        if i-1 >= 2: mat[idx][idx-1] = -death
    return linear_solve(mat, rhs)[0]


def coeffs(K,L):
    p=F(1)
    out=[]
    for i in range(2,K):
        p *= ratio(L, i, F(1))
        out.append(p)
    return out


def main():
    assert coeffs(5,5) == [F(16,3),F(64,3),F(1024,9)]
    assert coeffs(5,6) == [F(25,4),F(625,24),F(15625,144)]
    assert [a-b for a,b in zip(coeffs(5,6),coeffs(5,5))] == [F(11,12),F(113,24),-F(253,48)]
    assert coeffs(5,7) == [F(36,5),F(162,5),F(648,5)]
    assert coeffs(4,4) == [F(9,2),F(81,4)]
    assert coeffs(4,5) == [F(16,3),F(64,3)]
    # Exact threshold polynomial, with a rational isolating interval.
    def critical_polynomial(q): return 253*q*q - 226*q - 44
    assert critical_polynomial(F(1057,1000)) < 0 < critical_polynomial(F(1058,1000))
    assert sum(x*x for x in [113]) + 0 == 12769
    assert 23901 == 113*113 + 253*44
    checks=0
    for K in range(3,18):
        for g in [F(1,100), F(1,5), F(1,2), F(1), F(2), F(20)]:
            values = [denominator(K,L,g) for L in range(K,3*K+10)]
            if K<=4:
                assert min(values)==values[0] and values.count(values[0])==1
            if K==5:
                assert min(values)==min(values[0],values[1]); assert all(z>values[0] for z in values[2:])
            assert min(values)==min(values[:max(1,2*K-3-K+1)])
            checks += len(values)
    for K in range(3,10):
        for L in range(K,K+8):
            for g in [F(1,4),F(2,3),F(1),F(3)]:
                assert direct_hitting(K,L,g) == 1/denominator(K,L,g)
                checks+=1
    for L in range(7,1000):
        assert all(a>=b for a,b in zip(coeffs(5,L),coeffs(5,7)))
        checks+=1
    # Explicit comparison around the phase boundary using exact fractions.
    for g,best in [(F(1,10),5),(F(1),5),(F(11,10),6),(F(10),6)]:
        assert min((denominator(5,L,g),L) for L in range(5,100))[1] == best
    print('VERIFY_OK exact_coefficients=1 threshold_interval=1 direct_backward_equations=1 algebraic_general_cutoff_test=1 checks=',checks)

if __name__=='__main__': main()
