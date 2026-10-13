def gcd_degree_monomials(m, n, i, j):
    return min(i, j) + min(m-i, n-j)

cumulative_checks = exact_checks = pair_checks = 0

for m in range(1, 21):
    for n in range(m, 31):
        hist = [0] * (m + 1)

        for i in range(m + 1):
            for j in range(n + 1):
                g = gcd_degree_monomials(m, n, i, j)
                assert 0 <= g <= m
                hist[g] += 1
                pair_checks += 1

        assert sum(hist) == (m + 1) * (n + 1)

        for k in range(1, m + 1):
            cumulative = sum(hist[k:])
            expected = (m + 1) * (n + 1) - k * (k + 1)
            assert cumulative == expected, (m, n, k, cumulative, expected)
            cumulative_checks += 1

        assert hist[0] == 2
        for k in range(1, m):
            assert hist[k] == 2 * (k + 1), (m, n, k, hist[k])
            exact_checks += 1

        assert hist[m] == (m + 1) * (n - m + 1), (m, n, hist[m])
        exact_checks += 1

print("VERIFY_OK", cumulative_checks, exact_checks, pair_checks)
