"""Empirical check of the Bernstein pairwise-independent triple used in lane-20335.

Verifies on i.i.d. samples (A, B, A xor B) with A,B fair coins:
  (i)   each coordinate is fair (mean of (-1)^bit ~ 0);
  (ii)  each pair is independent (4 joint cells ~ 1/4);
  (iii) the triple product (-1)^A (-1)^B (-1)^{A xor B} is identically 1.
This is the finite-dimensional marginal of the joining lambda_Y in DRAFT.md.
Seeded for reproducibility.
"""
import random

random.seed(20335)
N = 200_000

s1 = s2 = s3 = 0
pair12 = [[0, 0], [0, 0]]
pair13 = [[0, 0], [0, 0]]
pair23 = [[0, 0], [0, 0]]
trip = 0

for _ in range(N):
    a = random.getrandbits(1)
    b = random.getrandbits(1)
    c = a ^ b
    s1 += 1 if a == 0 else -1  # (-1)^a with bit convention
    s2 += 1 if b == 0 else -1
    s3 += 1 if c == 0 else -1
    pair12[a][b] += 1
    pair13[a][c] += 1
    pair23[b][c] += 1
    # (-1)^a (-1)^b (-1)^c with (-1)^bit = 1-2*bit
    trip += (1 - 2 * a) * (1 - 2 * b) * (1 - 2 * c)

print("means:", s1 / N, s2 / N, s3 / N)
print("pair12:", [[v / N for v in row] for row in pair12])
print("pair13:", [[v / N for v in row] for row in pair13])
print("pair23:", [[v / N for v in row] for row in pair23])
print("triple-product mean:", trip / N)

assert abs(s1 / N) < 0.02 and abs(s2 / N) < 0.02 and abs(s3 / N) < 0.02
for grid in (pair12, pair13, pair23):
    for row in grid:
        for v in row:
            assert abs(v / N - 0.25) < 0.01
assert trip / N == 1.0
print("BERNSTEIN_CHECK_OK")
