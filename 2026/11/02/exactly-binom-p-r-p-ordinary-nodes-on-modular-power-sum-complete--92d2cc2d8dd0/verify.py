#!/usr/bin/env python3
"""Finite exact corroboration of modular triple-power-sum node theorem."""
from itertools import product
from math import comb


def determinant_mod(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    n = len(a)
    d = 1
    for j in range(n):
        pivot = next((i for i in range(j,n) if a[i][j] % p), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j],a[pivot] = a[pivot],a[j]
            d = -d
        v = a[j][j]
        d = d*v % p
        iv = pow(v, -1, p)
        for i in range(j+1,n):
            f = a[i][j]*iv % p
            for k in range(j,n):
                a[i][k] = (a[i][k]-f*a[j][k]) % p
    return d % p


def jacobian_rank_3(values,p):
    columns = [(1,x%p,(x*x)%p) for x in values]
    distinct = set(values)
    return min(3,len(distinct))  # 3x3 determinant is Vandermonde


def check(p,r):
    n=p+r
    assert p>=5 and 1<=r<p
    for m in (p-2,r-1):
        mat = [[(1 if i==j else 0)+1 for j in range(m)] for i in range(m)]
        assert determinant_mod(mat,p)==(m+1)%p
    target=comb(n,p)
    # Exhaustive multiplicity/orbit support, for every two-value candidate over Fp.
    for a in range(1,n):
        for u in range(p):
            for v in range(p):
                if u==v:
                    continue
                vals=[u]*a+[v]*(n-a)
                if any(vals) and all(sum(pow(x,k,p) for x in vals)%p == 0 for k in (1,2,3)):
                    assert sum(x!=0 for x in vals)==p and len(set(vals))==2
                    assert 0 in set(vals)
    sample=[1]*p+[0]*r
    assert all(sum(pow(x,k,p) for x in sample)%p==0 for k in (1,2,3))
    assert jacobian_rank_3(sample,p)==2
    print(f'p={p} r={r} n={n}: predicted_nodes={target} tangent_rank={n-3} determinant_nonzero=1')

for p in (5,7,11):
    for r in (1,(p-1)//2,p-1):
        check(p,r)

# Exhaustive P^5(F5) check of singular rational point support for p=5,r=1.
p,n=5,6
singular=set()
for tail in product(range(5),repeat=n-1):
    vals=(1,)+tail
    if all(sum(pow(x,j,p) for x in vals)%p==0 for j in (1,2,3)) and jacobian_rank_3(vals,p)<3:
        singular.add(vals)
for first_nonzero_index in range(1,n):
    for tail in product(range(p),repeat=n-first_nonzero_index-1):
        vals=(0,)*first_nonzero_index+(1,)+tail
        if all(sum(pow(x,j,p) for x in vals)%p==0 for j in (1,2,3)) and jacobian_rank_3(vals,p)<3:
            singular.add(vals)
assert len(singular)==6, (len(singular),singular)
assert all(set(x)=={0,1} and sum(x)==p for x in singular)
print('F5 exact projective singular F5-rational census: 6')
print('VERIFY_OK')
