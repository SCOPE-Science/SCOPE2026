"""Exact finite checks for marked-leaf pruning and terminal depth in recursive trees."""
from collections import Counter
from fractions import Fraction as Q
from itertools import product, combinations
from math import comb, factorial

count = 0

def eq(a, b):
    global count
    assert a == b, (a, b)
    count += 1

def hist(n):
    out = Counter()
    for pars in product(*(range(1, j) for j in range(2, n+1))):
        parent = (0, 0) + pars
        depth = [0] * (n+1)
        ch = [0] * (n+1)
        for j in range(2, n+1):
            depth[j] = depth[parent[j]] + 1
            ch[parent[j]] += 1
        leafs = frozenset(i for i in range(2, n+1) if ch[i] == 0)
        out[(depth[n], len(leafs), leafs)] += 1
    eq(sum(out.values()), factorial(n-1))
    return out

def dhist(n):
    h = Counter()
    for (d, leaves, subset), num in hist(n).items():
        h[d] += num
    return {d: Q(v, factorial(n-1)) for d,v in h.items()}

def eulerian(n):
    cur = [1]
    for r in range(2, n+1):
        nxt = [0]*r
        for k in range(r):
            nxt[k] = (k+1)*(cur[k] if k <len(cur) else 0)+(r-k)*(cur[k-1] if k else 0)
        cur = nxt
    return cur

def predict_joint(n):
    a = eulerian(n-1)
    out = Counter()
    for s in range(n-1):
        factorial_moment = sum(a[k]*comb(k,s) for k in range(s,len(a)))
        for d,ph in dhist(n-s).items():
            for j in range(s+1):
                out[(d,j)] += Q(factorial_moment,factorial(n-1))*ph * comb(s,j)*(-1)**(s-j)
    return out

for n in range(3,9):
    h = hist(n)
    joint = Counter()
    for (d, ell, subset),num in h.items():
        joint[(d,ell-1)] += Q(num,factorial(n-1))
    ans = predict_joint(n)
    for cell in set(joint)|set(ans):
        eq(joint[cell],ans[cell])
    emH = sum(Q(d*num,factorial(n-1)) for (d,ell,subset),num in h.items())
    emL = sum(Q(ell*num,factorial(n-1)) for (d,ell,subset),num in h.items())
    emHL = sum(Q(d*ell*num,factorial(n-1)) for (d,ell,subset),num in h.items())
    eq(emHL-emH*emL,Q(-(n-2),2*(n-1)))
    for r in range(n-1):
        for selected in combinations(range(2,n),r):
            s = frozenset(selected)
            count_cond = Counter()
            denom = 0
            for (d,ell,leafs),num in h.items():
                if s.issubset(leafs):
                    count_cond[d]+=num
                    denom+=num
            expected = dhist(n-r)
            for d in set(count_cond)|set(expected):
                eq(Q(count_cond[d],denom),expected.get(d,Q(0)))
print('PASSED:',count,'independent exact assertions through n=8')
