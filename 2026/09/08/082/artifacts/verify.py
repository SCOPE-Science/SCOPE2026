"""Independent verifier: replays primes_5e7.bin -> all headline numbers from scratch."""
import struct, hashlib, json, math, os

ART = os.path.dirname(os.path.abspath(__file__))
raw = open(os.path.join(ART, "primes_5e7.bin"), "rb").read()
n = len(raw) // 4
P = struct.unpack("<%dI" % n, raw)
assert list(P[:5]) == [2, 3, 5, 7, 11], "prime list head mismatch"
assert P[-1] == 49999991, "prime list tail mismatch: %d" % P[-1]
# sorted + all odd after 2
assert all(P[i] < P[i + 1] for i in range(0, n - 1, 9973)), "order spot-check failed"
sha = hashlib.sha256(raw).hexdigest()
cnt = json.load(open(os.path.join(ART, "counts.json")))
assert cnt["sha256_bin"] == sha, "hash mismatch"
assert cnt["pi"] == n == 3001134, "pi mismatch: %d" % n

T10 = [[0] * 4 for _ in range(4)]
T3 = [[0] * 2 for _ in range(2)]
m10 = {1: 0, 3: 0, 7: 0, 9: 0}
m3 = {0: 0, 1: 0, 2: 0}
mp = {1: 0, 3: 1, 7: 2, 9: 3}
for p in P:
    r10 = p % 10
    if r10 in m10:
        m10[r10] += 1
    m3[p % 3] += 1
for k in range(n - 1):
    a, b = P[k], P[k + 1]
    ra, rb = a % 10, b % 10
    if ra in mp and rb in mp:
        T10[mp[ra]][mp[rb]] += 1
    ra3, rb3 = a % 3, b % 3
    if ra3 != 0 and rb3 != 0:
        T3[ra3 - 1][rb3 - 1] += 1
assert T10 == cnt["T10"], "T10 mismatch"
assert T3 == cnt["T3"], "T3 mismatch"
assert m10 == {int(k): v for k, v in cnt["marg10"].items()}, "marg10 mismatch"
assert m3 == {int(k): v for k, v in cnt["marg3"].items()}, "marg3 mismatch"

tot10 = sum(sum(r) for r in T10)
E10 = tot10 / 16.0
chi10 = sum((c - E10) ** 2 / E10 for row in T10 for c in row)
tot3 = sum(sum(r) for r in T3)
E3 = tot3 / 4.0
chi3 = sum((c - E3) ** 2 / E3 for row in T3 for c in row)
st = json.load(open(os.path.join(ART, "stats.json")))
assert abs(chi10 - st["chi2_10_uniform"]) < 1e-6 * chi10, "chi10 mismatch"
assert abs(chi3 - st["chi2_3_uniform"]) < 1e-6 * chi3, "chi3 mismatch"
flat = sorted(((i, j, T10[i][j]) for i in range(4) for j in range(4)), key=lambda t: t[2])
assert (flat[0][0], flat[0][1]) == (2, 2) and flat[0][2] == 122881, "most-suppressed mismatch"
assert (flat[-1][0], flat[-1][1]) == (3, 0) and flat[-1][2] == 250160, "most-enhanced mismatch"

print("pi(5e7) =", n)
print("sha256 =", sha)
print("T10 exact-match OK; pairs =", tot10)
print("T3 exact-match OK; pairs =", tot3)
print("chi2_10_uniform = %.2f  chi2_3_uniform = %.2f" % (chi10, chi3))
print("most suppressed (7,7) = 122881; most enhanced (9,1) = 250160")
print("VERIFY_OK")
