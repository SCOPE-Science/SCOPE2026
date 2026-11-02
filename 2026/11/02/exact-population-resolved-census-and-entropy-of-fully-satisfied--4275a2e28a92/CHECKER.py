#!/usr/bin/env python3
"""Independent finite checks for a binary radius-two satisfaction census."""
from itertools import product
from collections import Counter
from math import comb

checks = 0
def require(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)

def stable(x):
    n = len(x)
    return all(sum(x[(i+j) % n] == x[i] for j in (-2,-1,1,2)) >= 2
               for i in range(n))

def run_lengths(x):
    n = len(x)
    if all(t == x[0] for t in x):
        return [n]
    starts = [i for i in range(n) if x[i] != x[(i-1)%n]]
    out = []
    for t, i in enumerate(starts):
        j = starts[(t+1)%len(starts)]
        out.append((j-i) % n or n)
    return out

def predicted(n,m):
    ans = int(m == 0 or m == n)
    if n % 2 == 0 and m == n//2:
        ans += 2
    for k in range(1, min(m//3, (n-m)//3)+1):
        num = n * comb(m-2*k-1,k-1)*comb(n-m-2*k-1,k-1)
        require(num % k == 0, ('integrality',n,m,k))
        ans += num//k
    return ans

def matrix_mult(A,B):
    N=len(A)
    return [[sum(A[i][t]*B[t][j] for t in range(N)) for j in range(N)]
            for i in range(N)]

T = [[0]*6 for i in range(6)]
for i,j in [(0,1),(1,2),(2,2),(2,3),(3,4),(4,5),(5,5),(5,0)]:
    T[i][j] = 1
I = [[int(i==j) for j in range(6)] for i in range(6)]
powers = [I]
for n in range(1,51):
    powers.append(matrix_mult(powers[-1], T))
for n in range(5,17):
    observed = Counter()
    for x in product((0,1), repeat=n):
        s = stable(x)
        lengths = run_lengths(x)
        classification = (len(lengths)==1 or
                          (n%2==0 and len(lengths)==n and all(a==1 for a in lengths)) or
                          all(a>=3 for a in lengths))
        require(s==classification, ('runs',n,x))
        if s:
            observed[sum(x)] += 1
    for m in range(n+1):
        require(observed[m]==predicted(n,m), ('composition',n,m))
    trace = sum(powers[n][i][i] for i in range(6))
    require(trace + 2*int(n%2==0)==sum(observed.values()), ('trace',n))
for n in range(5,51):
    trace = sum(powers[n][i][i] for i in range(6))
    H = sum(predicted(n,m) for m in range(n+1))
    require(H == trace+2*int(n%2==0), ('large trace',n))
# Matrix identity from the explicit six-state transition graph.
lhs = [[powers[6][i][j]-2*powers[5][i][j]+powers[4][i][j]-I[i][j]
        for j in range(6)] for i in range(6)]
require(all(x==0 for row in lhs for x in row), 'characteristic polynomial identity')
print('PASS', checks, 'assertions')
