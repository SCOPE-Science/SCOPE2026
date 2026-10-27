#!/usr/bin/env python3
"""Exact uniform fixed-margin incidence C-score enumerator.

No external dependencies. Each species occurs at three sites; each site
contains two species. Edge-multiplicity dynamic programming and an
independent exhaustive labeled-column check are compared for four species.
"""
from collections import defaultdict, Counter
from itertools import combinations, product
from fractions import Fraction
import json


def null_counts(n):
    """Counts n x (3n/2) labeled binary matrices grouped by B=sum choose(sij,2).

    The DP counts weighted unordered multisets of site pairs; 6**m scaling
    clears the factorial denominators. Labeling site columns is restored at end.
    """
    assert n >= 2 and n % 2 == 0
    m = 3 * n // 2
    d = {(0,)*n + (0,): 1}
    for i, j in combinations(range(n), 2):
        out = defaultdict(int)
        for st, weight in d.items():
            base = list(st[:-1]); b = st[-1]
            for k, v in enumerate((1,6,18,36)):
                if base[i]+k > 3 or base[j]+k > 3:
                    break
                x=base.copy(); x[i]+=k; x[j]+=k
                out[tuple(x)+(b+k*(k-1)//2,)]+=weight*v
        d=out
    raw=Counter({st[-1]:v for st,v in d.items() if st[:-1]==(3,)*n})
    # number of sequences of m pairs with multiplicity k is m!/product k!;
    # each DP term has weight 6**m / product k!.
    from math import factorial
    res={str(b): int(Fraction(v*factorial(m),6**m)) for b,v in sorted(raw.items())}
    assert sum(res.values()) > 0
    return res


def brute_four_species():
    """Enumerate 6**6 ordered site-pair sequences, no DP or coefficient method."""
    edges=list(combinations(range(4),2))
    h=Counter()
    for choice in product(range(6), repeat=6):
        degree=[0]*4
        occ=Counter()
        for e in choice:
            i,j=edges[e]; degree[i]+=1; degree[j]+=1;occ[e]+=1
        if degree != [3]*4:continue
        B=sum(s*(s-1)//2 for s in occ.values())
        h[B]+=1
    return {str(b):h[b] for b in sorted(h)}


def main():
    data={str(n):null_counts(n) for n in (2,4,6,8)}
    independent=brute_four_species()
    assert data['4']==independent, (data['4'],independent)
    assert data['2']=={'3':1}
    assert data['4']=={'0':720,'2':1080,'6':60}
    assert sum(data['4'].values())==1860
    assert Fraction(data['4']['6'],1860)==Fraction(1,31)
    assert Fraction(1,31)<Fraction(1,20)
    assert set(data['4'])=={'0','2','6'}
    assert min(map(int,data['4']))==0
    result={
      'method':'exact degree-constrained multiplicity DP and exhaustive labeled site-pair enumeration',
      'n4_independent_enumeration_agrees': True,
      'matrices_by_B':data,
      'n4_null_probabilities':{k:str(Fraction(v,1860)) for k,v in data['4'].items()},
      'smallest_even_species_count_with_strict_upper_tail_p_below_0.05':4,
      'n4_upper_tail_probability_at_max_score':'1/31',
      'n2_is_degenerate': True
    }
    print(json.dumps(result,sort_keys=True,separators=(',',':')))
if __name__=='__main__':main()
