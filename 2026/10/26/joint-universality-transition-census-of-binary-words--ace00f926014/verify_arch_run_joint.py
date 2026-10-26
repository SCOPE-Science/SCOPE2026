"""Exact finite cross-check for binary subsequence universality and symbol transitions."""
from collections import Counter
from itertools import product
from math import comb

def C(a,b):
    return comb(a,b) if 0 <= b <= a else 0

def joint(n,k,r):
    if n == k == r == 0:
        return 1
    if not n or r < 0 or r >= n:
        return 0
    if k == 0:
        return 2 if r == 0 else 0
    return 2*(C(n-k,k)*C(k-1,r-k)+C(n-k-1,k)*C(k-1,r-k-1))

def greedy_index(w):
    seen = set()
    arches = 0
    for symbol in w:
        seen.add(symbol)
        if len(seen) == 2:
            arches += 1
            seen.clear()
    return arches

def defining_index(w):
    def is_subseq(v):
        j = 0
        for x in w:
            if j < len(v) and x == v[j]:
                j += 1
        return j == len(v)
    k = 0
    while all(is_subseq(u) for u in product('01', repeat=k+1)):
        k += 1
    return k

assert joint(0,0,0) == 1
for n in range(1,18):
    histogram = Counter()
    for w in product('01', repeat=n):
        k = greedy_index(w)
        if n <= 11:
            assert k == defining_index(w), ('definition',w)
        r = sum(w[i] != w[i-1] for i in range(1,n))
        histogram[k,r] += 1
    for k in range(n+1):
        for r in range(n):
            expected = joint(n,k,r)
            actual = histogram[k,r]
            assert actual == expected, ('coefficient',n,k,r,actual,expected)
            if actual:
                assert (k == r == 0) or k <= r <= min(2*k,n-1)
    assert sum(histogram.values()) == 2**n
print('VERIFY_OK: definition through n=11, full joint coefficient enumeration through n=17')
