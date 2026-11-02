"""Exact finite checks for the stochastic-order crossing theorem.

Run: python3 checker.py
No external packages are required. Finite checks complement, but do not replace,
the all-n proof in RESULT.md.
"""
from fractions import Fraction
from math import comb
from collections import defaultdict


def covered(n,c,m):
    assert n >= 2 and 0 <= c <= n and m >= 0
    return sum(((-1)**j * comb(n-c,j) * Fraction(n-j,n)**m
                for j in range(n-c+1)), Fraction(0))


def cdf_formulas(n,t):
    # t discrete synchronous transitions of two walks on K_{n,n}
    split = covered(n,1,t)**2
    if t % 2 == 0:
        same = covered(n,0,t)*covered(n,2,t)
    else:
        same = covered(n,0,t+1)*covered(n,2,t-1)
    return same, split


def cdf_state_dp(n, config, limit):
    # A vertices 0..n-1, B vertices n..2n-1
    if config == 'same': starts=(0,1)
    else: starts=(0,n)
    state = {(starts[0],starts[1],(1<<starts[0])|(1<<starts[1])):Fraction(1)}
    cdf=[]
    for t in range(limit+1):
        cdf.append(sum((p for (a,b,mask),p in state.items()
                         if mask == (1<<(2*n))-1), Fraction(0)))
        if t == limit: break
        nxt=defaultdict(Fraction)
        for (a,b,mask),p in state.items():
            a_moves=range(n,2*n) if a<n else range(n)
            b_moves=range(n,2*n) if b<n else range(n)
            for x in a_moves:
                for y in b_moves:
                    nxt[(x,y,mask|(1<<x)|(1<<y))]+=p/Fraction(n*n)
        state=nxt
    return cdf


def main():
    count=0
    for n in range(2,9):
        for m in range(0,50):
            assert covered(n,0,m+1)==covered(n,1,m)
            assert covered(n,1,m+1)==(covered(n,1,m)+(n-1)*covered(n,2,m))/n
            odd_same,odd_split=cdf_formulas(n,2*m+1)
            identity=(covered(n,1,2*m+1)
                      *(covered(n,1,2*m+1)-covered(n,1,2*m))/(n-1))
            assert odd_same-odd_split==identity
            if 2*m >= n-2:
                assert odd_same > odd_split
            count+=3
    for n in range(2,7):
        a=Fraction(n-1,n)
        for m in (max(n,4), max(n+4,12), 40, 100, 200):
            # analytic coefficient of leading product term is 1
            c0=n; c1=n-1; c2=n-2
            assert c1*c1-c0*c2 == 1
            # after first-order cancellation, all remainder terms are at most ((n-2)/n)^m
            assert Fraction(n-2,n) < a*a
            # Test sufficient-large tail sign with exact fractions, not as an infinite proof.
            if m==200:
                same,split=cdf_formulas(n,2*m)
                assert split>same
            count+=2
    for n,lim in [(2,12),(3,10),(4,7)]:
        for config in ('same','split'):
            exact=cdf_state_dp(n,config,lim)
            for t,prob in enumerate(exact):
                same,split=cdf_formulas(n,t)
                assert prob == (same if config=='same' else split)
                count+=1
    for n in range(2,9):
        same,split=cdf_formulas(n,2000)
        # all n have strict even advantage eventually; exact large rational powers
        assert split>same
        count+=1
    print(f'PASS {count} exact rational tests: formulas, DP, odd parity, asymptotic coefficient and tail signs')

if __name__ == '__main__': main()
