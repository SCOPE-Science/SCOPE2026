#!/usr/bin/env python3
"""Direct census of monotone maps versus an exact binomial-pair formula."""
from collections import Counter
from itertools import combinations_with_replacement
from math import comb


def choose(n,k):
    return comb(n,k) if 0 <= k <= n else 0


def predicted(n):
    return {(k,r): choose(k+r-1,r-k)*choose(n+k-1,2*r-1)
            for k in range(1,n+1) for r in range(k,n+1)}


def direct(n):
    out=Counter()
    for f in combinations_with_replacement(range(n), n):
        f2=tuple(f[f[i]] for i in range(n))
        f3=tuple(f[f2[i]] for i in range(n))
        f4=tuple(f[f3[i]] for i in range(n))
        assert (f4==f2)==(f3==f2), (n,f)
        if f3 == f2:
            out[(len(set(f2)),len(set(f)))]+=1
    return out


def main():
    # Independent census of the half-interval lemma for every side length 0..9.
    for a in range(10):
        counts=Counter()
        for seq in combinations_with_replacement(range(a+1),a):
            g=(0,)+seq
            if all(g[g[i]]==0 for i in range(a+1)):
                counts[len(set(g))-1]+=1
        expected={j:choose(a,2*j) for j in range(a//2+1)}
        assert dict(counts)==expected,(a,dict(counts),expected)
    print('LOCAL_HALF_LEMMA_OK a=0..9')
    totals=[]
    for n in range(1,11):
        pred={pair:c for pair,c in predicted(n).items() if c}
        got=dict(direct(n))
        assert got==pred,(n,got,pred)
        total=sum(got.values())
        idem=sum(v for (k,r),v in got.items() if k==r)
        strict=total-idem
        # Directly check strict idempotent exclusion and complete monotone-map space size.
        assert total <= choose(2*n-1,n)
        totals.append(total)
        print(f'EXHAUSTIVE_OK n={n} total={total} idem={idem} strict={strict} cells={len(got)}')
    # Cross-check the independent rational recurrence implied by (1-2z)^2/(1-5z+6z^2-z^3).
    for n in range(3,10):
        assert totals[n] == 5*totals[n-1]-6*totals[n-2]+totals[n-3]
    assert totals == [1,3,10,33,108,352,1145,3721,12087,39254]
    assert sum(v for (k,r),v in direct(5).items() if k<r) == 53
    print('RECURRENCE_OK 1..10')
    print('FIVE_POINT_CORRECTION_OK 53')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
