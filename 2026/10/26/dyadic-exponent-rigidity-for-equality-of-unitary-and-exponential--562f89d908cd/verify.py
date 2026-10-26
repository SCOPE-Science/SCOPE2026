"""Independent finite consistency checks for the dyadic-exponent divisor-sum theorem.

The general proof is the symbolic argument in RESULT.md; enumeration alone
cannot establish the theorem for all integers.
"""
from math import isqrt


def primes_to(n):
    return [p for p in range(2, n+1) if p>1 and all(p%d for d in range(2, isqrt(p)+1))]


def divisor_power_sum(p, e):
    return sum(p**d for d in range(1, e+1) if e%d == 0)


primes=primes_to(100)
checked=0
for p in primes:
    for k in range(1, 8):
        a=2**k
        a_sum=divisor_power_sum(p,a)
        R=a_sum-p**a-1
        # General singleton-cofactor reduction.
        for q in primes:
            if p == q:
                continue
            unitary=(p**a+1)*(q+1)
            exponential=a_sum*q
            assert (unitary == exponential) == (p**a+1 == q*R)
            assert (unitary == exponential) == (k==1 and p in (2,3) and q==5)
            checked+=1

bases=0
for p in range(2,201):
    for k in range(2,11):
        R=sum(p**(2**j) for j in range(k))-1
        residue=(pow(p,2**k,R)+1)%R
        assert residue != 0, (p,k)
        if k==2:
            residue_witness=(p-1)**2+1
            assert 0 < residue_witness < R
        else:
            u=p**(2**(k-2))
            v=sum(p**(2**j) for j in range(k-2))
            witness=(u+v-1)**2+1
            assert R < witness < 2*R
            assert u >= 3*(v-2)
            assert witness%R == residue
        bases+=1

print(f'VERIFY_OK: {checked} prime-pair equalities and {bases} integer-base dyadic layers')
