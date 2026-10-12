#!/usr/bin/env python3
"""Exact two-method finite verification of first branching at exponent nine."""
from math import isqrt

def prime_sieve(N):
    s=bytearray(b'\x01')*(N+1)
    s[:2]=b'\x00\x00'
    for p in range(2,isqrt(N)+1):
        if s[p]:
            s[p*p:N+1:p]=b'\x00'*((N-p*p)//p+1)
    return s

prime=prime_sieve(1023)
observed={1:[3],2:[7],3:[],4:[31],5:[11],6:[127],7:[],8:[],9:[23,179]}

# First method: exhaustive binary-pair masks and exact reversal quotient.
for a in range(1,10):
    M=1<<(a+1)
    byprime={}
    for mask in range(1,M):
        x=sum((1<<i) for i in range(a+1) if (mask>>i)&1)
        y=sum((1<<(a-i)) for i in range(a+1) if (mask>>i)&1)
        denominator=M-y
        if x%denominator:continue
        p=x//denominator
        if p>=3 and p<M and prime[p]:
            byprime.setdefault(p,[]).append(mask)
    assert sorted(byprime)==observed[a],(a,sorted(byprime))
    # Second method: directly compute reciprocal-pair divisor subset sums
    # for every possible odd prime, with no use of reversal or quotient criterion.
    direct=[]
    for p in range(3,M):
        if not prime[p]:continue
        target=2*((1<<a)*p)
        reach=1
        for i in range(a+1):
            pair_sum=(1<<i)+(1<<(a-i))*p
            reach|=reach<<pair_sum
        if (reach>>target)&1:
            direct.append(p)
    assert direct==observed[a],(a,direct)

for p,mask,missing in [(179,895,{7}),(23,943,{4,6})]:
    a=9;M=1024
    bits={i for i in range(a+1) if mask&(1<<i)}
    assert bits==set(range(10))-missing
    S=[]
    for i in bits:S.extend([1<<i, (1<<(a-i))*p])
    n=(1<<a)*p
    assert len(S)==2*len(bits)
    assert len(set(S))==len(S)
    assert sum(S)==2*n
    assert set(n//d for d in S)==set(S)
    assert sum(S)==2*n

assert all(len(observed[a])<2 for a in range(1,9))
assert observed[9]==[23,179]
print('VERIFY_OK first_exponent_two_prime_completions=9 prime_values=23,179 rows_a1_to9=3;7;none;31;11;127;none;none;23,179 mask_enumeration=yes direct_divisor_subset_dp=yes exact_reciprocal_witnesses=yes')
