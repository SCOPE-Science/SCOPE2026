#!/usr/bin/env python3
"""Small exact checks for forbidden-subsequence saturation and unary hosts."""
from itertools import product

def embeds(pattern, word):
    j = 0
    for a in word:
        if j < len(pattern) and pattern[j] == a:
            j += 1
    return j == len(pattern)

def universal_block(alphabet, repetitions):
    return tuple(alphabet) * repetitions

def principal_host(alphabet, forbidden, horizon):
    out = ()
    for i, a in enumerate(forbidden):
        out += universal_block([b for b in alphabet if b != a], horizon)
        if i+1 < len(forbidden): out += (a,)
    return out

def unary_host(alphabet, letter, m, horizon):
    assert horizon >= m
    p = tuple(b for b in alphabet if b != letter)
    t = horizon - m + 1
    return (p*t + (letter,))*(m-1)+p*t

def targets(alphabet, k):
    return list(product(alphabet, repeat=k))

principal_cases=0
for q in [2,3]:
    alphabet = tuple(range(q))
    for m in range(1, 5 if q == 2 else 4):
        for v in targets(alphabet,m):
            for k in range(0, min(m+3,7)):
                w=principal_host(alphabet,v,k)
                assert not embeds(v,w), (q,m,k,v,w)
                for ell in range(k+1):
                    for x in targets(alphabet,ell):
                        assert embeds(x,w) == (not embeds(v,x)), (q,m,k,v,x,w)
                principal_cases+=1

# The insertion sphere size at each length-one extension
sphere_cases=0
for q in range(2,5):
    alphabet=tuple(range(q))
    for m in range(1,5 if q==2 else 4):
        for v in targets(alphabet,m):
            sphere={v[:i]+(a,)+v[i:] for i in range(m+1) for a in alphabet}
            assert len(sphere)==(q-1)*(m+1)+1
            sphere_cases+=1

# Independently brute-force the minimum unary host for small exact cases.
unary_cases=0
for q,m,k in [(2,1,2),(2,2,2),(2,2,3),(2,3,3),(2,3,4),(2,4,4),(3,1,2),(3,2,2),(3,2,3)]:
    alphabet=tuple(range(q)); a=0
    w=unary_host(alphabet,a,m,k)
    allowed=[x for x in targets(alphabet,k) if not embeds((a,)*m,x)]
    assert not embeds((a,)*m,w)
    assert all(embeds(x,w) for x in allowed)
    expected=m*(q-1)*(k-m+1)+m-1
    assert len(w)==expected
    # Every shorter word either contains the forbidden pattern, or omits a required pattern.
    for n in range(expected):
        for cand in targets(alphabet,n):
            if not embeds((a,)*m,cand):
                assert any(not embeds(x,cand) for x in allowed),(q,m,k,n,cand)
    unary_cases+=1
print('VERIFY_OK principal_instances=%d insertion_spheres=%d unary_exact_optima=%d' % (principal_cases,sphere_cases,unary_cases))
