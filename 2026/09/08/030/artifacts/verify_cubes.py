"""Independent verifier for subtract-a-cube S={1,8,27,64,125}.
Stdlib only. Recomputes W/SG by DP from rules alone and checks every
integer claim in DRAFT.md. Prints VERIFY_OK on full pass."""
S = (1, 8, 27, 64, 125)
M = max(S)
N = 5000
W = [False] * (N + 1)  # True = N-position (win)
SG = [0] * (N + 1)
for n in range(N + 1):
    reach = set()
    w = False
    for s in S:
        if s > n:
            continue
        reach.add(SG[n - s])
        if not W[n - s]:
            w = True
    W[n] = w if n > 0 else False
    m = 0
    while m in reach:
        m += 1
    SG[n] = m

COLD200 = [0,2,4,6,9,11,13,15,18,20,22,24,34,37,39,41,43,46,48,50,52,
 55,57,59,62,69,71,74,76,78,80,83,85,87,90,92,94,97,99,104,106,108,
 111,113,115,118,120,122,132,137,139,141,146,148,150,152,155,157,167,
 169,174,176,178,181,183,185,188,190,192,195,197]
assert [n for n in range(201) if SG[n] == 0] == COLD200, "cold200 mismatch"
assert len(COLD200) == 71
assert all((SG[n] == 0) == (not W[n]) for n in range(N + 1)), "SG0!=P"
from collections import Counter
c200 = Counter(SG[:201])
assert (c200[0], c200[1], c200[2], c200[3], c200[4]) == (71, 71, 34, 19, 6), c200
assert max(SG[:201]) == 4
assert [n for n in range(201) if SG[n] == 4] == [128, 144, 160, 165, 172, 200]
assert [n for n in range(N + 1) if SG[n] == 4] == [128, 144, 160, 165, 172, 200, 263]
assert max(SG[264:]) == 2, "tail max"

# Negative result: no period certificate with window>=M closes inside [0,200]
def certifiable(seq, N0):
    out = []
    for q in range(N0 + 1):
        for p in range(1, N0 + 1 - q):
            if N0 - p - q + 1 < M:
                continue
            if all(seq[n] == seq[n + p] for n in range(q, N0 - p + 1)):
                out.append((q, p))
                break
    return out
assert certifiable(W[:201], 200) == [], "W certifiable in 200?!"
assert certifiable(SG[:201], 200) == [], "SG certifiable in 200?!"

# Positive result: outcome period 7 from 263, SG period 7 from 264
assert [int(x) for x in W[263:270]] == [1, 1, 0, 1, 0, 1, 0]
assert SG[264:271] == [2, 0, 1, 0, 1, 0, 1]
# minimal induction base windows (length 125 = max S)
assert all(W[n] == W[n + 7] for n in range(263, 388))
assert all(SG[n] == SG[n + 7] for n in range(264, 389))
# extended confirmation to 5000
assert all(W[n] == W[n + 7] for n in range(263, N - 7 + 1))
assert all(SG[n] == SG[n + 7] for n in range(264, N - 7 + 1))
# leastness of preperiods: last mismatches
assert W[262] != W[269] and all(W[n] == W[n + 7] for n in range(263, N - 7 + 1))
assert SG[263] != SG[270] and all(SG[n] == SG[n + 7] for n in range(264, N - 7 + 1))
# leastness of period: every p<7 fails in the tail
for p in range(1, 7):
    assert any(W[n] != W[n + p] for n in range(263, N - p + 1)), p
    assert any(SG[n] != SG[n + p] for n in range(264, N - p + 1)), p
# residue tables
for n in range(263, N + 1):
    r = n % 7
    assert (not W[n]) == (r in (1, 3, 6)), (n, r)
for n in range(264, N + 1):
    r = n % 7
    exp = 2 if r == 5 else (0 if r in (1, 3, 6) else 1)
    assert SG[n] == exp, (n, r)
print("VERIFY_OK")
