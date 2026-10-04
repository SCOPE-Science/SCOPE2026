from itertools import combinations_with_replacement
from math import comb, prod

def wronskian_degree(N, ds, k):
    D = prod(ds)
    S = sum(ds)
    assert 1 <= k < min(ds)
    genus_numerator = D * (S - N - 1)
    assert genus_numerator % 2 == 0
    g_minus_1 = genus_numerator // 2
    M = comb(N + k, k)
    return M * (k * D + (M - 1) * g_minus_1)

def predicted_odd(N, ds, k):
    return (k % 2 == 1) and all(d % 2 == 1 for d in ds) and ((N & k) == 0)

tuple_checks = 0
for N in range(2, 9):
    codim = N - 1
    for k in range(1, 7):
        # A bounded family with all degrees above k, as required.
        for ds in combinations_with_replacement(range(k + 1, k + 6), codim):
            w = wronskian_degree(N, ds, k)
            assert (w & 1) == predicted_odd(N, ds, k)
            tuple_checks += 1

binary_checks = 0
for N in range(1, 256):
    for k in range(1, 256):
        assert (comb(N + k, k) & 1) == ((N & k) == 0)
        binary_checks += 1

# Standard-embedding corollary.
for N in range(2, 10):
    for ds in combinations_with_replacement(range(2, 9), N - 1):
        if min(ds) > 1:
            actual = wronskian_degree(N, ds, 1) & 1
            expected = (N % 2 == 0) and all(d % 2 == 1 for d in ds)
            assert actual == expected

print("VERIFY_OK", tuple_checks, binary_checks)
