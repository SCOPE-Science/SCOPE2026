# Exact Kummer borrow-count verifier for the first multiplier window.
from math import isqrt

def primes_to(n):
    return [p for p in range(2,n+1) if all(p%d for d in range(2,isqrt(p)+1))]

def valuation_binomial(n,k,p):
    count=0
    mod=p
    while mod<=n:
        count += (k%mod > n%mod)
        mod*=p
    return count

def predicted(p,q):
    if q==p+1: return 0
    if q==(p+1)//2:return 2
    return 1

runs=0
for p in primes_to(71):
    if p==2: continue
    m=2*p-1
    for q in range(2,p+2):
        actual=min(valuation_binomial(m*q,m*d,p) for d in range(1,q))
        expected=predicted(p,q)
        if actual!=expected:
            raise AssertionError((p,q,actual,expected))
        runs+=1
print('CERTIFICATE_OK',runs)
