#!/usr/bin/env python3
import math

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    d = 3
    while d*d <= n:
        if n % d == 0: return False
        d += 2
    return True

def vp(n,p):
    c=0
    while n and n%p==0:
        n//=p; c+=1
    return c

def vp_fact(n,p):
    s=0
    while n:
        n//=p; s+=n
    return s

def vp_binom(n,k,p):
    return vp_fact(n,p)-vp_fact(k,p)-vp_fact(n-k,p)

def carry_count(x,y,p):
    c=0; carry=0
    while x or y or carry:
        sx=x%p; sy=y%p
        z=sx+sy+carry
        if z>=p:
            c+=1; carry=1
        else:
            carry=0
        x//=p; y//=p
    return c

primes=[p for p in range(2,102) if is_prime(p)]
pretarget=target=direct_gcd=0
for p in primes:
    m=p+1
    assert p < m < p*p
    for q in range(2,p):
        N=m*q; k=m
        assert carry_count(k,N-k,p)==0
        assert vp_binom(N,k,p)==0
        vals=[vp_binom(N,m*d,p) for d in range(1,q)]
        assert min(vals)==0
        pretarget += 1
    q=p; N=m*q
    vals=[]
    for d in range(1,p):
        k=m*d
        c=carry_count(k,N-k,p)
        v=vp_binom(N,k,p)
        assert c==2 and v==2
        vals.append(v); target += 1
    assert min(vals)==2
    # Direct integer GCD check for modest primes; this corroborates the valuation minimum.
    if p <= 31:
        g=0
        for d in range(1,p):
            g=math.gcd(g, math.comb(N,m*d))
        assert vp(g,p)==2
        direct_gcd += 1
print(f"VERIFY_OK primes={len(primes)} pretarget_rows={pretarget} target_coefficients={target} direct_gcd_rows={direct_gcd}")
