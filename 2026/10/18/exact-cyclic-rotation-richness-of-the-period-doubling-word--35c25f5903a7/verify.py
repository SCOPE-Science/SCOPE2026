#!/usr/bin/env python3
"""Finite cross-checks for conjugacy multiplicities in the period-doubling word.

Uses a complete 2-block substitution cover, not an assumed prefix-length bound.
"""
from collections import Counter, defaultdict


def sigma(s):
    return ''.join('01' if a == '0' else '00' for a in s)


def exact_factors(n):
    length = 1
    while length < n:
        length *= 2
    level = length.bit_length() - 1
    words = ('00', '01', '10')
    for _ in range(level):
        words = tuple(map(sigma, words))
    return {w[i:i+n] for w in words for i in range(len(w)-n+1)}


def canon(s):
    """Lexicographically smallest cyclic rotation, Booth algorithm."""
    z=s+s
    n=len(s)
    i,j,k=0,1,0
    while i < n and j < n and k < n:
        if z[i+k] == z[j+k]:
            k+=1
        elif z[i+k] > z[j+k]:
            i=i+k+1
            if i <= j:i=j+1
            k=0
        else:
            j=j+k+1
            if j <= i:j=i+1
            k=0
    t=min(i,j)
    return z[t:t+n]


def profile(n):
    groups=defaultdict(set)
    for word in exact_factors(n):
        groups[canon(word)].add(word)
    return Counter(len(members) for members in groups.values())


def predicted_max(n):
    twopower = n & -n
    odd = n//twopower
    return n if odd == 1 else 3*twopower


def main():
    # All factor sets are exhaustive because every n-window meets at most
    # two adjacent 2^r-blocks, and 00,01,10 are exactly the 2-factors.
    for n in range(1,193):
        actual=profile(n)
        assert max(actual) == predicted_max(n), (n,actual)
        if n>=2 and n%2==0:
            parent=profile(n//2)
            if n//2 >= 2:
                assert actual==Counter({2*s:m for s,m in parent.items()}),(n,actual,parent)
        if n in [1,2,3,4,5,7,8,9,15,16,17,31,32,33,63,64,65,127,128,129,191,192]:
            print(n, dict(sorted(actual.items())), 'max',max(actual))
    # Check that every odd n has a factor of form 00u00 with three
    # pairwise distinct circular shifts 00u,0u0,u00.
    for n in range(3,193,2):
        f=exact_factors(n+2)
        found=False
        for x in f:
            if x[:2]=='00' and x[-2:]=='00':
                u=x[2:-2]
                if len({'00'+u, '0'+u+'0', u+'00'})==3:
                    found=True
                    break
        assert found,n
    print('VERIFY_OK 1..192 complete substitution-cover factor sets and all odd triple witnesses')

if __name__ == '__main__':
    main()
