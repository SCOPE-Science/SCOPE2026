#!/usr/bin/env python3
"""Exact independent tests for radix-renewal binary substitution."""
from collections import Counter

checks=0

def require(x, note='mismatch'):
    global checks
    assert x,note
    checks+=1

def fixed(k, length):
    w=[0]
    while len(w)<length:
        w=[y for a in w for y in ([0]*(k-1)+[1-a])]
    return w[:length]

def valuation_parity(k,n):
    v=0
    while n%k==0:
        n//=k;v+=1
    return v%2

def alternating(k,n):
    a=0;sgn=-1
    while n:
        a+=sgn*(n%k)
        n//=k;sgn=-sgn
    return a

def carry_range(k,n):
    assert n>0
    digits=[]
    while n:
        digits.append(n%k);n//=k
    h=len(digits)
    # Dynamic programming uses c_j for incoming carry; the weight of
    # c_(j+1) is (-1)^(j+2). All possible finite tails are included.
    states={0:{0}}
    for j,a in enumerate(digits):
        new={0:set(),1:set()}
        for c,vals in states.items():
            for cp in (0,1):
                if cp==0 and a+c==k:continue
                if cp==1 and a+c==0:continue
                for value in vals:
                    new[cp].add(value+(cp if j%2==0 else -cp))
        states=new
    # One must remove the last emitted carry weight, replacing it
    # with the full tail contribution from c_h onwards.
    outcomes=set(states[0])
    # state values already include weighted c_h, so add 0 or
    # the possible extra opposite-sign carry at c_(h+1).
    outcomes.update(states[1])
    outcomes.update(v + (-1 if h%2 else 1) for v in states[1])
    return min(outcomes),max(outcomes),outcomes

for k in range(2,7):
    length=min(k**6+200,20000)
    w=fixed(k,length)
    for n in range(length):
        require(w[n]==valuation_parity(k,n+1),(k,n,'valuation'))
    pref=[0]
    for x in w:pref.append(pref[-1]+x)
    for n in range(length+1):
        require((k+1)*pref[n]-n==alternating(k,n),(k,n,'digit'))
    for m in range(1,5):
        if k**m>length-100:break
        histogram=Counter((k+1)*pref[n]-n for n in range(k**m))
        expected=Counter({0:1})
        for j in range(m):
            new=Counter()
            for a,b in expected.items():
                for d in range(k):
                    new[a+(d if j%2 else -d)]+=b
            expected=new
        require(histogram==expected,(k,m,'histogram'))
        v=(k**(2*m)-1)//(k+1)
        if v>0:
            lo,hi,vals=carry_range(k,v)
            require((lo,hi)==(0,m),(k,m,'ladder'))
            require(vals==set(range(m+1)),(k,m,'full ladder'))
        for start in range(min(100,length-k**m)):
            count=pref[start+k**m]-pref[start]
            lo=k**m//(k+1)
            require(count in (lo,lo+1),(k,m,start,'scale'))
    for n in range(1, min(80,length//3)):
        lo,hi,vals=carry_range(k,n)
        # independent finite brute values for a long enough window start
        observed={pref[start+n]-pref[start] for start in range(length-n)}
        baseline=pref[n]
        require((min(observed),max(observed))==(baseline+lo,baseline+hi),(k,n,'extrema'))
        require(observed==set(range(baseline+lo,baseline+hi+1)),(k,n,'interval'))
print('OK:',checks,'independent exact assertions')
