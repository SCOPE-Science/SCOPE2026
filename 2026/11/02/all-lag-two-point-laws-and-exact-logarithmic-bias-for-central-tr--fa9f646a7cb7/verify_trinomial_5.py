#!/usr/bin/env python3
"""Finite reproducibility checks for the mod-five central-trinomial two-point theorem."""
from collections import Counter, defaultdict
from fractions import Fraction

W = (1, 1, 3, 2, 4)
G = range(1, 5)

def central_trinomial(n):
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for j in range(2, n + 1):
        z, rem = divmod((2*j-1)*b + 3*(j-1)*a, j)
        assert rem == 0
        a, b = b, z
    return b

def residue_digits(n):
    r = 1
    while n:
        r = r*W[n % 5] % 5
        n //= 5
    return r

# Independent integer recurrence versus base-five digit multiplication.
a, b = 1, 1
for n in range(4097):
    if n == 0:
        t = 1
    elif n == 1:
        t = 1
    else:
        numerator = (2*n-1)*b + 3*(n-1)*a
        assert numerator % n == 0
        t = numerator // n
        a, b = b, t
    assert t % 5 == residue_digits(n), (n,t % 5,residue_digits(n))

# Exact finite-level pair census, using a distinct digit-block recurrence.
pairs = Counter({(1, 1): 1})
marginal = Counter({1: 1})
S0 = {(1,1),(1,3),(3,2),(2,4)}
S1 = {(4,1),(4,3),(2,2),(3,4)}
for k in range(1,13):
    nxt = Counter()
    for u, ct in marginal.items():
        for a in range(4):
            nxt[(u*W[a]%5,u*W[a+1]%5)] += ct
    for (u,v),ct in pairs.items():
        nxt[(4*u%5,v)] += ct
    marginal_new = Counter()
    for u,ct in marginal.items():
        for w in W:
            marginal_new[u*w%5] += ct
    pairs,marginal = nxt,marginal_new
    assert sum(pairs.values()) == 5**k
    for u in G:
        assert marginal[u] == (5**k-1)//4 + (u==1)
        for v in G:
            numerator = (5**k-1)-4*k + 16*( ((k+1)//2)*((u,v) in S0) + (k//2)*((u,v) in S1) + ((u,v)==(pow(4,k,5),1)) )
            assert numerator % 16 == 0
            assert pairs[(u,v)] == numerator // 16, (k,u,v,pairs[(u,v)],numerator//16)

# Finite rational recurrence for the all-lag limiting ratio laws.
mu = {0:{1:Fraction(1)}, 1:{r:Fraction(1,4) for r in G}}
for h in range(2,73):
    q,b = divmod(h,5)
    d = defaultdict(Fraction)
    for a in range(5):
        j = q+(a+b)//5
        scale = W[(a+b)%5]*pow(W[a],-1,5)%5
        assert j < h
        for r,prob in mu[j].items():
            d[scale*r%5] += prob/5
    assert sum(d.values()) == 1
    mu[h] = dict(d)
assert mu[2] == {1:Fraction(1,10),2:Fraction(3,10),3:Fraction(1,2),4:Fraction(1,10)}

# Count ratio residues directly on a full base-five block and compare the
# abstract Haar limiting probabilities up to the proved carry-boundary error.
N=5**6
for h in range(0,39):
    c=Counter()
    for n in range(N):
        u,v=residue_digits(n),residue_digits(n+h)
        c[v*pow(u,-1,5)%5] += 1
    for r in G:
        assert abs(Fraction(c[r]) - N*mu[h].get(r,Fraction(0))) <= 2*h+1,(h,r,c[r],mu[h].get(r))

# Test the four-symbol pair counts without using the block recurrence above.
for k in range(1,7):
    c=Counter((residue_digits(n),residue_digits(n+1)) for n in range(5**k))
    for u in G:
        for v in G:
            q=(5**k-1)-4*k+16*( ((k+1)//2)*((u,v) in S0) + (k//2)*((u,v) in S1) + ((u,v)==(pow(4,k,5),1)))
            assert c[(u,v)] == q//16
print('VERIFY_OK integer_terms=4097 exact_pair_levels=12 ratio_lags=39 ratio_block=15625 direct_pair_levels=6')
