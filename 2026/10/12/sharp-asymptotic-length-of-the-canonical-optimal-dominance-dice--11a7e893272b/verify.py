import math

def threshold(N):
    if N % 2:
        return ((N + 1) // 2) ** 2
    m = N // 2
    return m * (m + 1)

def greedy_subcycle(N):
    T = threshold(N)
    k = 0
    seq = []
    while k < N:
        nxt = min(N, T // (N - k))
        if nxt <= k:
            raise AssertionError((N, k, nxt))
        seq.append(nxt)
        k = nxt
    return seq

def edge_ok(N, a, b):
    return (N - a) * b <= threshold(N)

known = {10: 6, 100: 24, 10000: 260, 1000000: 2628, 100000000: 26304}
for N, want in known.items():
    seq = greedy_subcycle(N)
    assert len(seq) == want
    a = 0
    for b in seq:
        assert edge_ok(N, a, b)
        a = b

for N in range(2, 151):
    T = threshold(N)
    dp = [10**9] * (N + 1)
    dp[0] = 0
    for a in range(N):
        if dp[a] >= 10**9:
            continue
        mx = min(N, T // (N - a))
        for b in range(a + 1, mx + 1):
            dp[b] = min(dp[b], dp[a] + 1)
    assert dp[N] == len(greedy_subcycle(N))

R = 2_000_000
S = sum((math.sqrt(r + 1) - math.sqrt(r)) / (r + 1) for r in range(R))
C_approx = math.sqrt(2) * (S + 1 / math.sqrt(R))
assert 2.6303 < C_approx < 2.6307

print("VERIFY_OK")
print("known_lengths", [(N, len(greedy_subcycle(N))) for N in known])
print("C_approx", format(C_approx, ".12f"))
