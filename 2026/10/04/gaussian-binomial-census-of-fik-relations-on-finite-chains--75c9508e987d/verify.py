#!/usr/bin/env python3
from itertools import combinations_with_replacement

def fc_direct(n, mask):
    def edge(i, j):
        return (mask >> (i*n + j)) & 1
    for i in range(n):
        for ip in range(i, n):
            for j in range(n):
                if edge(i, j):
                    if not any(edge(ip, jp) and j <= jp for jp in range(n)):
                        return False
    return True

def row_normal_form(n, mask):
    rows = []
    for i in range(n):
        S = [j for j in range(n) if (mask >> (i*n + j)) & 1]
        rows.append(S)

    seen_nonempty = False
    last_max = -1
    for S in rows:
        if not S:
            if seen_nonempty:
                return False
        else:
            seen_nonempty = True
            m = max(S)
            if m < last_max:
                return False
            last_max = m
    return True

def qbinom(N, K, q=2):
    if K < 0 or K > N:
        return 0
    row = [0] * (K + 1)
    row[0] = 1
    for n in range(1, N + 1):
        upper = min(n, K)
        for k in range(upper, 0, -1):
            row[k] = row[k] + (q ** (n-k)) * row[k-1]
    return row[K]

def formula_total(n):
    return sum(qbinom(n+k-1, k, 2) for k in range(n+1))

direct_counts = []
for n in range(1, 5):
    count = 0
    by_k = [0] * (n + 1)
    for mask in range(1 << (n*n)):
        a = fc_direct(n, mask)
        b = row_normal_form(n, mask)
        assert a == b, (n, mask)
        if a:
            count += 1
            k = sum(
                any((mask >> (i*n+j)) & 1 for j in range(n))
                for i in range(n)
            )
            by_k[k] += 1

    expected_by_k = [qbinom(n+k-1, k, 2) for k in range(n+1)]
    assert by_k == expected_by_k, (n, by_k, expected_by_k)
    assert count == formula_total(n)
    direct_counts.append(count)

assert direct_counts == [2, 11, 198, 13377]

# Independent fixed-k summation over weakly increasing maxima.
for n in range(1, 8):
    for k in range(n+1):
        if k == 0:
            explicit = 1
        else:
            explicit = 0
            for ms in combinations_with_replacement(range(1, n+1), k):
                weight = 1
                for m in ms:
                    weight *= 2 ** (m-1)
                explicit += weight
        assert explicit == qbinom(n+k-1, k, 2), (n, k)

vals = [formula_total(n) for n in range(1, 13)]
assert vals[:6] == [2, 11, 198, 13377, 3523028, 3661468103]

# Numeric asymptotic sanity check only.
P = 1.0
for j in range(1, 100):
    P *= 1.0 - 2.0**(-j)
C = 1.0 / P
ratios = [formula_total(n) / (2.0 ** (n*(n-1))) for n in range(2, 13)]
assert abs(C - 3.462746619455064) < 1e-14
assert ratios[-1] > ratios[0]
assert abs(ratios[-1] - C) < 0.01

print("DIRECT_COUNTS", direct_counts)
print("FORMULA_FIRST_12", vals)
print("ASYMPTOTIC_CONSTANT", format(C, ".15f"))
print("VERIFY_OK")
