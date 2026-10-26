#!/usr/bin/env python3
"""Independent finite Boolean-partition closure checks for a forward S4 chain."""
from itertools import product
from math import comb

def actual_atoms(word):
    n=len(word); U=(1<<n)-1
    groups=[]
    for col in sorted(set(word)):
        groups.append(sum(1<<i for i,c in enumerate(word) if c==col))
    while True:
        old=tuple(sorted(groups)); newer=list(groups)
        for a in old:
            d=sum(1<<i for i in range(n) if any((a>>j)&1 for j in range(i,n)))
            refined=[]
            for b in newer:
                if b&d and b&~d&U: refined.extend([b&d,b&~d&U])
                else: refined.append(b)
            newer=refined
        groups=sorted(newer)
        if tuple(groups)==old:
            return len(groups),groups

def run_number(word):
    return 1+sum(word[i]!=word[i-1] for i in range(1,len(word)))

for n in range(1,7):
    for k in range(0,3):
        m=1<<k
        hist={}
        for tup in product(range(m),repeat=n):
            observed, groups=actual_atoms(tup)
            predicted=run_number(tup)
            assert observed==predicted,(n,k,tup,observed,predicted,groups)
            hist[observed]=hist.get(observed,0)+1
        expected={r: m*comb(n-1,r-1)*(m-1)**(r-1) for r in range(1,n+1)}
        assert all(hist.get(r,0)==t for r,t in expected.items()),(n,k,hist,expected)
        print('n=%d k=%d count=%d full=%d'%(n,k,m**n,hist.get(n,0)))
print('ALL_CHECKS_OK')

def partitions(n):
    def rec(seq, maxi):
        if len(seq)==n:
            yield tuple(seq)
        else:
            for q in range(maxi+2):
                yield from rec(seq+[q],max(maxi,q))
    yield from rec([0],0)

for n in range(1,8):
    count=0
    U=(1<<n)-1
    for word in partitions(n):
        atoms=[sum(1<<i for i,t in enumerate(word) if t==q) for q in set(word)]
        closed=True
        for a in atoms:
            d=sum(1<<i for i in range(n) if any((a>>j)&1 for j in range(i,n)))
            if any(a0 & d and a0 & ~d & U for a0 in atoms):
                closed=False
                break
        is_intervals=all(len({word[i] for i in range(l,r+1)})==1 for q in set(word) for l,r in [(min(i for i,t in enumerate(word) if t==q), max(i for i,t in enumerate(word) if t==q))])
        assert closed==is_intervals,(n,word,closed,is_intervals)
        count+=closed
    assert count==2**(n-1),(n,count)
    print('all-partitions n=%d subalgebras=%d'%(n,count))
print('ALL_PARTITION_CHECKS_OK')
