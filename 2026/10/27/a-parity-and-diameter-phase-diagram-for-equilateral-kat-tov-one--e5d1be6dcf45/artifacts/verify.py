#!/usr/bin/env python3
"""Direct enumeration of finite integer-distance Katetov vectors."""
from itertools import product
from math import ceil


def exact(D, s, n):
    """Closed sum partitioned by the minimum distance."""
    assert 1 <= s <= D and n >= 1
    a = (s + 1) // 2
    high = sum((min(D, m+s)-m+1)**n - (min(D, m+s)-m)**n
               for m in range(a, D+1))
    low = n*sum((min(D, m+s) - (s-m)+1)**(n-1)
                for m in range(1,a))
    return high+low


def brute(D,s,n):
    return sum(1 for v in product(range(1,D+1),repeat=n)
               if all(abs(v[i]-v[j])<=s<=v[i]+v[j]
                      for i in range(n) for j in range(i+1,n)))


def asymptotic_data(D,s):
    a=(s+1)//2
    W=min(s+1,D-a+1)
    r=max(1,D-s-a+1)
    exceptional=(s>=3 and s%2==1 and D<=(3*s-1)//2)
    return (W,r,exceptional)


def main():
    checked=0
    for D in range(1,9):
        for s in range(1,D+1):
            for n in range(1,6):
                x=exact(D,s,n); y=brute(D,s,n)
                assert x==y,(D,s,n,x,y)
                checked+=1
    for D in range(1,6):
        for s in range(1,D+1):
            for n in [6,7]:
                x=exact(D,s,n);y=brute(D,s,n)
                assert x==y,(D,s,n,x,y)
                checked+=1
    for D in range(1,16):
        for s in range(1,D+1):
            W,r,exceptional=asymptotic_data(D,s)
            assert W>=1 and r>=1
            seq=exact(D,s,100)
            if exceptional:
                assert 0.95<seq/(100*W**99)<1.5,(D,s)
            else:
                assert abs(seq/(W**100)-r) < max(0.1,r*0.01),(D,s,seq/(W**100),r)
    print(f'BRUTE_FORCE_MATCHES={checked}')
    print('ASYMPTOTIC_REGIMES_CHECKED=120')
    print('ALL_TESTS_PASS')


if __name__=='__main__':
    main()
