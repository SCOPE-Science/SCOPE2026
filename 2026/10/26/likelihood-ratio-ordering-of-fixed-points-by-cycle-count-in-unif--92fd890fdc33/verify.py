"""Exact finite checks for the joint fixed-point/cycle-count likelihood-ratio theorem.

Run using Python 3.9+; no external dependencies. The analytic proof is in RESULT.md.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import comb, factorial

checks = Counter()

@lru_cache(None)
def d(n, k):
    if n == 0:
        return int(k == 0)
    if n == 1 or k < 1 or k > n // 2:
        return 0
    return (n - 1) * (d(n - 1, k) + d(n - 2, k - 1))

def cycles_and_fixed(perm):
    n = len(perm)
    visited = [False] * n
    cyc = 0
    fixed = sum(i == x for i, x in enumerate(perm))
    for i in range(n):
        if not visited[i]:
            cyc += 1
            j = i
            while not visited[j]:
                visited[j] = True
                j = perm[j]
    return cyc, fixed

for n in range(2, 9):
    brute = Counter(cycles_and_fixed(p) for p in permutations(range(n)))
    for k in range(n + 1):
        for f in range(n + 1):
            assert brute[k, f] == comb(n, f) * d(n-f, k-f)
            checks['brute_joint_cells'] += 1
    assert sum(brute.values()) == factorial(n)
    checks['brute_total'] += 1

# Every size up to 41, every minor, with exact arbitrary-precision arithmetic.
for n in range(2, 42):
    a = [[comb(n,f)*d(n-f,k-f) for f in range(n+1)] for k in range(n+1)]
    for k in range(1,n):
        for l in range(k+1,n+1):
            for f in range(n):
                for g in range(f+1,n+1):
                    assert a[k][f]*a[l][g] >= a[k][g]*a[l][f]
                    checks['tp2_minors'] += 1
    for k in range(1,n):
        for f in range(n):
            det = a[k][f]*a[k+1][f+1]-a[k][f+1]*a[k+1][f]
            assert det == comb(n,f)*comb(n,f+1)*(d(n-f,k-f)*d(n-f-1,k-f)-d(n-f,k-f+1)*d(n-f-1,k-f-1))
            checks['local_identity'] += 1

# Recurrence for the two contiguous-size derangement determinants.
for n in range(3,50):
    for r in range(-1,n+2):
        R = d(n,r)*d(n-1,r-1)-d(n,r-1)*d(n-1,r)
        T = d(n,r)*d(n-1,r)-d(n,r+1)*d(n-1,r-1)
        L = d(n-1,r)**2-d(n-1,r-1)*d(n-1,r+1)
        assert R >= 0 and T >= 0 and L >= 0
        checks['mixed_nonnegative'] += 1
        if n >= 4:
            prevT = d(n-1,r-1)*d(n-2,r-1)-d(n-1,r)*d(n-2,r-2)
            prevR = d(n-1,r)*d(n-2,r-1)-d(n-1,r-1)*d(n-2,r)
            assert R == (n-1)*prevT
            assert T == (n-1)*(L+prevR)
            checks['mixed_recursions'] += 1

# Independently compare P_n(z) to path-matching weighted enumeration.
for n in range(2,17):
    m=n-2
    weights=[Fraction(1,j+1) for j in range(1,m)]
    poly=Counter()
    for mask in range(1 << max(0,m-1)):
        if mask & (mask << 1):
            continue
        q=mask.bit_count()
        product=Fraction(1)
        for i,w in enumerate(weights):
            if mask & (1 << i):product*=w
        poly[q]+=product
    for q in range(max(0,m//2)+1):
        assert poly[q] == Fraction(d(n,q+1),factorial(n-1))
        checks['matching_coefficient']+=1

print('PASS', dict(sorted(checks.items())), 'total_assertions=',sum(checks.values()))
