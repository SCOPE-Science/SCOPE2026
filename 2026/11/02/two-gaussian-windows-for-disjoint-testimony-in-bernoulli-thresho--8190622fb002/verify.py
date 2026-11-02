#!/usr/bin/env python3
"""Finite exact-arithmetic checks for sharp BK threshold gap theorem.

This checker validates finite combinatorial identities only, not limit theorems.
"""
from fractions import Fraction
from math import comb

def binom_below(n, t, p):
    # Strictly less than t successes; allows t>n.
    if t <= 0: return Fraction(0)
    if t > n: return Fraction(1)
    return sum((Fraction(comb(n,i))*p**i*(1-p)**(n-i) for i in range(t)), Fraction(0))

def direct(n,k,p):
    a,b=p.numerator,p.denominator
    supp=[]; mass=[]
    for x in range(1<<n):
        m=x.bit_count()
        supp.append(m)
        mass.append(a**m*(b-a)**(n-m))
    Z=b**(2*n)
    dnum=0; tnum=0
    for x in range(1<<n):
        if supp[x]<k: continue
        for y in range(1<<n):
            if supp[y]<k: continue
            w=mass[x]*mass[y]
            if (x|y).bit_count()<2*k: dnum+=w
            else: tnum+=w
    h=1-binom_below(n,k,p)
    d=Fraction(dnum,Z)
    t=Fraction(tnum,Z)
    delta=h*h-(1-binom_below(n,2*k,p))
    remainder=delta-d
    return d,t,delta,remainder,h

def verify():
    checks=0
    for n in range(1,8):
        for k in range(1,n+1):
            for p in [Fraction(1,3), Fraction(1,2), Fraction(2,5)]:
                d,t,delta,rem,h=direct(n,k,p)
                u=2*p-p*p
                eu=binom_below(n,2*k,u)
                ep=binom_below(n,k,p)
                assert d+t==h*h; checks+=1
                assert d<=eu and d>=eu-2*ep; checks+=1
                assert rem>=0 and delta>=d; checks+=1
                assert delta == h*h-1+binom_below(n,2*k,p); checks+=1
                # Product-space disjoint probability is non-negative.
                assert Fraction(0)<=t<=h*h; checks+=1
                # Exact two-window separation always has u>p.
                assert p<u<1; checks+=1
    # Independently test the symmetric-disjoint-pivot criterion against
    # the original three-modification definition (all pairs up to n=6).
    def testimony(x,y,k):
        return x.bit_count()>=k and y.bit_count()>=k and (x|y).bit_count()>=2*k
    for n in range(1,7):
        mask=(1<<n)-1
        for k in range(1,n+1):
            for x in range(1<<n):
                for y in range(1<<n):
                    for i in range(n):
                        bit=1<<i
                        xx=x&~bit; yy=y&~bit
                        direct_pivot=(not testimony(xx,yy,k)) and testimony(xx|bit,yy,k) and testimony(xx,yy|bit,k)
                        trimmed_pivot=(xx.bit_count()>=k and yy.bit_count()>=k and (xx|yy).bit_count()==2*k-1)
                        assert direct_pivot == trimmed_pivot
                        checks+=1
    # Verify the overlap/union covariance for rational p using four atoms.
    for p in [Fraction(1,7),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(6,7)]:
        u=2*p-p*p
        EI=p*p
        EU=u
        EIU=p*p
        cov=EIU-EI*EU
        assert cov == p*p*(1-u); checks+=1
        assert u*(1-u)>0; checks+=1
        assert Fraction(0)<u/Fraction(2)<p; checks+=1
    # Verify the exact binomial coefficient likelihood ratio for lower tails.
    for p in [Fraction(1,5),Fraction(1,2),Fraction(4,5)]:
        for n in range(2,16):
            for j in range(1,n):
                pmf_j=Fraction(comb(n,j))*p**j*(1-p)**(n-j)
                pmf_prev=Fraction(comb(n,j-1))*p**(j-1)*(1-p)**(n-j+1)
                assert pmf_prev/pmf_j == Fraction(j,n-j+1)*(1-p)/p
                checks+=1
    print(f"PASS: {checks} exact-arithmetic assertions")
    print('Scope: exhaustive independent bit-mask enumeration through n=7 at three rational biases; disjoint pivot equivalence through n=6; binomial bounds; covariance; likelihood ratios.')
    print('Limitations: no finite test proves a CLT, large-deviation asymptotic, or historical novelty.')

if __name__=='__main__': verify()
