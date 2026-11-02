#!/usr/bin/env python3
"""Exact independent verification of a binary block-retrieval counterexample.
Uses no external packages; expected runtime below a second on a normal machine.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, combinations_with_replacement
from math import comb

F1 = frozenset((0, 1))
F2 = frozenset((0, 2, 4, 6))

def span(columns):
    ans = {0}
    for v in columns:
        ans |= {z ^ v for z in tuple(ans)}
    return frozenset(ans)

def subset_formula(cols, target):
    n = len(cols)
    h = sum((Fraction(1, j) for j in range(1,n+1)),Fraction(0))
    E = n*h
    for s in range(1,n):
        good = sum(target.issubset(span(cols[j] for j in S))
                   for S in combinations(range(n),s))
        E -= Fraction(good, comb(n-1,s))
    return E

def dynamic_formula(cols, target):
    n = len(cols)
    states = {span(cols[j] for j in range(n) if mask >> j & 1)
              for mask in range(1 << n)}
    states = sorted(states, key=lambda S: -len(S))
    E = {}
    for state in states:
        if target.issubset(state):
            E[state] = Fraction(0)
            continue
        inside = sum(v in state for v in cols)
        assert inside < n
        num = Fraction(n)
        for v in cols:
            if v not in state:
                num += E[span(tuple(state)+(v,))]
        E[state] = num / (n-inside)
    return E[frozenset((0,))]

def get_costs(cols):
    a = subset_formula(cols,F1)
    b = subset_formula(cols,F2)
    assert (a,b) == (dynamic_formula(cols,F1),dynamic_formula(cols,F2))
    return a,b

def main():
    base=(1,1,2,4)
    assert span(base)==frozenset(range(8))
    assert get_costs(base)==(Fraction(2),Fraction(6))
    total=0
    mcount=Counter()
    e1min={}
    low=[]
    for cols in combinations_with_replacement(range(8),5):
        if span(cols)!=frozenset(range(8)):
            continue
        total+=1
        m=cols.count(1)
        mcount[m]+=1
        e1,e2=get_costs(cols)
        e1min[m]=min(e1min.get(m,e1),e1)
        assert (e1>2) or (e1==Fraction(5,3) and e2>=Fraction(15,2))
        if e1<=2:low.append((e1,e2,cols))
    assert total==476
    assert len(low)==12
    assert all(e1==Fraction(5,3) for e1,e2,cols in low)
    assert min(e2 for e1,e2,cols in low)==Fraction(15,2)
    assert mcount==Counter({0:241, 1:167, 2:56, 3:12})
    print('VERIFY_OK')
    print('base_expected_times=2,6')
    print('full_rank_five_column_multisets=',total)
    print('multiplicity_of_e1_counts=',dict(sorted(mcount.items())))
    print('minimum_E1_by_multiplicity=',{k:str(v) for k,v in sorted(e1min.items())})
    print('codebooks_with_E1_at_most_2=',len(low))
    print('minimum_E2_among_them=',min(e2 for e1,e2,cols in low))

if __name__=='__main__':main()
