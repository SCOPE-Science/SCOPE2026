#!/usr/bin/env python3
"""Exact arithmetic checks for the binomial recursion for flattened parking functions.
Run with: python3 verify.py (Python >= 3.10, standard library only).
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product
from math import comb


def binomial_run_counts(n):
    if n < 1:
        raise ValueError('n must be positive')
    K = (n + 1) // 2
    D = {(0, 0, 0): 1}  # (number placed, number of opened runs, completed-boundary mask)
    for value in range(1, n + 1):
        E = defaultdict(int)
        for (t, k, mask), multiplicity in D.items():
            available = [j for j in range(max(0, k-1)) if not (mask & (1 << j))]
            b = mask.bit_count()
            for choice in range(1 << len(available)):
                added = sum((1 << j) for v, j in enumerate(available) if choice & (1 << v))
                q = added.bit_count()
                for newk in range(k, K+1):
                    h = newk - k
                    for a in range(max(0, value-t, h+q), n-t+1):
                        if k == 0:
                            if h == 0: continue
                            ways = comb(a-1, h-1)
                        else:
                            ways = comb(a+b, b+q+h)
                        E[(t+a, newk, mask | added)] += multiplicity*ways
        D = E
    return [D.get((n, k, (1 << (k-1))-1), 0) for k in range(1, K+1)]


@lru_cache(None)
def weak_allocations(total, old, new):
    # Return all vectors of length old+new with old entries >=0 and new entries >=1.
    m = old + new
    if m == 0:
        return ((),) if total == 0 else ()
    if total < new: return ()
    def build(rem, slots):
        if slots == 1:
            yield (rem,)
        else:
            for i in range(rem+1):
                for right in build(rem-i, slots-1):
                    yield (i,)+right
    return tuple(tuple(x+(i>=old) for i,x in enumerate(v))
                 for v in build(total-new, m))


def allocation_run_counts(n):
    # A different transition implementation: explicitly assign copies at each value to runs.
    K=(n+1)//2
    D={(0,0,0):1}
    for value in range(1,n+1):
        E=defaultdict(int)
        for (t,k,mask),count in D.items():
            for newk in range(k,K+1):
                h=newk-k
                for a in range(max(value-t,h),n-t+1):
                    for allocation in weak_allocations(a,k,h):
                        added=sum((1<<j) for j in range(k-1) if allocation[j]>0)
                        E[(t+a,newk,mask | added)]+=count
        D=E
    return [D.get((n,k,(1<<(k-1))-1),0) for k in range(1,K+1)]


def literal_counts(n):
    # Directly tests defining conditions on words in [n]^n (independent of both transfers).
    out=[0]*((n+1)//2)
    for a in product(range(1,n+1),repeat=n):
        if any(x > position for position,x in enumerate(sorted(a),1)):
            continue
        first=[a[0]]+[a[i] for i in range(1,n) if a[i-1]>a[i]]
        if first == sorted(first):
            out[len(first)-1]+=1
    return out


PUBLISHED = {
    1:[1],2:[2],3:[5,3],4:[14,32],5:[42,245,49],
    6:[132,1656,1149],7:[429,10563,17008,1629],
    8:[1430,65472,204815,65015],
}
NEW_ROWS={
    9:[4862,400257,2201191,1547655,83946],
    10:[16796,2433340,22084807,28745746,5031230],
    11:[58786,14780194,212127438,461537277,174127144,5915812],
    12:[208012,89935440,1980589881,6746765103,4582660742,493794095],
    15:[9694845,20713494195,1476586479142,15415670435050,37520284756825,24152599557961,3610148625226,58016147482],
    20:[6564120420,194611784063400,83182024839571630,3971331108876751847,42873155802835238918,141922364921449069697,163868395200949245641,66939533708401641124,8630371602352737343,235941250732529667],
}


def main():
    for n in range(1,7):
        assert literal_counts(n) == binomial_run_counts(n), f'definitional enumeration n={n}'
    for n in range(1,13):
        assert allocation_run_counts(n) == binomial_run_counts(n), f'compositions vs binomials n={n}'
    for n,row in PUBLISHED.items():
        assert binomial_run_counts(n)==row, f'published data n={n}'
    for n,row in NEW_ROWS.items():
        assert binomial_run_counts(n)==row, f'numerical row n={n}'
    assert sum(binomial_run_counts(20))==428524470238784969687
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
