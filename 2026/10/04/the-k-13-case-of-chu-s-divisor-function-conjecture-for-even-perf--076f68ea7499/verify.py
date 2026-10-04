#!/usr/bin/env python3
# Exact finite replay for the k=13 reduction.

K = 13
M = 2**K - 1

def vp(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e

def S(alpha):
    return (2**(K * alpha) - 1) // M

# Growth cutoffs used in the proof.
assert 5**31 > (2**78 - 1) // M
assert 3**37 > 2**65 // M
assert 5**32 > 8193
assert 3**64 > 2**13

# Case p == 1 mod 4.  We over-enumerate all integers, not just primes.
case1 = {}
for v in range(1, 5):
    rows = []
    for alpha in range(2, v + 2):
        s = S(alpha)
        bound = 3 * 2**(alpha - 1) - 1
        for p in range(5, bound):
            if p % 4 == 1 and s % p == 0:
                rows.append((alpha, p, vp(s, p)))
    case1[v] = rows

assert case1[1] == []
assert case1[2] == []
assert case1[3] == [(4, 5, 1)]
assert case1[4] == [(4, 5, 1)]

# Case p == 3 mod 4.  Again composites are retained deliberately.
# p=M is handled symbolically in RESULT.md and is omitted here.
case3 = {}
for v in range(1, 6):
    rows = {}

    # alpha <= v: direct finite range.
    for alpha in range(2, v + 1):
        s = S(alpha)
        bound = 3 * 2**(alpha - 1) - 1
        for p in range(3, bound):
            if p % 4 == 3 and p != M and s % p == 0:
                rows[(alpha, p)] = vp(s, p)

    # alpha > v: use t and the nonzero divisor D_{v,t}.
    for t in range(1, 3 * 2**(v - 1)):
        if t == 2**v:
            continue
        D = abs(2**(13 * v) - t**13)
        if D == 0:
            continue
        m = 1
        while t * 2**m <= D + 1:
            alpha = v + m
            p = t * 2**m - 1
            if p >= 3 and p % 4 == 3 and p != M and D % p == 0:
                s = S(alpha)
                if s % p == 0:
                    rows[(alpha, p)] = vp(s, p)
            m += 1

    case3[v] = sorted((a, p, u) for (a, p), u in rows.items())

max_u = {v: max((u for _, _, u in rows), default=0)
         for v, rows in case3.items()}
assert max_u == {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}

# The divisibility requirement would need u >= 2^v-1.
for v in range(2, 6):
    assert max_u[v] < 2**v - 1
assert case3[1] == []

print("CASE1_COUNTS", {v: len(rows) for v, rows in case1.items()})
print("CASE3_COUNTS", {v: len(rows) for v, rows in case3.items()})
print("CASE3_MAX_U", max_u)
print("VERIFY_OK")
