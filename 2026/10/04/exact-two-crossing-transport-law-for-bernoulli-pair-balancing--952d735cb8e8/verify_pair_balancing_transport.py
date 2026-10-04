#!/usr/bin/env python3
from fractions import Fraction
import random

def conv(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def bern(p):
    return [1-p,p]

def pb(ps):
    a=[Fraction(1)]
    for p in ps:
        a=conv(a,bern(p))
    return a

def get(a,k):
    return a[k] if 0<=k<len(a) else Fraction(0)

def d1(a):
    return [get(a,k)-get(a,k-1) for k in range(0,len(a)+1)]

def d2(a):
    return [get(a,k)-2*get(a,k-1)+get(a,k-2) for k in range(0,len(a)+2)]

def sign_changes(seq):
    ss=[1 if x>0 else -1 for x in seq if x]
    return ss, sum(ss[i]!=ss[i-1] for i in range(1,len(ss)))

def cdf(a,k):
    return sum((a[j] for j in range(0,min(k,len(a)-1)+1)),Fraction(0)) if k>=0 else Fraction(0)

def tv(a,b):
    n=max(len(a),len(b))
    return sum(abs(get(a,k)-get(b,k)) for k in range(n))/2

def dk(a,b):
    n=max(len(a),len(b))
    return max(abs(cdf(a,k)-cdf(b,k)) for k in range(-1,n+1))

def w1_integer(a,b):
    n=max(len(a),len(b))
    return sum(abs(cdf(a,k)-cdf(b,k)) for k in range(-1,n+1))

def stoploss(a,h):
    return sum(Fraction(max(k-h,0))*p for k,p in enumerate(a))

def is_unimodal(a):
    m=max(a)
    first=a.index(m)
    last=len(a)-1-a[::-1].index(m)
    return all(a[i]<=a[i+1] for i in range(first)) and all(a[i]>=a[i+1] for i in range(last,len(a)-1))

def run():
    rng=random.Random(20261002)
    pmf_checks=0
    cdf_checks=0
    metric_checks=0
    stoploss_checks=0
    crossing_checks=0
    variation_checks=0

    for _ in range(18000):
        ps=[Fraction(rng.randrange(0,13),12) for __ in range(rng.randrange(0,9))]
        a=pb(ps)
        assert is_unimodal(a)
        dd1=d1(a)
        dd2=d2(a)

        ss,ch=sign_changes(dd2)
        assert ch==2
        assert ss[0]==1 and ss[-1]==1
        # With exactly two changes and positive ends, the nonzero pattern is +,-,+.
        crossing_checks+=1

        assert sum(abs(x) for x in dd1)==2*max(a)
        variation_checks+=1

        p=Fraction(rng.randrange(0,13),12)
        q=Fraction(rng.randrange(0,13),12)
        s=p+q
        pt=qt=s/2
        delta=pt*qt-p*q
        assert delta>=0

        w=conv(a,conv(bern(p),bern(q)))
        wt=conv(a,conv(bern(pt),bern(qt)))
        n=max(len(w),len(wt))

        for k in range(n):
            assert get(wt,k)-get(w,k)==delta*get(dd2,k)
            pmf_checks+=1

        for k in range(-1,n+1):
            rhs=delta*(get(a,k)-get(a,k-1))
            assert cdf(wt,k)-cdf(w,k)==rhs
            cdf_checks+=1

        assert tv(wt,w)==delta*sum(abs(x) for x in dd2)/2
        assert dk(wt,w)==delta*max(abs(x) for x in dd1)
        assert w1_integer(wt,w)==2*delta*max(a)
        metric_checks+=3

        for h in range(-2,len(w)+2):
            assert stoploss(wt,h)-stoploss(w,h)==delta*get(a,h-1)
            stoploss_checks+=1

    # Exhaustive small rational grids, including deterministic backgrounds.
    vals=[Fraction(i,4) for i in range(5)]
    for nbg in range(0,5):
        from itertools import product
        for ps in product(vals, repeat=nbg):
            a=pb(list(ps))
            ss,ch=sign_changes(d2(a))
            assert ch==2 and ss[0]==1 and ss[-1]==1
            assert is_unimodal(a)
            assert sum(abs(x) for x in d1(a))==2*max(a)
            crossing_checks+=1
            variation_checks+=1

    print(
        "VERIFY_OK "
        f"pmf_checks={pmf_checks} "
        f"cdf_checks={cdf_checks} "
        f"metric_checks={metric_checks} "
        f"stoploss_checks={stoploss_checks} "
        f"crossing_checks={crossing_checks} "
        f"variation_checks={variation_checks}"
    )

if __name__=="__main__":
    run()
