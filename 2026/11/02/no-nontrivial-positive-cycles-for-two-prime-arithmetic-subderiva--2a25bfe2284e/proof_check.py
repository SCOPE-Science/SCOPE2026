#!/usr/bin/env python3
"""Self-contained finite checks for the two-prime arithmetic-subderivative theorem.
These computations are diagnostic; the infinite theorem uses an explicit proof.
"""
from math import gcd

def primes_up_to(n):
    return [a for a in range(2,n+1) if all(a%d for d in range(2,int(a**.5)+1))]

def valuation(n,p):
    v=0
    while n and n%p==0:
        n//=p;v+=1
    return v

def subderivative(n,p,q):
    if not n: return 0
    a,b=valuation(n,p),valuation(n,q)
    return (n//p)*a+(n//q)*b if (a and b) else (n*a//p+n*b//q)

def U_next(u,p,q):
    return u-(p+q)+q*valuation(u,p)+p*valuation(u,q)

def smooth(u,p,q):
    while u%p==0: u//=p
    while u%q==0: u//=q
    return u==1

ps=primes_up_to(53)
pairs=0;smooth_cases=0;cycles=0;trials=0
for i,p in enumerate(ps):
    for q in ps[i+1:]:
        pairs+=1;P=p*q
        # Check the key threshold transition for every p,q-smooth U in an explicit finite rectangle.
        for a in range(18):
            for b in range(18):
                u=p**a*q**b
                if u>P:
                    smooth_cases+=1
                    assert U_next(u,p,q)>P,(p,q,a,b,u,U_next(u,p,q))
        # Independently verify fixed-point classification in the integer range.
        if q<=19:
            for n in range(1,2501):
                fixed=(subderivative(n,p,q)==n)
                c1=(valuation(n,p)==p and valuation(n,q)==0)
                c2=(valuation(n,p)==0 and valuation(n,q)==q)
                assert fixed==(c1 or c2),(p,q,n)
                trials+=1
                # Bounded numerical dynamical check, not a proof of aperiodicity.
                if n%10: continue
                x=n;seen={}
                for step in range(60):
                    if not x or x.bit_length()>135: break
                    if x in seen:
                        assert step-seen[x]==1, (p,q,n,seen[x],step,x)
                        cycles+=1
                        break
                    seen[x]=step
                    x=subderivative(x,p,q)
# Show smoothness is necessary: non-smooth u=7>P=6 descends under T_{2,3}.
assert not smooth(7,2,3) and U_next(7,2,3)==2
print('VERIFY_OK prime_pairs=%d smooth_threshold_cases=%d fixed_tests=%d repeated_fixed_orbits=%d nonsmooth_boundary=7_to_2' % (pairs,smooth_cases,trials,cycles))
