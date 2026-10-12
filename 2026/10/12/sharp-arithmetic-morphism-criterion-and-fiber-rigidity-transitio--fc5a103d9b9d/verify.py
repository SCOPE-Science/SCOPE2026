#!/usr/bin/env python3
"""Independent finite verification of cardinality-threshold Boolean-algebra homomorphisms."""
from collections import Counter
from itertools import product, combinations
from math import factorial


def balanced_allowed(n,m,l,k):
    q,r=divmod(n,m)
    highest=(l-1)*q+min(l-1,r)
    lowest=l*q+max(0,l-(m-r))
    return highest < k <= lowest


def exact_count_by_partitions(n,m,l,k):
    total=0
    for lam in combinations(range(1,n),m-1):
        cuts=(0,)+lam+(n,)
        v=tuple(cuts[i+1]-cuts[i] for i in range(m))
        if tuple(sorted(v)) != v:continue
        if sum(v[:l]) <k or sum(v[m-l+1:])>=k:continue
        multi=Counter(v)
        denom=1
        for a in multi.values():denom*=factorial(a)
        arrangements=factorial(m)//denom
        denom2=1
        for a in v:denom2*=factorial(a)
        per=factorial(n)//denom2
        total+=arrangements*per
    return total


def direct_count(n,m):
    # Independent of the sorted-size inequalities: inspect all subsets of target
    # for every concrete function, checking the Boolean modal equation directly.
    masks_by_size=[[] for _ in range(m+1)]
    for mask in range(1<<m):masks_by_size[mask.bit_count()].append(mask)
    ans=Counter()
    maps=0
    for f in product(range(m),repeat=n):
        maps+=1
        preimage_sizes=[sum(bool(mask&(1<<f[x])) for x in range(n)) for mask in range(1<<m)]
        for l in range(1,m+1):
            for k in range(1,n+1):
                if all(((mask.bit_count()>=l)==(preimage_sizes[mask]>=k)) for mask in range(1<<m)):
                    ans[(l,k)]+=1
    return ans,maps


def main():
    map_tables=0
    tests=0
    positive=0
    for n in range(1,7):
        for m in range(1,7):
            direct,num=direct_count(n,m)
            map_tables+=num
            for l in range(1,m+1):
                for k in range(1,n+1):
                    observed=direct[(l,k)]
                    predicted=exact_count_by_partitions(n,m,l,k) if n>=m else 0
                    assert observed==predicted,(n,m,l,k,observed,predicted)
                    assert (observed>0)==(balanced_allowed(n,m,l,k) if n>=m else False),(n,m,l,k)
                    # Duality in cardinality thresholds.
                    assert observed==direct[(m-l+1,n-k+1)],(n,m,l,k)
                    if n==m:
                        assert observed==(factorial(n) if l==k else 0),(n,m,l,k,observed)
                    if observed:positive+=1
                    tests+=1
    direct9,_=direct_count(9,3)
    assert [direct9[(2,k)] for k in (4,5,6)]==[1680,11130,1680]
    expected=exact_count_by_partitions(9,3,2,5)
    assert expected==11130,expected
    assert exact_count_by_partitions(9,3,2,4)==1680
    assert exact_count_by_partitions(9,3,2,6)==1680
    print('VERIFY_OK direct_function_tables',map_tables,'threshold_parameter_comparisons',tests,
          'positive_hom_families',positive,'nine_to_three_direct_maps',19683,'nine_to_three_counts',(1680,11130,1680))

if __name__=='__main__':main()
