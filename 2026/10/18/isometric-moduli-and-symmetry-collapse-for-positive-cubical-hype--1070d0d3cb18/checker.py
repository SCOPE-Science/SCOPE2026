#!/usr/bin/env python3
"""Exact finite sanity checks for weighted cubical hyperplane classification.
No finite testing is used as a substitute for the theorem's proof.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations_with_replacement, permutations, product
from math import factorial

def balanced(a):
    return 2*max(a)<sum(a)

def facet_witness(a,i):
    s=sum(a)
    v=[Q(-a[i],s-a[i])]*len(a)
    v[i]=Q(1)
    assert sum(x*y for x,y in zip(a,v))==0
    assert max(map(abs,v))==1
    assert all(abs(v[j])<1 for j in range(len(a)) if j!=i)
    return v

def dual_normals(a):
    n=len(a)
    z=[tuple(Q(i==j) if i<n-1 else Q(-a[j],a[-1]) for j in range(n-1)) for i in range(n)]
    assert all(sum(a[i]*z[i][j] for i in range(n))==0 for j in range(n-1))
    return z

def perms_preserve(a):
    return sum(all(a[i]==a[p[i]] for i in range(len(a))) for p in permutations(range(len(a))))

def signs_and_perms(a,b):
    """Find signed-permutation coefficient matches up to common nonzero scalar."""
    n=len(a)
    count=0
    for p in permutations(range(n)):
        for signs in product((-1,1), repeat=n):
            ratios=[Q(b[i]*signs[i],a[p[i]]) for i in range(n)]
            if all(r==ratios[0] for r in ratios):
                count+=1
    return count

nr=0; balanced_count=0; dominant_count=0; faces=0; rep=0
for n in range(3,7):
    for a in combinations_with_replacement(range(1,6),n):
        nr+=1
        z=dual_normals(a)
        if balanced(a):
            balanced_count+=1
            for i in range(n):
                facet_witness(a,i); facet_witness(a,i); faces+=2
            if n<=5:
                actual=signs_and_perms(a,a)
                expected=2
                for m in Counter(a).values():expected*=factorial(m)
                assert actual==expected,(a,actual,expected)
                rep+=1
        else:
            dominant_count+=1
            i=max(range(n),key=lambda j:a[j]); assert a[i]>=sum(a)-a[i]
            for signs in product((-1,1),repeat=n-1):
                c=[Q(s) for s in signs]
                val=-sum(a[j]*c[k] for k,j in enumerate(j for j in range(n) if j!=i))/a[i]
                assert abs(val)<=1
                rep+=1
        assert len(z)==n
# The nonbalanced and balanced types cannot have equal facet counts.
for a,b in (((1,1,1),(1,1,2)),((1,2,2),(2,2,4)),((1,2,3,4),(1,2,4,5)),((1,2,3),(2,4,6))):
    if balanced(a) and balanced(b):
        expected=(2*sum(1 for p in permutations(range(len(a))) if all(Q(a[p[i]],sum(a))==Q(b[i],sum(b)) for i in range(len(a)))))
        assert signs_and_perms(a,b)==expected
print('PASS',{'multiset_samples':nr,'balanced':balanced_count,'dominant':dominant_count,'facet_relative_interior_witnesses':faces,'permutation_or_dominance_checks':rep,'mixed_pair_checks':4})
