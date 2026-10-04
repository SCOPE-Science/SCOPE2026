#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations

PRIMES = [3, 5, 7, 11, 13, 17, 19]

def equal_partition(values):
    total = sum(values)
    if total & 1:
        return False
    target = total // 2
    m = len(values)
    for mask in range(1 << m):
        s = 0
        for i, v in enumerate(values):
            if mask >> i & 1:
                s += v
        if s == target:
            return True
    return False

def unitary_divisors(alpha, p, beta, q, gamma):
    A, B, C = 2**alpha, p**beta, q**gamma
    return sorted([1, A, B, C, A*B, A*C, B*C, A*B*C])

def predicted(alpha, p, beta, q, gamma):
    if alpha == 1 and p == 3 and beta == 1:
        return True
    if (alpha, p, beta, q, gamma) == (2, 3, 1, 5, 1):
        return True
    if (alpha, p, beta, q, gamma) == (1, 5, 1, 7, 1):
        return True
    if (alpha, p, beta, q, gamma) == (1, 3, 2, 5, 1):
        return True
    return False

def check_partitions():
    for q in (5, 7, 11, 19):
        for c in (1, 2, 4):
            Q = q**c
            full_left = [6, 6*Q]
            full_right = [1, 2, 3, Q, 2*Q, 3*Q]
            assert sum(full_left) == sum(full_right)
            half_left = [6, 3*Q]
            half_right = [1, 2, 3, Q, 2*Q]
            assert sum(half_left) == sum(half_right)

    assert sum([60]) == sum([1,3,4,5,12,15,20])
    assert sum([2,70]) == sum([1,5,7,10,14,35])
    assert sum([90]) == sum([1,2,5,9,10,18,45])

    assert sum([1,4,5,20]) == sum([3,12,15])
    assert sum([2,35]) == sum([1,5,7,10,14])
    assert sum([45]) == sum([1,2,5,9,10,18])

def check_inequalities():
    assert Fraction(3,2)*Fraction(8,7)*Fraction(12,11) < 2
    assert Fraction(3,2)*Fraction(6,5)*Fraction(12,11) < 2
    assert Fraction(5,4)*Fraction(6,5)*Fraction(8,7) < 2
    assert Fraction(3,2)*Fraction(26,25)*Fraction(8,7) < 2
    assert Fraction(3,2)*Fraction(6,5)*Fraction(50,49) < 2
    assert Fraction(5,4)*Fraction(10,9)*Fraction(6,5) < 2
    assert Fraction(9,8)*Fraction(4,3)*Fraction(6,5) < 2
    assert Fraction(3,2)*Fraction(28,27)*Fraction(6,5) < 2

def check_grid():
    checked = 0
    for p, q in combinations(PRIMES, 2):
        for alpha in range(1, 5):
            for beta in range(1, 5):
                for gamma in range(1, 5):
                    ds = unitary_divisors(alpha, p, beta, q, gamma)
                    actual = equal_partition(ds)
                    expect = predicted(alpha, p, beta, q, gamma)
                    assert actual == expect, (alpha, p, beta, q, gamma, ds, actual, expect)
                    if expect:
                        n = max(ds)
                        proper = [d for d in ds if d != n]
                        assert equal_partition(proper), (alpha, p, beta, q, gamma, proper)
                    checked += 1
    return checked

def main():
    check_inequalities()
    check_partitions()
    checked = check_grid()
    print("VERIFY_OK")
    print("grid_cases=" + str(checked))
    print("prime_pairs=" + str(len(list(combinations(PRIMES, 2)))))
    print("exponents=1..4")

if __name__ == "__main__":
    main()
