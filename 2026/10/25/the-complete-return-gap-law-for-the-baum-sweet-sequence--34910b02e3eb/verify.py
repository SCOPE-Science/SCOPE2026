"""Finite independent checks of the Baum--Sweet return-gap theorem.
All infinite assertions depend on the symbolic proof in RESULT.md.
"""
from collections import Counter
from math import isclose, sqrt

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

def is_baum_sweet(n):
    if n == 0:
        return True
    bits = format(n, 'b')
    return all(len(run) % 2 == 0 for run in bits.split('1') if run)

def gap_bridge(m):
    return 2**(m-2) + 1 + (m % 2 == 0)

def predicted(K):
    c = Counter({1: (K+1)//2, 2: K//2})
    for m in range(2, K):
        c[gap_bridge(m)] += fibonacci(K-m+2)-1
    return +c

def recursive_groups(max_m):
    v = [[], [1]]
    v[0] = [0]
    for m in range(2, max_m+1):
        v.append(v[m-2] + [2**(m-1)+x for x in v[m-1]])
        assert all(v[m][i] < v[m][i+1] for i in range(len(v[m])-1))
        assert len(v[m]) == fibonacci(m+1)
        assert v[m][0] == (m%2)
        assert v[m][-1] == (2**m - 1)
        assert v[m][len(v[m-2])] - v[m][len(v[m-2])-1] == gap_bridge(m)
    return v

v = recursive_groups(16)
for K in range(1, 16):
    actual = [n for n in range(1<<K) if is_baum_sweet(n)]
    direct = [0] + [2**(L-1) + x for L in range(1,K+1) for x in v[L-1]]
    assert direct == actual, ('language', K)
    assert len(actual) == fibonacci(K+2)
    counts = Counter(b-a for a,b in zip(actual, actual[1:]))
    assert counts == predicted(K), (K, counts, predicted(K))
    assert sum(counts.values()) == fibonacci(K+2)-1
    print(f'K={K:02d} support={len(actual):5d} gap_classes={len(counts):2d} counts={dict(sorted(counts.items()))}')
phi = (1+sqrt(5))/2
N = 1 << 19
actual = [n for n in range(N) if is_baum_sweet(n)]
c = Counter(b-a for a,b in zip(actual,actual[1:]))
for m in range(4, 13):
    target = phi**(-m)
    observed = c[gap_bridge(m)]/(len(actual)-1)
    assert abs(observed-target) < .02
print('VERIFY_OK independent_integer_predicate_vs_token_recursion K=1..15')
print('VERIFY_OK exact_histogram_recurrence_and_boundary_gaps K=1..15')
print('VERIFY_OK dyadic_fibonacci_limit_samples K=19, bridge_m=4..12')
