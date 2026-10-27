#!/usr/bin/env python3
"""Finite checks for a binary two-deletion list bound.

This finite calculation corroborates but does not prove the all-length theorem.
Uses distinct word sets, rather than deletion-position counts.
"""
from collections import Counter
from itertools import product
import random


def subword(y, x):
    it = iter(x)
    return all(any(a == b for b in it) for a in y)


def one_insertions(y):
    return {y[:i] + (b,) + y[i:] for i in range(len(y) + 1) for b in (0, 1)}


def two_insertions(y):
    result = set()
    for z in one_insertions(y):
        result.update(one_insertions(z))
    return result


def checksum(x):
    return sum((i + 1) * b for i, b in enumerate(x))


def singleton_candidates(y):
    # Run extension or insertion of an entirely new length-two opposite run.
    m = len(y)
    if not m:
        return {(0, 0), (1, 1)}
    out = set()
    i = 0
    while i < m:
        j = i + 1
        while j < m and y[j] == y[i]: j += 1
        out.add(y[:j] + (y[i], y[i]) + y[j:])
        i = j
    for k in range(m+1):
        if k == 0:
            out.add((1-y[0],)*2 + y)
        elif k == m:
            out.add(y + (1-y[-1],)*2)
        elif y[k-1] == y[k]:
            out.add(y[:k] + (1-y[k],)*2 + y[k:])
    return out


def verify(y):
    n = len(y)+2
    zset = one_insertions(y)
    xset = two_insertions(y)
    assert len(zset) == n
    assert len(xset) == 1+n+n*(n-1)//2
    groups = Counter(checksum(x) % (n+1) for x in xset)
    assert max(groups.values()) <= n//2 + 1, (y, groups)
    s = {x for x in xset if len({x[:j]+x[j+1:] for j in range(n)} & zset)==1}
    sc = singleton_candidates(y)
    assert s==sc, (y, s^sc)
    delta = [checksum(x)-checksum(y) for x in s]
    assert len(delta) == n and len(set(delta))==n
    assert all(0<=d<=2*n-1 for d in delta)
    assert max(Counter(d % (n+1) for d in delta).values())<=2
    for a in range(n+1):
        zshadows=[{x[:i]+x[i+1:] for i in range(n)} & zset for x in xset if checksum(x)%(n+1)==a]
        assert len(set().union(*zshadows))==sum(map(len,zshadows)), (y,a)

samples=0
for n in range(2,12):
    for y in product((0,1), repeat=n-2):
        verify(y)
        samples+=1
    zero=(0,)*(n-2)
    v=sum(checksum(x)%(n+1)==0 for x in two_insertions(zero))
    assert v==n//2+1, (n,v)
    print(f'n={n}: all {2**(n-2)} received words checked; sharp zero syndrome={v}')
rng=random.Random(290516)
for n in (12,15,20,26,35,45):
    for j in range(24):
        y=tuple(rng.randrange(2) for _ in range(n-2))
        verify(y)
        samples+=1
print(f'VT_TWO_DELETION_VERIFY_OK {samples} complete-received-word samples')
