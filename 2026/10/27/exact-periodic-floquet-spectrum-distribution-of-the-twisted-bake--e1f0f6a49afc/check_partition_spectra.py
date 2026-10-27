#!/usr/bin/env python3
"""Exact-integer spot checks for the stated twisted-baker spectral census."""
from itertools import combinations
from math import gcd, comb


def identity(d):
    return [[int(i == j) for j in range(d)] for i in range(d)]


def matmul(a, b):
    d = len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(d)) for j in range(d)] for i in range(d)]


def jacobians(d):
    left = identity(d)
    left[0][0] = 2
    right = [[0]*d for _ in range(d)]
    for j in range(d-1):
        right[j+1][j] = 1
    right[0][d-1] = -2
    return left, right


def charpoly(a):
    d = len(a)
    b = identity(d)
    result = [1]
    for i in range(1,d+1):
        v = matmul(a,b)
        tr = sum(v[j][j] for j in range(d))
        assert tr % i == 0
        coef = -tr//i
        result.append(coef)
        for j in range(d):
            v[j][j] += coef
        b=v
    return tuple(result)


def multiply_poly_high(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            z[i+j] += x*y
    return z


def weak_compositions(N,g):
    if g==1:
        yield (N,)
    else:
        for i in range(N+1):
            for tail in weak_compositions(N-i,g-1):
                yield (i,)+tail


def expected_polys(d,n,k):
    g=gcd(d,k)
    ell=d//g
    sign=(-1)**(k//g)
    out=set()
    for b in weak_compositions(n-k,g):
        poly=[1]
        for bi in b:
            factor=[1]+[0]*(ell-1)+[-sign*2**(k//g+bi)]
            poly=multiply_poly_high(poly,factor)
        out.add(tuple(poly))
    return out


def partition_count(N,g):
    def rec(v,last):
        if v==0:return 1
        if last==0:return 0
        return sum(rec(v-i,i) for i in range(min(last,v),0,-1))
    # partitions of N into at most g parts = parts of size at most g.
    return rec(N,g)


def check():
    comparisons=0
    classes=0
    for d in range(2,7):
        left,right=jacobians(d)
        for n in range(1,9):
            for k in range(1,n+1):
                target=expected_polys(d,n,k)
                realized=set()
                counts={}
                for inds in combinations(range(n),k):
                    inds=set(inds)
                    a=identity(d)
                    for j in range(n):
                        a=matmul((right if j in inds else left),a)
                    poly=charpoly(a)
                    assert poly in target,(d,n,k,tuple(sorted(inds)),poly,target)
                    realized.add(poly)
                    counts[poly] = counts.get(poly,0)+1
                    comparisons+=1
                assert realized==target,(d,n,k,target-realized)
                assert len(realized)==partition_count(n-k,gcd(d,k))
                g=gcd(d,k)
                q=k//g
                ell=d//g
                sign=(-1)**q
                predicted={}
                for b in weak_compositions(n-k,g):
                    poly=[1]
                    for bj in b:
                        poly=multiply_poly_high(poly,[1]+[0]*(ell-1)+[-sign*2**(q+bj)])
                    t=tuple(poly)
                    weight=comb(b[0]+q,q)
                    for bj in b[1:]:
                        weight*=comb(bj+q-1,q-1)
                    predicted[t]=predicted.get(t,0)+weight
                assert counts==predicted,(d,n,k,counts,predicted)
                assert sum(predicted.values())==comb(n,k)
                classes+=1
    print('CHECK_OK',comparisons,'exact Jacobian characteristic-polynomial comparisons,',classes,'exact spectral-frequency distributions')

if __name__=='__main__':check()
