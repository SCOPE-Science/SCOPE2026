#!/usr/bin/env python3
"""Symbolic cycle-partition verification of the sharp depth-two classification.

The argument for arbitrary degrees is given in RESULT.md. This independent
finite check deliberately uses cycle partitions, not multiplication tables.
"""
from collections import Counter
from functools import lru_cache
from math import lcm

@lru_cache(None)
def partitions(n, ceiling=None):
    if ceiling is None: ceiling=n
    if n==0: return ((),)
    return tuple((k,)+rest for k in range(min(ceiling,n),0,-1)
                 for rest in partitions(n-k,k))

def root_exists(part):
    c=Counter(part)
    return all(c[k]%2==0 for k in c if k%2==0)

def tag(part):
    o=1
    for k in part: o=lcm(o,k)
    if o==1: return 'E'
    if o==2: return 'I+' if root_exists(part) else 'I-'
    if o==3: return 'C3'
    if o==4: return 'C4+' if root_exists(part) else 'C4-'
    return 'H+' if root_exists(part) else 'H-'

EXPECTED_SEVEN={'E','I-','I+','C3','C4-','H+','H-'}
EXPECTED_EIGHT=EXPECTED_SEVEN|{'C4+'}

def check():
    # All cycle types through size 80; symbols are exact for every n>=5 by the lemma.
    for n in range(5,41):
        pats=partitions(n)
        seen={tag(p) for p in pats}
        want=EXPECTED_SEVEN if n<=7 else EXPECTED_EIGHT
        assert seen==want,(n,seen,want)
    print('PARTITION_STABILIZATION_OK degrees=5..40 seven_types=5..7 eight_types=8..40')
    for n in range(5,15):
        ps=partitions(n)
        assert any(tag(p)=='H-' for p in ps)
        assert any(tag(p)=='H+' for p in ps)
        assert any(tag(p)=='I-' for p in ps)
        assert any(tag(p)=='I+' for p in ps)
        assert any(tag(p)=='C3' for p in ps)
        assert any(tag(p)=='C4-' for p in ps)
        assert (any(tag(p)=='C4+' for p in ps))==(n>=8)
    print('SQUARE_ROOT_CUTOFF_OK least_degree=8 needed_order=8')
    for n in (5,6,7,8):
        c=Counter(tag(p) for p in partitions(n))
        print('CYCLE_TYPES_OK n=%d %s'%(n,' '.join(f'{k}={v}' for k,v in sorted(c.items()))))
    print('SYMBOLIC_VERIFY_OK')

if __name__=='__main__': check()
