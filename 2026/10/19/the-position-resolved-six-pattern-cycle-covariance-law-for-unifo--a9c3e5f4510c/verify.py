"""Independently check finite-position cycle-pattern covariance identities.

Run with Python 3.9+ and no third-party packages.
"""
from fractions import Fraction
from itertools import permutations, combinations
from math import factorial

PATTERNS = ((1, 2, 3), (1, 3, 2), (2, 1, 3),
            (2, 3, 1), (3, 1, 2), (3, 2, 1))

def cycle_count(p):
    n = len(p)
    seen = [False] * n
    total = 0
    for start in range(n):
        if not seen[start]:
            total += 1
            j = start
            while not seen[j]:
                seen[j] = True
                j = p[j] - 1
    return total

def pat3(p, i):
    seq = p[i:i+3]
    return tuple(1 + sum(x < v for x in seq) for v in seq)

def coefficient(n, i, pat):
    # i uses 1-based indexing.
    a, b, c = pat
    if pat == (1, 2, 3): return 3*n-2
    if pat == (1, 3, 2): return 9*n-14-12*i
    if pat == (2, 1, 3): return 12*i-3*n-2
    if pat == (2, 3, 1): return 12*i-9*n+10
    if pat == (3, 1, 2): return 3*n-2-12*i
    if pat == (3, 2, 1): return 10-3*n
    raise AssertionError('pattern')

def combinatorial_count(n, i, pat):
    a = (i, i+1, i+2)
    def nchoose2(t): return t * (t-1) // 2
    count1 = 0
    for j, rank in enumerate(pat):
        x = a[j]
        count1 += {1:nchoose2(n-x),2:(x-1)*(n-x),3:nchoose2(x-1)}[rank]
    count2=0
    for j,k in combinations(range(3),2):
        if pat[j] > pat[k]:
            x,y=a[j],a[k]
            rem=3-j-k
            count2 += {1:x-1,2:y-x-1,3:n-y}[pat[rem]]
    count3=int(pat in ((2,3,1),(3,1,2)))
    return 6*(count1+count2+count3)-(3*n*n-6*n+2)

def verify():
    count=0
    for n in range(3,9):
        total=factorial(n)
        C_sum=0
        I_sum={(i,p):0 for i in range(n-2) for p in PATTERNS}
        CI_sum=dict.fromkeys(I_sum,0)
        for perm in permutations(range(1,n+1)):
            cyc=cycle_count(perm)
            C_sum+=cyc
            for i in range(n-2):
                pattern=pat3(perm,i)
                I_sum[i,pattern]+=1
                CI_sum[i,pattern]+=cyc
        for i in range(n-2):
            for pattern in PATTERNS:
                assert I_sum[i,pattern]==total//6
                observed=Fraction(CI_sum[i,pattern],total)-Fraction(C_sum*I_sum[i,pattern],total*total)
                predicted=Fraction(coefficient(n,i+1,pattern),6*n*(n-1)*(n-2))
                assert observed==predicted,(n,i,pattern,observed,predicted)
                count+=1
    for n in range(3,151):
        for i in range(1,n-1):
            for pat in PATTERNS:
                assert combinatorial_count(n,i,pat)==coefficient(n,i,pat)
                count+=1
    print(f'PASS: {count} independent finite checks, n=3..8 exhaustive; n=3..150 combinatorial')

if __name__=='__main__': verify()
