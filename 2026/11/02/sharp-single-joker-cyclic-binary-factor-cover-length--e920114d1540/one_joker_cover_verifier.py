#!/usr/bin/env python3
"""Reproducible finite checks for the one-joker cyclic factor-cover theorem."""
from collections import Counter, defaultdict
from itertools import product


def witness(k):
    if k == 1:
        return '*'
    if k == 2:
        return '*10'
    if k == 3:
        return '*10001'
    L = '0' * (k - 2) + '1'
    R = L[1:] + L[0]
    deleted = [ (L+b+R)[i:i+k] for b in '01' for i in range(k)]
    counts = Counter(deleted)
    assert len(counts) == 2*k-1
    assert {x:v for x,v in counts.items() if v>1} == {L+'0':2}
    remaining = {format(i, f'0{k}b') for i in range(1 << k)} - set(deleted)
    edges=defaultdict(list)
    for word in sorted(remaining, reverse=True):
        edges[word[:-1]].append(word[1:])
    route=[]
    stack=[R]
    while stack:
        u=stack[-1]
        if edges[u]:
            stack.append(edges[u].pop())
        else:
            route.append(stack.pop())
    route.reverse()
    assert len(route)==len(remaining)+1
    assert route[0]==R and route[-1]==L
    host='*'+R+''.join(v[-1] for v in route[1:])
    assert len(host)==(1<<k)-k+1
    return host


def multiplicities(word,k):
    n=len(word)
    counts=Counter()
    for i in range(n):
        window=''.join(word[(i+j)%n] for j in range(k))
        if '*' in window:
            assert window.count('*')==1
            for b in '01':counts[window.replace('*',b)]+=1
        else:counts[window]+=1
    return counts


def exhaustive_minimality(k):
    # Only k=2,3,4: all one-joker cyclic hosts below the proposed optimum.
    proposed=(1<<k)-k+1 if k>1 else 1
    checked=0
    for n in range(k,proposed):
        for tail in product('01',repeat=n-1):
            host='*'+''.join(tail)
            checked+=1
            assert len(multiplicities(host,k)) < (1<<k)
    return checked


def run():
    total=0
    for k in range(1,13):
        w=witness(k)
        c=multiplicities(w,k)
        expected=(1<<k)-k+1 if k>=2 else 1
        assert len(w)==expected
        assert len(c)==1<<k
        if k>=2:
            assert sum(c.values())==len(w)+k
            assert sorted(c.values())==[1]*(2**k-1)+[2]
        else:assert set(c)=={'0','1'}
        total+=len(w)
        print(f'k={k} length={len(w)} distinct={len(c)} excess={sum(c.values())-len(c)}',flush=True)
    count=sum(exhaustive_minimality(k) for k in (2,3,4))
    print(f'VERIFY_OK k=1..12, checked_window_positions={total}, short_host_exhaustion={count}')

if __name__=='__main__':run()
