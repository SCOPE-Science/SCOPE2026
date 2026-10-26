#!/usr/bin/env python3
"""Exact finite checks for PAV on consecutive-pair approval elections.
Uses integer doubled PAV score; this program is auxiliary to an analytic proof.
"""
from itertools import combinations

def adjacency(mask):
    return (mask & (mask >> 1)).bit_count()

def is_local(mask, m):
    baseline=adjacency(mask)
    occupied=[i for i in range(m) if mask>>i&1]
    missing=[j for j in range(m) if not (mask>>j&1)]
    return all(adjacency(mask ^ (1 << i) ^ (1 << j)) >= baseline
               for i in occupied for j in missing)

def extremal_word(k):
    r,s=divmod(k,3)
    if r==0:
        return '10'*(k-1)+'1'
    return ('110'*r + '100'*r)[:-1] + '10'*s

def main():
    assert adjacency(sum(1 << i for i in range(0,9,2))) == 0
    for k in range(1,11):
        m=2*k-1
        worst=-1
        total=0
        trapped=0
        for indices in combinations(range(m),k):
            mask=sum(1 << i for i in indices)
            if is_local(mask,m):
                total+=1
                val=adjacency(mask)
                worst=max(worst,val)
                trapped+=bool(val)
                assert val <= k//3, (k, indices)
        word=extremal_word(k)
        assert len(word)==m and word.count('1')==k
        exemplar=sum(1<<i for i,c in enumerate(word) if c=='1')
        assert is_local(exemplar,m)
        assert adjacency(exemplar)==k//3
        assert worst==k//3
        print(f'k={k}; candidates={m}; local_committees={total}; suboptimal_locals={trapped}; '
              f'exact_worst_overlap={worst}; sharp_word={word}')
if __name__=='__main__':
    main()
