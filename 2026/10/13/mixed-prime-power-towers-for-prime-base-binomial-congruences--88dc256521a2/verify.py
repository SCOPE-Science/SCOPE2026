#!/usr/bin/env python3
"""Independent finite corroboration for mixed-prime-power binomial congruences.
No finite test is interpreted as proving a universal statement.
"""
import math

def isprime(n):
    return n >= 2 and all(n%d for d in range(2,math.isqrt(n)+1))

def digitsum(n,q):
    s = 0
    while n:
        n,d = divmod(n,q)
        s += d
    return s

def binom_limit_mod(q,t,p,r):
    # Each positive dilation j contributes modulo p^(3*j),
    # so B_j is within p^r of the infinite p-adic limit
    # once 3*(j+1) >= r.
    j=max(0,(r+2)//3-1)
    return math.comb(q**(t+1)*p**j,q**t*p**j) % p**r

def teich_mod(q,p,t,r):
    return pow(q,(q**t)*p**r,p**r)

cases=0
filtered=0
for q in [2,3,5,7,11,13]:
    for t in [1,2,3]:
        for p in [5,7,11,13,17,19,23]:
            if q==p: continue
            for r in [1,2]:
                n=q**t*p**r
                if n>370: continue
                lhs=math.comb(q*n,n)
                actual=(lhs-pow(q,n,n))%n==0
                padic=binom_limit_mod(q,t,p,r)==teich_mod(q,p,t,r)
                dig=digitsum((q-1)*p**r,q)>=(q-1)*t
                predicted=padic and dig
                assert actual==predicted,(q,t,p,r,actual,padic,dig)
                if padic and not dig: filtered+=1
                cases+=1

explicit=[(31,1,5,1,True),(31,1,5,2,True),(31,1,5,3,True),
          (31,1,5,4,False),(23,1,7,1,True),(23,1,7,2,True),
          (23,1,7,3,False),(19,2,7,1,False),(19,2,7,2,False)]
for q,t,p,r,expected in explicit:
    n=q**t*p**r
    padic=binom_limit_mod(q,t,p,r)==teich_mod(q,p,t,r)
    digital=digitsum((q-1)*p**r,q)>=(q-1)*t
    predicted=padic and digital
    assert predicted==expected,(q,t,p,r,padic,digital)
    if n<=20000:
        actual=(math.comb(q*n,n)-pow(q,n,n))%n==0
        assert actual==expected,(q,t,p,r,actual)

# Witness that the prime-base q is not Wieferich for p=5 or p=7,
# despite valid second/cubic mixed towers.
assert pow(31,4,25)==21
assert pow(23,6,49)==29
assert math.comb(31**2,31)%625 == 251
assert math.comb(31**2*5,31*5)%625 == 251
assert teich_mod(31,5,1,4)==1
assert math.comb(19**3,19**2)%49==teich_mod(19,7,2,2)
assert digitsum(18*7,19)==18 and digitsum(18*49,19)==18
assert math.comb(19**3,19**2)%343 == 215
assert teich_mod(19,7,2,3) == 19
assert binom_limit_mod(19,2,7,3) != teich_mod(19,7,2,3)
print(f'VERIFY_OK grid_direct_cases={cases} digit_filtered={filtered} boundary_cases={len(explicit)} non_wieferich_cubic=PASS')
