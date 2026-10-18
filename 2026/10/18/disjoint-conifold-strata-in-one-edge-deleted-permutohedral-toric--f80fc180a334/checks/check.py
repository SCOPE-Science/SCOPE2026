#!/usr/bin/env python3
"""Exact finite combinatorial checks for the graphical fan of K_n with edge {0,1} removed.

The infinite classification is proved in RESULT.md. This script verifies
small cases, integer ray relations, and the predicted maximal-cone counts.
"""
from itertools import permutations, combinations
from math import factorial
from collections import defaultdict
from sympy import Matrix


def rays_of_order(p):
    out=[]
    mask=0
    for x in p[:-1]:
        mask |= 1<<x
        out.append(mask)
    return out


def primitive_ray(mask, n):
    # Quotient Z^n/Z(1,...,1), identified using the last coordinate as zero.
    return Matrix([int(bool(mask & (1<<i))) - int(bool(mask & (1<<(n-1))))
                   for i in range(n-1)])


def review(n):
    seen={}
    for p in permutations(range(n)):
        i,j=p.index(0),p.index(1)
        if abs(i-j)==1:
            lo=min(i,j)
            canonical=p[:lo]+(-1,)+p[lo+2:]
            key=('block',canonical)
            if key not in seen:
                q=p[:lo]+(p[lo+1],p[lo])+p[lo+2:]
                seen[key]={'rays':set(rays_of_order(p))|set(rays_of_order(q)),
                           'S':frozenset(p[:lo]), 'lo':lo, 'p':p, 'q':q}
        else:
            seen[('linear',p)]={'rays':set(rays_of_order(p)), 'S':None,'p':p}

    assert len(seen)==factorial(n)-factorial(n-1)
    singular={}
    smooth_count=0
    for key,d in seen.items():
        rays=d['rays']
        s=d['S']
        if s is None or not s or len(s)==n-2:
            if s is not None and not s:
                # The {a,b} prefix is a non-extreme ray.
                rays.remove(3)
            if s is not None and len(s)==n-2:
                # The prefix comprising all vertices except {a,b} is non-extreme.
                rays.remove(sum(1<<i for i in s))
            assert len(rays)==n-1
            smooth_count+=1
            continue
        assert len(rays)==n
        S=sum(1<<i for i in s)
        core={S,S|1,S|2,S|3}
        assert core<=rays
        assert set(rays_of_order(d['p'])) | set(rays_of_order(d['q'])) == rays
        v={x:primitive_ray(x,n) for x in core}
        assert v[S]+v[S|3]==v[S|1]+v[S|2]
        # The 3-subcone is saturated: complete the braid-chain basis of the
        # adjacent permutation. Its determinant is exactly +1 or -1.
        B=Matrix.hstack(*(primitive_ray(x,n) for x in rays_of_order(d['p'])))
        assert abs(B.det())==1
        assert len(core)==4 and Matrix.hstack(*v.values()).rank()==3
        singular.setdefault(frozenset(s),[]).append(key)
    expected={frozenset(S) for r in range(1,n-2)
              for S in combinations(range(2,n),r)}
    assert set(singular)==expected
    assert len(singular)==2**(n-2)-2
    singular_count=sum(map(len,singular.values()))
    assert singular_count==(n-3)*factorial(n-2)
    for S,keys in singular.items():
        assert len(keys)==factorial(len(S))*factorial(n-2-len(S))
    assert smooth_count==(n*n-3*n+4)*factorial(n-2)
    print(f'n={n}: orientations={len(seen)}, singular_fixed={singular_count}, '
          f'smooth_fixed={smooth_count}, disjoint_core_components={len(singular)}')


for n in range(4,8):
    review(n)
print('VERIFY_OK')
