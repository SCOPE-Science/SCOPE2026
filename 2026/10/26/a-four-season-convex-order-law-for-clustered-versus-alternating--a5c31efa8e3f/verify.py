"""Exact rational checks for four-season Beverton--Holt capacity orderings.

This finite computation supplements, but does not replace, the all-parameter proof.
Run with: python verify.py > certificate.json
"""
from fractions import Fraction as F
from itertools import combinations
import json


def periodic_inverse(R, capacity_sequence):
    a = 1 / R
    b = [(1-a) / K for K in capacity_sequence]
    n = len(b)
    y = sum(a**(n-1-j)*b[j] for j in range(n))/(1-a**n)
    out = []
    for bj in b:
        out.append(y)
        y = a*y + bj
    assert y == out[0]
    return out


def check(R, low, high):
    assert R>1 and 0<low<high
    A = periodic_inverse(R, [high,low,high,low])
    B = periodic_inverse(R, [high,high,low,low])
    aa = sorted(A,reverse=True)
    bb = sorted(B,reverse=True)
    assert sum(aa)==sum(bb)
    assert all(sum(bb[:j])>sum(aa[:j]) for j in range(1,4))
    assert sum(1/z for z in B)>sum(1/z for z in A)
    assert 1/max(B)<1/max(A)
    assert 1/min(B)>1/min(A)
    c=(1/high+1/low)/2
    d=(1/low-1/high)/2
    a=1/R
    D=(1-a)/(1+a)
    Bcoeff=(1-a*a)/(1+a*a)
    Ccoeff=(1-a)**2/(1+a*a)
    assert aa==[c+D*d,c+D*d,c-D*d,c-D*d]
    assert bb==[c+Bcoeff*d,c+Ccoeff*d,c-Ccoeff*d,c-Bcoeff*d]
    assert (sum((z-c)**2 for z in B)/sum((z-c)**2 for z in A)) == (1+a)**2/(1+a*a)
    # Every allocation of two high seasons is a rotation of exactly one class.
    all_classes=[]
    for subset in combinations(range(4),2):
        k=[high if j in subset else low for j in range(4)]
        ys=periodic_inverse(R,k)
        assert sorted(ys,reverse=True) in (aa,bb)
        all_classes.append('alternating' if sorted(ys,reverse=True)==aa else 'clustered')
    assert all_classes.count('alternating')==2
    assert all_classes.count('clustered')==4
    return {'growth':str(R),'low_capacity':str(low),'high_capacity':str(high),
            'alternating_inverse':list(map(str,aa)),
            'clustered_inverse':list(map(str,bb)),
            'mean_population_alternating':str(sum(1/z for z in A)/4),
            'mean_population_clustered':str(sum(1/z for z in B)/4),
            'inverse_variance_ratio':str((1+a)**2/(1+a*a))}

if __name__ == '__main__':
    cases=[(F(3,2),F(1),F(2)),(F(2),F(1),F(10)),
           (F(5),F(3),F(7)),(F(7,3),F(2),F(19))]
    result={'schema':'exact_rational_four_season_checks_v1',
            'scope':'finite parameter examples; symbolic proof is in RESULT.md',
            'cases':[check(*case) for case in cases]}
    print(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True))
