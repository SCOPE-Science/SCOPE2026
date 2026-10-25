#!/usr/bin/env python3
"""Exact, finite checks for hyper-base expansion parity counts.

The infinite spectral theorem is proved in the accompanying mathematical argument,
not inferred from these computations.
"""


def parity_polynomial_bits(base, level):
    """GF(2) coefficients of prod_{0<=j<level}(sum_{r=0}^base x^(r*base^j)), below x^(base^level)."""
    size = base**level
    mask = (1 << size) - 1
    polynomial = 1
    power = 1
    for _ in range(level):
        previous = polynomial
        polynomial = 0
        for digit in range(base+1):
            polynomial ^= previous << (digit*power)
        polynomial &= mask
        power *= base
    return polynomial


def matrix_states(base, level):
    x,y,z = 1,0,0
    for _ in range(level):
        x,y,z = x+y,(base-1)*x+(base-2)*y+z,y+z
    return x,y,z


def recurrence_value(base, level):
    if level==0:return 1
    if level==1:return base
    prevprev,prev=1,base
    for _ in range(2,level+1):
        prevprev,prev=prev,(base-1)*prev+2*prevprev-1
    return prev


def stern_values(base, last_index):
    s = [0]*(last_index+1)
    s[1] = 1
    for index in range(2,last_index+1):
        q,r=divmod(index,base)
        s[index]=s[q] if r==0 else s[q]+s[q+1] if r==1 else s[q+1]
    return s


def main():
    checked_blocks=0
    checked_coefficients=0
    for base in range(2,11):
        for level in range(7):
            n=base**level
            if n>1_000_000:continue
            coefficients=parity_polynomial_bits(base,level)
            count=coefficients.bit_count()
            x,y,z=matrix_states(base,level)
            assert count==x+y==recurrence_value(base,level), (base,level,count,x+y)
            assert x-z==1 and 0<=x+y+z<=n
            checked_blocks+=1
        # Fully independent integer Stern recurrence check of every coefficient
        # against polynomial multiplication, not merely aggregate counts.
        level=5 if base<=6 else 4
        n=base**level
        bits=parity_polynomial_bits(base,level)
        s=stern_values(base,n)
        for index in range(n):
            assert ((bits>>index)&1)==(s[index+1]&1),(base,index)
        checked_coefficients+=n
        for level in range(7,101):
            x,y,z=matrix_states(base,level)
            assert x+y==recurrence_value(base,level) and x-z==1
    # For binary Stern numbers, parity is 0 precisely at multiples of 3.
    s=stern_values(2,50000)
    for n in range(50001):
        assert (s[n]&1)==int(n%3!=0)
    print('CERTIFICATE_OK bases=2..10 independent_GF2_blocks',checked_blocks,
          'coefficient_comparisons',checked_coefficients,
          'matrix_recurrence_levels=0..100',
          'binary_mod3_indices=0..50000')

if __name__=='__main__':
    main()
