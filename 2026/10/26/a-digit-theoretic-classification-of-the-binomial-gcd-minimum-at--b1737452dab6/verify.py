"""Exact independent tests for the binomial-GCD function on six times a prime."""
from math import comb, gcd

def primes(limit):
    sieve = bytearray(b'\x01')*(limit+1)
    sieve[0:2] = b'\x00\x00'
    for j in range(2,int(limit**.5)+1):
        if sieve[j]: sieve[j*j::j] = b'\x00'*(((limit-j*j)//j)+1)
    return [j for j in range(2,limit+1) if sieve[j]]

def ternary_zero_one(p):
    while p:
        if p%3 == 2: return False
        p//=3
    return True

def predicted(p):
    if p==5: return 6
    if ternary_zero_one(p): return 2
    if not (p&(p<<1)): return 3
    return 6

def lucas_nonzero(n,k,p):
    while k:
        if k%p > n%p: return False
        k//=p; n//=p
    return True

def mod_lucas_gcd(n,k,p):
    ans=1
    for q in (2,3,p):
        if not lucas_nonzero(n,k,q): ans*=q
    return ans

def run():
    sample=[]
    for p in primes(151):
        if p<=3: continue
        n=6*p
        expected=predicted(p)
        # direct independent integer binomial evaluation
        actual=min(gcd(n,comb(n,k)) for k in range(2,n//2+1))
        assert actual==expected,(p,actual,expected)
        sample.append((p,actual))
    reps = {2:[],3:[],6:[]}
    for p in primes(997):
        if p<=5: continue
        n=6*p
        actual=min(mod_lucas_gcd(n,k,p) for k in range(2,n//2+1))
        expected=predicted(p)
        assert actual==expected,(p,actual,expected)
        if len(reps[actual])<8: reps[actual].append(p)
    assert gcd(30,comb(30,5))==6
    print('VERIFY_OK: %d primes <=151 via all exact binomial coefficients; %d primes <=997 by independent Lucas digit test; examples %s' % (len(sample),len(primes(997))-3,reps))
if __name__=='__main__':run()
