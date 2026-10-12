from itertools import combinations
from math import comb

pairs = 0
coordinate_checks = 0
tangent_basis_checks = 0
weight_checks = 0

for n in range(4, 15):
    universe = tuple(range(n))
    for k in range(2, n-1):
        pairs += 1
        subsets = list(combinations(universe, k))

        weights = [sum(1 << i for i in I) for I in subsets]
        assert len(weights) == len(set(weights)) == comb(n, k)
        weight_checks += len(weights)

        for I in subsets:
            Iset = set(I)
            comp = [x for x in universe if x not in Iset]
            a, b = I[0], I[1]
            c, d = comp[0], comp[1]
            Jset = (Iset - {a, b}) | {c, d}
            J = tuple(sorted(Jset))
            assert len(Iset & Jset) == k - 2

            # Coordinate basis of wedge^{k-1} J wedge C^n:
            tangent_coords = {
                K for K in subsets if len(set(K) & Jset) >= k - 1
            }
            assert I not in tangent_coords
            assert len(tangent_coords) == 1 + k * (n - k)
            coordinate_checks += 1
            tangent_basis_checks += len(tangent_coords)

assert pairs == sum(n-3 for n in range(4,15))
print("VERIFY_OK", pairs, coordinate_checks, tangent_basis_checks, weight_checks)
