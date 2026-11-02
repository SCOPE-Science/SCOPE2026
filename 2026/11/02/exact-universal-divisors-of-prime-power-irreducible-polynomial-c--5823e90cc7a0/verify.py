"""Exact checks for universal divisors of prime-power necklace polynomials.
Run with Python 3; uses only the standard library. The general theorem is proved
symbolically in its accompanying manuscript, not by these finite checks.
"""
from math import gcd, isqrt

def primes_upto(n):
    sieve=bytearray(b'\x01')*(n+1)
    if n >=0:sieve[0]=0
    if n >=1:sieve[1]=0
    for d in range(2,isqrt(n)+1):
        if sieve[d]:sieve[d*d:n+1:d]=b'\0'*(((n-d*d)//d)+1)
    return [i for i in range(2,n+1) if sieve[i]]

def valuation(n,p):
    v=0
    while n%p==0 and n:
        n//=p;v+=1
    return v

def predicted(p,a):
    n=p**a;t=p**(a-1);k=t*(p-1)
    out={}
    for ell in primes_upto(k+1):
        if ell == 2:
            h=1 if k%2 else valuation(k,2)+2
        elif k%(ell-1)==0:
            h=1+valuation(k,ell)
        else:
            h=0
        e=min(t,h)- (a if ell==p else 0)
        assert e>=0,(p,a,ell,e)
        if e:out[ell]=e
    g=1
    for ell,e in out.items():g*=ell**e
    return g,out

def primepowers(bound):
    primes=primes_upto(bound)
    out=set(primes)
    for p in primes:
        n=p*p
        while n<=bound:
            out.add(n);n*=p
    return sorted(out)

cases=0
for p in [2,3,5,7,11]:
    for a in range(1,8 if p==2 else 4 if p<=5 else 3):
        n=p**a
        if n>1024:continue
        g,ex=predicted(p,a)
        measured=0
        for x in primepowers(70):
            I=(pow(x,n)-pow(x,n//p))//n
            measured=gcd(measured,I)
            assert I%g==0,(p,a,x,g)
        assert measured==g,(p,a,g,measured)
        cases+=1
        print('degree',n,'universal_gcd',g,'prime_exponents',ex)
print('VERIFY_OK cases=',cases,'all_prime_power_samples<=70 and exact_gcd_witnesses')
