#!/usr/bin/env python3
"""Direct finite-field verification of quadratic exterior-multiplication spectra."""
from itertools import combinations, product
from math import comb
from collections import Counter


def fm(a, b, q):
    assert q in (2, 4)
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if q == 4 and a & 4:
            a ^= 7
    return ans


def fp(a, exp, q):
    ans = 1
    while exp:
        if exp & 1:
            ans = fm(ans, a, q)
        a = fm(a, a, q)
        exp >>= 1
    return ans


def rank(mat, q):
    if not mat:
        return 0
    a = [list(row) for row in mat]
    m = len(a)
    n = len(a[0])
    row = 0
    for col in range(n):
        pivot = next((j for j in range(row, m) if a[j][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        inv = fp(a[row][col], q-2, q)
        a[row] = [fm(v, inv, q) for v in a[row]]
        for j in range(row+1, m):
            v = a[j][col]
            if v:
                a[j] = [w ^ fm(v, z, q) for w,z in zip(a[j], a[row])]
        row += 1
        if row == m:
            break
    return row


def qbinom(n, k, q):
    a = 1
    b = 1
    for i in range(k):
        a *= q**(n-i)-1
        b *= q**(k-i)-1
    return a // b


def predicted(n, r, q):
    return qbinom(n, 2*r, q) * q**(r*(r-1)) * __import__('math').prod(q**(2*j-1)-1 for j in range(1,r+1))


def coefficient_matrix(n, pairs, coeffs):
    mat = [[0]*n for _ in range(n)]
    for (i,j),a in zip(pairs, coeffs):
        mat[i][j] = mat[j][i] = a
    return mat


def grade_ranks(n, pairs, coeffs, q):
    masks = [tuple(s for s in range(1<<n) if s.bit_count()==degree) for degree in range(n+1)]
    result = []
    for degree in range(n+1):
        src = masks[degree]
        tgt = masks[degree+2] if degree+2<=n else ()
        lookup = {t:i for i,t in enumerate(tgt)}
        a = [[0]*len(src) for _ in tgt]
        for j,mask in enumerate(src):
            for (u,v),coef in zip(pairs, coeffs):
                edge = (1<<u)|(1<<v)
                if not mask & edge:
                    a[lookup[mask|edge]][j] = coef
        result.append(rank(a,q))
    return result


def check_form(n, pairs, coeffs, q):
    r2 = rank(coefficient_matrix(n,pairs,coeffs),q)
    assert r2%2==0
    r=r2//2
    actual=grade_ranks(n,pairs,coeffs,q)
    hilb=[comb(n,i)-actual[i]-(actual[i-2] if i>=2 else 0) for i in range(n+1)]
    expected=[2**r*comb(n-2*r,i-r) if 0<=i-r<=n-2*r else 0 for i in range(n+1)]
    assert hilb==expected,(n,q,coeffs,r,hilb,expected)
    total=sum(actual)
    assert 2*total+sum(hilb)==2**n
    assert total==(2**(n-1)-2**(n-r-1) if r>0 else 0)
    return r


def main():
    cases=0
    for q,n in [(2,2),(2,3),(2,4),(2,5),(4,2),(4,3),(4,4)]:
        pairs=list(combinations(range(n),2))
        counts=Counter()
        for coeffs in product(range(q),repeat=len(pairs)):
            r=check_form(n,pairs,coeffs,q)
            counts[r]+=1
            cases+=1
        expected={r:predicted(n,r,q) for r in range(n//2+1)}
        assert dict(counts)==expected,(q,n,counts,expected)
        assert sum(counts.values())==q**len(pairs)
    # Higher-dimensional randomly structured, deterministic coefficient tests.
    for q,n in [(2,6),(4,5),(4,6),(2,7)]:
        pairs=list(combinations(range(n),2))
        for seed in range(48):
            coeffs=tuple(((11*seed+7*i+13*i*i+(seed*i)**2) % q) for i in range(len(pairs)))
            check_form(n,pairs,coeffs,q)
            cases+=1
    print('VERIFY_OK_CHAR2_QUADRATIC_MULTIPLIERS', cases)

if __name__=='__main__':
    main()
