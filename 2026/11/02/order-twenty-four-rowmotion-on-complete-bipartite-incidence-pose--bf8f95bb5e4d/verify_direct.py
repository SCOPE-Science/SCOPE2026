#!/usr/bin/env python3
"""Independent full finite rowmotion census for K_{2,n}, 1<=n<=6."""
from collections import Counter
from itertools import combinations


def predicted(n):
    return {2: 2**(n-1),
            3: 3**(n-1) - 2**n + 2,
            4: 2**n - 2,
            6: (5**n - 7*3**n + 11*2**n - 6)//6,
            8: 3*2**(n-1) - 2,
            24: 3**(n-1) - 2**n + 1}

def row(left, cols):
    # Distinct bitwise recurrence derived directly from the minimal-complement definition.
    ua = [bool((left & 1) and (c & 1) and not (c & 2)) for c in cols]
    ub = [bool((left & 2) and (c & 1) and not (c & 4)) for c in cols]
    next_left = (int(not (left & 1) or any(ua)) +
                 2*int(not (left & 2) or any(ub)))
    next_cols = tuple(int(not (c & 1) or ua[j] or ub[j]) +
                      2*int(ua[j]) + 4*int(ub[j])
                      for j,c in enumerate(cols))
    return next_left, next_cols

def direct_states(n):
    states=[]
    for left in range(4):
        options=[]
        for c in range(8):
            r,ta,tb=c&1,c&2,c&4
            if ta and (not r or not(left&1)):continue
            if tb and (not r or not(left&2)):continue
            options.append(c)
        # Generate independently, not by calling finite-support verifier.
        import itertools
        states.extend((left,c) for c in itertools.product(options, repeat=n))
    return states

def main():
    for n in range(1,7):
        states=direct_states(n)
        assert len(states)==5**n+2*(3**n)+2**n
        index={s:i for i,s in enumerate(states)}
        trans=[index[row(*s)] for s in states]
        assert len(set(trans))==len(trans)
        remaining=set(range(len(states)))
        cycles=Counter()
        while remaining:
            first=min(remaining)
            cur=first
            d=0
            while cur in remaining:
                remaining.remove(cur)
                d+=1
                cur=trans[cur]
            assert cur==first
            cycles[d]+=1
        want={k:v for k,v in predicted(n).items() if v}
        assert dict(cycles)==want,(n,cycles,want)
        print('FULL_CENSUS_OK n=%d ideals=%d cycles=%s'%(n,len(states),dict(sorted(cycles.items()))))
    print('FULL_REPLAY_OK')

if __name__=='__main__':main()
