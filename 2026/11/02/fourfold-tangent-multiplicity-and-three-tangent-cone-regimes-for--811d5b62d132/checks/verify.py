#!/usr/bin/env python3
"""Exact finite-characteristic checks for four consecutive power-sum equations."""
from itertools import product
from math import comb, factorial


def determinant_mod(matrix, p):
    a = [[v % p for v in row] for row in matrix]
    n = len(a)
    det = 1
    for i in range(n):
        piv = next((j for j in range(i, n) if a[j][i] % p), None)
        if piv is None:
            return 0
        if piv != i:
            a[i], a[piv] = a[piv], a[i]
            det = -det
        t = a[i][i] % p
        det = det * t % p
        inv = pow(t, -1, p)
        for j in range(i+1, n):
            w = a[j][i] * inv % p
            for k in range(i, n):
                a[j][k] = (a[j][k] - w * a[i][k]) % p
    return det % p


def gram(m, p):
    return [[(int(i == j) + 1) % p for j in range(m)] for i in range(m)]


def coefficients(k, a, b, p):
    """Coefficients of t^0,t^1,t^2 in sum(1+t*a)^k+sum(t*b)^k."""
    return (
        (len(a) % p),
        (k * sum(a) + (k if k == 1 else 0) * sum(b)) % p,
        (comb(k, 2) * sum(u*u for u in a) + (int(k == 2) * sum(v*v for v in b))) % p,
    )


def test_jet(p, r):
    u = [(i*i + 2*i + 3) % p for i in range(p-2)]
    v = [(i*i + 3*i + 1) % p for i in range(r-1)]
    a = [0] + u + [(-sum(u)) % p]
    b = v + [(-sum(v)) % p]
    assert len(a) == p and len(b) == r
    assert sum(a) % p == 0 and sum(b) % p == 0
    c = {k: coefficients(k, a, b, p) for k in (1,2,3,4)}
    assert all(c[k][0] == c[k][1] == 0 for k in (1,2,3,4))
    qu, qv = sum(t*t for t in a) % p, sum(t*t for t in b) % p
    inv2 = pow(2, -1, p)
    q3 = (c[3][2] - 3*inv2*c[2][2]) % p
    q4 = (c[4][2] - 2*c[3][2] + c[2][2]) % p
    assert q3 == 3*inv2*(qu-qv) % p
    assert q4 == (qu+qv) % p
    detu, detv = determinant_mod(gram(p-2, p), p), determinant_mod(gram(r-1, p), p)
    assert detu == (p-1) % p, (p,r,detu)
    assert detv == r % p, (p,r,detv)
    return dict(p=p, r=r, n=p+r, singular_support_count=comb(p+r,p),
                tangent_block_ranks=[p-2,r-1],
                gram_determinants_mod_p=[detu,detv], multiplicity=4,
                tangent_cone_type=('nonreduced' if r == 2 else 'reducible_reduced' if r == 3 else 'normal_integral'))


def exhaustive(p,r):
    n=p+r
    singular=[]
    for pivot in range(n):
        head=(0,)*pivot+(1,)
        for tail in product(range(p),repeat=n-pivot-1):
            x=head+tail
            if any(sum(pow(t,j,p) for t in x)%p for j in range(1,5)):
                continue
            if len(set(x))<4:
                singular.append(x)
    expected={tuple(int(i in s) for i in range(n))
              for s in __import__('itertools').combinations(range(n),p)}
    assert set(singular)==expected, (p,r,len(singular),len(expected))
    return (p,r,len(singular))

if __name__=='__main__':
    rows=[]
    for p in (5,7,11):
        for r in (2,3,4):
            if r>=p: continue
            rows.append(test_jet(p,r))
    print('JET_AND_GRAM_OK', rows)
    print('FINITE_FIELD_EXHAUSTIVE', [exhaustive(5,r) for r in (2,3)])
    print('VERIFY_OK')
