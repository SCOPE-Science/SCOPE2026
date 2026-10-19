#!/usr/bin/env python3
"""Independent exact census of directed zero-product triangles among finite-field projections.

Only standard-library Python is required. Run: python check_triangles.py
"""
from collections import Counter
from functools import lru_cache
from itertools import product


def ff_add(x, y, q):
    return x ^ y if q == 4 else (x + y) % q


def ff_mul(x, y, q):
    if q != 4:
        return x * y % q
    # F_4 = F_2[t]/(t^2+t+1), represented by binary coefficients.
    z = 0
    while y:
        if y & 1:
            z ^= x
        y >>= 1
        x <<= 1
        if x & 4:
            x ^= 7
    return z


def ff_inv(x, q):
    assert x != 0
    return next(y for y in range(1, q) if ff_mul(x, y, q) == 1)


def matrix_product(A, B, n, q):
    out = []
    for i in range(n):
        for j in range(n):
            z = 0
            for k in range(n):
                z = ff_add(z, ff_mul(A[i*n+k], B[k*n+j], q), q)
            out.append(z)
    return tuple(out)


def matrix_rank(A, n, q):
    rows = [list(A[n*i:n*i+n]) for i in range(n)]
    pivots = 0
    for col in range(n):
        pivot = next((i for i in range(pivots, n) if rows[i][col] != 0), None)
        if pivot is None:
            continue
        rows[pivots], rows[pivot] = rows[pivot], rows[pivots]
        inverse = ff_inv(rows[pivots][col], q)
        rows[pivots] = [ff_mul(v, inverse, q) for v in rows[pivots]]
        for i in range(n):
            if i != pivots and rows[i][col]:
                factor = rows[i][col]
                rows[i] = [ff_add(rows[i][j], ff_mul(factor, rows[pivots][j], q), q) if q == 4 else (rows[i][j] - factor * rows[pivots][j]) % q for j in range(n)]
        pivots += 1
        if pivots == n:
            break
    return pivots


@lru_cache(None)
def gaussian(n, k, q):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return gaussian(n-1, k, q) + q**(n-k) * gaussian(n-1, k-1, q)


def surjections(r, u, q):
    z = 1
    for i in range(u):
        z *= q**r - q**i
    return z


def predicted(n, q):
    ans = {}
    for r in range(n+1):
        for s in range(n+1):
            for t in range(n+1):
                if r+s > n:
                    ans[r,s,t] = 0
                    continue
                total = 0
                for u in range(min(r,s)+1):
                    if t > n-r-s+u:
                        continue
                    total += gaussian(s,u,q) * surjections(r,u,q) * gaussian(n-r-s+u,t,q) * q**(t*(n-t-u))
                ans[r,s,t] = (gaussian(n,r,q) * q**(r*(n-r))
                                * gaussian(n-r,s,q) * q**(s*(n-r-s)) * total)
    return ans


def exhaustive(n, q):
    idempotents = []
    for mat in product(range(q), repeat=n*n):
        if matrix_product(mat,mat,n,q) == mat:
            idempotents.append(mat)
    m = len(idempotents)
    ranks = [matrix_rank(M,n,q) for M in idempotents]
    zero = (0,)*(n*n)
    out = [0] * m
    inp = [0] * m
    for i, A in enumerate(idempotents):
        for j, B in enumerate(idempotents):
            if matrix_product(A,B,n,q) == zero:
                out[i] |= (1 << j)
                inp[j] |= (1 << i)
    masks = [0] * (n+1)
    for i,r in enumerate(ranks):
        masks[r] |= 1 << i
    observed = Counter()
    for i in range(m):
        for j in range(m):
            if (out[i] >> j) & 1:
                options = out[j] & inp[i]
                for t in range(n+1):
                    observed[ranks[i],ranks[j],t] += (options & masks[t]).bit_count()
    reference = predicted(n,q)
    diff = [(k, observed[k], v) for k,v in reference.items() if observed[k] != v]
    if diff:
        raise AssertionError(f'Failed (n,q)={(n,q)}; mismatches={diff[:8]}')
    for (r,s,t),c in observed.items():
        assert c == observed[(s,t,r)] == observed[(t,r,s)], (r,s,t)
    positive_rank_triplets = {(r,s,t) for (r,s,t),count in observed.items() if count and min(r,s,t)>0}
    expected_support = {(r,s,t) for r in range(1,n) for s in range(1,n) for t in range(1,n)
                        if r+s<=n and s+t<=n and t+r<=n}
    assert positive_rank_triplets == expected_support, (positive_rank_triplets,expected_support)
    E = sum(gaussian(n,r,q)*q**(r*(n-r)) for r in range(n+1))
    assert m == E, (n,q,m,E)
    print(f'CASE n={n} q={q}: {m} idempotents, {m*m} ordered pair tests, '
          f'{m*m*m} logically covered ordered triples; exact rank coefficients, cyclic symmetry, and support PASS')
    return observed


def main():
    tests = [(1,2),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)]
    for n,q in tests:
        exhaustive(n,q)
    # Formula-only checks for dimensions where cubic enumeration is larger.
    for n,q in [(5,2),(6,2),(5,3),(4,4)]:
        tab = predicted(n,q)
        for (r,s,t), x in tab.items():
            assert x == tab[(s,t,r)] == tab[(t,r,s)]
            if min(r,s,t)>0:
                assert (x>0) == (r+s<=n and s+t<=n and t+r<=n)
        print(f'FORMULA n={n} q={q}: cyclic symmetry and exact support PASS')
    print('ALL_EXACT_CHECKS_PASSED')


if __name__=='__main__':
    main()
