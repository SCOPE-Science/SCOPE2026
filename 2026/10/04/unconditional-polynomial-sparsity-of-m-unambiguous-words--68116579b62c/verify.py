#!/usr/bin/env python3
from collections import Counter
from itertools import product
from math import comb

def contiguous_patterns(s):
    out=[]
    for ell in range(1,s+1):
        for i in range(s-ell+1):
            out.append(tuple(range(i,i+ell)))
    return out

def subseq_count(word, pat):
    dp=[0]*(len(pat)+1)
    dp[0]=1
    for x in word:
        for j in range(len(pat)-1,-1,-1):
            if x==pat[j]:
                dp[j+1]+=dp[j]
    return dp[-1]

def signature(word,s):
    return tuple(subseq_count(word,p) for p in contiguous_patterns(s))

def bound_P(s,n):
    z=1
    for ell in range(1,s+1):
        z *= (comb(n,ell)+1)**(s-ell+1)
    return z

def exhaustive(s,maxn):
    total_words=0
    total_prefix_checks=0
    exact_unamb={}
    for n in range(maxn+1):
        words=[]
        for m in range(n+1):
            words.extend(product(range(s), repeat=m))
        total_words=max(total_words,len(words))
        sigs=[signature(w,s) for w in words]
        fibers=Counter(sigs)
        u=sum(1 for sig in sigs if fibers[sig]==1)
        exact_unamb[n]=u
        assert u <= len(fibers) <= bound_P(s,n)
        for w,sig in zip(words,sigs):
            k=0
            for ell in range(1,s+1):
                cap=comb(n,ell)
                for _ in range(s-ell+1):
                    assert 0 <= sig[k] <= cap
                    k+=1
        total_prefix_checks+=1
    return total_words,total_prefix_checks,exact_unamb

w2,c2,u2=exhaustive(2,9)
w3,c3,u3=exhaustive(3,7)

# Published binary exact count: for exact length m>=4, 6m-10.
# Convert cumulative U(n) to exact-length increments and cross-check.
for m in range(4,10):
    exact=u2[m]-u2[m-1]
    assert exact==6*m-10, (m,exact)

# Algebraic exponent identity in the polynomial bound.
for s in range(2,51):
    lhs=sum(ell*(s-ell+1) for ell in range(1,s+1))
    rhs=comb(s+2,3)
    assert lhs==rhs

print(
    "VERIFY_OK alphabets=2,3 "
    f"max_n=9,7 words_at_max={w2},{w3} "
    "binary_formula_n=4..9 exponent_identity_s=2..50"
)
