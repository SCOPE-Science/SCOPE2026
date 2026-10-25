"""Exact checks for endpoint distance-two occupation in hard-core chains.

Python 3 standard library only. Finite checks supplement the general counting proof.
"""
from fractions import Fraction
from math import comb


def subsets(n, k):
    def dfs(start, need, chosen):
        if not need:
            yield tuple(chosen)
            return
        for i in range(start, n + 1):
            if n - i + 1 < 2 * need - 1:
                break
            chosen.append(i)
            yield from dfs(i + 2, need - 1, chosen)
            chosen.pop()
    yield from dfs(1, k, [])


def cov_formula(n, k):
    N = n - k + 1
    return Fraction(k * (N - k) * (k*k + 1 - n),
                    N*N*(N - 1)*(N - 2))


def direct_cov(S):
    total = len(S)
    a = sum(1 in s for s in S)
    b = sum(3 in s for s in S)
    ab = sum((1 in s) and (3 in s) for s in S)
    return Fraction(ab, total) - Fraction(a*b, total*total)


def cycle_formula(n, k):
    return Fraction(k * (k * (k + 1) - n), n * n * (n-k-1))


def cycle_subsets(n,k):
    for s in subsets(n,k):
        if not (1 in s and n in s):
            yield s


def test():
    assertions = 0
    count = 0
    for n in range(4, 22):
        for k in range(1, (n+1)//2 + 1):
            S = list(subsets(n,k))
            assert len(S) == comb(n-k+1,k)
            assertions += 1
            count += len(S)
            observed = direct_cov(S)
            desired = cov_formula(n,k)
            assert observed == desired, (n,k,observed,desired)
            assertions += 1
            assert (observed == 0) == (n == 2*k - 1 or n == k*k + 1)
            assertions += 1
    for n in range(5, 22):
        for k in range(1, n//2 + 1):
            S = list(cycle_subsets(n,k))
            assert len(S) * (n-k) == n * comb(n-k,k)
            assertions += 1
            count += len(S)
            observed = direct_cov(S)
            desired = cycle_formula(n,k)
            assert observed == desired, (n,k,observed,desired)
            assertions += 1
            assert (observed == 0) == (n == k*(k+1))
            assertions += 1
    for k in range(2,100):
        n = k*(k+1)
        assert cycle_formula(n,k) == 0
        assert cycle_formula(n-1,k) > 0
        assert cycle_formula(n+1,k) < 0
        assertions += 3
    for k in range(2,100):
        n = k*k+1
        assert cov_formula(n,k) == 0
        assert cov_formula(n-1,k) > 0
        assert cov_formula(n+1,k) < 0
        assertions += 3
    for n in range(4,16):
        all_sets = [s for k in range((n+1)//2+1) for s in subsets(n,k)]
        for activity in [Fraction(1,7),Fraction(1,2),Fraction(1),Fraction(7)]:
            Z = sum((activity**len(s) for s in all_sets),Fraction(0))
            aa = sum((activity**len(s) for s in all_sets if 1 in s),Fraction(0))
            bb = sum((activity**len(s) for s in all_sets if 3 in s),Fraction(0))
            ab = sum((activity**len(s) for s in all_sets if 1 in s and 3 in s),Fraction(0))
            p2 = sum((activity**len(s) for s in all_sets if 2 in s),Fraction(0))/Z
            r = 1-p2
            a = activity/(1+activity)
            b = sum((activity**len(s) for s in all_sets if 3 in s and 2 not in s),Fraction(0))/(r*Z)
            cv = ab/Z-aa*bb/(Z*Z)
            assert cv == r*(1-r)*a*b > 0, (n,activity)
            assertions += 1
    print(f'VERIFY_OK {assertions} exact assertions; {count} canonical samples; grand-canonical positives')

if __name__ == '__main__':
    test()
