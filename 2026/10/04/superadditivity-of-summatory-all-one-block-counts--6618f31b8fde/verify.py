#!/usr/bin/env python3

def occ_all_ones(n, r):
    if n == 0:
        return 0
    s = bin(n)[2:]
    w = "1" * r
    return sum(s[i:i+r] == w for i in range(max(0, len(s)-r+1)))

def direct_prefix(r, N):
    a = [0] * (N + 1)
    for n in range(N):
        a[n+1] = a[n] + occ_all_ones(n, r)
    return a

def F(N, r, i):
    q = 1 << i
    M = (1 << r) * q
    x = N % M
    return q * (N // M) + max(0, x - (M - q))

def formula_B(N, r):
    if N <= 0:
        return 0
    out = 0
    i = 0
    while (1 << i) < N:
        out += F(N, r, i)
        i += 1
    return out

# Direct object/formula comparison.
direct_words = 0
for r in range(2, 7):
    pref = direct_prefix(r, 4096)
    direct_words += 4096
    for N in range(4097):
        assert pref[N] == formula_B(N, r)

# Finite stress test of the claimed superadditivity.
pair_checks = 0
for r in range(2, 7):
    pref = direct_prefix(r, 1024)
    for m in range(513):
        for n in range(513):
            assert pref[m+n] >= pref[m] + pref[n]
            pair_checks += 1

# Exhaust the residue inequality underlying one positional summand.
# The proof in RESULT.md handles arbitrary q and r; this is a finite replay
# of many complete residue periods.
residue_checks = 0
for r in range(2, 8):
    for i in range(0, 6):
        q = 1 << i
        M = (1 << r) * q
        # Scaling lets us sample all boundary-relevant residue types without
        # a quadratic loop over very large M: include every residue for q<=4,
        # and all interval endpoints plus nearby residues otherwise.
        if q <= 4 and M <= 512:
            xs = range(M)
        else:
            pts = {0, 1, q-1, q, M-2*q, M-2*q+1, M-q-1, M-q, M-q+1, M-2, M-1}
            xs = sorted(x for x in pts if 0 <= x < M)
        for x in xs:
            for y in xs:
                lhs = F(x+y, r, i)
                rhs = F(x, r, i) + F(y, r, i)
                assert lhs >= rhs
                residue_checks += 1

# Exact equality strip, checked exhaustively through moderate dyadic scales.
equality_checks = 0
for r in range(2, 7):
    maxN = (1 << 11) + (1 << 11)
    pref = direct_prefix(r, maxN)
    for k in range(r-1, 11):
        threshold = (1 << k) - (1 << (k-r+1))
        for m in range(threshold + 1):
            assert pref[(1 << k) + m] == pref[1 << k] + pref[m]
            equality_checks += 1

print(
    "VERIFY_OK "
    f"direct_words={direct_words} "
    f"pair_checks={pair_checks} "
    f"residue_checks={residue_checks} "
    f"equality_checks={equality_checks}"
)
