#!/usr/bin/env python3
from math import comb, gcd
from fractions import Fraction

def lcm(a, b):
    return a // gcd(a, b) * b

def primes_upto(n):
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    out = []
    for p in range(2, n + 1):
        if sieve[p]:
            out.append(p)
            if p * p <= n:
                sieve[p*p:n+1:p] = [False] * (((n - p*p) // p) + 1)
    return out

def vp(x, p):
    e = 0
    while x and x % p == 0:
        x //= p
        e += 1
    return e

def fixed_row_opt(r, n, max_index=None):
    m = r // 2
    if max_index is not None:
        m = min(m, max_index)
    d = m + 1
    if d < n:
        return None
    coeff = [comb(r, k) for k in range(d)]
    full = 1
    for x in coeff:
        full = lcm(full, x)
    omit_budget = d - n

    dp = {0: 1}
    for p in primes_upto(r):
        vals = [vp(x, p) for x in coeff]
        E = max(vals)
        if E == 0:
            continue
        options = {}
        for e in range(E + 1):
            mask = 0
            for i, v in enumerate(vals):
                if v > e:
                    mask |= 1 << i
            if mask.bit_count() <= omit_budget:
                saving = p ** (E - e)
                if saving > options.get(mask, 0):
                    options[mask] = saving
        new = {}
        for oldmask, oldsave in dp.items():
            for mask, save in options.items():
                union = oldmask | mask
                if union.bit_count() <= omit_budget:
                    total = oldsave * save
                    if total > new.get(union, 0):
                        new[union] = total
        dp = new

    maxsaving = max(dp.values())
    min_defect = None
    min_mask = None
    for mask, saving in dp.items():
        if saving != maxsaving:
            continue
        survivors = [i for i in range(d) if ((mask >> i) & 1) == 0]
        if len(survivors) >= n:
            defect = 1 + survivors[n - 1] - n
            if min_defect is None or defect < min_defect:
                min_defect = defect
                min_mask = mask
    return full // maxsaving, min_defect, maxsaving, min_mask, full

def standard_upper(n):
    z = 1
    for k in range(1, 2*n):
        z = lcm(z, k)
    return z // (2*n - 1)

def cutoff(n, upper):
    r = 2*n - 2
    while comb(r, n - 1) <= upper:
        r += 1
    return r

def global_opt(n):
    upper = standard_upper(n)
    R = cutoff(n, upper)
    best = None
    for r in range(2*n - 2, R):
        z = fixed_row_opt(r, n)
        candidate = (z[0], z[1], r, z[2], z[3])
        if best is None or candidate[:2] < best[:2]:
            best = candidate
    return best, R

def restricted_global(n, max_index):
    upper = standard_upper(n)
    R = cutoff(n, upper)
    best = None
    for r in range(2*n - 2, R):
        z = fixed_row_opt(r, n, max_index=max_index)
        if z is None:
            continue
        candidate = (z[0], z[1], r, z[2], z[3])
        if best is None or candidate[:2] < best[:2]:
            best = candidate
    return best

def prune_divisibility(states):
    kept = []
    for x in sorted(set(states)):
        if not any(x % y == 0 for y in kept):
            kept.append(x)
    return set(kept)

def lcm_state_row(r, n):
    coeff = [comb(r, k) for k in range(r//2 + 1)]
    q = len(coeff) - n
    dp = [set() for _ in range(q + 1)]
    dp[0] = {1}
    for x in coeff:
        new = [set() for _ in range(q + 1)]
        for omitted in range(q + 1):
            for z in dp[omitted]:
                new[omitted].add(lcm(z, x))
            if omitted > 0:
                new[omitted].update(dp[omitted - 1])
        for omitted in range(q + 1):
            if new[omitted]:
                new[omitted] = prune_divisibility(new[omitted])
        dp = new
    return min(dp[q])

# Published benchmark from Huber, Proposition 6.3.
bench = fixed_row_opt(90, 41)
assert bench[1] == 3
assert bench[2] == 23 * 31 * 47
assert [i for i in range(46) if (bench[3] >> i) & 1] == [22, 29, 30, 44, 45]

expected = {
    42: (1, 91), 43: (1, 91), 44: (1, 91),
    45: (0, 92), 46: (0, 92), 47: (0, 95),
    48: (0, 95), 49: (0, 99), 50: (0, 99),
    51: (0, 101), 52: (0, 104), 53: (0, 105),
    54: (0, 107), 55: (0, 116), 56: (0, 116),
    57: (2, 120),
}
results = {}
for n in range(42, 58):
    best, R = global_opt(n)
    results[n] = best
    assert (best[1], best[2]) == expected[n]

A57 = 34745667272226689670077824806669345127280961600
best57 = results[57]
assert best57[0] == A57
assert best57[2] == 120
assert best57[3] == 41 * 61
assert [i for i in range(61) if (best57[4] >> i) & 1] == [39, 40, 60]

# Candidate-based cutoff: every row r >= 176 is excluded by the binomial lower bound.
assert cutoff(57, A57) == 176

best_def1 = restricted_global(57, 57)
B1 = 65841579578883348912626466335327204421864343200
assert best_def1[0] == B1 and best_def1[2] == 118
assert Fraction(B1, A57) == Fraction(451, 238)

best_prefix = restricted_global(57, 56)
B0 = 130585799498118642010042491565065622103364280680
assert best_prefix[0] == B0 and best_prefix[2] == 119
assert Fraction(B0, A57) == Fraction(451, 120)

# Distinct local implementation on the decisive row.
assert lcm_state_row(120, 57) == A57

print(
    "VERIFY_OK first_defect_two=57 row=120 saving=2501 "
    "excluded=39,40,60 "
    "a57=34745667272226689670077824806669345127280961600 "
    "best_defect_le1_ratio=451/238 best_prefix_ratio=451/120 "
    "source_benchmark_n41=yes local_lcm_state=yes"
)
