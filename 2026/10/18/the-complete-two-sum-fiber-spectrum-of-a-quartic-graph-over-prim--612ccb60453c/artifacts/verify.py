#!/usr/bin/env python3
"""Exact two-sum fiber census for the quartic graph over prime-square rings."""
from collections import Counter

def chi(a,p):
    a%=p
    if a==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

def closed(p):
    b,c,e=(chi(-1,p),chi(-3,p),chi(-6,p))
    h=4 if p%4==1 else 2
    L=(p-2+b)//4
    H=(p-4-b-2*c-2*e)//8
    assert 4*L==p-2+b and 8*H==p-4-b-2*c-2*e
    assert L>=0 and H>=0
    u,v=1+c,1+e
    unit=Counter({2:p*L,4:p*H})
    unit[p+v]+=1
    unit[v]+=p-1
    unit[p*u]+=1
    unit[0]+=p*p-sum(unit.values())
    div=Counter({h:p*(p-1)//h,p:1})
    div[0]+=p*p-sum(div.values())
    agg=Counter()
    for k,vv in unit.items():agg[k]+=(p*p-p)*vv
    for k,vv in div.items():agg[k]+=p*vv
    agg={k:v for k,v in agg.items() if v}
    assert sum(agg.values())==p**4
    energy=sum(k*k*v for k,v in agg.items())
    expected=p*p*(6*p*p-8*p+3+2*(p-1)*(p-2)*c)
    assert energy==expected
    return agg,energy

def direct(p):
    n=p*p
    observed=Counter()
    for a in range(n):
        a4=pow(a,4,n)
        for b in range(n):
            observed[((a+b)%n,(a4+pow(b,4,n))%n)]+=1
    return Counter(list(observed.values())+[0]*(n*n-len(observed)))

for p in (5,7,11,13,17,19):
    predicted,E=closed(p)
    measured=direct(p)
    assert measured==Counter(predicted),(p,measured,predicted)
    assert sum(k*k*v for k,v in measured.items())==E
    print("p=%d distinct_fibers=%d sumset=%d energy=%d"%(p,len(measured),p**4-measured[0],E))
print("VERIFY_OK primes=6 exact_pair_counts=PASS exact_fiber_spectra=PASS")
