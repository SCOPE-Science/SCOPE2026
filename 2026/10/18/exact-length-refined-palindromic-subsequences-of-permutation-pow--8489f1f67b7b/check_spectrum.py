"""Reproducibility checks for palindrome subsequence spectra of permutation powers.
Python standard library only. This script is an independent finite test, not a general proof.
"""
from collections import Counter
from itertools import permutations
from math import comb


def exhaustive_spectrum(q, m, perm=None):
    p = tuple(range(q)) if perm is None else tuple(perm)
    s = p * m
    out = set()
    for mask in range(1, 1 << len(s)):
        w = tuple(s[i] for i in range(len(s)) if mask & (1 << i))
        if w == w[::-1]:
            out.add(w)
    return Counter(map(len, out)), out


def theorem_spectrum(q, m):
    ans = Counter()
    for t in range(m):
        if t + 1 <= m:
            ans[2 * t + 1] = q * sum(comb(t, e) * (q - 1)**(t-e)
                                           for e in range(min(t, m-t-1) + 1))
    for t in range(1, m):
        ans[2 * t] = q * sum(comb(t-1, e) * (q - 1)**(t-1-e)
                                       for e in range(min(t-1, m-t-1) + 1))
    return +ans


def dp_total_distinct(q, m):
    # Character-separated interval DP, independent of the theorem's greedy cost.
    s = tuple(range(q)) * m
    from functools import lru_cache
    @lru_cache(None)
    def f(i,j):
        if i >= j:
            return 0
        result=0
        for c in range(q):
            first=next((k for k in range(i,j) if s[k]==c),None)
            if first is None:
                continue
            last=next(k for k in range(j-1,i-1,-1) if s[k]==c)
            result += 1 if first==last else 2 + f(first+1,last)
        return result
    return f(0,len(s))


def rational_total(q, limit):
    # Coefficients of q*z*(1+z)/((1-z)*(1-(q-1)*z-z*z)).
    a=[0]*(limit+1)
    for m in range(1,limit+1):
        a[m] = q*a[m-1]-(q-2)*(a[m-2] if m>=2 else 0)-(a[m-3] if m>=3 else 0)+(q if m in (1,2) else 0)
    return a


def algebra_spectrum(q, m):
    # coefficient in z^m of q*u*z*(1+u*z)/((1-z)*(1-u^2*z*(q-1+z)))
    d = {(0, 0): 1}
    # formal sum indexed by t and equal-edge count, accumulated for minimal period <=m
    counts = Counter()
    for t in range(m):
        for e in range(t + 1):
            cost = 1 + t + e
            if cost <= m:
                counts[2*t+1] += q * comb(t,e) * (q-1)**(t-e)
        if t>=1:
            for e in range(t):
                cost=1+t+e
                if cost<=m:
                    counts[2*t]+=q*comb(t-1,e)*(q-1)**(t-1-e)
    return +counts


if __name__ == '__main__':
    cells=0
    for q in (2,3,4,5):
        for m in range(1, 6):
            if q*m > 17:
                continue
            brute, words = exhaustive_spectrum(q,m)
            formula=theorem_spectrum(q,m)
            independent=algebra_spectrum(q,m)
            assert brute==formula==independent, (q,m,brute,formula,independent)
            assert sum(brute.values()) == dp_total_distinct(q,m) == rational_total(q,m)[m]
            # Check word-by-word claim: minimal required periods = 1 + weak descents.
            for w in words:
                assert 1+sum(a>=b for a,b in zip(w,w[1:]))<=m, (q,m,w)
            cells+=1
            print(f'OK alphabet={q}, periods={m}, palindrome_count={sum(brute.values())}, length_profile={dict(sorted(brute.items()))}')
    for q in (2,3,4):
        for m in (1,2,3):
            baseline=exhaustive_spectrum(q,m)[0]
            for p in permutations(range(q)):
                assert exhaustive_spectrum(q,m,p)[0]==baseline
    extra=0
    for q in range(2,8):
        for m in range(1,24):
            assert dp_total_distinct(q,m) == sum(theorem_spectrum(q,m).values()) == rational_total(q,m)[m]
            extra+=1
    print('ALL_CHECKS_PASSED',cells,'brute force base cases, 9 relabeling classes,',extra,'independent interval-DP cases')
