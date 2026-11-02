#!/usr/bin/env python3
"""Direct checks of the square-zero hook-centralizer count.

Only standard Python. Run `python verify.py`. Matrix products, not the
coefficient constraints from the proof, decide whether X is square-zero.
"""
from itertools import product
from math import prod


def add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def mul(x, y, q):
    if q != 4:
        return (x * y) % q
    z = 0
    for i in range(2):
        for j in range(2):
            if (x >> i) & 1 and (y >> j) & 1:
                z ^= 1 << (i + j)
    if z & 8:
        z ^= 0b1110  # x^3 = x^2+x over F_2[x]/(x^2+x+1)
    if z & 4:
        z ^= 0b111   # x^2 = x+1
    return z


def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    return prod(q ** (n - i) - 1 for i in range(k)) // prod(q ** (k - i) - 1 for i in range(k))


def rank_k_square_zero_count(r, k, q):
    return gaussian(r, k, q) * gaussian(r - k, k, q) * prod(q ** k - q ** i for i in range(k))


def predicted(n, r, q):
    assert n >= 2 and r >= 0
    total = 0
    for k in range(r // 2 + 1):
        s = r - 2*k
        if s == 0:
            core = 1
        elif n % 2 == 0:
            core = q**(2*s-1) + (q - 1) * q**(s-1)
        else:
            core = q**(2*s)
        total += rank_k_square_zero_count(r, k, q) * q**(2*k) * core
    return q**(n//2) * total


def build(n, r, a, b, c, d):
    N = n + r
    x = [[0] * N for _ in range(N)]
    for power, v in enumerate(a):
        for j in range(n-power):
            x[j+power][j] = v
    for j in range(r):
        x[n-1][n+j] = b[j]
        x[n+j][0] = c[j]
        for k in range(r):
            x[n+j][n+k] = d[j*r+k]
    return x


def is_sqzero(A, q):
    N = len(A)
    for i in range(N):
        for j in range(N):
            x = 0
            for k in range(N):
                x = add(x, mul(A[i][k], A[k][j], q), q)
            if x:
                return False
    return True


def direct(n, r, q):
    count = 0
    for a in product(range(q), repeat=n):
        for b in product(range(q), repeat=r):
            for c in product(range(q), repeat=r):
                for d in product(range(q), repeat=r*r):
                    if is_sqzero(build(n, r, a, b, c, d), q):
                        count += 1
    return count


def rank(A, q):
    # Only for prime fields in the independent rank census.
    B=[list(row) for row in A]
    n=len(B)
    if n == 0:return 0
    m=len(B[0]); t=0
    for col in range(m):
        pivot=next((j for j in range(t,n) if B[j][col]%q),None)
        if pivot is None:continue
        B[t],B[pivot]=B[pivot],B[t]
        inv=pow(B[t][col],-1,q)
        B[t]=[x*inv%q for x in B[t]]
        for j in range(n):
            if j!=t and B[j][col]:
                z=B[j][col]
                B[j]=[(x-z*y)%q for x,y in zip(B[j],B[t])]
        t+=1
        if t==n:break
    return t


def check_D_strata(q,r):
    frequencies={}
    for d in product(range(q),repeat=r*r):
        A=[d[i*r:(i+1)*r] for i in range(r)]
        if is_sqzero(A,q):
            k=rank(A,q)
            frequencies[k]=frequencies.get(k,0)+1
    expected={k:rank_k_square_zero_count(r,k,q) for k in range(r//2+1)}
    assert frequencies==expected,(r,q,frequencies,expected)


def main():
    cases=[(2,0,2),(3,0,3),(2,1,2),(3,1,2),
           (4,1,3),(2,2,2),(3,2,2),(2,2,3),
           (5,2,2),(3,3,2),(2,1,4),(3,1,4),
           (2,1,5)]
    for n,r,q in cases:
        e=predicted(n,r,q)
        v=direct(n,r,q)
        assert e==v,(n,r,q,e,v)
    for r in range(5):
        check_D_strata(2,r)
    for r in range(4):
        check_D_strata(3,r)
    for q in (2,3,4,5,7):
        for r in range(1,7):
            even=predicted(2,r,q)//q
            odd=predicted(3,r,q)//q
            assert odd>even
        for r in range(5):
            assert predicted(2,r,q)//q==predicted(6,r,q)//(q**3)
            assert predicted(3,r,q)//q==predicted(7,r,q)//(q**3)
    print('VERIFY_OK: 13 complete hook-centralizer square censuses; '
          '9 independent square-zero block-rank censuses; '
          'parity normalization and strict gaps over five field orders')

if __name__=='__main__':
    main()
