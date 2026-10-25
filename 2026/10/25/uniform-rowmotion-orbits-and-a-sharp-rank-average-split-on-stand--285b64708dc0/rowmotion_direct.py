#!/usr/bin/env python3
"""Order-ideal rowmotion by minimal-complement generation on standard examples."""
from collections import Counter


def ideals(n):
    full=(1<<n)-1
    for lower in range(1<<n):
        possible=[j for j in range(n) if (lower | (1<<j))==full]
        bound=sum(1<<j for j in possible)
        top=bound
        while True:
            yield lower,top
            if top==0: break
            top=(top-1)&bound


def rowmotion(state,n):
    a,b=state
    full=(1<<n)-1
    missing_minima=full^a
    eligible_tops=0
    for j in range(n):
        if not(b&(1<<j)) and (a|(1<<j))==full:
            eligible_tops|=1<<j
    new_minima=missing_minima
    for j in range(n):
        if eligible_tops&(1<<j):
            new_minima|=full^(1<<j)
    return new_minima,eligible_tops


def classify(n):
    states=set(ideals(n))
    assert len(states)==2**(n+1)+n-1
    successors={s:rowmotion(s,n) for s in states}
    assert set(successors.values())==states
    remaining=states.copy();by_length=Counter();by_average=Counter()
    while remaining:
        x=min(remaining)
        path=[];y=x
        while y in remaining:
            remaining.remove(y);path.append(y);y=successors[y]
        assert y==x
        length=len(path)
        rank_sum=sum(a.bit_count()+b.bit_count() for a,b in path)
        by_length[length]+=1
        # Record average twice its value, avoiding floats.
        assert 2*rank_sum%length==0
        by_average[2*rank_sum//length]+=1
    expected={l:v for l,v in ((2,2**n-2*n-2),(3,1),(5,n)) if v>0}
    assert dict(by_length)==expected
    expected_averages={2*n:n+1}
    if n>=4:
        b=2**(n-1)-n-1
        expected_averages={n:b,2*n:n+1,3*n:b}
    assert dict(by_average)==expected_averages
    return len(states),dict(sorted(by_length.items())),dict(sorted(by_average.items()))


if __name__=='__main__':
    for n in range(3,12):
        count,cycles,averages=classify(n)
        print(f'n={n} ideals={count} cycles={cycles} twice_rank_mean={averages}')
