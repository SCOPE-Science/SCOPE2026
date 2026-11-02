#!/usr/bin/env python3
"""Independent exhaustive oracle for a cyclic-order bi-threshold sweep.

Each site is visited once in the order 0,...,n-1. The closed-neighborhood
population thresholds are 1 (a zero becomes one) and 3 (a one stays one).
"""
from collections import Counter
from math import gcd


def update(state, n):
    bits = [(state >> j) & 1 for j in range(n)]
    for j in range(n):
        p = bits[(j-1)%n] + bits[j] + bits[(j+1)%n]
        bits[j] = int(p >= (3 if bits[j] else 1))
    return sum(bit << j for j,bit in enumerate(bits))


def expected_fiber(state,n):
    a=state&1
    assert ((state>>(n-1))&1)==a
    if ((state>>(n-2))&1)!=a:return 1
    for j in range(1,n-2):
        if ((state>>j)&1)!=a:return j+1
    return n


def run_sizes(word):
    if len(set(word))==1:return []
    d=len(word)
    start=next(i for i in range(d) if word[i]!=word[i-1])
    run=[]; size=1
    for z in range(1,d):
        if word[(start+z)%d]==word[(start+z-1)%d]:size+=1
        else:run.append(size);size=1
    run.append(size)
    return run


def main():
    for n in range(3,13):
        l=n-1;states=range(1<<n)
        full={x:update(x,n) for x in states}
        image=set(full.values())
        recurrent={x for x in states if (x&1)==((x>>(n-1))&1)}
        assert image==recurrent
        fibers=Counter(full.values())
        assert all(fibers[z]==expected_fiber(z,n) for z in recurrent)
        assert all(full[z] in recurrent for z in recurrent)
        for x in recurrent:
            word=[(x>>j)&1 for j in range(l)]
            rot=word[1:]+word[:1]
            expected=sum(v<<j for j,v in enumerate(rot))+(rot[0]<<(n-1))
            assert full[x]==expected
        remaining=set(recurrent)
        orbits=Counter(); total_basin=0;largest=0
        while remaining:
            x=min(remaining);cycle=[];z=x
            while z not in cycle:
                assert z in remaining
                cycle.append(z)
                remaining.remove(z)
                z=full[z]
            assert z==x
            d=len(cycle)
            assert l%d==0
            actual_basin=sum(fibers[t] for t in cycle)
            word=[(x>>j)&1 for j in range(d)]
            if d==1: expected_basin=n
            else:
                sizes=run_sizes(word)
                expected_basin=sum(s*(s+1)//2 for s in sizes)
            assert actual_basin==expected_basin, (n,x,actual_basin,expected_basin)
            orbits[d]+=1;total_basin+=actual_basin
            largest=max(largest,actual_basin)
        assert total_basin==(1<<n)
        for d in range(1,l+1):
            if l%d:assert orbits[d]==0;continue
            # Count aperiodic length-d words directly, independent of Mobius formulas.
            primitive=0
            for w in range(1<<d):
                if all(any(((w>>i)&1)!=((w>>((i+t)%d))&1) for i in range(d)) for t in range(1,d)):
                    primitive+=1
            assert orbits[d]==primitive//d,(n,d,orbits[d],primitive)
        print(f'n={n} states={1<<n} recurrent={len(recurrent)} attractors={sum(orbits.values())} periods={dict(sorted(orbits.items()))} basin_sum={total_basin} max_basin={largest}')
    print('PASS: all finite examples match the theoretical formulas; no finite check substitutes for proof.')

if __name__=='__main__':main()
