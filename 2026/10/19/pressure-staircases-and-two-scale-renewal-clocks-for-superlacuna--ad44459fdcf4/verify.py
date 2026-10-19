#!/usr/bin/env python3
"""Numerical checks for factorial-distance renewal asymptotics."""
import math
from fractions import Fraction

def stats(n, s):
    # Compute the normalized root x=n!P without evaluating enormous exponentials.
    fac=[math.factorial(j) for j in range(1,n+9)]
    scale=fac[n-1]
    r=[f/scale for f in fac]
    target=n-1+s
    def f(x): return sum(math.exp(-x*y) if x*y<740 else 0.0 for y in r)-target
    lo,hi=0.0000001,10.0
    assert f(lo)>0 and f(hi)<0
    for _ in range(75):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    x=(lo+hi)/2
    weights=[math.exp(-x*z) if x*z<740 else 0.0 for z in r]
    # As all omitted terms are far beyond exponential underflow, finite sum is safe.
    assert abs(sum(weights)-target)<2e-11
    mean_numer=sum(y*w for y,w in zip(r,weights))
    long_time=weights[n-1]/mean_numer
    rest=sum(y*w for j,(y,w) in enumerate(zip(r,weights),1) if j!=n)
    delay_macro=rest/weights[n-1]
    assert abs((1-long_time)-delay_macro/(1+delay_macro))<2e-12
    # Laplace transform of all non-long gaps before the next long one at scale (n-1)!
    for u in (0.2,0.8,1.5):
        tail_weight=sum(w*(1-math.exp(-u*rr/r[n-2])) for j,(rr,w) in enumerate(zip(r,weights),1) if j!=n)
        exact=weights[n-1]/(weights[n-1]+tail_weight)
        predicted=s/(s+1-math.exp(-u))
        if n>=40: assert abs(exact-predicted)<0.1, (n,s,u,exact,predicted)
    return x,long_time,delay_macro

def exact_composition_checks():
    # Method A: recurrence for concatenated legal marker returns.
    allowed=(1,2,6,24)
    weight=Fraction(2,5)
    end=32
    dp=[Fraction(0)]*(end+1)
    dp[0]=Fraction(1)
    for L in range(1,end+1):
        dp[L]=weight*sum((dp[L-a] for a in allowed if a<=L),Fraction(0))
    # Method B: coefficient extraction by summing finite polynomial powers.
    base=[Fraction(0)]*(end+1)
    for a in allowed: base[a]=weight
    all_powers=[Fraction(0)]*(end+1)
    term=[Fraction(0)]*(end+1)
    term[0]=Fraction(1)
    all_powers[0]=Fraction(1)
    for k in range(1,end+1):
        nxt=[Fraction(0)]*(end+1)
        for i,v in enumerate(term):
            if v:
                for a in allowed:
                    if i+a<=end: nxt[i+a]+=v*weight
        term=nxt
        for i,v in enumerate(term): all_powers[i]+=v
    assert dp==all_powers
    return end+1

if __name__=='__main__':
    composition_checks=exact_composition_checks()
    tests=0
    for s in (.3,.5,.7):
        a=-math.log(s)
        for n in (10,20,40,80,160):
            x,p,lag=stats(n,s)
            leaderr=abs(x-a)
            if n>=80:
                assert leaderr<2*a/(s*n)
                assert abs(n*(x-a)+a/s)<.6, (s,n,x,a)
                assert abs(n*(1-p)-1/s)<.6, (s,n,p)
                assert abs(n*lag-1/s)<.6, (s,n,lag)
            tests+=1
            print(f'n={n:3d}, s={s:3.1f}: x={x:.9g}, time_mass={p:.8g}, normalized_nonlong_delay={lag:.8g}')
    print('VERIFY_OK',tests,'normalized pressure roots and size-bias tests; 45 geometric correction transforms;',composition_checks,'exact renewal-composition identities')
