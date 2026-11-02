#!/usr/bin/env python3
"""Standalone exact checker for the fixed-energy clique diffusion cycle census."""
from collections import Counter
from itertools import combinations_with_replacement
from math import factorial


def update(state):
    """Vertexwise simultaneous integer diffusion on a complete graph."""
    return tuple(x + sum((y > x) - (y < x) for j, y in enumerate(state) if j != i)
                 for i, x in enumerate(state))


def compositions(n):
    if not n:
        yield ()
    else:
        for m in range(1, n+1):
            for tail in compositions(n-m):
                yield (m,)+tail


def formula(n):
    answer=[0]*n
    facts=[factorial(i) for i in range(n+1)]
    for blocks in compositions(n):
        weight=facts[n]
        for size in blocks:
            weight//=facts[size]
        residues=[0]*n
        residues[0]=1
        prefix=0
        for j in range(len(blocks)-1):
            prefix+=blocks[j]
            step=n-prefix
            new=[0]*n
            for gap in range(1,blocks[j]+blocks[j+1]):
                for r,number in enumerate(residues):
                    new[(r+step*gap)%n]+=number
            residues=new
        for r,number in enumerate(residues):
            answer[r]+=weight*number
    return answer


def independent_vertexwise(n):
    # Proof establishes max spread 2n-4 for n>=3; 1 for n=2.
    max_spread=max(1,2*n-4)
    facts=[factorial(i) for i in range(n+1)]
    answer=[0]*n
    extremes=[0]*n
    tested=0
    for tail in combinations_with_replacement(range(max_spread+1),n-1):
        x=(0,)+tail
        tested+=1
        if update(update(x)) != x:
            continue
        mult=facts[n]
        for count in Counter(x).values():
            mult//=facts[count]
        residue=sum(x)%n
        answer[residue]+=mult
        if n>=4 and max(x)-min(x)==max_spread:
            extremes[residue]+=mult
    return answer,extremes,tested


def main():
    total=0
    for n in range(2,10):
        f=formula(n)
        d,extremes,k=independent_vertexwise(n)
        assert f==d, (n,f,d)
        if n>=4:
            assert extremes==[n*(n-1)]+[0]*(n-1), (n,extremes)
        assert all((v-(r==0))%2==0 for r,v in enumerate(f))
        total+=k
        print(f'n={n}: periodic-state counts by sum mod n {f}; checked_normalized_profiles={k}')
    outside_tested=0
    # Extra tests outside the theoretically allowed region; this is a finite
    # stress test, not a proof of the universal spread bound.
    for n in range(2,8):
        theoretical=max(1,2*n-4)
        for tail in combinations_with_replacement(range(3*n+1),n-1):
            x=(0,)+tail
            if x[-1]<=theoretical:
                continue
            outside_tested+=1
            assert update(update(x))!=x, (n,x)
    print(f'outside_spread_profiles_tested={outside_tested}')
    # Illustrate 2-state asymmetry of the sharp max-spread example.
    for n in range(4,30):
        h=n-2
        x=(0,)+(h,)*(n-2)+(2*h,)
        y=update(x)
        assert max(x)-min(x)==2*n-4
        assert max(y)-min(y)==2
        assert update(y)==x
        assert sum(x)%n==0
    print(f'CLIQUES_DIFFUSION_EXACT_CENSUS_VERIFIED; normalized_profiles={total}; sharp_witnesses=26')

if __name__=='__main__':
    main()
