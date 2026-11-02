"""Exact enumerative and algebraic checks for recursive-tree leaf/path-length dependence."""
from fractions import Fraction as Q
from itertools import product
from math import factorial, log


def H(m):
    return sum((Q(1, j) for j in range(1, m+1)), Q(0))


def expected_formula(n, i):
    return Q(i-1, n-1)*(H(n-1)-H(i-1))


def test_enumeration(n):
    total = factorial(n-1)
    sum_t = sum_leaves = sum_lt = 0
    sum_leaf = [0]*(n+1)
    sum_i_t = [0]*(n+1)
    seen = 0
    for tup in product(*(range(1, j) for j in range(2, n+1))):
        seen += 1
        depth = [0]*(n+1)
        child_count = [0]*(n+1)
        for j, parent in enumerate(tup, 2):
            depth[j] = depth[parent]+1
            child_count[parent] += 1
        t = sum(depth)
        leaves = [i for i in range(2, n+1) if child_count[i] == 0]
        ell = len(leaves)
        sum_t += t
        sum_leaves += ell
        sum_lt += ell*t
        for i in leaves:
            sum_leaf[i] += 1
            sum_i_t[i] += t
    assert seen == total
    expected_t = Q(sum_t,total)
    assert expected_t == n*(H(n)-1), (n,'mean depth', expected_t)
    assert Q(sum_leaves,total) == Q(n,2)
    assert Q(sum_lt,total)-Q(sum_leaves,total)*expected_t == -Q(n-2,4)
    tests = 4
    for i in range(2,n+1):
        pi = Q(sum_leaf[i],total)
        assert pi == Q(i-1,n-1), (n, i, 'leaf mass',pi)
        mean_leaf = Q(sum_i_t[i],sum_leaf[i])
        assert mean_leaf-expected_t == -(H(n-1)-H(i-1)), (n,i,'conditional',mean_leaf-expected_t)
        assert Q(sum_i_t[i],total)-pi*expected_t == -expected_formula(n,i), (n,i,'covariance')
        tests += 3
    return seen,tests


def main():
    checked = enumerated = 0
    for n in range(2,10):
        seen, tests = test_enumeration(n)
        checked += tests
        enumerated += seen
    for n in range(2,201):
        profile = [expected_formula(n,i) for i in range(2,n+1)]
        assert sum(profile) == Q(n-2,4)
        checked += 1
        for i in range(2,n):
            assert profile[i-1]-profile[i-2] == (H(n-1)-H(i-1)-1)/Q(n-1)
            checked += 1
    for n in [10**3, 10**4]:
        # Use floating harmonic sums for asymptotic sanity only.
        harm = [0.0]
        for j in range(1,n):
            harm.append(harm[-1]+1/j)
        imax = max(range(2,n+1),key=lambda i:(i-1)/(n-1)*(harm[-1]-harm[i-1]))
        assert abs(imax/n-1/2.718281828459045) < .005
        checked += 1
    print(f'PASS: {checked} exact-algebra/enumeration assertions; {enumerated} recursively labeled trees enumerated; asymptotic location checked numerically twice')


if __name__=='__main__':
    main()
