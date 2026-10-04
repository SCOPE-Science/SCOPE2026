from itertools import combinations_with_replacement
from math import prod, comb

def v2(n):
    assert n > 0
    r = 0
    while n % 2 == 0:
        r += 1
        n //= 2
    return r

def h_complete(xs, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for x in xs:
        nd = [0] * (n + 1)
        for j in range(n + 1):
            if dp[j] == 0:
                continue
            p = 1
            for q in range(n - j + 1):
                nd[j + q] += dp[j] * p
                p *= x
        dp = nd
    return dp[n]

def dual_degree(ds, n):
    return prod(ds) * h_complete([d - 1 for d in ds], n)

checks = 0
for c in range(1, 6):
    for n in range(1, 7):
        for ds in combinations_with_replacement(range(2, 11), c):
            delta = dual_degree(ds, n)
            e = sum(d % 2 == 0 for d in ds)
            assert delta % 2 == 0

            if e > 0:
                A = sum(v2(d) for d in ds)
                exact = (n & (e - 1)) == 0
                assert (v2(delta) == A) == exact
                if not exact:
                    assert v2(delta) >= A + 1
            else:
                f = sum(d % 4 == 3 for d in ds)
                exact = f > 0 and ((n & (f - 1)) == 0)
                assert (v2(delta) == n) == exact
                if not exact:
                    assert v2(delta) >= n + 1

            if n >= 2:
                predicted_mod4_two = (
                    sum(d % 2 == 0 for d in ds) == 1
                    and any(d % 4 == 2 for d in ds)
                )
                assert (delta % 4 == 2) == predicted_mod4_two
            else:
                case1 = (
                    sum(d % 2 == 0 for d in ds) == 1
                    and any(d % 4 == 2 for d in ds)
                )
                case2 = (
                    all(d % 2 == 1 for d in ds)
                    and sum(d % 4 == 3 for d in ds) % 2 == 1
                )
                assert (delta % 4 == 2) == (case1 or case2)

            checks += 1

binomial_checks = 0
for n in range(1, 128):
    for r in range(1, 128):
        assert (comb(n + r - 1, n) & 1) == int((n & (r - 1)) == 0)
        binomial_checks += 1

assert dual_degree((2, 3, 3), 2) == 306
assert dual_degree((3, 3), 2) == 108

print("VERIFY_OK", checks, binomial_checks)
