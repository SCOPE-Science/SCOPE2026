"""verify_lemma2.py — stress test of Lemma 2 on small analogue (stdlib only).

Small analogue: n=6, tau=(0 1 2)(3 4 5), c=2, f=0.
Lemma 2 predicts: every tau-stable binary self-dual [6,3] code has fixed
subcode of dimension (c+f)/2 = 1.
Checks by exhaustive enumeration of all binary self-dual [6,3] codes.
"""
import itertools
import math

tau = [1, 2, 0, 4, 5, 3]


def apply(p, v):
    return tuple(v[p[i]] for i in range(len(p)))


def add(a, b):
    return tuple((x + y) % 2 for x, y in zip(a, b))


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) % 2


def span(basis):
    S = {tuple([0] * 6)}
    for b in basis:
        S = S | {add(s, b) for s in S}
    return S


vecs = [v for v in itertools.product([0, 1], repeat=6) if sum(v) % 2 == 0]
total = 0
stable = 0
for combo in itertools.combinations(vecs, 3):
    S = span(combo)
    if len(S) != 8:
        continue
    if any(dot(a, b) != 0 for a in combo for b in combo):
        continue
    total += 1
    if all(apply(tau, v) in S for v in S):
        stable += 1
        fix = [v for v in S if apply(tau, v) == v]
        d = int(math.log2(len(fix)))
        assert d == 1, (combo, d)
assert total == 420, total
assert stable == 84, stable
print(f"enumerated {total} self-dual [6,3] codes, {stable} tau-stable, all fixed-dim 1 OK")
print("VERIFY_OK")
