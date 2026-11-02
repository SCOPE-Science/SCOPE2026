"""Exact finite checks for blockwise records in uniform random compositions."""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial


def H(n, power=1):
    return sum((Fraction(1, j**power) for j in range(1, n+1)), Fraction(0))


def compositions(n, k):
    if k == 1:
        yield (n,)
        return
    for first in range(1, n-k+2):
        for rest in compositions(n-first, k-1):
            yield (first,) + rest


def formula(n, k):
    assert n >= k >= 2
    d = n-k+1
    delta = H(n)-H(k-1)
    second = H(n+1, 2)-H(k-1, 2)
    mean = Fraction(n, d)*delta
    cross = Fraction(n*(n+1), d*(d+1))*((delta+Fraction(1,n+1))**2-second)
    marginal_second = H(n, 2)-H(k-1, 2)
    variance = Fraction(n, d)*(delta-marginal_second-Fraction(k-1, d)*delta**2)
    return mean, variance, cross-mean**2


def records(seq):
    largest = -1
    count = 0
    for value in seq:
        if value > largest:
            count += 1
            largest = value
    return count


def exact_composition_comparison():
    checks = 0
    for n in range(2, 15):
        for k in range(2, n+1):
            parts = list(compositions(n, k))
            assert len(parts) == comb(n-1, k-1)
            e1 = sum((H(part[0]) for part in parts), Fraction(0))/len(parts)
            e2 = sum((H(part[0])*H(part[1]) for part in parts), Fraction(0))/len(parts)
            expected_mean, expected_var, expected_cov = formula(n, k)
            e_var = sum((H(part[0])**2+H(part[0])-H(part[0],2) for part in parts), Fraction(0))/len(parts) - e1**2
            assert e_var == expected_var, ('variance', n, k)
            assert e1 == expected_mean, ('mean', n, k)
            assert e2-e1**2 == expected_cov, ('cov', n, k)
            assert (expected_cov == 0 if n == k else expected_cov < 0)
            checks += 4
    return checks


def exact_label_comparison():
    checks = 0
    microstates = 0
    for n in range(3, 8):
        perms = tuple(permutations(range(n)))
        for k in range(2, min(n, 5)+1):
            count = 0
            first = second = cross = squares = 0
            for part in compositions(n, k):
                a,b=part[0],part[1]
                # Each order is equally likely for independent continuous labels.
                for perm in perms:
                    r1=records(perm[:a])
                    r2=records(perm[a:a+b])
                    first += r1
                    second += r2
                    cross += r1*r2
                    squares += r1*r1
                    count += 1
            assert count == factorial(n)*comb(n-1, k-1)
            mean, variance, covariance = formula(n,k)
            assert Fraction(first,count) == mean
            assert Fraction(second,count) == mean
            assert Fraction(cross,count) - Fraction(first*second,count*count) == covariance
            assert Fraction(squares,count) - Fraction(first*first,count*count) == variance
            checks += 4
            microstates += count
    return checks,microstates


def main():
    count=exact_composition_comparison()
    extra,micro=exact_label_comparison()
    print(f'PASS: {count+extra} independent exact identities/sign assertions')
    print(f'PASS: {micro} explicitly enumerated (composition, label order) microstates')
    print('These finite tests do not establish the asymptotic or all-order theorems.')


if __name__ == '__main__':
    main()
