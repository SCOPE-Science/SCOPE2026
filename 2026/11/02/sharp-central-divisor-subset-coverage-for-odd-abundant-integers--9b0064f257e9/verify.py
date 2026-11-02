#!/usr/bin/env python3
"""Exact finite certificates for a central divisor-subset interval theorem.

All operations use Python integers. No external modules or network access are needed.
"""
from fractions import Fraction

BASES = (
    (3, 1, 1, 7), (2, 2, 1, 7), (2, 1, 2, 7),
    (3, 2, 1, 11),
    (5, 2, 1, 13), (4, 3, 1, 13),
    (4, 2, 2, 13), (3, 3, 2, 13),
)

def sigma_prime_power(p, e):
    return (p ** (e+1) - 1) // (p-1)

def idx(p, e):
    return Fraction(sigma_prime_power(p, e), p**e)

def divisors(a,b,c,q):
    return sorted(3**i * 5**j * q**k
                  for i in range(a+1)
                  for j in range(b+1)
                  for k in range(c+1))

def reachable_bits(ds):
    bits = 1  # initially only the empty subset has sum 0
    for d in ds:
        bits |= bits << d   # include or omit each distinct divisor once
    return bits

def verify_interval(a,b,c,q):
    ds=divisors(a,b,c,q)
    n=3**a*5**b*q**c
    sig=sum(ds)
    assert sig == sigma_prime_power(3,a)*sigma_prime_power(5,b)*sigma_prime_power(q,c)
    assert n == ds[-1] and sig>2*n
    bits=reachable_bits(ds)
    # The contiguous run of bits at positions 23,...,sigma-23 is all ones.
    length=sig-45
    assert length>0
    assert ((bits>>23)&((1<<length)-1))==(1<<length)-1
    assert (bits >> sig)==1
    return n,sig,sig-2*n,len(ds),bits

def verify_primitive_thresholds():
    # All inequalities are exact, and encode an exhaustive monotone partition
    # of the possible exponent triples in the written mathematical proof.
    assert Fraction(5,4)*Fraction(7,6)*Fraction(11,10)<2
    assert Fraction(3,2)*Fraction(7,6)*Fraction(11,10)<2
    assert Fraction(3,2)*Fraction(5,4)*Fraction(17,16)<2
    assert idx(3,1)*Fraction(5,4)*Fraction(7,6)<2
    assert idx(3,2)*idx(5,1)*idx(7,1)<2
    assert idx(3,2)*idx(5,2)*idx(7,1)>2
    assert idx(3,2)*idx(5,1)*idx(7,2)>2
    assert idx(3,3)*idx(5,1)*idx(7,1)>2
    assert idx(3,2)*Fraction(5,4)*Fraction(11,10)<2
    assert Fraction(3,2)*idx(5,1)*Fraction(11,10)<2
    assert idx(3,3)*idx(5,2)*idx(11,1)>2
    assert idx(3,2)*Fraction(5,4)*Fraction(13,12)<2
    assert Fraction(3,2)*idx(5,1)*Fraction(13,12)<2
    assert idx(3,3)*Fraction(5,4)*idx(13,1)<2
    assert idx(3,3)*idx(5,2)*Fraction(13,12)<2
    assert idx(3,4)*idx(5,2)*idx(13,1)<2
    assert idx(3,3)*idx(5,3)*idx(13,2)>2
    assert idx(3,4)*idx(5,3)*idx(13,1)>2
    assert idx(3,4)*idx(5,2)*idx(13,2)>2
    assert idx(3,5)*idx(5,2)*idx(13,1)>2
    for r in (7,11,13):
        for a in range(1,12):
            for b in range(1,9):
                for c in range(1,8):
                    abundant=(idx(3,a)*idx(5,b)*idx(r,c)>2)
                    covered=any((rr==r and a>=x and b>=y and c>=z)
                                for x,y,z,rr in BASES)
                    assert abundant == covered,(a,b,c,r)

def verify_sharp_22():
    ds=divisors(3,2,1,11)
    small=[d for d in ds if d<=22]
    assert small==[1,3,5,9,11,15],small
    bits=reachable_bits(small)
    assert not ((bits>>22)&1)

def verify_two_paths():
    # Separate Boolean subset-sum construction checks the bitset certificate
    # at two bases, including the sharp endpoint and the smallest q=13 base.
    for a,b,c,q in ((3,2,1,11),(5,2,1,13)):
        ds=divisors(a,b,c,q); cap=sum(ds)
        reachable=bytearray(cap+1);reachable[0]=1
        bound=0
        for d in ds:
            for t in range(bound,-1,-1):
                if reachable[t]: reachable[t+d]=1
            bound+=d
        assert all(reachable[t] for t in range(23,cap-22))
        assert (reachable[22]==0)==(q==11)

def verify_extensions():
    for a,b,c,q in ((4,2,1,7),(3,3,1,11),(6,2,1,13),
                    (4,3,2,13),(4,3,1,7)):
        n,sig,ab,count,bits=verify_interval(a,b,c,q)
        assert ab>=26

def main():
    verify_primitive_thresholds()
    records=[verify_interval(*z) for z in BASES]
    assert min(v[2] for v in records)==26
    verify_sharp_22()
    verify_two_paths()
    verify_extensions()
    print('VERIFY_OK primitive_bases=8 maximum_base=570375'
          ' sharp_first_missing=22 sharp_base=7425'
          ' uniform_interval_start=23 base_divisor_counts='
          +','.join(str(z[3]) for z in records)
          +' minimum_abundance=26 independent_boolean_bases=2 extensions=5')

if __name__ == '__main__':
    main()
