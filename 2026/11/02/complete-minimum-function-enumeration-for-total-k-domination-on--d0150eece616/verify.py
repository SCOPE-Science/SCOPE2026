#!/usr/bin/env python3
"""Independent direct DP and brute-force checks for optimal total-{k} domination functions on paths."""
from itertools import product
from math import comb


def predicted(n, k):
    assert n >= 2 and k >= 1
    s, r = divmod(n, 4)
    if r == 0:
        return 2*s*k, 1
    if r == 1:
        return (2*s+1)*k, comb(k+s-1, s-1)
    if r == 2:
        return 2*(s+1)*k, comb(k+s, s)**2
    return 2*(s+1)*k, comb(k+s+1, s+1)


def direct_dp(n, k):
    assert n >= 2
    # A state (a,b) records the last two labels, with the optimal total
    # cost and multiplicity among assignments satisfying all constraints
    # through the penultimate vertex.
    d = {(a, k): (a+k, 1) for a in range(k+1)}
    if n == 2:
        return k+k, 1
    for i in range(3, n+1):
        e = {}
        for (a,b),(value,count) in d.items():
            for c in range(k+1):
                if a+c < k:
                    continue
                key = (b,c)
                cost = value+c
                prev = e.get(key)
                if prev is None or cost<prev[0]:
                    e[key]=(cost,count)
                elif cost==prev[0]:
                    e[key]=(cost,prev[1]+count)
        d=e
    best=min(v for (a,b),(v,c) in d.items() if a==k)
    return best,sum(c for (a,b),(v,c) in d.items() if a==k and v==best)


def brute(n,k):
    best=None;count=0
    for f in product(range(k+1), repeat=n):
        if f[1]!=k or f[n-2]!=k:
            continue
        if any(f[i-1]+f[i+1]<k for i in range(1,n-1)):
            continue
        w=sum(f)
        if best is None or w<best:
            best=w;count=1
        elif w==best:
            count+=1
    return best,count


def main():
    checked=0
    for k in range(1,13):
        for n in range(2,81):
            want=predicted(n,k)
            found=direct_dp(n,k)
            assert found==want,(n,k,found,want)
            checked+=1
    exhaustive=0
    for k in range(1,5):
        for n in range(2,11):
            if (k+1)**n > 250000:
                continue
            want=predicted(n,k)
            found=brute(n,k)
            assert found==want,(n,k,found,want)
            exhaustive+=1
    for n,k in ((6,3),(9,5),(10,7),(13,2),(18,4),(22,9),(23,6)):
        print('CASE',n,k,'weight,count',predicted(n,k))
    print('DP_MATCH',checked,'cases')
    print('EXHAUSTIVE_MATCH',exhaustive,'cases')
    print('VERIFY_OK')

if __name__=='__main__':
    main()
