#!/usr/bin/env python3
"""Independent small-instance verification of rook-graph power domination.

Usage: python3 verify.py. No third-party dependencies or input files.
"""
from collections import Counter
from fractions import Fraction
from math import comb, factorial


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def counted_coefficient(m, n, k):
    # Exactly 0 or 1 empty rows, irrespective of columns.
    ar = sum(choose(m,a) * sum((-1)**i * choose(m-a,i)
              * choose(n*(m-a-i),k) for i in range(m-a+1))
              for a in (0,1))
    ac = sum(choose(n,b) * sum((-1)**j * choose(n-b,j)
              * choose(m*(n-b-j),k) for j in range(n-b+1))
              for b in (0,1))
    both = sum(choose(m,a)*choose(n,b)*
              sum((-1)**(i+j)*choose(m-a,i)*choose(n-b,j)*
                  choose((m-a-i)*(n-b-j),k)
                  for i in range(m-a+1) for j in range(n-b+1))
              for a in (0,1) for b in (0,1))
    return ar + ac - both


def rook_neighborhoods(m, n):
    return [sum(1 << (u*n+v) for u in range(m) for v in range(n)
                if (u==i or v==j) and (u,v)!=(i,j))
            for i in range(m) for j in range(n)]


def direct_power_dominates(selected, nbrs):
    size=len(nbrs)
    full=(1<<size)-1
    observed=selected
    for v in range(size):
        if (selected>>v)&1:
            observed |= nbrs[v]
    while observed!=full:
        new=0
        for v in range(size):
            if (observed>>v)&1:
                missing=nbrs[v] & (full^observed)
                if missing and missing & (missing-1)==0:
                    new |= missing
        if not new:
            break
        observed|=new
    return observed==full


def criterion(mask,m,n):
    rows=0;cols=0
    for i in range(m):
        for j in range(n):
            if (mask>>(i*n+j))&1:
                rows |= 1<<i
                cols |= 1<<j
    return rows.bit_count() >= m-1 or cols.bit_count() >= n-1


def verify_small(m,n):
    nbrs=rook_neighborhoods(m,n)
    cnt=Counter()
    for mask in range(1<<(m*n)):
        d=direct_power_dominates(mask,nbrs)
        c=criterion(mask,m,n)
        if d!=c:
            raise AssertionError((m,n,mask,d,c))
        if d:
            cnt[mask.bit_count()]+=1
    for k in range(m*n+1):
        assert cnt[k]==counted_coefficient(m,n,k),(m,n,k,cnt[k],counted_coefficient(m,n,k))
    mind=min(cnt)
    assert mind==min(m,n)-1
    predicted=(m*(n**(m-1)) if m<n else n*(m**(n-1)) if m>n else 2*(n**n)-(n**2)*factorial(n-1))
    assert cnt[mind]==predicted,(m,n,cnt[mind],predicted)
    print('FULL_OK',m,n,'minimum',mind,'min_sets',cnt[mind],
          'total',sum(cnt.values()), 'coefficients', dict(sorted(cnt.items())))


def check_joint_moments(m=3,n=4):
    p=Fraction(1,3)
    outcomes=[(mask, p**mask.bit_count()*(1-p)**(m*n-mask.bit_count()))
              for mask in range(1<<(m*n))]
    def falling(x,r):
        z=1
        for t in range(r):z*=x-t
        return z
    for r in range(3):
        for s in range(3):
            total=Fraction(0)
            for mask,prob in outcomes:
                empty_rows=sum(not any((mask>>(i*n+j))&1 for j in range(n)) for i in range(m))
                empty_cols=sum(not any((mask>>(i*n+j))&1 for i in range(m)) for j in range(n))
                total+=prob*falling(empty_rows,r)*falling(empty_cols,s)
            predicted=falling(m,r)*falling(n,s)*(1-p)**(n*r+m*s-r*s)
            assert total==predicted,(r,s,total,predicted)
    print('EXACT_JOINT_FACTORIAL_MOMENTS_OK',m,n)


def check_fixed_size_moments(m=3,n=4,t=4):
    # Uniform sampling without replacement: enumerate all equally likely subsets.
    from itertools import combinations
    bits=range(m*n)
    masks=[sum(1<<v for v in selected) for selected in combinations(bits,t)]
    def falling(x,r):
        v=1
        for a in range(r): v*=x-a
        return v
    for r in range(3):
        for s in range(3):
            total=0
            for mask in masks:
                er=sum(not any((mask>>(i*n+j))&1 for j in range(n)) for i in range(m))
                ec=sum(not any((mask>>(i*n+j))&1 for i in range(m)) for j in range(n))
                total+=falling(er,r)*falling(ec,s)
            forbidden=n*r+m*s-r*s
            predicted=Fraction(falling(m,r)*falling(n,s)*choose(m*n-forbidden,t),choose(m*n,t))
            assert Fraction(total,len(masks))==predicted,(r,s,total,predicted)
    print('FIXED_SIZE_FACTORIAL_MOMENTS_OK',m,n,t)


def main():
    for m,n in ((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(4,3),(4,4)):
        verify_small(m,n)
    check_joint_moments()
    check_fixed_size_moments()
    print('ALL_VERIFY_OK')

if __name__=='__main__':
    main()
