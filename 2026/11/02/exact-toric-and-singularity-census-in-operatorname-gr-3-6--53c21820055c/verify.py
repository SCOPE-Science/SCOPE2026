"""Exact exhaustive verification of the toric rank-three Gr(3,6) census.

Run with: python verify.py  (alongside compute.py and independent.py).
"""
from collections import Counter
from compute import necklaces, support as necklace_support, binary, dimension, is_smooth_toric, forbidden_U24
from independent import exact_binary_grassmannian, support as matrix_support, is_positroid, dim_and_smooth

N = necklaces(6, 3)
assert len(N) == 883
necklace_bases = set()
toric = {}
for neck in N:
    B = necklace_support(neck, 6, 3)
    assert B not in necklace_bases
    necklace_bases.add(B)
    b = binary(B, 6, 3)
    assert b != forbidden_U24(B, 6, 3)[0]
    if b:
        d = dimension(B, 6)
        sm, _ = is_smooth_toric(B, 6)
        toric[frozenset(B)] = (d, sm)

assert len(necklace_bases) == 883
assert len(toric) == 703
matrix_positroids = {}
num_subspaces = 0
for rows in exact_binary_grassmannian(6, 3):
    num_subspaces += 1
    B = matrix_support(rows, 6, 3)
    if is_positroid(B, 6, 3):
        assert B not in matrix_positroids
        matrix_positroids[B] = dim_and_smooth(B, 6)
assert num_subspaces == 1395
assert len(matrix_positroids) == 703
assert matrix_positroids == toric  # Entire support-by-support classification, not only totals.

observed = Counter(toric.values())
expected = {
    (0, True): 20,
    (1, True): 90,
    (2, True): 180,
    (3, True): 95,
    (3, False): 120,
    (4, True): 6,
    (4, False): 144,
    (5, False): 48,
}
assert dict(observed) == expected, (observed, expected)
print('VERIFY_OK')
print('all_rank_three_positroids', len(necklace_bases))
print('F2_three_planes', num_subspaces)
print('toric_positroids', len(toric))
print('smooth_toric', sum(ct for (d, sm), ct in observed.items() if sm))
print('singular_toric', sum(ct for (d, sm), ct in observed.items() if not sm))
print('dimensions (dimension, smooth):')
for key in sorted(observed):
    print(key, observed[key])
