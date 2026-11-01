#!/usr/bin/env python3
"""Exact enumeration of chip-firing two-cycle counts on complete graphs with a deleted matching."""
from math import comb, exp
from itertools import combinations, product


def exact_count(n, k):
    assert n >= 3 and 0 <= k <= n // 2
    unpaired = n - 2*k
    total = 0
    for s in range(k+1):
        for p in range(k-s+1):
            for t in range(unpaired+1):
                a = s + 2*p + t
                b = n-a
                if not (1 <= a < n):
                    continue
                multiplicity = comb(k, s)*2**s*comb(k-s,p)*comb(unpaired,t)
                # 0**0 = 1, correctly: no vertex of that particular type
                product_of_cross_degrees = b**(a-s)*a**(b-s)*((a-1)*(b-1))**s
                total += multiplicity * product_of_cross_degrees
    assert total % 2 == 0
    return total // 2


def direct_cut_count(n,k):
    missing = {tuple(sorted((2*j,2*j+1))) for j in range(k)}
    weight=0
    for bit in range(1,2**n-1):
        side={i for i in range(n) if bit>>i&1}
        w=1
        for i in range(n):
            c=sum((i in side)!=(j in side) for j in range(n) if i!=j and tuple(sorted((i,j))) not in missing)
            w*=c
        weight+=w
    assert weight%2 == 0
    return weight//2


def direct_chip_states(n,k):
    missing={tuple(sorted((2*j,2*j+1))) for j in range(k)}
    adj=[[j for j in range(n) if i!=j and tuple(sorted((i,j))) not in missing] for i in range(n)]
    d=[len(row) for row in adj]
    found=set()
    for bit in range(1,2**n-1):
        fire=[bool(bit>>i&1) for i in range(n)]
        cross=[sum(fire[j]!=fire[i] for j in adj[i]) for i in range(n)]
        if 0 in cross:continue
        rr=[range(d[i],d[i]+cross[i]) if fire[i] else range(d[i]-cross[i],d[i]) for i in range(n)]
        for chips in product(*rr):
            fired=tuple(int(chips[i]>=d[i]) for i in range(n))
            assert fired == tuple(map(int,fire))
            y=tuple(chips[i]-d[i]*fired[i]+sum(fired[j] for j in adj[i]) for i in range(n))
            fired2=tuple(int(y[i]>=d[i]) for i in range(n))
            assert fired2==tuple(1-e for e in fired)
            z=tuple(y[i]-d[i]*fired2[i]+sum(fired2[j] for j in adj[i]) for i in range(n))
            assert z==chips and y!=chips and min(y)>=0
            found.add(min(chips,y))
    return len(found)

if __name__ == '__main__':
    print('Direct cut and state checks')
    for n in range(3,7):
        for k in range(n//2+1):
            a=exact_count(n,k)
            b=direct_cut_count(n,k)
            c=direct_chip_states(n,k)
            assert a==b==c,(n,k,a,b,c)
            print(n,k,a,'PASS')
    print('Further independent cut enumerations')
    for n in range(7, 11):
        for k in range(n//2 + 1):
            a = exact_count(n,k)
            b = direct_cut_count(n,k)
            assert a == b, (n,k,a,b)
            print(n,k,a,'PASS')
    print('Asymptotic computations')
    for n in [10,20,40,80,120]:
        base=exact_count(n,0)
        rows=[]
        for k in [0,n//8,n//4,n//2]:
            ratio=exact_count(n,k)/base
            limit=exp(-2*k/n)
            rows.append((k,round(ratio,10),round(limit,10),round(n*abs(ratio-limit),8)))
        print(n,rows)
    print('ALL CHECKS PASSED')
