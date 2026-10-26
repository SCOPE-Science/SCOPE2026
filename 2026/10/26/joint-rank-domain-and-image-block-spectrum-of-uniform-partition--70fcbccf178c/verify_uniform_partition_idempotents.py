#!/usr/bin/env python3
"""Finite checks for the uniform-partition idempotent profile.

Run: python3 verify_uniform_partition_idempotents.py
No third-party packages or external data are required.
"""
from collections import Counter
from itertools import product
from math import comb


def mult(a, b):
    out = Counter()
    for (r1,d1,k1), c1 in a.items():
        for (r2,d2,k2), c2 in b.items():
            out[(r1+r2,d1+d2,k1+k2)] += c1*c2
    return out


def component(j, n):
    """Polynomial weight of a connected component on j labeled blocks.

    A nonempty component has one image-bearing block and j-1 satellites.
    The only other allowed component is a single entirely undefined block.
    """
    out = Counter()
    if j == 1:
        out[(0,0,0)] = 1
    for r in range(1,n+1):
        root = Counter({(r,r+h,1):comb(n,r)*comb(n-r,h)*r**h
                        for h in range(n-r+1)})
        satellite = Counter({(0,h,0):comb(n,h)*r**h for h in range(1,n+1)})
        for _ in range(j-1):
            root = mult(root, satellite)
        for key, val in root.items():
            out[key] += j*val  # choice of the centered block
    return out


def egf_coefficients(m, n):
    """Use the labeled exponential formula through its block-1 recurrence."""
    polys = [Counter({(0,0,0):1})]
    parts = [None] + [component(j,n) for j in range(1,m+1)]
    for size in range(1,m+1):
        ans = Counter()
        for j in range(1,size+1):
            ways = comb(size-1,j-1)
            for key, value in mult(parts[j], polys[size-j]).items():
                ans[key] += ways*value
        polys.append(ans)
    return polys[m]


def direct_partial_maps(m, n):
    """Enumerate actual partial functions, test preservation and f^2=f."""
    N=m*n
    counts = Counter()
    for f in product(range(-1,N), repeat=N):
        target = {}
        allowed = True
        for x, y in enumerate(f):
            if y == -1:
                continue
            src_block, dst_block = x//n, y//n
            if src_block in target and target[src_block] != dst_block:
                allowed = False
                break
            target[src_block] = dst_block
            if f[y] != y:
                allowed = False
                break
        if not allowed:
            continue
        images = {y for y in f if y >= 0}
        rank = len(images)
        domain = sum(y >= 0 for y in f)
        image_blocks = len({y//n for y in images})
        counts[(rank,domain,image_blocks)] += 1
    return counts


def expected_full_idempotents(m, n):
    """The classical full-map rooted-block decomposition (not using partial maps)."""
    f = [1]
    for z in range(1,m+1):
        value=0
        for j in range(1,z+1):
            rooted = sum(comb(n,r)*r**(n-r) * (r**n)**(j-1)
                         for r in range(1,n+1))
            value += comb(z-1,j-1)*j*rooted*f[z-j]
        f.append(value)
    return f[m]


def main():
    small = [(1,1),(1,4),(4,1),(2,2),(3,2),(2,3)]
    for m,n in small:
        a = egf_coefficients(m,n)
        b = direct_partial_maps(m,n)
        assert a == b, ('trivariate mismatch',m,n,a-b,b-a)
        assert a[(0,0,0)] == 1
        assert sum(v for (r,d,k),v in a.items() if r==1) == m*n*2**(m*n-1)
        assert a[(m*n,m*n,m)] == 1
        full = sum(v for (r,d,k),v in a.items() if d == m*n)
        assert full == expected_full_idempotents(m,n)
        if n>=2:
            assert sum(v for (r,d,k),v in a.items() if r==m*n-1) == m*n*n
        print('m=%d n=%d: %d profile cells; %d idempotents; %d full; exact' %
              (m,n,len(a),sum(a.values()),full))
    for m,n in [(3,3),(4,2),(5,2),(2,5)]:
        a=egf_coefficients(m,n)
        assert sum(v for (r,d,k),v in a.items() if r==1) == m*n*2**(m*n-1)
        assert sum(v for (r,d,k),v in a.items() if d==m*n) == expected_full_idempotents(m,n)
        assert sum(v for (r,d,k),v in a.items() if r==m*n-1) == m*n*n
        print('m=%d n=%d: %d profile cells; %d idempotents; full specialization exact' %
              (m,n,len(a),sum(a.values())))
    print('VERIFY_OK_UNIFORM_PARTITION_PARTIAL_IDEMPOTENT_TRIVARIATE')

if __name__=='__main__':
    main()
