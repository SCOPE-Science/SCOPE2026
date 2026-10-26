"""Independent finite checks for two-cycle statistics of uniform finite maps.

No external data or packages are required.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import log, sqrt, pi


def harmonic(k):
    return sum((Fraction(1,j) for j in range(1,k+1)), Fraction(0))


def exact_cycle_law(n):
    assert n>=2
    a=Fraction(1)
    w={}
    for k in range(1,n+1):
        a*=Fraction(n-k+1,n)
        if k>=2:
            w[k]=a*harmonic(k-1)
    z=sum(w.values(),Fraction(0))
    out={}
    for k in range(2,n+1):
        h=harmonic(k-1)
        for s in range(1,k//2+1):
            if 2*s==k:
                pr=Fraction(k,2*s*s)/h
            else:
                pr=(Fraction(1,s)+Fraction(1,k-s))/h
            out[k,s]=w[k]*pr/z
    assert sum(out.values(),Fraction(0))==1
    return out,z


def cycle_lengths(f):
    n=len(f); seen=set(); cycles=[]
    for v in range(n):
        if v in seen: continue
        trail={}; at=v
        while at not in trail and at not in seen:
            trail[at]=len(trail)
            at=f[at]
        if at in trail:
            cycles.append(len(trail)-trail[at])
        seen.update(trail)
    return cycles


def exhaustive(n):
    counts=Counter()
    for f in product(range(n),repeat=n):
        cyc=cycle_lengths(f)
        if len(cyc)==2:
            counts[(sum(cyc),min(cyc))]+=1
    law,z=exact_cycle_law(n)
    total=sum(counts.values())
    assert Fraction(total,n**n)==z/n
    assert set(counts)==set(law)
    for key,pr in law.items():
        assert Fraction(counts[key],total)==pr, (n,key,counts[key],pr)
    return total, len(counts)


def asymptotic(n):
    a=1.0; z=0.0; m1=0.0; m2=0.0; harmonic_prev=0.0
    # ratio recurrence stable in the transition range k=O(sqrt(n))
    # beyond k=10 sqrt(n), a is negligible; this is only a numerical diagnostic.
    cap=min(n, int(12*sqrt(n))+10)
    for k in range(1,cap+1):
        a*=1-(k-1)/n
        if k>=2:
            harmonic_prev+=1/(k-1)
            z+=a*harmonic_prev
            h_half=sum(1/j for j in range(1,k//2+1))
            # Exact unnormalized first and second power moments.
            tail_h=harmonic_prev-h_half
            m1+=a*(k*tail_h+(k%2==0))
            j=(k-1)//2
            m2+=a*(k*k*tail_h-k*j+(k/2 if k%2==0 else 0))
    return z,m1/z,m2/z

if __name__=='__main__':
    for n in range(2,7):
        total,strata=exhaustive(n)
        print('EXACT_MAP_ENUMERATION_PASS',n,n**n,'maps',total,'two-component maps',strata,'strata')
    const=2*log(2)*sqrt(2/pi)
    for n in (1000,10000,100000):
        z,mean,second=asymptotic(n)
        scale=mean*log(n)/sqrt(n)
        scale2=second*log(n)/n
        print('NUMERICAL_MOMENT_DIAGNOSTIC',n,'mean',round(mean,10),'scaled',round(scale,8),'target',round(const,8),'second_scaled',round(scale2,8),'second_target',round(2*log(2)-1,8))
    print('VERIFY_OK')
