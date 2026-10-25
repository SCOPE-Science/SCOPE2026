#!/usr/bin/env python3
"""Independent finite checks of four-run binary string-attractor classification.

Only finite checks; the all-parameter theorem is proved separately.
"""
from itertools import combinations, product
from collections import Counter
from math import comb


def factor_masks(w):
    """For each distinct factor, union all positions it occupies in any occurrence."""
    d = {}
    for i in range(len(w)):
        mask = 0
        for j in range(i,len(w)):
            mask |= (1 << j)
            u = w[i:j+1]
            d[u] = d.get(u,0) | mask
    return tuple(d.values())


def covers(all_masks,positions):
    selected = sum(1 << i for i in positions)
    return all(selected & occurrences for occurrences in all_masks)


def run_word(a,b,c,d):
    return '0'*a + '1'*b + '0'*c + '1'*d


def formula(a,b,c,d):
    return 3 if (a>c and d>b) or (c>=a+2 and b>=d+2) else 2


def witness(a,b,c,d):
    # 0-based positions of the run endpoints:
    end_a = a-1
    start_b = a
    end_b = a+b-1
    start_c = a+b
    end_c = a+b+c-1
    start_d = a+b+c
    if a>=c and b>=d:
        return (end_a,end_b)
    if a<=c and b<=d:
        return (start_c,start_d)
    if c==a+1 and b>d:
        return (start_b,start_c)
    if c>a and b==d+1:
        return (end_b,end_c)
    if b>=d:
        return (end_a,end_b,end_c)
    return (end_a,start_c,start_d)


def brute_minimal_at_most_three(w):
    all_masks = factor_masks(w)
    for k in range(1,4):
        for positions in combinations(range(len(w)),k):
            if covers(all_masks,positions):
                return k
    return 4


def check():
    cases = 0
    n_counts = Counter()
    for a,b,c,d in product(range(1,8),repeat=4):
        w=run_word(a,b,c,d)
        masks=factor_masks(w)
        expected=formula(a,b,c,d)
        chosen=witness(a,b,c,d)
        assert len(chosen)==expected and covers(masks,chosen), (a,b,c,d,'witness',chosen)
        brute=brute_minimal_at_most_three(w)
        assert brute==expected, (a,b,c,d,'min',brute,expected)
        cases+=1
        n_counts[(len(w),expected)]+=1
    for n in range(4,23):
        count=0
        total=0
        for a in range(1,n-2):
            for b in range(1,n-a-1):
                for c in range(1,n-a-b):
                    d=n-a-b-c
                    total+=1
                    count+=formula(a,b,c,d)==3
        assert total==comb(n-1,3)
        coefficient=sum((t+1)*(q+1) for h in (6,8) for rem in [n-h] if rem>=0 for q in range(rem//2+1) for t in [rem-2*q])
        assert count==coefficient,(n,count,coefficient)
    print(f'FOUR_RUN_ATTRACTORS_PASS brute_parameter_tuples={cases} max_run_length=7 exact_length_coefficients=4..22')

if __name__=='__main__':
    check()
