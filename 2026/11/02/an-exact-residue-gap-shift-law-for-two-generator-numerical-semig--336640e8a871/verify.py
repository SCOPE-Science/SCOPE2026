#!/usr/bin/env python3
"""Exact independent finite checks of a residue-gap shift law."""
from math import gcd
from fractions import Fraction


def gaps(a, b):
    # Sylvester conductor for coprime positive generators; direct membership
    # is computed independently by forward dynamic programming.
    assert a >= 2 and b > a and gcd(a, b) == 1
    f = a*b-a-b
    reachable = [False] * (f+1)
    reachable[0] = True
    for n in range(1, f+1):
        reachable[n] = (n >= a and reachable[n-a]) or (n >= b and reachable[n-b])
    return [n for n in range(1, f+1) if not reachable[n]]


def profile(a, k, m):
    out = [0]*m
    for v in gaps(a,a+k):
        out[v%m] += 1
    return out


def predicted(a,k,m):
    d,e=gcd(a,m),gcd(a+k,m)
    assert gcd(a,k)==gcd(a+m,k)==1 and gcd(d,e)==1
    invd=pow(k,-1,d) if d>1 else 0
    inve=pow(k,-1,e) if e>1 else 0
    twice_base=2*a+k+m-d+e
    assert twice_base%2==0
    base=twice_base//2
    return [base + ((t*invd)%d) - ((t*inve)%e) - (e if t%e==0 else 0) for t in range(m)]


def check():
    instances=cases=0
    for m in range(2,22):
        for k in range(1,19):
            for a in range(2,34):
                if gcd(a,k)>1 or gcd(a+m,k)>1:
                    continue
                actual=[y-x for x,y in zip(profile(a,k,m),profile(a+m,k,m))]
                want=predicted(a,k,m)
                assert actual==want,(a,k,m,actual,want)
                d,e=gcd(a,m),gcd(a+k,m)
                assert max(actual)-min(actual)==d+e-2
                mean=Fraction(sum(actual),m)
                variance=sum((Fraction(x)-mean)**2 for x in actual)/m
                assert variance==Fraction(d*d+e*e-2,12)
                assert (len(set(actual))==1)==(d==e==1)
                assert actual[0]==a+(k+m-d-e)//2
                pairs={}
                for t in range(m):
                    u=(t*pow(k,-1,d))%d if d>1 else 0
                    v=((t*pow(k,-1,e))%e if e>1 else 0)
                    if v==0:v=e
                    pairs[(u,v)]=pairs.get((u,v),0)+1
                assert len(pairs)==d*e
                assert set(pairs.values())=={m//(d*e)}
                instances+=m
                cases+=1
    print('VERIFY_OK parameters=%d residue_instances=%d independent_dp=yes CRT_and_variance=yes exact_rationals=yes' % (cases,instances))

if __name__=='__main__':
    check()
