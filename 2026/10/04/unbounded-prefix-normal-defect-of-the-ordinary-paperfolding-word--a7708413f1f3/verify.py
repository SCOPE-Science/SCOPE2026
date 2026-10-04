#!/usr/bin/env python3

def bit(n):
    assert n >= 1
    while n % 2 == 0:
        n //= 2
    return 0 if n % 4 == 1 else 1

MAXN = 1 << 22
pref = [0] * (MAXN + 1)
for n in range(1, MAXN + 1):
    pref[n] = pref[n-1] + bit(n)

def S(n):
    return pref[n]

# Check the elementary prefix-sum recurrences used in the proof.
for n in range(1, 200000):
    assert S(2*n) == S(n) + n//2
    assert S(2*n+1) == S(n) + n//2 + (n & 1)

levels = 0
for m in range(2, 22):
    Lm = (1 << m) // 3
    Lnext = (1 << (m+1)) // 3
    assert Lm + Lnext == (1 << m) - 1
    assert S((1 << m) - 1) == (1 << (m-1)) - 1
    assert S(Lm) == Lm//2 - (m-1)//2
    # The interval [Lnext+1, 2^m-1] has length Lm.
    assert ((1 << m) - 1) - Lnext == Lm
    heavy = S((1 << m) - 1) - S(Lnext)
    ordinary_prefix = S(Lm)
    assert heavy - ordinary_prefix == m - 1
    levels += 1

# Directly check the finite witnesses for prepending c ones.
prepend_checks = 0
for c in range(0, 18):
    m = c + 2
    Lm = (1 << m) // 3
    Lnext = (1 << (m+1)) // 3
    assert Lm >= c
    q_prefix_ones = c + S(Lm - c)
    witness_ones = S((1 << m) - 1) - S(Lnext)
    assert witness_ones > q_prefix_ones
    prepend_checks += 1

print(
    "VERIFY_OK "
    f"levels={levels} "
    f"prefix_recurrence_n=1..199999 "
    f"prepend_checks={prepend_checks} "
    "witness_gap=m-1"
)
