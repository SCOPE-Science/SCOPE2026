#!/usr/bin/env python3
"""Exact finite checks for Schubert pairings of odd biisotropic two-plane sections.

All operations are over the integers.  The accompanying mathematical proof,
not these finite tests, establishes the asserted identities for every n >= 2.
"""
from math import comb


def partitions(weight, width):
    return [(a, weight-a) for a in range(weight, -1, -1)
            if a >= weight-a >= 0 and a <= width]


def pairing_pieri(lam, mu, width):
    """Integral Gr(2,width+2) Schubert integral of sigma_lam sigma_mu H^2."""
    nu = (width-lam[1], width-lam[0])
    if sum(nu) != sum(mu) + 2:
        return 0
    horizontal = int(nu[0] >= mu[0] >= nu[1] >= mu[1])
    vertical = int(nu == (mu[0]+1, mu[1]+1))
    return horizontal + vertical


def pairing_monomials(lam, mu, width):
    """Independent two-variable coefficient-extraction realization."""
    # sigma_(a,b)(x,y) = sum_{r=0}^{a-b} x^(a-r)y^(b+r).
    # Integral is [x^(W+1)y^W] (x-y) sigma_lam sigma_mu (x+y)^2.
    # Equivalently [x^W y^W]f - [x^(W+1)y^(W-1)]f.
    result = 0
    for r in range(lam[0]-lam[1]+1):
        for s in range(mu[0]-mu[1]+1):
            a = lam[0]-r + mu[0]-s
            b = lam[1]+r + mu[1]+s
            for ypower, coefficient in ((0, 1), (1, 2), (2, 1)):
                xp = a + 2 - ypower
                yp = b + ypower
                if (xp, yp) == (width, width):
                    result += coefficient
                if (xp, yp) == (width+1, width-1):
                    result -= coefficient
    return result


def determinant(m):
    """Bareiss determinant: division exact at every step."""
    a = [row[:] for row in m]
    n = len(a)
    sign, prev = 1, 1
    for k in range(n-1):
        if a[k][k] == 0:
            p = next((p for p in range(k+1, n) if a[p][k]), None)
            if p is None:
                return 0
            a[k], a[p] = a[p], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = pivot*a[i][j] - a[i][k]*a[k][j]
                q, rem = divmod(num, prev)
                assert rem == 0
                a[i][j] = q
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


def check_n(n, cross_check=False):
    width = 2*n-1
    d = 4*n-4
    middle = 2*n-2
    partitions_mid = partitions(middle, width)
    assert len(partitions_mid) == n
    M = [[pairing_pieri(a,b,width) for b in partitions_mid]
         for a in partitions_mid]
    expected = [[(1 if i==j==n-1 else 2 if i==j else
                  1 if abs(i-j)==1 else 0) for j in range(n)]
                for i in range(n)]
    assert M == expected
    assert determinant(M) == 1
    for j in range(middle+1, d+1):
        ell = d-j
        rows = partitions(j, width)
        cols = partitions(ell, width)
        B = [[pairing_pieri(a,b,width) for b in cols] for a in rows]
        r = len(cols)
        assert len(rows) >= r
        assert all(B[i][i] == 1 and all(B[i][k] == 0 for k in range(i+1,r))
                   for i in range(r)), (n,j,B)
        assert determinant([row[:r] for row in B[:r]]) == 1
        if cross_check:
            for a,row in zip(rows, B):
                for b,c in zip(cols,row):
                    assert pairing_monomials(a,b,width) == c, (n,j,a,b,c)
    if cross_check:
        for a,row in zip(partitions_mid,M):
            for b,c in zip(partitions_mid,row):
                assert pairing_monomials(a,b,width) == c
    degree = comb(2*width, width) - comb(2*width,width+1)
    catalan = comb(2*width,width)//(width+1)
    assert degree == catalan
    if n == 2:
        assert M == [[2,1],[1,1]] and degree == 5
    if n == 3:
        assert M == [[2,1,0],[1,2,1],[0,1,1]] and degree == 42
    return degree


def main():
    degrees = [check_n(n, cross_check=(n<=12)) for n in range(2,36)]
    print('VERIFY_OK range=2..35 middle_det=1 high_minors=1')
    print('crosscheck=monomials_vs_Pieri n=2..12')
    print('degrees_n2_to_n6=' + ','.join(str(x) for x in degrees[:5]))


if __name__ == '__main__':
    main()
