#!/usr/bin/env python3
"""Standalone finite checks of a matching-perturbed enemy graph Nash-product theorem.

This program verifies finite instances only; the arbitrary-size theorem needs its proof.
Run: python3 VERIFY.py
"""
from math import comb


def partitions(n):
    groups = []
    def rec(i):
        if i == n:
            yield tuple(tuple(g) for g in groups)
            return
        for group in groups:
            group.append(i)
            yield from rec(i + 1)
            group.pop()
        groups.append([i])
        yield from rec(i + 1)
        groups.pop()
    yield from rec(0)


def predicted(a, b, t):
    assert a >= 4 and b >= 2 and 1 <= t <= a // 2
    if t == 1:
        a_product = (a-3)**(a-2)
        count = a-2 if a == 4 else 2*(a-2)
    else:
        a_product = (t-1)**t * (a-t-1)**(a-t)
        count = 2**(t-1) if a == 2*t else 2**t
    return a_product*(b-1)**b, count


def measure(partition, bad_edges):
    product=1
    for block in partition:
        if len(block) == 1:
            return 0
        s=set(block)
        if any(u in s and v in s for u,v in bad_edges):
            return 0
        product *= (len(block)-1)**len(block)
    return product


def exhaustive(a, b, t, full):
    n=a+b if full else a
    bad_edges={(2*i, 2*i+1) for i in range(t)}
    if full:
        bad_edges.update((i,j) for i in range(a) for j in range(a, a+b))
    best, count, total, shapes = -1, 0, 0, set()
    for partition in partitions(n):
        total+=1
        score=measure(partition,bad_edges)
        if score > best:
            best,count,shapes=score,0,set()
        if score == best:
            count+=1
            shapes.add(tuple(sorted((len(g) for g in partition),reverse=True)))
    p,c=predicted(a,b,t) if full else predicted(a,2,t)
    if not full:
        p=p # b=2, factor (b-1)^b equals 1
    assert (best,count)==(p,c), (a,b,t,full,best,count,p,c)
    assert len(shapes)==1,(a,b,t,shapes)
    return total


def main():
    cases=0
    visited=0
    for a in range(4,11):
        for t in range(1,a//2+1):
            visited+=exhaustive(a,2,t,False)
            cases+=1
    for a in range(4,7):
        for b in range(2,4):
            for t in range(1,a//2+1):
                visited+=exhaustive(a,b,t,True)
                cases+=1
    for a in range(4,101):
        assert predicted(a,2,1)[0]==predicted(a,2,2)[0]
    print(f'VERIFY_OK: {cases} exact instances, {visited} unrestricted set partitions, plateau for a=4..100')


if __name__=='__main__':
    main()
