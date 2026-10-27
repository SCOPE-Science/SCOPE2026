"""Exact finite checker for conditional rank-sum variance by binary run count.
Run with: python3 verify.py
Requires only Python's standard library.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def v_even(a, b, k):
    return Fraction(
        a*b*(2*a*b*k + 4*a*b - (a+b)*k*k - (a+b)*k
             + 2*(a+b) + k*k-k), 12*k*(k+1))


def oriented_odd(a, b, k):
    return Fraction(a*b*(2*a*b-(a+b)*k+a-3*b+k-1), 12*(k+1))


def v_odd(a, b, k):
    assert a+b > 2*k
    return (Fraction(a-k, a+b-2*k)*oriented_odd(a, b, k)
            + Fraction(b-k, a+b-2*k)*oriented_odd(b, a, k))


def variance_formula(a, b, r):
    return v_even(a,b,r//2) if r%2 == 0 else v_odd(a,b,(r-1)//2)


def exhaustive(a, b):
    out=defaultdict(list)
    n=a+b
    for subset in combinations(range(n),a):
        bits=[0]*n
        for i in subset: bits[i]=1
        runs=1+sum(bits[i]!=bits[i-1] for i in range(1,n))
        ones=0; inv=0
        for bit in bits:
            if bit: ones+=1
            else: inv+=ones
        out[runs].append(inv)
    return out


def main():
    checks=0
    for a in range(1,9):
        for b in range(1,9):
            observed=exhaustive(a,b)
            assert sum(len(t) for t in observed.values())==comb(a+b,a)
            checks+=1
            for r,arr in observed.items():
                z=len(arr)
                mean=Fraction(sum(arr),z)
                var=Fraction(sum(u*u for u in arr),z)-mean*mean
                assert mean==Fraction(a*b,2), (a,b,r,'mean',mean)
                assert var==variance_formula(a,b,r),(a,b,r,'variance',var,variance_formula(a,b,r))
                checks+=2
            for k in range(1,min(a,b)+1):
                if 2*k+1 in observed:
                    assert v_even(a,b,k)>v_odd(a,b,k)
                    checks+=1
                if 2*k+2 in observed:
                    assert v_even(a,b,k+1)>v_odd(a,b,k)
                    assert v_even(a,b,k)>v_even(a,b,k+1)
                    checks+=2
    print('PASS conditional means, exact variances, and strict parity comparisons; assertions:',checks)

if __name__=='__main__': main()
