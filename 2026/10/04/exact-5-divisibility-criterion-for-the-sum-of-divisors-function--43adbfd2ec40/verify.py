#!/usr/bin/env python3
from math import isqrt

LIMIT = 200000

def factorint(n):
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def v5(n):
    c = 0
    while n % 5 == 0:
        c += 1
        n //= 5
    return c

def sigma_from_factorization(f):
    ans = 1
    for p, a in f.items():
        ans *= (p ** (a + 1) - 1) // (p - 1)
    return ans

def local_v5(p, a):
    if p == 5:
        return 0
    r = p % 5
    if r == 1:
        return v5(a + 1)
    if r == 4:
        if a % 2 == 0:
            return 0
        return v5(a + 1) + v5(p + 1)
    if r in (2, 3):
        if a % 4 != 3:
            return 0
        return v5(a + 1) + v5(p * p + 1)
    raise AssertionError((p, a))

def predicted_v5(n):
    return sum(local_v5(p, a) for p, a in factorint(n).items())

def main():
    first = []
    exact_one_count = 0
    for n in range(1, LIMIT + 1):
        f = factorint(n)
        sigma = sigma_from_factorization(f)
        direct = v5(sigma)
        predicted = sum(local_v5(p, a) for p, a in f.items())
        assert direct == predicted, (n, f, sigma, direct, predicted)
        if n < 100 and direct > 0:
            first.append(n)
        if direct == 1:
            exact_one_count += 1

    expected = [8, 19, 24, 27, 29, 38, 40, 54, 56, 57, 58, 59,
                72, 76, 79, 87, 88, 89, 95]
    assert first == expected, (first, expected)

    # Mod-25 roots used in the exact level-one refinement.
    roots = [x for x in range(25) if (x * x + 1) % 25 == 0]
    assert roots == [7, 18]

    print("VERIFY_OK")
    print("checked_n_max=" + str(LIMIT))
    print("initial_mod5_divisibility_list_matches_source=true")
    print("roots_x2_plus_1_mod25=7,18")
    print("exact_level_one_count_through_limit=" + str(exact_one_count))

if __name__ == "__main__":
    main()
