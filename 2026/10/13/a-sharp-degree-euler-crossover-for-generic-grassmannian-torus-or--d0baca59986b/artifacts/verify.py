from math import comb

def eulerian_row(m):
    assert m >= 1
    row = [1]
    for n in range(2, m + 1):
        nxt = [0] * n
        for j in range(n):
            left = row[j - 1] if j - 1 >= 0 else 0
            right = row[j] if j < len(row) else 0
            nxt[j] = (n - j) * left + (j + 1) * right
        row = nxt
    return row

comparison_checks = interior_bound_checks = central_bound_checks = 0

for n in range(2, 121):
    row = eulerian_row(n - 1)
    for k in range(1, n):
        D = row[k - 1]
        E = comb(n, k)

        expected_less = (n <= 4) or (k in (1, n - 1))
        expected_greater = (n >= 5) and (2 <= k <= n - 2)
        assert expected_less ^ expected_greater
        assert (D < E) == expected_less, (n, k, D, E)
        assert (D > E) == expected_greater, (n, k, D, E)
        assert D != E
        comparison_checks += 1

        if 2 <= k <= n - 2:
            assert D >= 2 ** (n - 1) - n
            interior_bound_checks += 1

    if n >= 5:
        assert 2 ** (n - 1) - n > comb(n, n // 2)
        central_bound_checks += 1

assert eulerian_row(3)[1] == 4
assert eulerian_row(4)[1] == 11
assert comb(4, 2) == 6
assert comb(5, 2) == 10

print("VERIFY_OK", comparison_checks, interior_bound_checks, central_bound_checks)
