def fixed_euler(n, d, s):
    assert 1 <= s <= d < n
    off = 0
    rejected = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            # E_ij sends e_j to e_i.
            if s < d:
                ok = True
            else:
                ok = not (j < d and i >= d)
            if ok:
                off += 1
            else:
                rejected += 1
    return n + off, rejected

checked = 0
for n in range(2, 31):
    for d in range(1, n):
        vals = []
        for s in range(1, d + 1):
            got, rejected = fixed_euler(n, d, s)
            expected = n*n if s < d else n*n - d*(n-d)
            assert got == expected
            assert rejected == (0 if s < d else d*(n-d))
            vals.append(got)
            checked += 1

        if d >= 2:
            for s in range(1, d):
                diff = vals[s-1] - vals[s]
                expected_diff = 0 if s <= d-2 else d*(n-d)
                assert diff == expected_diff

weight_checks = 0
for n in range(2, 21):
    w = [1 << i for i in range(n)]
    seen = {}
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            z = w[i] - w[j]
            assert z not in seen, (n, i, j, seen.get(z))
            seen[z] = (i, j)
            weight_checks += 1

assert checked > 4000
assert weight_checks > 2000
print("VERIFY_OK", checked, weight_checks)
