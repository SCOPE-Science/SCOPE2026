"""Finite checks for normalized partition-polynomial integral limit law.

Run with Python 3.11 or newer. This tests exact finite identities and
Laplace-transform arithmetic, not the infinite weak-convergence proof.
"""
from functools import lru_cache
from itertools import product
from math import gamma, pi, sqrt

@lru_cache(None)
def partitions(n, cap):
    if n == 0:
        return ((),)
    if cap == 0 or n < 0:
        return ()
    result = []
    for k in range(min(n, cap), 0, -1):
        for rest in partitions(n - k, k):
            result.append((k,) + rest)
    return tuple(result)

def partition_numbers(N):
    p = [0] * (N + 1)
    p[0] = 1
    for n in range(1, N + 1):
        s, k = 0, 1
        while True:
            a, b = k * (3*k-1)//2, k * (3*k+1)//2
            if a > n:
                break
            sign = 1 if k & 1 else -1
            s += sign * p[n-a]
            if b <= n:
                s += sign * p[n-b]
            k += 1
        p[n] = s
    return p

def run():
    p = partition_numbers(1200)
    finite_tests = 0
    for n in range(0, 19):
        all_parts = partitions(n, n)
        assert len(all_parts) == p[n]
        for r1, r2, r3 in product(range(3), repeat=3):
            s = r1 + 2*r2 + 3*r3
            count = sum((l.count(1) >= r1 and l.count(2) >= r2 and l.count(3) >= r3) for l in all_parts)
            assert count == (p[n-s] if s <= n else 0), (n,r1,r2,r3)
            finite_tests += 1
        # Check direct partwise integral numerator against a marked-part identity.
        direct = sum(sum(1.0/(j+1) for j in l) for l in all_parts)
        marked = sum(sum(p[n-j*r] for r in range(1, n//j + 1))/(j+1) for j in range(1, n+1))
        assert abs(direct-marked) < 1e-8 * max(1, abs(direct))
    for n in (100, 300, 600, 1200):
        mean_A = sum(sum(p[n-j*r] / p[n] for r in range(1,n//j+1))/(j+1) for j in range(1,n+1))/sqrt(n)
        print('n=%d, E[weighted-part sum/sqrt(n)]=%.9f, limit=%.9f' % (n, mean_A, sqrt(6)/pi))
        assert 0 < mean_A < 2
    laplace_tests = 0
    for t in (0.0, 0.015, 0.09, 0.12):
        alpha=(1+sqrt(1-8*t))/2
        beta=(1-sqrt(1-8*t))/2
        exact=gamma(1+alpha)*gamma(1+beta)
        product_value=1.0
        for j in range(1,5001):
            product_value*=j*(j+1)/(j*(j+1)+2*t)
        assert abs(exact-product_value)<2e-4, (t,exact,product_value)
        laplace_tests+=1
    assert abs(sum(1/(j*(j+1)) for j in range(1,100000))- (1-1/100000)) < 2e-12
    print('PASS: %d exact joint-tail identities; 19 marked-part identities; %d gamma/product checks.' % (finite_tests,laplace_tests))
    print('The normalizing denominator uses the classical Erdos-Lehner theorem.')

if __name__=='__main__':
    run()
