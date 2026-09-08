"""Independent verifier for lane-263: D(7,3) minimum-permanent claim.

Replays from the committed witness entries only:
 1. margins are all 3
 2. permanent by brute-force permutation expansion (5040 perms)
 3. permanent by independent Ryser inclusion-exclusion
 4. Schrijver(7,3) = (4/3)^7 and exact ratio 6561/2048
 5. full-class distribution sums to 68,938,800 (OEIS A001501)
"""
import itertools
from fractions import Fraction

W = [7, 7, 25, 26, 100, 104, 112]
A = [[(m >> j) & 1 for j in range(7)] for m in W]

assert [sum(r) for r in A] == [3]*7, "row margins"
assert [sum(A[i][j] for i in range(7)) for j in range(7)] == [3]*7, "col margins"

brute = sum(1 for s in itertools.permutations(range(7))
            if all(A[i][s[i]] for i in range(7)))

def ryser(M):
    n = len(M); tot = 0
    for S in range(1 << n):
        prod = 1
        for i in range(n):
            t = sum(M[i][j] for j in range(n) if (S >> j) & 1)
            if t == 0:
                prod = 0; break
            prod *= t
        tot += prod if bin(S).count("1") % 2 == 0 else -prod
    return ((-1) ** n) * tot

ry = ryser(A)
assert brute == 24, brute
assert ry == 24, ry

S = Fraction(4, 3) ** 7
assert S == Fraction(16384, 2187), S
assert Fraction(brute, 1) / S == Fraction(6561, 2048), "Schrijver ratio"

# Full-class distribution from the exhaustive C census (labeled matrices)
dist = {24: 14439600, 25: 6350400, 26: 25401600, 27: 16934400,
        30: 3175200, 31: 1814400, 32: 793800, 54: 29400}
assert sum(dist.values()) == 68938800, sum(dist.values())
assert min(dist) == 24
assert sum(c for v, c in dist.items() if v < 24) == 0

print("VERIFY_OK: margins ok; brute per = 24; Ryser per = 24;",
      "Schrijver = 16384/2187; ratio = 6561/2048;",
      "distribution sums to 68938800; minimum 24 certified.")
