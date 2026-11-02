#!/usr/bin/env python3
"""Exact, self-contained verification of a finite lottery compatibility theorem.
Run: python3 verify_ternary.py ternary_lottery_witnesses.json
Requires Python 3 standard library only.
"""
import sys, json, itertools, math
from fractions import Fraction
from collections import Counter

def verify(path):
    with open(path, 'r', encoding='utf-8') as stream:
        certificates = json.load(stream)
    values = (1, 2, 3)
    columns = tuple(itertools.product(values, repeat=3))
    agent_perms = tuple(itertools.permutations(range(3)))
    assignments = tuple(itertools.product(range(3), repeat=4))
    owners = tuple(tuple(tuple(g for g in range(4) if a[g]==i) for i in range(3)) for a in assignments)
    factorial = math.factorial
    count = 0
    labeled_count = 0
    max_support = 0
    support_hist = Counter()
    each_agent_three_values = 0
    some_agent_three_values = 0
    for colset in itertools.combinations_with_replacement(columns, 4):
        orbit = {
            tuple(sorted(tuple(col[p] for p in perm) for col in colset))
            for perm in agent_perms
        }
        if colset != min(orbit):
            continue
        assert count < len(certificates)
        # Agent permutations of column-multisets, then all distinct item permutations.
        for cols in orbit:
            multiples = Counter(cols)
            labeled_count += factorial(4)//math.prod(factorial(mult) for mult in multiples.values())
        v = tuple(tuple(col[i] for col in colset) for i in range(3))
        if all(len(set(row))==3 for row in v):
            each_agent_three_values += 1
        if any(len(set(row))==3 for row in v):
            some_agent_three_values += 1
        support = certificates[count]
        assert isinstance(support, list) and support
        count += 1
        assert len({part[0] for part in support})==len(support)
        weights = []
        for part in support:
            assert isinstance(part, list) and len(part)==3
            a,num,den = part
            assert type(a)==int and 0<=a<81
            assert type(num)==int and type(den)==int and num>0 and den>0
            weights.append((a,Fraction(num,den)))
        assert sum((p for _,p in weights),Fraction(0))==1
        max_support = max(max_support,len(support))
        support_hist[len(support)]+=1
        # Independently reconstruct utilities for ALL 81 complete allocations.
        comparison = tuple(tuple(tuple(sum(v[i][g] for g in owners[a][j]) for j in range(3)) for i in range(3)) for a in range(81))
        own_values = tuple(tuple(comparison[a][i][i] for i in range(3)) for a in range(81))
        for a,p in weights:
            # Genuine Pareto optimality among ALL 81 deterministic complete allocations.
            assert not any(all(own_values[b][i]>=own_values[a][i] for i in range(3)) and
                           any(own_values[b][i]>own_values[a][i] for i in range(3)) for b in range(81))
            # Ex-post EFX, removing ANY good from every other nonempty bundle.
            for i in range(3):
                for j in range(3):
                    if i==j:continue
                    for g in owners[a][j]:
                        assert own_values[a][i] >= comparison[a][i][j] - v[i][g]
        # Ex-ante EF on each ordered pair, evaluated with exact rational weights.
        for i in range(3):
            for j in range(3):
                if i==j:continue
                assert sum((p*(comparison[a][i][i]-comparison[a][i][j]) for a,p in weights), Fraction(0))>=0
    assert count==len(certificates)==5053
    assert labeled_count == 3**12 == 531441
    assert each_agent_three_values==392 and some_agent_three_values==3767
    assert max_support==4 and support_hist==Counter({1:1123,2:2091,3:1772,4:67})
    print('VERIFY_OK canonical=%d labeled=%d all_three_level=%d any_three_level=%d max_support=%d support_hist=%s' % (count,labeled_count,each_agent_three_values,some_agent_three_values,max_support,dict(sorted(support_hist.items()))))

if __name__=='__main__':
    assert len(sys.argv)==2, 'Usage: verify_ternary.py ternary_lottery_witnesses.json'
    verify(sys.argv[1])
