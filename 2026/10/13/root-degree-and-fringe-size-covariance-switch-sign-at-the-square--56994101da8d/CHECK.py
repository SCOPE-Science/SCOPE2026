"""Standalone finite checks for root-degree/fringe-size covariance in random recursive trees.

Run with Python 3 using no third-party packages. These finite checks complement,
but do not replace, the all-size proof in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import factorial, sqrt


def harmonic(q):
    return sum((Fraction(1, j) for j in range(1, q + 1)), Fraction(0))


def probability(n, v, k):
    if not 1 <= k <= n - 1 or not 2 <= v <= n-k+1:
        return Fraction(0)
    return Fraction((v-1) * factorial(n-k-1) * factorial(n-v),
                    factorial(n-1) * factorial(n-v-k+1))


def covariance(n, k):
    return Fraction(1, k) * (
        1 - Fraction(n, k + 1) *
        sum((Fraction(1, n-j) for j in range(1, k+1)), Fraction(0)))


def enumerate_recursive_trees(n):
    for parents in product(*(range(1, v) for v in range(2, n+1))):
        children = [[] for _ in range(n+1)]
        for v, p in enumerate(parents, 2):
            children[p].append(v)
        sizes = [0] * (n+1)
        for v in range(n, 0, -1):
            sizes[v] = 1 + sum(sizes[w] for w in children[v])
        yield len(children[1]), sizes


def exact_enumeration():
    num_trees = 0
    tests = 0
    for n in range(2, 10):
        total = factorial(n-1)
        counts = {(v,k): 0 for v in range(2,n+1) for k in range(1,n)}
        degrees = {(v,k): 0 for v in range(2,n+1) for k in range(1,n)}
        profile = {k:[0,0] for k in range(1,n)}
        root_degrees = 0
        seen = 0
        for d,sizes in enumerate_recursive_trees(n):
            seen += 1
            root_degrees += d
            for v in range(2,n+1):
                k = sizes[v]
                counts[v,k] += 1
                degrees[v,k] += d
                profile[k][0] += 1
                profile[k][1] += d
        assert seen == total
        num_trees += seen
        assert Fraction(root_degrees, total) == harmonic(n-1)
        tests += 1
        for k in range(1,n):
            a,b = profile[k]
            assert Fraction(a,total) == Fraction(n,k*(k+1))
            assert Fraction(b,total) - harmonic(n-1)*Fraction(a,total) == covariance(n,k)
            tests += 2
            for v in range(2,n+1):
                cnt = counts[v,k]
                assert Fraction(cnt,total) == probability(n,v,k)
                tests += 1
                if cnt:
                    assert Fraction(degrees[v,k],cnt) == harmonic(n-k-1)+Fraction(1,v-1)
                    tests += 1
        assert sum((covariance(n,k) for k in range(1,n)), Fraction(0)) == 0
        tests += 1
    return num_trees, tests


def algebra_and_threshold_checks():
    tests = 0
    for n in range(3,501):
        H = Fraction(0)
        prev = Fraction(0)
        first = None
        for k in range(1,n):
            H += Fraction(1,n-k)
            h = Fraction(n,k+1)*H
            assert h > prev, (n,k)
            prev = h
            cov = covariance(n,k)
            assert (cov > 0) == (h < 1)
            assert (cov < 0) == (h > 1)
            if first is None and h >= 1:
                first = k
            tests += 3
        assert first is not None
        assert first == 1 or covariance(n,first-1) > 0
        assert covariance(n,first) <= 0
        assert covariance(n,n-1) < 0
        tests += 4
    return tests


def main():
    trees, test1 = exact_enumeration()
    test2 = algebra_and_threshold_checks()
    print('Exact labelled recursive trees enumerated:', trees)
    print('Exact enumeration identities:', test1)
    print('Additional exact threshold identities:', test2)
    for n in (1000,10000,100000):
        harmonic_tail = 0.0
        kstar = None
        for k in range(1,n):
            harmonic_tail += 1/(n-k)
            if n*harmonic_tail/(k+1) >= 1:
                kstar=k
                break
        print('n=',n,'first nonpositive rank=',kstar,
              'rank/sqrt(n)=',round(kstar/sqrt(n),9))
    print('CHECK_OK')


if __name__ == '__main__':
    main()
