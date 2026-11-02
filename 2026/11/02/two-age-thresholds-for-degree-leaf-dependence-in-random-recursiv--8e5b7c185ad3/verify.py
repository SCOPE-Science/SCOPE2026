"""Exact finite checks for the birth-label covariance law in uniform recursive trees.

Run with Python 3: python verify.py. No third-party packages.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import factorial, log


def harmonic(m):
    return sum((Fraction(1, k) for k in range(1, m + 1)), Fraction(0))


def predicted(n, v):
    if v == 1:
        return Fraction(n - 2, 2 * (n - 1))
    if v == n:
        return Fraction(0)
    return (Fraction(n - v, 2 * (n - 1))
            - Fraction(v - 1, n - 1) * (harmonic(n - 2) - harmonic(v - 2)))


def predicted_local(n, v, j):
    return Fraction(j - 2 * v, 2 * (n - 1) * (j - 2))


def exhaustive(n):
    count = factorial(n - 1)
    total_l = 0
    degree = [0] * (n + 1)
    d_l = [0] * (n + 1)
    attach_count = defaultdict(int)
    attach_l = defaultdict(int)
    for parents in product(*(range(1, j) for j in range(2, n + 1))):
        counts = [0] * (n + 1)
        for p in parents:
            counts[p] += 1
        leaves = sum(counts[i] == 0 for i in range(2, n + 1))
        total_l += leaves
        for v in range(1, n + 1):
            degree[v] += counts[v]
            d_l[v] += counts[v] * leaves
        for j in range(3, n + 1):
            v = parents[j - 2]
            attach_count[v, j] += 1
            attach_l[v, j] += leaves
    assert total_l == Fraction(n, 2) * count
    assertions = 1
    for v in range(1, n + 1):
        value = Fraction(d_l[v], count) - Fraction(degree[v] * total_l, count * count)
        assert value == predicted(n, v), (n, v, value, predicted(n, v))
        assertions += 1
        for j in range(max(3, v+1), n+1):
            val = (Fraction(attach_l[v, j], count)
                   - Fraction(attach_count[v, j]*total_l, count*count))
            assert val == predicted_local(n, v, j), (n,v,j,val,predicted_local(n,v,j))
            assertions += 1
    return assertions


def main():
    tests = 0
    for n in range(3, 10):
        k = exhaustive(n)
        tests += k
        print(f'n={n}: exhaustive {(n-1)}!={factorial(n-1)} trees, {k} covariance identities')
    for n in range(3, 201):
        values = [predicted(n,v) for v in range(2,n)]
        signs = [1 if x > 0 else -1 if x < 0 else 0 for x in values]
        if n <= 6:
            assert all(s < 0 for s in signs)
        else:
            assert signs[0] > 0 and signs[-1] < 0
            assert not any(signs[i] < signs[j] for i in range(len(signs)) for j in range(i+1,len(signs)))
        tests += 1
    a = 0.2846681370409073
    assert abs((1-a)/2 + a*log(a)) < 1e-13
    for n in (100, 1000, 10000):
        for alpha in (0.1,0.2,0.4,0.6,0.8):
            v=max(2,min(n-1,int(alpha*n)))
            exact=float(predicted(n,v))
            target=(1-alpha)/2+alpha*log(alpha)
            assert abs(exact-target)<0.05
            tests+=1
    print(f'PASSED {tests} exact/numerical grouped checks')

if __name__=='__main__':
    main()
