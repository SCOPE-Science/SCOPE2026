"""Exact checks for the restricted Stirling first-collision kernel.
Requires Python 3 stdlib only; no external files.
"""
from itertools import combinations, permutations
from math import prod
from math import comb

checks = 0

def must(condition, label):
    global checks
    if not condition:
        raise AssertionError(label)
    checks += 1


def restricted(n, k, r):
    if not (0 <= r <= n and 0 <= k <= n):
        return 0
    v = [0] * (n + 1)
    v[r] = 1
    for _ in range(r+1, n+1):
        v = [(v[j-1] if j else 0) + j*v[j] for j in range(n+1)]
    return v[k]


def h(n, t, k):
    if not (1 <= k <= n and 2 <= t <= n+1):
        return 0
    return int(k == n) if t == n+1 else (t-1)*restricted(n-1, k, t-1)


def enumerate_rgs(n):
    def rec(seq, maximum):
        if len(seq) == n:
            yield tuple(seq)
            return
        for x in range(maximum+2):
            yield from rec(seq+[x], max(maximum,x))
    yield from rec([0],0)

for n in range(2,10):
    table = {(t,k):0 for t in range(2,n+2) for k in range(1,n+1)}
    for seq in enumerate_rgs(n):
        k = max(seq)+1
        seen=set()
        first=n+1
        for i,x in enumerate(seq,1):
            if x in seen:
                first=i
                break
            seen.add(x)
        table[first,k] += 1
    for (t,k), actual in table.items():
        must(actual == h(n,t,k), (n,t,k,actual,h(n,t,k)))
    for k in range(1,n+1):
        must(sum(h(n,t,k) for t in range(2,n+2)) == restricted(n,k,0), (n,k,'colsum'))
    for t1 in range(2,n+2):
        for t2 in range(t1+1,n+2):
            for k1 in range(1,n+1):
                for k2 in range(k1+1,n+1):
                    must(h(n,t1,k1)*h(n,t2,k2) >= h(n,t1,k2)*h(n,t2,k1), (n,t1,t2,k1,k2,'TP2'))

# Higher-order minors of the complete first-repeat matrix, independently checked.
def determinant(a):
    d = len(a)
    return sum((-1)**sum(p[i]>p[j] for i in range(d) for j in range(i+1,d))
               * prod(a[i][p[i]] for i in range(d))
               for p in permutations(range(d)))

for n in range(3,10):
    for d in range(3,min(5,n+1)):
        for rows in combinations(range(2,n+2),d):
            for cols in combinations(range(1,n+1),d):
                must(determinant([[h(n,t,k) for k in cols] for t in rows]) >= 0,
                     (n,d,rows,cols,'higher-minor'))

# Independently check total positivity of pure-birth kernels for finite uniform alphabets.
for m in range(2,12):
    B=[[0]*(m+1) for _ in range(m+1)]
    for j in range(m+1):
        B[j][j]=j
        if j<m: B[j][j+1]=m-j
    Q=[[int(i==j) for j in range(m+1)] for i in range(m+1)]
    for steps in range(0,m+1):
        for i in range(m+1):
            for j in range(i+1,m+1):
                for a in range(m+1):
                    for b in range(a+1,m+1):
                        must(Q[i][a]*Q[j][b] >= Q[i][b]*Q[j][a], (m,steps,i,j,a,b,'bridge'))
        Q=[[sum(Q[i][z]*B[z][j] for z in range(m+1)) for j in range(m+1)] for i in range(m+1)]
print(f'PASS: {checks} exact assertions; full partition census through n=9, minors through order four, and transition-kernel TP2 tests.')
