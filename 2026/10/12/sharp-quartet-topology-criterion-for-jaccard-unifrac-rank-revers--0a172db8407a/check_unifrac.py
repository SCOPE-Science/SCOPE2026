#!/usr/bin/env python3
"""Exact-rational check of a four-tip phylogenetic beta-diversity ordering criterion.

No external dependencies. Every community is a nonempty subset of tip labels.
Branch incidence, not precomputed score tables, defines UniFrac.
"""
from fractions import Fraction as F
from itertools import combinations

def tree(kind, a, b):
    if kind == 'balanced':
        assert 0 < a < 1 and 0 < b < 1
        return [({1, 2}, a), ({3, 4}, b), ({1}, 1-a),
                ({2}, 1-a), ({3}, 1-b), ({4}, 1-b)]
    assert kind == 'caterpillar' and 0 < a < b < 1
    return [({1}, F(1)), ({2, 3, 4}, a), ({2}, 1-a),
            ({3, 4}, b-a), ({3}, 1-b), ({4}, 1-b)]

def scores(A, B, branches):
    assert A != B and A and B
    j = F(len(A ^ B), len(A | B))
    both = [(int(bool(A & cl)), int(bool(B & cl)), w)
            for cl, w in branches]
    numerator = sum((w for x, y, w in both if x != y), F(0))
    denominator = sum((w for x, y, w in both if x or y), F(0))
    assert denominator > 0
    return j, numerator / denominator

def has_reversal(branches, r):
    assemblages = list(map(set, combinations(range(1, 5), r)))
    items = [scores(A, B, branches)
             for A, B in combinations(assemblages, 2)]
    return any((j-k)*(u-v) < 0
               for (j,u),(k,v) in combinations(items,2))

def check(kind, a, b):
    branches = tree(kind, a, b)
    a, b = F(a), F(b)
    asms = list(map(set, combinations(range(1,5),2)))
    scores2 = [scores(A,B,branches) for A,B in combinations(asms,2)]
    overlaps = [u for j,u in scores2 if j == F(2,3)]
    disjoint = [u for j,u in scores2 if j == F(1)]
    assert len(overlaps)==12 and len(disjoint)==3
    if kind == 'balanced':
        f=lambda t:(2-t)/(3-t)
        g=lambda t:2*(1-t)/(3-t)
        cross=2*(2-a-b)/(4-a-b)
        expected_overlap=sorted([f(a)]*4 + [f(b)]*4 + [g(a)]*2 + [g(b)]*2)
        expected_disjoint=sorted([F(1),cross,cross])
        expected=(a+b)*(4-min(a,b))>4
    else:
        f=lambda t:(2-t)/(3-t)
        g=lambda t:2*(1-t)/(3-t)
        h=2*(1-b)/(3-a-b)
        k=(2-a-b)/(3-a-b)
        d1=(4-2*a-b)/(4-a-b)
        d2=(4-a-2*b)/(4-a-b)
        expected_overlap=sorted([f(a)]*4+[g(a)]*2+[f(b)]*2+[g(b),h,k,k])
        expected_disjoint=sorted([d1,d2,d2])
        expected=False
    assert sorted(overlaps)==expected_overlap
    assert sorted(disjoint)==expected_disjoint
    actual=has_reversal(branches,2)
    assert actual==expected
    assert (min(disjoint)<max(overlaps))==expected
    assert not has_reversal(branches,1)
    assert not has_reversal(branches,3)
    # Every distinct pair at richness 1 or 3 has the same Jaccard score.
    return expected, len(scores2)

def main():
    n=0; yes=0; pair_cases=0
    for a_int in range(1,40):
        for b_int in range(1,40):
            a,b=F(a_int,40),F(b_int,40)
            for kind in ('balanced','caterpillar'):
                if kind=='caterpillar' and a>=b:continue
                result,cases=check(kind,a,b)
                n+=1;yes+=int(result);pair_cases+=cases
    # Independent rational test at the strict boundary and on both sides.
    assert check('balanced',F(3,4),F(3,4))[0]
    assert not check('balanced',F(1,2),F(1,2))[0]
    assert not check('caterpillar',F(1,4),F(3,4))[0]
    assert not check('balanced',F(1,10),F(1,10))[0]
    # Explicit common-reference witness for equal crown stem length 3/4.
    t=F(3,4);br=tree('balanced',t,t)
    assert scores({1,3},{2,4},br)==(F(1),F(2,5))
    assert scores({1,3},{1,2},br)==(F(2,3),F(5,9))
    print(f'VERIFY_OK profiles={n} classifies_reversal={yes} direct_pair_scores={pair_cases}')

if __name__=='__main__':main()
