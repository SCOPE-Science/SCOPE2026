#!/usr/bin/env python3
from math import isqrt

A_MAX = 9
P_MAX = 300

def is_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True

def direct_two_layered_test(a, p):
    h = 1 << a
    n = h * p * p
    sigma = (2 * h - 1) * (p * p + p + 1)
    target = (sigma - 1) // 2 - n
    if target < 0:
        return False

    proper = []
    for i in range(a + 1):
        two = 1 << i
        for j in range(3):
            d = two * (p ** j)
            if d != 1 and d != n and d <= target:
                proper.append(d)

    # Exact subset-sum test for Behzadipour's criterion, truncated at target.
    bits = 1
    mask = (1 << (target + 1)) - 1
    for d in proper:
        bits |= bits << d
        bits &= mask
    return bool((bits >> target) & 1)

def main():
    cases = 0
    violations = []
    boundary_true = []
    for a in range(1, A_MAX + 1):
        h = 1 << a
        for p in range(3, P_MAX + 1, 2):
            if not is_prime(p):
                continue
            cases += 1
            got = direct_two_layered_test(a, p)
            expected = p < h
            if got != expected:
                violations.append((a, p, got, expected))
            if got and p == max([q for q in range(3, h, 2) if is_prime(q)], default=-1):
                boundary_true.append((a, p))
    assert not violations, violations[:10]
    print('VERIFY_OK')
    print('cases=' + str(cases))
    print('a_max=' + str(A_MAX))
    print('p_max=' + str(P_MAX))
    print('violations=0')
    print('largest_true_prime_by_layer=' + repr(boundary_true))

if __name__ == '__main__':
    main()
