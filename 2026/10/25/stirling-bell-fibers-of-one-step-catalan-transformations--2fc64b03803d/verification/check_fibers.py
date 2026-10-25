"""Enumerate N-tableaux and directly evaluate the stylic-to-Catalan generator map.
Usage: python3 verification/check_fibers.py
Requires only the Python standard library. The computation checks finite n <= 8,
not the unrestricted mathematical theorem.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
from math import comb

@lru_cache(None)
def stirling(n, k):
    if n == k == 0: return 1
    if not (0 < k <= n): return 0
    return stirling(n-1, k-1) + k*stirling(n-1, k)

@lru_cache(None)
def bell(n):
    return sum(stirling(n,k) for k in range(n+1))

def rows_above(row):
    yield ()
    for r in range(1, len(row)+1):
        for c in combinations(row[1:],r):
            for rest in rows_above(c):
                yield (c,) + rest

def all_tableaux(n):
    yield ()
    for r in range(1,n+1):
        for base in combinations(range(1,n+1),r):
            for rest in rows_above(base):
                yield (base,) + rest

def quotient_image(tableau,n):
    mapping=list(range(n+1))
    for row in reversed(tableau):
        for letter in row:
            mapping=[v-1 if v==letter else v for v in mapping]
    return tuple(mapping)

def support_runs(s):
    return sum(x-1 not in s for x in s)

for n in range(1,9):
    profiles = {}
    total=0
    for T in all_tableaux(n):
        total+=1
        img=quotient_image(T,n)
        profiles.setdefault(img,Counter())[len(T)]+=1
    assert total == bell(n+1), (n,total,bell(n+1))
    weighted_by_runs=Counter()
    for mask in range(1<<n):
        S=frozenset(i+1 for i in range(n) if mask&(1<<i))
        b=support_runs(S)
        img=tuple(y-1 if y in S else y for y in range(n+1))
        got=profiles.get(img,Counter())
        expected=Counter({h:stirling(b,h) for h in range(b+1) if stirling(b,h)})
        assert got==expected,(n,S,b,got,expected)
        weighted_by_runs[b]+=1
    for b in range((n+1)//2+1):
        assert weighted_by_runs[b]==comb(n+1,2*b)
    print('n=%d complete_tableaux=%d one_step_profiles=%d CHECK_OK' % (n,total,1<<n))
print('VERIFY_OK')
