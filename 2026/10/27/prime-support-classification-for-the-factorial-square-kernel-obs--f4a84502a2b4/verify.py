#!/usr/bin/env python3
"""Exact finite checks for the squarefree factorial kernel obstruction."""
from math import gcd, factorial

def primes_to(n):
    return [k for k in range(2,n+1) if all(k%d for d in range(2,int(k**0.5)+1))]

def kernel(m):
    out=1
    p=2
    while p*p<=m:
        e=0
        while m%p==0:
            m//=p;e+=1
        if e&1:out*=p
        p+=1
    if m>1:out*=m
    return out

def factorial_kernel(n, primes):
    out=1
    for p in primes:
        if p>n:break
        t=n;e=0
        while t:
            t//=p;e+=t
        if e&1:out*=p
    return out

P=primes_to(41)
K=[factorial_kernel(n,P) for n in range(41)]
a=1
for n in range(41):
    if n>0:a*=n
    assert kernel(a)==K[n], (n, a, K[n])
assert K[12:17]==[231,3003,858,1430,1430]
assert all(K[c]>c*c for c in range(12,41))

# Singleton exclusions before 12; the analytical part excludes all c >=12.
small_bad=[]
for p in P:
    if p<=11:
        bad=[(c,K[c]) for c in range(0,12) if gcd(p,K[c])**2>K[c]]
        if bad:small_bad.append(p)
        assert bad, p
    else:
        assert all(gcd(p,K[c])**2<=K[c] for c in range(0,41)),p
assert small_bad == [2,3,5,7,11]

# The mathematical proof shows all pairs with a small factor <= 11 fail,
# and those with a largest prime >= 41 pass. Compare all remaining pairs.
bad={}
for i,p in enumerate(P):
    if p<13 or p>37:continue
    for q in P[i+1:]:
        if q>37:continue
        failures=[(c,K[c],gcd(p*q,K[c])) for c in range(q,41) if gcd(p*q,K[c])**2>K[c]]
        if failures:bad[(p,q)]=failures
expected={(13,17),(13,19),(17,19),(17,23),(19,23)}
assert set(bad)==expected,(set(bad),expected)
expected_first={
    (13,17):(17,24310,221),
    (13,19):(20,46189,247),
    (17,19):(20,46189,323),
    (17,23):(26,104006,391),
    (19,23):(26,104006,437),
}
assert {pair:failures[0] for pair,failures in bad.items()} == expected_first

# For c < q, only the smaller prime can occur; the c^2 bound handles it.
for i,p in enumerate(P):
    if p<13 or p>37:continue
    for q in P[i+1:]:
        if q>37:continue
        assert all(gcd(p*q,K[c])**2<=K[c] for c in range(q))

print('VERIFY_OK kernels_0_to_40=41 singleton_forbidden='+','.join(map(str,small_bad)))
for pair in sorted(bad):
    print('bad_pair',*pair,'first_witness',bad[pair][0])
print('all_remaining_prime_pairs_13_to_37: PASS')
print('analytic_tail: use R_3=17, R_5=41 from Ramanujan prime theorem')
