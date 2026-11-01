"""Independent finite-field rank crosscheck of the integer Smith data.
Run alongside verify.py; requires only the Python standard library.
"""
from verify import compute, sparse_rank_modp

_, _, boundaries = compute(5)
expected = {
    2: [101, 468, 831, 668, 206],
    5: [101, 469, 831, 667, 207],
    7: [101, 469, 831, 668, 207],
}
for prime, ranks in expected.items():
    actual = [sparse_rank_modp(boundaries[d], prime) for d in range(1, 6)]
    assert actual == ranks, (prime, actual, ranks)
    print('PRIME', prime, 'RANKS', actual)
print('MODULAR_CROSSCHECK_OK')
