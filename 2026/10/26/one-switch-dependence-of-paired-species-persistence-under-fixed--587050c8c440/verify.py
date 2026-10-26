"""Reproduce exact finite checks for the fixed-quota co-survival theorem.

Python 3 standard library; no external packages or data.
"""
from fractions import Fraction
from itertools import combinations
from math import comb
import hashlib
import json


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def covariance(n, a, b, h, q):
    total = choose(n, q)
    da = Fraction(choose(n-a, q), total)
    db = Fraction(choose(n-b, q), total)
    dab = Fraction(choose(n-a-b+h, q), total)
    return dab-da*db


def sign(x):
    return (x > 0)-(x < 0)


def expected_pattern(n, a, b, h):
    Q = n-max(a,b)
    signs = [sign(covariance(n,a,b,h,q)) for q in range(1,Q+1)]
    if not signs:
        return signs
    if h==0 or (h<min(a,b) and n*h<a*b):
        assert all(z==-1 for z in signs)
    elif h<min(a,b) and n*h==a*b:
        assert signs[0]==0 and all(z==-1 for z in signs[1:])
    elif h==min(a,b):
        assert all(z==1 for z in signs)
    else:
        assert 0<h<min(a,b) and n*h>a*b
        assert signs[0]==1 and signs[-1]==-1
        nonzero=[z for z in signs if z]
        assert nonzero==sorted(nonzero,reverse=True)
        assert signs.count(0)<=1
    return signs


def main():
    exact_patterns=0
    covariance_compares=0
    reversals=0
    zero_cases=0
    exhaustive_sets=0
    exhaustive_samples=0
    digest=hashlib.sha256()
    for n in range(2,51):
        for a in range(1,n):
            for b in range(1,n):
                for h in range(max(0,a+b-n),min(a,b)+1):
                    signs=expected_pattern(n,a,b,h)
                    exact_patterns+=1
                    covariance_compares+=len(signs)
                    reversals+= int(1 in signs and -1 in signs)
                    zero_cases+=int(0 in signs)
                    digest.update(f'{n},{a},{b},{h}:{"".join("+" if s>0 else "-" if s<0 else "0" for s in signs)}\n'.encode())
                    if n<=8:
                        A=set(range(a))
                        B=set(range(h))|set(range(a,a+b-h))
                        assert len(B)==b and len(A&B)==h
                        for q in range(n+1):
                            subsets=list(combinations(range(n),q))
                            p=Fraction(sum(bool(A.intersection(s)) for s in subsets),len(subsets))
                            r=Fraction(sum(bool(B.intersection(s)) for s in subsets),len(subsets))
                            pair=Fraction(sum(bool(A.intersection(s)) and bool(B.intersection(s)) for s in subsets),len(subsets))
                            assert pair-p*r==covariance(n,a,b,h,q)
                            exhaustive_samples+=len(subsets)
                            exhaustive_sets+=1
    assert covariance(5,2,2,1,1)==Fraction(1,25)
    assert covariance(5,2,2,1,2)==Fraction(1,100)
    assert covariance(5,2,2,1,3)==Fraction(-1,100)
    assert covariance(5,2,2,1,4)==0
    for n in range(2,5):
        for a in range(1,n):
            for b in range(1,n):
                for h in range(max(0,a+b-n),min(a,b)+1):
                    x=expected_pattern(n,a,b,h)
                    assert not (1 in x and -1 in x)
    output={
        'certificate_kind':'exact_finite_reproduction',
        'formula':'Cov(1[T meets A],1[T meets B]) = (C(n-a-b+h,q)*C(n,q)-C(n-a,q)*C(n-b,q))/C(n,q)^2',
        'parameter_range':'2<=n<=50; 1<=a,b<n; max(0,a+b-n)<=h<=min(a,b)',
        'parameter_cases':exact_patterns,
        'nonstrivial_sign_checks':covariance_compares,
        'positive_to_negative_cases':reversals,
        'cases_with_zero_covariance_within_nondegenerate_range':zero_cases,
        'exhaustive_subsample_size_cases_through_n8':exhaustive_sets,
        'enumerated_uniform_subsets_through_n8':exhaustive_samples,
        'smallest_example':{'n':5,'a':2,'b':2,'overlap':1,'covariances_for_q1_to4':['1/25','1/100','-1/100','0']},
        'pattern_sha256':digest.hexdigest(),
        'qualification':'Finite checks support but do not prove the all-size theorem.'
    }
    print(json.dumps(output,sort_keys=True,indent=2))

if __name__=='__main__':
    main()
