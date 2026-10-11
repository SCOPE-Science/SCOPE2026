#!/usr/bin/env python3
"""Supplementary finite checks of the dyadic lower-oscillation Bellman envelope.

The analytic proof, not this bounded enumeration, establishes the universal theorem.
"""
import itertools
import math
from fractions import Fraction


def nodes(values):
    n = len(values)
    width = n
    while width >= 1:
        for j in range(0, n, width):
            sub = values[j:j+width]
            minimum = min(sub)
            average = sum(sub)/len(sub)
            yield minimum, average, sub
        width //= 2


def one_step(lam, d, a1):
    q = math.exp(lam)
    c = (q-1)/(2-q)
    return c*d - (q**d-1)*(1+c*a1)


def verify():
    comparisons=0
    for lam in [0.07,0.2,0.5,0.69]:
        q = math.exp(lam)
        c = (q-1)/(2-q)
        for j in range(501):
            d=2*j/500
            for k in range(51):
                a1=min(1, 2-d)*k/50
                assert one_step(lam,d,a1)>-2e-12
                comparisons += 1
        for leaves in itertools.product((0,1,2), repeat=8):
            profile=list(nodes(leaves))
            if all(av-mi<=1+1e-12 for mi,av,_ in profile):
                for mi,av,vals in profile:
                    lhs=sum(math.exp(lam*(v-mi)) for v in vals)/len(vals)
                    assert lhs<=1+c*(av-mi)+1e-11
                    comparisons+=1
    # Exact rational staircase arithmetic, q=3/2 <2.
    q=Fraction(3,2)
    for N in (1,2,4,8,16,32,64):
        truncated=sum((q**k)/2**(k+1) for k in range(N))+(q**(N+1))/2**N
        limit=1/(2-q)
        assert truncated<=limit
        assert limit-truncated==(q/2)**N*(limit-q)  # exact remainder
        comparisons+=1
    # q=2 is critical: leftmost-child geometric staircase moments grow linearly.
    q=Fraction(2,1)
    assert all(sum((q**k)/2**(k+1) for k in range(N))+(q**(N+1))/2**N==Fraction(N,2)+2 for N in range(1,33))
    comparisons+=32
    print("PASSED",comparisons,"supplementary checks; universal proof is analytic")

if __name__=='__main__':
    verify()
