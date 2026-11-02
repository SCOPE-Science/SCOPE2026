"""Reproduce finite ordered-interval Littlestone thresholds and check a depth-10 witness.
Standard-library-only; run: python verify.py. The proof of the state reduction is in RESULT.md.
"""
from __future__ import annotations
import json
from functools import lru_cache
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent
MAX_N = 55

def logfloor(m: int) -> int:
    assert m >= 1
    return m.bit_length()-1

@lru_cache(None)
def no_positive_rank(lengths: tuple[int,...]) -> int:
    """Exact minimax dimension of intervals entirely within disjoint blocks."""
    if not lengths:
        return -1   # empty concept class (not a valid depth-zero leaf)
    best = 0
    for length in sorted(set(lengths)):
        others = list(lengths)
        others.remove(length)
        for x in range(1,length+1):
            remain = tuple(sorted(y for y in others+[x-1,length-x] if y>0))
            if not remain:
                continue
            positive_rank = logfloor(x) + logfloor(length-x+1)
            candidate = 1 + min(positive_rank, no_positive_rank(remain))
            best = max(best,candidate)
    return best

def lengths(blocks):
    return tuple(sorted(b-a+1 for a,b in blocks))

def make_negative_tree(blocks, depth):
    assert blocks and no_positive_rank(lengths(blocks))>=depth
    if not depth:
        a,b=blocks[0]
        return {'interval':[a,a]}
    for index,(a,b) in enumerate(blocks):
        rest=blocks[:index]+blocks[index+1:]
        for q in range(a,b+1):
            remainder=sorted(rest+([(a,q-1)] if a<q else [])+([(q+1,b)] if q<b else []))
            if not remainder:
                continue
            positive_rank=logfloor(q-a+1)+logfloor(b-q+1)
            if positive_rank>=depth-1 and no_positive_rank(lengths(remainder))>=depth-1:
                return {'q':q,'zero':make_negative_tree(remainder,depth-1),
                        'one':make_positive_tree(a,q,q,b,depth-1)}
    raise AssertionError('No negative-state split at expected rank')

def make_positive_tree(l0,l1,r0,r1,depth):
    assert l0<=l1<=r0<=r1
    a=l1-l0+1
    b=r1-r0+1
    assert logfloor(a)+logfloor(b)>=depth
    if not depth:
        return {'interval':[l0,r0]}
    if a>=2:
        k=logfloor(a)
        q=l0+(1<<(k-1))-1
        return {'q':q,'zero':make_positive_tree(q+1,l1,r0,r1,depth-1),
                'one':make_positive_tree(l0,q,r0,r1,depth-1)}
    k=logfloor(b)
    assert k>=1
    q=r0+(1<<(k-1))
    return {'q':q,'zero':make_positive_tree(l0,l1,r0,q-1,depth-1),
            'one':make_positive_tree(l0,l1,q,r1,depth-1)}

def check_tree(t,n,depth):
    witnesses=[]
    def walk(node,history,d):
        if not d:
            assert set(node)=={'interval'}
            l,r=node['interval']
            assert 1<=l<=r<=n
            assert all((l<=q<=r)==bool(y) for q,y in history)
            witnesses.append((l,r))
            return
        assert set(node)=={'q','zero','one'}
        q=node['q']; assert 1<=q<=n
        walk(node['zero'],history+[(q,0)],d-1)
        walk(node['one'],history+[(q,1)],d-1)
    walk(t,[],depth)
    assert len(witnesses)==2**depth
    assert len(set(witnesses))==len(witnesses)
    return len(witnesses),len(witnesses)-1

def brute_rank(n):
    # Independent bit-set recurrence directly over interval concepts and point queries.
    concepts=[(a,b) for a in range(1,n+1) for b in range(a,n+1)]
    masks=[sum((1<<i) for i,(a,b) in enumerate(concepts) if a<=q<=b) for q in range(1,n+1)]
    @lru_cache(None)
    def f(S):
        best=0
        for m in masks:
            yes=S&m
            no=S^yes
            if yes and no:
                best=max(best,1+min(f(yes),f(no)))
        return best
    return f((1<<len(concepts))-1)

def main():
    ranks=[no_positive_rank((n,)) for n in range(1,MAX_N+1)]
    starts=[]
    for d in range(1,max(ranks)+1):
        starts.append(min(n for n in range(1,MAX_N+1) if ranks[n-1]>=d))
    assert starts==[2,3,4,6,9,13,19,27,39,55],starts
    assert all(brute_rank(n)==ranks[n-1] for n in range(1,13))
    # At n=8, the number of distinct concepts permits depth five, but it is unattainable.
    assert ranks[7]==4 and 8*9//2>=32
    t=json.loads((ROOT/'tree_n55_d10.json').read_text())
    count,nodes=check_tree(t,55,10)
    assert (count,nodes)==(1024,1023)
    summary=json.loads((ROOT/'dimensions.json').read_text())
    assert summary['dimension_thresholds_depth_1_through_10']==starts
    assert summary['ranks_n_1_through_55']==ranks
    print('SEGMENT_RECURRENCE_THRESHOLDS_PASS',starts)
    print('DIRECT_CONCEPT_RECURRENCE_PASS n=1..12')
    print('FIRST_CARDINALITY_GAP_PASS n=8 LDIM=4 concepts=36')
    print('ADAPTIVE_TREE_CERTIFICATE_PASS n=55 depth=10 nodes=1023 leaves=1024')
    print('FINAL_ORDERED_INTERVAL_CHECKS_PASS')

if __name__=='__main__':
    main()
