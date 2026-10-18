#!/usr/bin/env python3
"""Finite exact verification of the deterministic ranked-record-age coupling bound.
This is corroboration only; the general statement has a direct boundary proof.
"""
from fractions import Fraction
from itertools import combinations

def ages_from_boundaries(n, times):
    v=[t-s for s,t in zip(times, times[1:])]+[n-times[-1]]
    return sorted(v,reverse=True)

def check(n, bits, record_indices, q):
    active=[t for t,b in enumerate(bits,1) if b]
    m=len(active)
    if m==0:return
    t=[0]+[active[j-1] for j in record_indices]
    s=[0]+list(record_indices)
    l=ages_from_boundaries(n,t)
    a=ages_from_boundaries(m,s)
    l=[Fraction(x,n) for x in l]
    a=[Fraction(x,m) for x in a]
    L=max(len(l),len(a))
    l+=[Fraction(0)]*(L-len(l));a+=[Fraction(0)]*(L-len(a))
    D=max(abs(sum(bits[:t])-q*t) for t in range(n+1))
    assert max(abs(x-y) for x,y in zip(l,a))<=3*D/(q*n),(n,bits,record_indices,q,l,a,D)
    h=(q*n).numerator//(q*n).denominator
    if h>=1:
        # The same jump sequence extended to h active steps; specify an arbitrary
        # compatible continuation of record indicators after m if h>m.
        # Choose no additional records; the theorem holds for every continuation.
        sh=[0]+[j for j in record_indices if j<=h]
        z=ages_from_boundaries(h,sh)
        z=[Fraction(x,h) for x in z]
        LL=max(len(l),len(z)); l2=l+[Fraction(0)]*(LL-len(l));z+=[Fraction(0)]*(LL-len(z))
        assert max(abs(x-y) for x,y in zip(l2,z))<=3*D/(q*n)+2*(D+1)/h

checks=0
for q in [Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]:
    for n in range(2,10):
        for mask in range(1,1<<n):
            bits=[(mask>>j)&1 for j in range(n)]
            m=sum(bits)
            for recordmask in range(1<<m):
                rec=[j+1 for j in range(m) if (recordmask>>j)&1]
                check(n,bits,rec,q)
                checks+=1
print('PASS:',checks,'exact rational tests over masks, record-time patterns and holding probabilities')
