"""Exact finite checks for reciprocal divisor-power sums. Python standard library only."""
from math import gcd

LIM=30000
spf=list(range(LIM+1))
for p in range(2,int(LIM**0.5)+1):
    if spf[p]==p:
        for x in range(p*p,LIM+1,p):
            if spf[x]==x:spf[x]=p

def factors(n):
    out={}
    while n>1:
        p=spf[n]; out[p]=out.get(p,0)+1;n//=p
    return out

def v2(n):
    s=0
    while n%2==0:
        s+=1;n//=2
    return s

def good(f):
    return all(((a+1)&a)==0 for a in f.values())

def sigma(f,k):
    z=1
    for p,a in f.items():
        # Mersenne exponent factorization independently of modular-order reasoning.
        z*=sum(p**(k*j) for j in range(a+1))
    return z

PRIMES=[i for i in range(3,1001,2) if all(i%d for d in range(3,int(i**.5)+1,2))]
for k in (2,4,6,8,12):
    processed=0; support=0; seen=set(); t=v2(k)
    bad_mod_primes=[q for q in PRIMES if v2(q-1)<=t]
    for n in range(1,LIM+1):
        f=factors(n)
        if not good(f):continue
        a=sigma(f,k); processed+=1
        # No numerator prime q<=1000 in forbidden residue classes.
        for q in bad_mod_primes:
            assert a%q!=0,(k,n,q)
        den=n**k//gcd(a,n**k)
        for q,e in f.items():
            if q!=2 and v2(q-1)<=t:
                assert den%(q**(k*e))==0,(k,n,q)
        if all(q==2 or v2(q-1)<=t for q in f):
            support+=1
            red=(a,den)
            assert red not in seen,(n,k)
            seen.add(red)
    print('CHECK',k,'Mersenne-exponent',processed,'protected-only',support,'distinct',len(seen),'forbidden-primes',len(bad_mod_primes))
assert sigma(factors(63),2)%7==0
assert sigma(factors(15),2)%5==0
print('BOUNDARY_OK')
