#!/usr/bin/env python3
"""Exact-rational and numerical checks for Taylor-RK positivity on multipartite graphs.

The analytical all-size proof is in RESULT.md. This script gives independent
matrix-power checks of the spectral formulas and tests the phase boundaries.
It uses only the Python standard library.
"""
from fractions import Fraction as F
from math import isfinite


def partitions(n, high=None):
    high = n if high is None else min(high, n)
    for a in range(high, 0, -1):
        if a == n:
            yield (a,)
        else:
            for rest in partitions(n-a, a):
                yield (a,) + rest


def lap(parts):
    n = sum(parts)
    tag = [j for j, c in enumerate(parts) for _ in range(c)]
    return [[F(n-parts[tag[i]]) if i == j else
             F(-1) if tag[i] != tag[j] else F(0)
             for j in range(n)] for i in range(n)], tag


def mult(a, b):
    n = len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)), F(0))
             for j in range(n)] for i in range(n)]


def matrix_taylor(L, h, order):
    n = len(L)
    ans = [[F(i == j) for j in range(n)] for i in range(n)]
    term = [[F(i == j) for j in range(n)] for i in range(n)]
    for k in range(1, order+1):
        term = mult(term, L)
        scale = (-h)/k
        term = [[v*scale for v in row] for row in term]
        ans = [[ans[i][j]+term[i][j] for j in range(n)] for i in range(n)]
    return ans


def r(z, order):
    acc, term = 1, 1
    for k in range(1, order+1):
        term = term*(-z)/k
        acc += term
    return acc


def entries(parts, h, order):
    n = sum(parts)
    z = r(n*h, order)
    cross = (1-z)/n
    d, o = [], []
    for a in parts:
        q = n-a
        within = (1-z)/n + (z-r(q*h, order))/a
        d.append(within+r(q*h, order))
        o.append(within)
    return cross, d, o


def eta(n):
    lo, hi = 0.0, 4.0
    for _ in range(90):
        mid = (lo+hi)/2
        if r(mid, 3) > -1/(n-1):
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def rho4():
    lo, hi = 0.0, 4.0
    for _ in range(90):
        mid = (lo+hi)/2
        if mid**3-4*mid**2+12*mid-24 < 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def horizon(parts, order):
    n = sum(parts)
    if order == 2:
        return 2/n
    if order == 4:
        return rho4()/n
    vals = [eta(n)/n] if 1 in parts else []
    vals += [3/(2*n-a) for a in parts if a >= 2]
    return min(vals)


def all_min_entries(parts, h, order):
    cross, ds, os = entries(parts, h, order)
    vals = [cross] + ds + [o for a,o in zip(parts,os) if a>=2]
    return min(vals)


def main():
    exact = 0
    for n in range(2,9):
        for parts in partitions(n):
            if len(parts) < 2:
                continue
            L, tag = lap(parts)
            for order in (2,3,4):
                for h in (F(1,11),F(3,8),F(4,5)):
                    A = matrix_taylor(L,h,order)
                    c,ds,os = entries(parts,h,order)
                    for i in range(n):
                        for j in range(n):
                            want = ds[tag[i]] if i==j else os[tag[i]] if tag[i]==tag[j] else c
                            assert A[i][j] == want, (parts,order,h,i,j,A[i][j],want)
                            exact += 1
                    assert all(sum(row)==1 for row in A)
    phase = 0
    for n in range(2,18):
        for parts in partitions(n):
            if len(parts)<2:
                continue
            for order in (2,3,4):
                hstar = horizon(parts,order)
                assert isfinite(hstar) and hstar>0
                assert all_min_entries(parts,hstar*0.999,order)>-1.e-10,(parts,order,'below')
                assert all_min_entries(parts,hstar*1.001,order)<-1.e-10,(parts,order,'above')
                phase += 1
    for n in range(4,18):
        vals = [(horizon(part,3),part) for part in partitions(n) if len(part)>=2]
        lo = min(v for v,_ in vals)
        assert abs(lo-3/(2*n-2))<1e-12, (n,lo)
        if n>=6:
            hi=max(v for v,_ in vals)
            expected=3/(2*n-n//2)
            assert abs(hi-expected)<1e-12,(n,hi,expected)
            winners=[part for v,part in vals if abs(v-hi)<1e-12]
            assert winners==[(n-n//2,n//2)],(n,winners)
    assert abs(rho4()-2.7852935634052816)<1e-12
    for n in range(2,31):
        if n<=3:
            assert eta(n)>2
        elif n==4:
            assert abs(eta(n)-2)<1e-14
        else:
            assert eta(n)<2
    print('PASS exact matrix entries:',exact)
    print('PASS phase-transition cases:',phase)
    print('rho4:',format(rho4(),'.15f'))
    print('PASS finite checks supplement the all-size algebraic proof')


if __name__=='__main__':
    main()
