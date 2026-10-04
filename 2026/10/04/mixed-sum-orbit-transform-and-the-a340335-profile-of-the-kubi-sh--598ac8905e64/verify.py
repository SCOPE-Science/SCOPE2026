#!/usr/bin/env python3
from itertools import combinations, permutations
from math import comb, factorial
from fractions import Fraction

N=12

def a_formula(n):
    return sum(comb(n,p)*factorial(n-p)*(1 << (p*(n-p))) for p in range(n+1))

A=[a_formula(n) for n in range(N+1)]
A340335=[1,2,7,43,441,7241,185233,7252337,429318529,38079107713,5026601726721,982190576713985,282875400939199489]
assert A==A340335

# Direct finite-age replay for the Kubiś–Shelah finite-set/linear-order mixed sum.
# An object on the fixed labelled carrier [n] is: a left subset L, a linear order
# (permutation) of R=[n]\\L, and an arbitrary L x R edge set.
def direct_count(n):
    V=tuple(range(n))
    total=0
    for p in range(n+1):
        for Ltuple in combinations(V,p):
            L=set(Ltuple)
            R=tuple(v for v in V if v not in L)
            for order in permutations(R):
                # Iterate every cross-edge mask, not just its cardinality.
                pairs=tuple((x,y) for x in Ltuple for y in order)
                for mask in range(1 << len(pairs)):
                    # Touch each bit so this is an actual object-level replay.
                    edges=tuple(pairs[j] for j in range(len(pairs)) if (mask>>j)&1)
                    assert len(edges) <= len(pairs)
                    total += 1
    return total

for n in range(0,7):
    d=direct_count(n)
    assert d==A[n], (n,d,A[n])

# All ordered tuples arise by an equality-kernel partition followed by an injective tuple.
S2=[[0]*(N+1) for _ in range(N+1)]
S2[0][0]=1
for n in range(1,N+1):
    for k in range(1,n+1):
        S2[n][k]=S2[n-1][k-1]+k*S2[n-1][k]
B=[1]+[sum(S2[n][k]*A[k] for k in range(1,n+1)) for n in range(1,N+1)]
B_expected=[1,2,9,66,750,12833,326602,12323706,690051563,57429171592,7109345894406,1308234499500151,357191625841297820]
assert B==B_expected

# EGF identity A(x)=sum_{p>=0} (x^p/p!)/(1-2^p x).
# Compare coefficients through x^N exactly over Q.
for n in range(N+1):
    coeff=sum(Fraction((1 << (p*(n-p))), factorial(p)) for p in range(n+1))
    assert coeff*factorial(n)==A[n]

# General mixed-sum transform sanity checks on synthetic labelled profiles.
def mixed(f,g,n):
    return sum(comb(n,p)*f[p]*g[n-p]*(1 << (p*(n-p))) for p in range(n+1))
# pure-set / pure-set and linear-order / linear-order examples
ones=[1]*(N+1)
facts=[factorial(n) for n in range(N+1)]
for n in range(N+1):
    assert mixed(ones,ones,n)==sum(comb(n,p)*(1 << (p*(n-p))) for p in range(n+1))
    assert mixed(ones,facts,n)==A[n]
    assert mixed(facts,facts,n)==factorial(n)*sum((1 << (p*(n-p))) for p in range(n+1))

print('injective', A[:11])
print('all_tuples', B[:11])
print('direct_replay_through_n', 6)
print('VERIFY_OK')
