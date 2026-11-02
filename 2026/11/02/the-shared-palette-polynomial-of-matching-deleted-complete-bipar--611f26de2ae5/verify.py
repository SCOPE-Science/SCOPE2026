#!/usr/bin/env python3
"""Reproduce the matching-deleted-biclique PCF coloring census.

Usage: python3 verify.py
Uses only the Python standard library. Named colors are 0,...,q-1;
missing colors are permitted. Tests explicitly examine graph neighborhoods.
"""
from functools import lru_cache
from itertools import product
from math import comb, factorial

@lru_cache(None)
def stirling(n, k):
    if n < 0 or k < 0:
        return 0
    if n == 0:
        return int(k == 0)
    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)

@lru_cache(None)
def associated(n, k):
    if n < 0 or k < 0:
        return 0
    return sum((-1) ** j * comb(n, j) * stirling(n - j, k - j)
               for j in range(n + 1))

def falling(n, k):
    if k < 0 or k > n:
        return 0
    ans = 1
    for a in range(k):
        ans *= n - a
    return ans

def forced_doubletons(p, t, k):
    # t distinguished elements must lie in blocks of size exactly two;
    # all nondistinguished blocks must have size at least two.
    u = p - t
    total = 0
    for j in range(t // 2 + 1):
        d = t - 2 * j
        if d > u:
            continue
        pairings = comb(t, 2 * j) * factorial(2 * j) // (2 ** j * factorial(j))
        total += pairings * falling(u, d) * associated(u - d, k - t + j)
    return total

def accepted_partitions(p, t, other, s, k):
    if s >= 2:
        return stirling(p - s, k)
    if s == 1:
        return stirling(p - 1, k) - associated(p - 1, k)
    return (stirling(p, k) - associated(p, k)
            - t * associated(p - 1, k - 1)
            + (forced_doubletons(p, t, k) if other == t else 0))

def formula_profile(m, n, t, q):
    out = {}
    for s in range(t + 1):
        total = 0
        for k in range(m - s + 1):
            ak = accepted_partitions(m, t, n, s, k)
            for ell in range(n - s + 1):
                bl = accepted_partitions(n, t, m, s, ell)
                total += comb(t, s) * ak * bl * falling(q, s + k + ell)
        out[s] = total
    return out

def direct_profile(m, n, t, q):
    # Independently reconstruct the (m+n)-vertex bipartite graph.
    adjacency = [[] for _ in range(m+n)]
    for i in range(m):
        for j in range(n):
            if i < t and i == j:
                continue
            adjacency[i].append(m+j)
            adjacency[m+j].append(i)
    out = {s:0 for s in range(t+1)}
    for labels in product(range(q), repeat=m+n):
        if any(labels[v] == labels[w] for v in range(m+n)
               for w in adjacency[v]):
            continue
        if any(not any(sum(labels[w] == c for w in adjacency[v]) == 1
                           for c in set(labels[w] for w in adjacency[v]))
               for v in range(m+n) if adjacency[v]):
            continue
        shared = sum(labels[i] == labels[m+i] for i in range(t))
        out[shared] += 1
    return out

def predicted_chromatic_number(m, n, t):
    small, big = sorted((m,n))
    if (m,n,t) == (2,2,2):
        return 2
    if ((m,n,t) == (2,2,1)
            or (small == t == 2 and big > 2)
            or (m,n,t) == (3,3,3)):
        return 3
    return 4

def main():
    exact_comparisons=0
    for m in range(2,5):
        for n in range(2,5):
            for t in range(min(m,n)+1):
                for q in range(1,5):
                    expected=direct_profile(m,n,t,q)
                    found=formula_profile(m,n,t,q)
                    assert found==expected, (m,n,t,q,expected,found)
                    exact_comparisons+=1
    extra=[(3,3,t,5) for t in range(4)]+[
        (2,5,2,4),(3,5,3,4),(4,5,4,4),(4,4,2,5)]
    for m,n,t,q in extra:
        assert direct_profile(m,n,t,q)==formula_profile(m,n,t,q)
        exact_comparisons+=1
    assert formula_profile(4,4,4,4)=={0:216,1:0,2:144,3:0,4:24}
    chi_cases=0
    for m in range(2,11):
        for n in range(2,11):
            for t in range(min(m,n)+1):
                actual=next(q for q in range(1,5) if sum(formula_profile(m,n,t,q).values())>0)
                expect=predicted_chromatic_number(m,n,t)
                assert actual==expect,(m,n,t,actual,expect)
                if actual==3:
                    assert sum(formula_profile(m,n,t,3).values())==6
                if actual==2:
                    assert sum(formula_profile(m,n,t,2).values())==4
                chi_cases+=1
    print('EXACT_PROFILE_COMPARISONS',exact_comparisons)
    print('CHROMATIC_CLASSIFICATION_CHECKS',chi_cases)
    print('CROWN_FOUR_COLOR_PROFILE',formula_profile(4,4,4,4))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
