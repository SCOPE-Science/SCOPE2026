#!/usr/bin/env python3
"""Reproduce closed-factor identities for four-run binary words.

No dependencies beyond Python 3.9+; computations are finite spot checks,
while the mathematical theorem is proved separately in RESULT.md.
"""
from collections import Counter
from itertools import product
from math import comb
from random import Random


def is_closed_via_occurrences(s):
    if len(s) <= 1:
        return True
    for k in range(1, len(s)):
        p = s[:k]
        if p != s[-k:]:
            continue
        starts = [j for j in range(len(s)-k+1) if s[j:j+k] == p]
        if starts == [0, len(s)-k]:
            return True
    return False


def is_closed_via_prefix_function(s):
    if len(s) <= 1:
        return True
    pi = [0]*len(s)
    for i in range(1,len(s)):
        j = pi[i-1]
        while j and s[j]!=s[i]:
            j=pi[j-1]
        if s[i]==s[j]:
            j+=1
        pi[i]=j
    k=pi[-1]
    if not k:
        return False
    return all(s[j:j+k]!=s[:k] for j in range(1,len(s)-k))


def brute_closed_factors(s, predicate=is_closed_via_occurrences):
    all_factors = {s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1)}
    return {''} | {t for t in all_factors if predicate(t)}


def explicit_closed_factors(a,b,c,d):
    # The five disjoint run-pattern classes, including epsilon.
    out={''}
    out.update('0'*i for i in range(1,max(a,c)+1))
    out.update('1'*i for i in range(1,max(b,d)+1))
    out.update('0'*i+'1'*b+'0'*i for i in range(1,min(a,c)+1))
    out.update('1'*i+'0'*c+'1'*i for i in range(1,min(b,d)+1))
    out.update('0'*i+'1'*b+'0'*c+'1'*j for i in range(1,min(a,c)+1) for j in range(1,min(b,d)+1))
    return out


def predicted(a,b,c,d):
    n=a+b+c+d
    return n+1+min(a,c)*min(b,d)


def maximum(n):
    t=n//2
    return n+1+(t//2)*(t-t//2)


def extremal_count(n):
    return (1,4,2,8)[n%4]


def verify():
    tested=0
    # Every possible positive four-run composition through length 16.
    for n in range(4,17):
        hist=Counter()
        for a in range(1,n-2):
            for b in range(1,n-a-1):
                for c in range(1,n-a-b):
                    d=n-a-b-c
                    s='0'*a+'1'*b+'0'*c+'1'*d
                    f1=brute_closed_factors(s)
                    f2=brute_closed_factors(s,is_closed_via_prefix_function)
                    ff=explicit_closed_factors(a,b,c,d)
                    assert f1==f2==ff, (a,b,c,d,len(f1),len(f2),len(ff))
                    assert len(f1)==predicted(a,b,c,d)
                    hist[len(f1)]+=1
                    tested+=1
        assert sum(hist.values())==comb(n-1,3)
        assert max(hist)==maximum(n)
        assert hist[maximum(n)]==extremal_count(n)
    # Longer, independently selected parameter tests (no exhaustive claim here).
    rng=Random(1729)
    for _ in range(128):
        a,b,c,d=(rng.randint(1,22) for _ in range(4))
        s='0'*a+'1'*b+'0'*c+'1'*d
        assert brute_closed_factors(s)==explicit_closed_factors(a,b,c,d)
        tested+=1
    # Check the bivariate generating-series identity coefficientwise via
    # min-pair weights, for all n through 20.
    for n in range(4,21):
        direct=Counter()
        for a in range(1,n-2):
            for b in range(1,n-a-1):
                for c in range(1,n-a-b):
                    d=n-a-b-c
                    direct[min(a,c)*min(b,d)]+=1
        predicted_counts=Counter()
        for x in range(1,n//2+1):
            for y in range(1,n//2+1):
                rem=n-2*x-2*y
                if rem<0: continue
                # ((1+z)/(1-z))^2 coefficient at z^rem
                weight=1 if rem==0 else 4*rem
                predicted_counts[x*y]+=weight
        assert direct==predicted_counts,(n,direct,predicted_counts)
    print('VERIFY_OK', 'word_checks',tested,'exhaustive_through_length',16,
          'generating_function_through_length',20)


if __name__=='__main__':
    verify()
