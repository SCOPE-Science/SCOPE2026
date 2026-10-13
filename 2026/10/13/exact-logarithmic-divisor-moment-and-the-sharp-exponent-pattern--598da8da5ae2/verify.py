#!/usr/bin/env python3
import math
from collections import Counter


def factorint(n):
    out = Counter()
    x = n
    p = 2
    while p*p <= x:
        while x % p == 0:
            out[p] += 1
            x //= p
        p = 3 if p == 2 else p + 2
    if x > 1:
        out[x] += 1
    return dict(out)


def divisors_from_factorization(f):
    ds = [1]
    for p, a in f.items():
        ds = [d * (p ** e) for d in ds for e in range(a + 1)]
    return ds


def tau_from_factorization(f):
    t = 1
    for a in f.values():
        t *= a + 1
    return t

max_n = 20000
formula_checks = 0
bound_checks = 0
prime_power_equalities = 0
multi_support_strict_checks = 0
max_abs_error = 0.0
min_strict_margin = float('inf')

for n in range(2, max_n + 1):
    f = factorint(n)
    ds = divisors_from_factorization(f)
    tau = tau_from_factorization(f)
    lhs = sum(math.log(d) ** 2 for d in ds)
    logn = math.log(n)
    q = sum(a * (a + 2) * (math.log(p) ** 2) for p, a in f.items())
    rhs = tau * (logn * logn / 4.0 + q / 12.0)
    err = abs(lhs - rhs)
    max_abs_error = max(max_abs_error, err)
    if err > 2e-10 * max(1.0, abs(lhs)):
        raise AssertionError(("exact_formula", n, lhs, rhs, err))
    formula_checks += 1

    B = sum(a / (a + 2.0) for a in f.values())
    C = 0.25 + 1.0 / (12.0 * B)
    lower = C * tau * logn * logn
    margin = lhs - lower
    if margin < -2e-10 * max(1.0, abs(lhs)):
        raise AssertionError(("pattern_bound", n, lhs, lower, margin))
    bound_checks += 1
    if len(f) == 1:
        if abs(margin) > 2e-10 * max(1.0, abs(lhs)):
            raise AssertionError(("prime_power_equality", n, margin))
        prime_power_equalities += 1
    else:
        if margin <= 0:
            raise AssertionError(("multi_support_strictness", n, margin))
        min_strict_margin = min(min_strict_margin, margin)
        multi_support_strict_checks += 1

# Exact squarefree pattern constant check at the coefficient level.
for r in range(1, 9):
    B = r / 3.0
    C = 0.25 + 1.0 / (12.0 * B)
    expected = (r + 1.0) / (4.0 * r)
    if abs(C - expected) > 1e-15:
        raise AssertionError(("squarefree_constant", r, C, expected))

print("VERIFY_OK")
print(f"n_max={max_n}")
print(f"formula_checks={formula_checks}")
print(f"bound_checks={bound_checks}")
print(f"prime_power_equalities={prime_power_equalities}")
print(f"multi_support_strict_checks={multi_support_strict_checks}")
print(f"squarefree_patterns_checked=8")
print(f"max_abs_formula_error={max_abs_error:.3e}")
print(f"min_positive_strict_margin={min_strict_margin:.6e}")
