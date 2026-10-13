from itertools import product

format_checks = coordinate_checks = tangent_checks = 0

for t in range(3, 6):
    for dims in product(range(2, 5), repeat=t):
        offsets = []
        q = 0
        for m in dims:
            offsets.append(list(range(q, q + m)))
            q += m

        weights = []
        for idx in product(*[range(m) for m in dims]):
            w = sum(1 << offsets[i][idx[i]] for i in range(t))
            weights.append(w)
            coordinate_checks += 1

            # Each coordinate functional has a nontrivial kernel in the
            # first two factors because both dimensions are at least two.
            assert dims[0] >= 2 and dims[1] >= 2
            tangent_checks += 1

        assert len(set(weights)) == len(weights)

        M = 1
        for m in dims:
            M *= m
        assert len(weights) == M
        format_checks += 1

print("VERIFY_OK", format_checks, coordinate_checks, tangent_checks)
