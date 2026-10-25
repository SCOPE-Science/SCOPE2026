#!/usr/bin/env python3
"""Exhaustive independent test using only poset relations and toggle legality."""
from collections import Counter


def lower_sets(n):
    return [0 for _ in range(n)]+[
        sum(1<<j for j in range(n) if j!=i) for i in range(n)
    ]


def is_ideal(mask,low):
    for vertex,required in enumerate(low):
        if mask&(1<<vertex) and required&~mask:
            return False
    return True


def sweep(mask,n,low):
    # All maximal elements, then all minimal elements: reverse linear extension.
    for vertex in list(range(n,2*n))+list(range(n)):
        after=mask^(1<<vertex)
        if is_ideal(after,low):
            mask=after
    return mask


def classify(n):
    low=lower_sets(n)
    states={mask for mask in range(1<<(2*n)) if is_ideal(mask,low)}
    f={mask:sweep(mask,n,low) for mask in states}
    assert set(f.values())==states
    remaining=set(states)
    cycles=Counter();mean2=Counter()
    while remaining:
        base=min(remaining);x=base;orbit=[]
        while x in remaining:
            remaining.remove(x);orbit.append(x);x=f[x]
        assert x==base
        size=len(orbit)
        cycles[size]+=1
        rank_sum=sum(k.bit_count() for k in orbit)
        assert (2*rank_sum)%size==0
        mean2[2*rank_sum//size]+=1
    return len(states),dict(sorted(cycles.items())),dict(sorted(mean2.items()))


if __name__=='__main__':
    for n in range(3,9):
        count,cycles,averages=classify(n)
        assert count==2**(n+1)+n-1
        assert cycles=={k:v for k,v in ((2,2**n-2*n-2),(3,1),(5,n)) if v>0}
        print(f'n={n} ideals={count} cycles={cycles} twice_rank_mean={averages}')
