#!/usr/bin/env python3
"""Exact checks for the bounded-interior-pattern avoidance enumerator.
Self-contained, standard library only. All summations use integer arithmetic.
"""
from itertools import combinations
from collections import Counter
from math import comb

def contains(word,pat):
    k=0
    for x in word:
        if k<len(pat) and x==pat[k]: k+=1
    return k==len(pat)

def enumerate_avoid(A,B,t):
    ans=[0]*(A*B+1)
    n=A+B
    for apos in combinations(range(n),A):
        pos=set(apos)
        word=''.join('a' if i in pos else 'b' for i in range(n))
        ab=sum((n-1-i)-sum(j>i for j in apos) for i in apos)
        assert 0<=ab<=A*B
        if not contains(word,'a'+'b'*t+'a'):
            ans[ab]+=1
    return ans

def gbin(N,k):
    # Gaussian polynomial, partitions inside k x (N-k), by recurrence
    if k<0 or k>N:return []
    P=[[1] for _ in range(N+1)]
    for i in range(1,N+1):
        Q=[[1] for _ in range(i+1)]
        for j in range(1,i):
            # [i choose j]_q = [i-1 choose j]_q + q^(i-j) [i-1 choose j-1]_q
            out=[0]*(j*(i-j)+1)
            for e,v in enumerate(P[j]):out[e]+=v
            for e,v in enumerate(P[j-1]):out[e+i-j]+=v
            Q[j]=out
        P=Q
    return P[k]

def formula(A,B,t):
    assert A>=2 and B>=0 and t>=2
    coeff=[0]*(A*B+1)
    for d in range(min(t-1,B)+1):
        g=gbin(A+d-2,d)
        for z in range(B-d+1):
            for j,v in enumerate(g):
                exponent=d+A*z+j
                assert exponent<len(coeff)
                coeff[exponent]+=v
    return coeff

def partitions(n,maxparts=None):
    # count partitions of n with <=maxparts parts via unrestricted part sizes <=maxparts
    assert n>=0
    if maxparts is None:maxparts=n
    p=[0]*(n+1);p[0]=1
    for part in range(1,min(maxparts,n)+1):
        for s in range(part,n+1):p[s]+=p[s-part]
    return p[n]

def denominator(A,B):
    return gbin(A+B,A)

checks=0; total_words=0; tested=0
for A in range(2,8):
    for B in range(0,8):
        if A+B>11:continue
        total_words+=comb(A+B,A)
        for t in range(2,8):
            expected=enumerate_avoid(A,B,t)
            actual=formula(A,B,t)
            assert actual==expected,(A,B,t,actual,expected)
            assert all(0<=a<=b for a,b in zip(actual,denominator(A,B)))
            checks+=len(actual)
            tested+=1
print(f'FINITE_EXHAUSTIVE PASS: {tested} parameter triples, {checks} coefficient comparisons; source words enumerated per t: {total_words}.')

stable_tests=0
for C in range(0,40):
    for t in range(2,10):
        A=B=C+2
        coeff=formula(A,B,t)[C]
        expected=partitions(C,t-1)
        assert coeff==expected,(C,t,coeff,expected)
        assert denominator(A,B)[C]==partitions(C)
        stable_tests+=1
print(f'STAB_RESTRICTED_PARTITION PASS: {stable_tests} cases (C=0..39, t=2..9).')

for C in (0,1,2,3,4,5,6,8,10,12,16,20):
    P=partitions(C)
    v3=partitions(C,2)
    print(f'C={C}: p(C)={P}; avoid_abbb a(t=3)={v3}; probability={(P-v3)}/{P}')
