"""Exact, self-contained certificate of a sharp heterogeneous pivotality bound.
Requires only Python 3 standard library; run: python3 icos_influence_certificate.py
"""
from collections import Counter
from itertools import combinations

N = range(6)
WINNING_TRIPLES = (
    (0, 1, 2), (0, 1, 3), (0, 2, 4), (0, 3, 5), (0, 4, 5),
    (1, 2, 5), (1, 3, 4), (1, 4, 5), (2, 3, 4), (2, 3, 5),
)
TW = {sum(1 << j for j in triple) for triple in WINNING_TRIPLES}
assert len(TW) == 10
assert all(((1 << 6) - 1) ^ t not in TW for t in TW)

def winning(mask):
    size = mask.bit_count()
    return int(size >= 4 or (size == 3 and mask in TW))

assert all(winning(mask) + winning(63 ^ mask) == 1 for mask in range(64))
assert all(winning(mask) <= winning(mask | (1 << i)) for mask in range(64) for i in N)
assert [sum((t >> i) & 1 for t in TW) for i in N] == [5] * 6

# We use delta = 1 - 2alpha. At every vertex of the product-probability
# box, p_j=(1+epsilon_j*delta)/2, epsilon_j in {+1,-1}.
# 32 * pivotal_probability[i] is a degree <=5 integer polynomial in delta.
# Each factor (1 + sign*delta) is multiplied without approximation.
def poly_add_product(coeffs, signs):
    poly = [1]
    for sign in signs:
        out = [0] * (len(poly) + 1)
        for k, value in enumerate(poly):
            out[k] += value
            out[k+1] += sign * value
        poly = out
    for k, value in enumerate(poly):
        coeffs[k] += value

def vertex_pivotal(mask, i):
    other = [j for j in N if j != i]
    epsilon = {j: 1 if mask & (1 << j) else -1 for j in N}
    coeffs = [0] * 6
    for bits in range(32):
        subset = sum(1 << other[k] for k in range(5) if bits & (1 << k))
        if winning(subset | (1 << i)) - winning(subset):
            signs = [epsilon[j] if subset & (1 << j) else -epsilon[j] for j in other]
            poly_add_product(coeffs, signs)
    return tuple(coeffs)

# For each of 64 box vertices, exhaust all 15 unordered pairs of voters.
# The exact signed coefficient histogram of 32*(beta_i-beta_j):
expected = Counter({
    (0, 0, 0, 0, 0, 0): 360,
    (0, 0, 32, 0, 0, 0): 150,
    (0, 0, -32, 0, 0, 0): 150,
    (0, 0, 24, 0, 8, 0): 60,
    (0, 0, -24, 0, -8, 0): 60,
    (0, 0, 16, 0, -16, 0): 30,
    (0, 0, -16, 0, 16, 0): 30,
    (0, 0, 8, 0, -8, 0): 60,
    (0, 0, -8, 0, 8, 0): 60,
})
observed = Counter()
for corner in range(64):
    vals = [vertex_pivotal(corner, i) for i in N]
    assert all(v[0] == 10 and v[1] == v[3] == v[5] == 0 for v in vals)
    for i, j in combinations(N, 2):
        diff = tuple(x-y for x, y in zip(vals[i], vals[j]))
        observed[diff] += 1
assert observed == expected, (observed, expected)
# Witness: mask=3; voters 2 and 4 have beta_2-beta_4 = delta^2.
v = [vertex_pivotal(3, i) for i in N]
assert tuple(a-b for a,b in zip(v[2],v[4])) == (0, 0, 32, 0, 0, 0)
print('PASS: rule complementarity, monotonicity, and 5-fold triple regularity')
print('PASS: all 64 corner patterns times all 15 voter pairs = 960 exact polynomial identities')
print('PASS: exact 9-class coefficient histogram and attaining witness')
print('CONCLUSION: sup_p max_{i,j}|beta_i(p)-beta_j(p)|=(1-2alpha)^2 for 0<=alpha<=1/2')
