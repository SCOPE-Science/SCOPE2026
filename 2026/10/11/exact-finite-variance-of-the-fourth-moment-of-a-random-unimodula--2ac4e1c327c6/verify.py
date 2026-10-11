from collections import Counter

def exponent_vector(n, k, i, j):
    e = [0] * n
    e[i + k] += 1
    e[i] -= 1
    e[j + k] -= 1
    e[j] += 1
    return tuple(e)

def expected_var_e(n):
    if n % 2 == 0:
        return n * (n - 2) * (4 * n - 7) // 6
    return (n - 1) * (4 * n * n - 11 * n + 3) // 6

def check(n):
    counts = Counter()
    constants = 0
    for k in range(1, n):
        for i in range(n - k):
            for j in range(n - k):
                v = exponent_vector(n, k, i, j)
                if all(x == 0 for x in v):
                    constants += 1
                else:
                    counts[v] += 1

    assert constants == n * (n - 1) // 2
    assert set(counts.values()).issubset({1, 2})
    variance = sum(m * m for m in counts.values())
    assert variance == expected_var_e(n)

    n1 = sum(1 for m in counts.values() if m == 1)
    expected_n1 = n * (n - 2) // 2 if n % 2 == 0 else (n - 1) ** 2 // 2
    assert n1 == expected_n1

for n in range(2, 41):
    check(n)

print("VERIFY_OK n_range=2..40 parity_variance=exact")
