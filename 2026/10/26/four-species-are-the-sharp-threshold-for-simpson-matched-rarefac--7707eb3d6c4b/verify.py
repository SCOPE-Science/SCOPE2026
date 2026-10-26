#!/usr/bin/env python3
"""Exact rational verification for Simpson-matched species accumulation curves.

Usage: python verify.py > certificate.json
Requires Python >=3.9 standard library only.
"""
import json
from collections import defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement
from math import factorial

A = (1, 4, 6, 10)
B = (2, 2, 8, 9)
TOTAL = 21

def delta_n(a, b, n, total=TOTAL):
    """Numerator of expected richness A minus expected richness B."""
    assert sum(a) == sum(b) == total
    return sum((total-x)**n for x in b)-sum((total-x)**n for x in a)

def via_multinomial(a, n, total=TOTAL):
    """Independent finite multinomial enumeration, exact numerator."""
    out = 0
    # Explicit compositions rather than recurrence division.
    def comp(left, length):
        if length == 1:
            yield (left,)
        else:
            for j in range(left+1):
                for tail in comp(left-j,length-1):
                    yield (j,)+tail
    for v in comp(n,len(a)):
        multinomial=factorial(n)
        denom=1
        power=1
        for mass,count in zip(a,v):
            denom*=factorial(count)
            power*=mass**count
        multinomial//=denom
        out += sum(x>0 for x in v)*multinomial*power
    return out

def test_triples():
    comparisons=0
    triples=0
    for total in range(3,19):
        groups=defaultdict(list)
        for a in combinations_with_replacement(range(1,total),3):
            if sum(a)==total:
                groups[sum(x*x for x in a)].append(a)
                triples+=1
        for group in groups.values():
            for i,a in enumerate(group):
                for b in group[i+1:]:
                    signs=[]
                    for k in range(3,17):
                        num=delta_n(a,b,k,total)
                        signs.append((num>0)-(num<0))
                    assert len(set(signs))==1,(total,a,b,signs)
                    comparisons+=1
    return triples,comparisons

def main():
    assert sum(A)==sum(B)==TOTAL
    assert sum(x*x for x in A)==sum(x*x for x in B)==153
    assert sum(x**3 for x in A)-sum(x**3 for x in B)==24
    results={str(n):delta_n(A,B,n) for n in range(2,14)}
    assert results['2']==0
    assert all(results[str(n)]>0 for n in range(3,8))
    assert all(results[str(n)]<0 for n in range(8,14))
    assert 20**14>2*19**14
    assert 17>13 and 15>12
    multinomial=[]
    for n in (2,3,4,5,7,8):
        x=via_multinomial(A,n)
        y=via_multinomial(B,n)
        assert x-y == results[str(n)]
        multinomial.append(n)
    triple_count,pair_comparisons=test_triples()
    cert={
      'schema_version':1,
      'method':'exact integer power sums, independent multinomial enumeration, finite triple sanity grid',
      'abundance_numerators_A':list(A),
      'abundance_numerators_B':list(B),
      'denominator':TOTAL,
      'sum_squares':153,
      'simpson_index':'32/49',
      'delta_numerator_by_n':results,
      'positive_range':[3,7],
      'negative_checked_range':[8,13],
      'tail_bound_start':14,
      'tail_inequality_numerator':20**14-2*19**14,
      'multinomial_checked_n':multinomial,
      'triple_grid_number_of_vectors':triple_count,
      'triple_grid_pairs_tested':pair_comparisons,
      'triple_grid_sample_range':[3,16],
      'conclusion':'checks_passed; analytic proof of general theorem is in RESULT.md'
    }
    print(json.dumps(cert,sort_keys=True,separators=(',',':')))

if __name__=='__main__':
    main()
