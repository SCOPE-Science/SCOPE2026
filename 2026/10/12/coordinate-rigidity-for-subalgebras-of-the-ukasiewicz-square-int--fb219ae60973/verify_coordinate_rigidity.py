#!/usr/bin/env python3
"""Exact finite verification of coordinate rigidity for the square-negation-join reduct.
Standalone; Python 3 standard library only; exhaustive over stated finite ranges.
"""
from itertools import combinations_with_replacement
from fractions import Fraction
from math import comb

def star(x):
    return max(0, 2*x-1)

def neg(x):
    return 1-x

def lo(x):
    return neg(star(neg(x)))

def clamp(x):
    return max(0,min(1,x))

def ramp(k,j,x):
    assert k>=0 and (k==0 and j==0 or k>0 and 0<=j<2**k)
    if k==0: return x
    z=ramp(k-1,j//2,x)
    return star(z) if j%2 else lo(z)

checks=0
for k in range(9):
    for j in range(2**k):
        for i in range(257):
            x=Fraction(i,256)
            assert ramp(k,j,x)==clamp(2**k*x-j)
            checks+=1
for i in range(257):
    x=Fraction(i,256)
    assert star(neg(max(x,neg(x))))==0
    checks+=1

def chain(n):
    return tuple(Fraction(i,n) for i in range(n+1))

def subalgebras(n):
    C=chain(n)
    ans=[]
    for bits in range(1<<(n-1)):
        s={C[0],C[-1]}
        s.update(C[i] for i in range(1,n) if bits>>(i-1)&1)
        if all(neg(x) in s and star(x) in s for x in s):
            ans.append(tuple(sorted(s)))
    return ans

def maps(A,B):
    assert A[0]==0 and A[-1]==1 and B[0]==0 and B[-1]==1
    for inner in combinations_with_replacement(B,len(A)-2):
        h=dict(zip(A,(B[0],)+inner+(B[-1],)))
        yield h

def is_hom(A,h):
    return (all(h[neg(x)]==neg(h[x]) and h[star(x)]==star(h[x]) for x in A)
            and all(h[max(x,y)]==max(h[x],h[y]) for x in A for y in A))

# Exhaustive monotone candidate maps of every full chain with denominator up to 9.
full_candidates=0
full_homs=0
for n in range(1,10):
    A=chain(n)
    for m in range(1,10):
        B=chain(m)
        actual=[]
        for h in maps(A,B):
            full_candidates+=1
            if is_hom(A,h):actual.append(h)
        expected=1 if m%n==0 else 0
        assert len(actual)==expected,(n,m,len(actual),expected)
        for h in actual:
            assert all(h[x]==x for x in A)
        checks+=1
        full_homs+=len(actual)

# Exhaustive homomorphism census for every pair of subalgebras of small chains.
sub_candidates=0
sub_homs=0
sub_pairs=0
for n in range(1,8):
    As=subalgebras(n)
    for m in range(1,8):
        Bs=subalgebras(m)
        for A in As:
            for B in Bs:
                sub_pairs+=1
                actual=[]
                for h in maps(A,B):
                    sub_candidates+=1
                    if is_hom(A,h): actual.append(h)
                assert len(actual)==int(set(A)<=set(B)),(n,m,A,B,len(actual))
                for h in actual:
                    assert all(h[x]==x for x in A)
                sub_homs+=len(actual)
                checks+=1

# Examples showing the two operations play distinct roles.
A=chain(4)
h=dict(zip(A,(Fraction(0),Fraction(0),Fraction(1,2),Fraction(1),Fraction(1))))
assert all(h[neg(x)]==neg(h[x]) for x in A)
assert all(h[max(x,y)]==max(h[x],h[y]) for x in A for y in A)
assert any(h[star(x)]!=star(h[x]) for x in A)
B=chain(1)
h2={Fraction(0):Fraction(1),Fraction(1):Fraction(0)}
assert all(h2[neg(x)]==neg(h2[x]) and h2[star(x)]==star(h2[x]) for x in B)
assert h2[max(B)]!=max(h2.values())
checks+=5
print(f'VERIFY_OK {checks} exact structural assertions; {sum(2**k for k in range(9))*257} exact ramp evaluations; {full_candidates} full-chain monotone candidate maps screened; {full_homs} actual full-chain homomorphisms; {sub_pairs} subalgebra pairs; {sub_candidates} subalgebra monotone maps screened; {sub_homs} actual subalgebra homomorphisms')
