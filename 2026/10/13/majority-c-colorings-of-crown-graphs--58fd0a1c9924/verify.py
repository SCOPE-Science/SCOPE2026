#!/usr/bin/env python3
from itertools import product
from math import comb


def majority_ok(assign, n, k):
    # Vertices are a_0,...,a_{n-1}, b_0,...,b_{n-1}; a_i b_i is deleted.
    if set(assign) != set(range(k)):
        return False
    h = n // 2  # ceil((n-1)/2)
    for i in range(n):
        c = assign[i]
        same = sum(assign[n+j] == c for j in range(n) if j != i)
        if same < h:
            return False
    for j in range(n):
        c = assign[n+j]
        same = sum(assign[i] == c for i in range(n) if i != j)
        if same < h:
            return False
    return True


def expected_two_count(n):
    if n % 2 == 0:
        return comb(n, n // 2)
    r = (n - 1) // 2
    return 2 * comb(n, r) * (r + 2)


def structural_two(assign, n):
    S = {i for i in range(n) if assign[i] == 0}
    T = {i for i in range(n) if assign[n+i] == 0}
    a, b, c = len(S), len(T), len(S & T)
    if n % 2 == 0:
        r = n // 2
        return (a, b, c) == (r, r, 0) and T == set(range(n)) - S
    r = (n - 1) // 2
    allowed = {(r, r, 0), (r, r+1, 0), (r+1, r, 0), (r+1, r+1, 1)}
    return (a, b, c) in allowed


def construction(n):
    if n % 2 == 0:
        r = n // 2
        S = set(range(r))
        T = set(range(r, n))
    else:
        r = (n - 1) // 2
        S = set(range(r))
        T = set(range(r, n))
    a = [0 if i in S else 1 for i in range(n)]
    b = [0 if i in T else 1 for i in range(n)]
    return tuple(a + b)


def main():
    assignment_checks = 0
    count_cases = []
    for n in range(2, 10):
        valid = 0
        for bits in product(range(2), repeat=2*n):
            assignment_checks += 1
            ok = majority_ok(bits, n, 2)
            if ok:
                valid += 1
                assert structural_two(bits, n), (n, bits)
        exp = expected_two_count(n)
        assert valid == exp, (n, valid, exp)
        count_cases.append((n, valid))

    # Direct three-color exhaustions at the only small orders where a third color
    # is not ruled out merely by the universal color-class size bound.
    three = {}
    for n in range(2, 6):
        v = 0
        for a in product(range(3), repeat=2*n):
            if majority_ok(a, n, 3):
                v += 1
        three[n] = v
    assert three == {2: 0, 3: 12, 4: 0, 5: 0}, three

    # Formula constructions over a much larger parameter range.
    for n in range(2, 201):
        w = construction(n)
        assert majority_ok(w, n, 2), n
        h = n // 2
        bound = (2*n) // (2*h)
        if n >= 6:
            assert bound == 2, (n, bound)

    print(
        "ALL CHECKS PASSED; "
        f"two_color_assignment_checks={assignment_checks}; "
        f"two_color_counts={count_cases}; "
        f"three_color_small_counts={three}; "
        "construction_range=2..200; exact_claim_range=n>=6"
    )


if __name__ == '__main__':
    main()
