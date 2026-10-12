#!/usr/bin/env python3
from math import isqrt
LIMIT = 100_000
MAX_EXP = 24
is_prime = bytearray(b'\x01') * LIMIT
is_prime[0:2] = b'\x00\x00'
for q in range(2,isqrt(LIMIT-1)+1):
    if is_prime[q]:
        for t in range(q*q,LIMIT,q):
            is_prime[t]=0
primes = [p for p in range(3,LIMIT,2) if is_prime[p]]
assert primes[0]==3
checked=0
hits=[]
for a in range(1,MAX_EXP+1):
    pow2=1<<a
    for p in primes:
        n=pow2*p
        phi=(pow2//2)*(p-1)
        sigma=(2*pow2-1)*(p+1)
        direct=((sigma-n)%phi==0)
        expected=((a,p) in ((1,3),(2,3)) or p==3*pow2-1)
        assert direct==expected,(a,p,n,direct,expected)
        if direct:
            quotient=(sigma-n)//phi
            predicted=3 if (a,p)==(1,3) else 4 if (a,p)==(2,3) else 2
            assert quotient==predicted,(a,p,quotient,predicted)
            hits.append((a,p,quotient))
        checked+=1
for a in range(2,41):
    x=1<<(a-1)
    M=3*x-1
    candidates=[t for t in (1,x+1,2*x+1) if M%t==0]
    assert candidates==([1,5] if a==2 else [1]),(a,candidates)
assert (1,3,3) in hits and (2,3,4) in hits
print('VERIFY_OK',f'prime_limit={LIMIT}',f'max_exp={MAX_EXP}',f'prime_pairs={checked}',f'hits={hits}',f'parameter_layers=39')
