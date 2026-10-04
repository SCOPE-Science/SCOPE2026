#!/usr/bin/env python3
from math import gcd
from fractions import Fraction

def pair_r9(x, y):
    return x*x-y*y, x*x-4*y*y

def pair_r4(x, y):
    return x*x+y*y, x*x-y*y

def common_zero_count(pair, p):
    return sum(1 for x in range(p) for y in range(p)
               if pair(x,y)[0] % p == 0 and pair(x,y)[1] % p == 0)

def local_good(pair, bad_primes, x, y):
    for p in bad_primes:
        a,b = pair(x,y)
        if a % p == 0 and b % p == 0:
            return False
    return True

def mu_sieve(n):
    mu=[1]*(n+1)
    isprime=[True]*(n+1)
    primes=[]
    mu[0]=0
    for i in range(2,n+1):
        if isprime[i]:
            primes.append(i); mu[i]=-1
        for p in primes:
            if i*p>n: break
            isprime[i*p]=False
            if i%p==0:
                mu[i*p]=0
                break
            mu[i*p]=-mu[i]
    return mu

def direct_count(pair, n):
    c=0
    for x in range(1,n+1):
        for y in range(1,n+1):
            a,b=pair(x,y)
            if gcd(abs(a),abs(b))==1:
                c+=1
    return c

def mobius_local_count(pair, bad_primes, n):
    mu=mu_sieve(n)
    total=0
    for d in range(1,n+1):
        if mu[d]==0 or any(d%p==0 for p in bad_primes):
            continue
        y=n//d
        b=sum(1 for u in range(1,y+1) for v in range(1,y+1)
              if local_good(pair,bad_primes,u,v))
        total += mu[d]*b
    return total

# The two examples have univariate dehomogenized resultants 9 and 4.
for p in (2,5,7,11,13):
    assert common_zero_count(pair_r9,p)==1
assert common_zero_count(pair_r9,3)==5
for p in (3,5,7,11,13):
    assert common_zero_count(pair_r4,p)==1
assert common_zero_count(pair_r4,2)==2

# Exact pointwise characterization on a finite test grid.
for pair,bad in ((pair_r9,(3,)),(pair_r4,(2,))):
    for x in range(1,151):
        for y in range(1,151):
            a,b=pair(x,y)
            lhs=(gcd(abs(a),abs(b))==1)
            rhs=(gcd(x,y)==1 and local_good(pair,bad,x,y))
            assert lhs==rhs

# Exact Möbius-local formula versus direct value-gcd counting.
cases=[]
for name,pair,bad in (("R9",pair_r9,(3,)),("R4",pair_r4,(2,))):
    for n in (20,50,120):
        direct=direct_count(pair,n)
        reconstructed=mobius_local_count(pair,bad,n)
        assert direct==reconstructed
        cases.append((name,n,direct))

# Finite Euler correction factors relative to 1/zeta(2).
assert Fraction(1,1)-Fraction(5,9) == Fraction(4,9)
assert Fraction(4,9) / (Fraction(1,1)-Fraction(1,9)) == Fraction(1,2)
assert Fraction(1,1)-Fraction(2,4) == Fraction(1,2)
assert Fraction(1,2) / (Fraction(1,1)-Fraction(1,4)) == Fraction(2,3)

print("VERIFY_OK local_resultant_counts exact; pointwise_grid=150x150 exact; mobius_cases="+str(len(cases))+" exact; finite_corrections=1/2,2/3 exact")
