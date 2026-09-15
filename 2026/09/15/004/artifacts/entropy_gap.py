"""Reproducible entropy-gap computation for the target disproof.

Shows that for fixed small eps (e.g. 0.01), the per-container dense-subgraph
tail exponent H(8*eps)/8 is bounded away from 1/8, so any container family
with e(C) <= (1/8+o(1))n^2 and |C| = 2^{o(n^2)} forces
log2|F| <= (H(8eps)/8+o(1))n^2, contradicting (1/8+o(1))n^2.
"""
import math


def H(p: float) -> float:
    assert 0.0 < p < 1.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


TARGET = 1.0 / 8.0
print("eps, 8eps, H(8eps)/8, gap_to_1/8")
for eps in [0.005, 0.01, 0.02, 0.03, 0.05, 0.0625]:
    x = 8 * eps
    if x >= 1.0:
        print(eps, x, "n/a (x>=1)", "n/a")
        continue
    c = H(x) / 8.0
    print(f"{eps:.4f} {x:.4f} {c:.6f} {TARGET - c:.6f}")

# Assert the key instance used in the proof.
eps = 0.01
c = H(8 * eps) / 8.0
assert c < 0.06, c  # ~0.0503, far below 0.125
assert TARGET - c > 0.07, c
print("OK: at eps=0.01 the gap exceeds 0.07*n^2 bits.")
