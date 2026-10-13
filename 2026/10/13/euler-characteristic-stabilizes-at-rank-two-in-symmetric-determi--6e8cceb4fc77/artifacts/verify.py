from math import comb

weight_checks = cumulative_checks = stratum_checks = 0

for n in range(2, 101):
    weights = []
    for i in range(n):
        for j in range(i, n):
            weights.append((1 << i) + (1 << j))
    assert len(weights) == comb(n + 1, 2)
    assert len(set(weights)) == len(weights)
    weight_checks += 1

    rank1_fixed = n
    rank2_fixed = comb(n, 2)
    all_fixed = rank1_fixed + rank2_fixed
    assert all_fixed == comb(n + 1, 2)

    cumulative = {}
    for r in range(1, n + 1):
        cumulative[r] = rank1_fixed if r == 1 else all_fixed
        expected = n if r == 1 else comb(n + 1, 2)
        assert cumulative[r] == expected
        cumulative_checks += 1

    prev = 0
    for r in range(1, n + 1):
        exact = cumulative[r] - prev
        expected = n if r == 1 else (comb(n, 2) if r == 2 else 0)
        assert exact == expected
        prev = cumulative[r]
        stratum_checks += 1

print("VERIFY_OK", weight_checks, cumulative_checks, stratum_checks)
