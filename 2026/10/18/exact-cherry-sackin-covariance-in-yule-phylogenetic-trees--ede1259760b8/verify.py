"""Exact, independent checks for cherry count and Sackin path-length covariance.
No external packages are required. Run: python verify.py
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import factorial

@lru_cache(None)
def statistics(tree):
    if tree is None:
        return (1, 0, 0)  # leaves, cherries, leaf-depth sum
    a, b = statistics(tree[0]), statistics(tree[1])
    leaves = a[0] + b[0]
    cherries = a[1] + b[1] + int(tree[0] is None and tree[1] is None)
    path = a[2] + b[2] + leaves
    return leaves, cherries, path

def split_at_each_leaf(tree):
    if tree is None:
        yield (None, None)
        return
    for x in split_at_each_leaf(tree[0]):
        yield (x, tree[1])
    for y in split_at_each_leaf(tree[1]):
        yield (tree[0], y)

# Enumeration of all uniformly chosen leaf-splitting histories, retaining their
# exact integer multiplicities. Does not use the root-splitting recurrence.
history_counts = Counter({None: 1})
checks = 0
for n in range(1, 10):
    total = factorial(n - 1)
    assert sum(history_counts.values()) == total
    raw_c = sum(count * statistics(tree)[1] for tree, count in history_counts.items())
    raw_s = sum(count * statistics(tree)[2] for tree, count in history_counts.items())
    raw_cs = sum(count * statistics(tree)[1] * statistics(tree)[2] for tree, count in history_counts.items())
    raw_c2 = sum(count * statistics(tree)[1] ** 2 for tree, count in history_counts.items())
    raw_s2 = sum(count * statistics(tree)[2] ** 2 for tree, count in history_counts.items())
    emc, ems, ecs, ec2 = [F(v, total) for v in (raw_c, raw_s, raw_cs, raw_c2)]
    covariance = ecs - emc*ems
    variance_c = ec2 - emc*emc
    variance_s = F(raw_s2,total)-ems*ems
    Hn = sum(F(1,j) for j in range(1,n+1))
    Hn2 = sum(F(1,j*j) for j in range(1,n+1))
    if n >= 2:
        assert variance_s == 7*n*n - 4*n*n*Hn2 - 2*n*Hn - n
        checks += 1
    if n >= 3:
        assert covariance == -F(n, 9) + F(2, 3*(n-1)), (n, covariance)
        assert emc == F(n, 3)
        checks += 2
    if n >= 5:
        assert variance_c == F(2*n, 45), (n, variance_c)
        assert covariance/variance_c == -F(5,2) + F(15, n*(n-1))
        checks += 2
    if n == 4:
        assert variance_c == F(2,9)
        checks += 1
    if n >= 2:
        assert ems == 2*n*(sum(F(1,j) for j in range(1,n+1))-1)
        checks += 1
    if n < 9:
        next_histories = Counter()
        for tree, mult in history_counts.items():
            for split in split_at_each_leaf(tree):
                next_histories[split] += mult
        history_counts = next_histories
    checks += 1

# Separate exact root-split moment recursion, valid at arbitrarily large sizes.
N = 120
means_c = [F(0)]*(N+1)
means_s = [F(0)]*(N+1)
covs = [F(0)]*(N+1)
vars_c = [F(0)]*(N+1)
vars_s = [F(0)]*(N+1)
for n in range(2,N+1):
    if n == 2:
        means_c[n], means_s[n] = F(1),F(2)
        continue
    cs = [means_c[k]+means_c[n-k] for k in range(1,n)]
    ss = [means_s[k]+means_s[n-k]+n for k in range(1,n)]
    means_c[n] = sum(cs,F(0))/(n-1)
    means_s[n] = sum(ss,F(0))/(n-1)
    force = sum((x-means_c[n])*(y-means_s[n]) for x,y in zip(cs,ss))/(n-1)
    covs[n] = 2*sum(covs[1:n],F(0))/(n-1) + force
    g = sum((x-means_c[n])**2 for x in cs)/(n-1)
    vars_c[n] = 2*sum(vars_c[1:n],F(0))/(n-1) + g
    hs = sum((x-means_s[n])**2 for x in ss)/(n-1)
    vars_s[n] = 2*sum(vars_s[1:n],F(0))/(n-1) + hs
    hn = sum(F(1,j) for j in range(1,n+1))
    hn2 = sum(F(1,j*j) for j in range(1,n+1))
    assert vars_s[n] == 7*n*n-4*n*n*hn2-2*n*hn-n
    checks += 1
    assert covs[n] == -F(n,9) + F(2, 3*(n-1)), (n,covs[n])
    assert means_c[n] == F(n,3)
    assert means_s[n] == 2*n*(sum(F(1,j) for j in range(1,n+1))-1)
    if n>=5:
        assert vars_c[n] == F(2*n,45)
        assert covs[n]/vars_c[n] == -F(5,2) + F(15,n*(n-1))
        checks += 2
    checks += 3
print('VERIFICATION_OK',checks,'exact assertions; all Yule histories through 9 leaves and split recurrences through 120 leaves.')
