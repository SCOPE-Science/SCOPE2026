#!/usr/bin/env python3
from itertools import product, permutations


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def orbit_count_direct(n, group, k):
    pts = list(product(range(n), repeat=k))
    seen = set()
    count = 0
    for x in pts:
        if x in seen:
            continue
        count += 1
        orb = {tuple(g[a] for a in x) for g in group}
        seen.update(orb)
    return count


def orbit_count_burnside(n, group, k):
    total = 0
    for g in group:
        fixed = sum(g[i] == i for i in range(n))
        total += fixed ** k
    assert total % len(group) == 0
    return total // len(group)


def stirling2(n, k):
    d = [[0]*(n+1) for _ in range(n+1)]
    d[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            d[i][j] = d[i-1][j-1] + j*d[i-1][j]
    return d[n][k]


def stirling1_signed(n, k):
    d = [[0]*(n+1) for _ in range(n+1)]
    d[0][0] = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            d[i][j] = d[i-1][j-1] - (i-1)*d[i-1][j]
    return d[n][k]


def support_count(q, r):
    # Number of subsets of q orbit-types containing r prescribed types.
    assert 0 <= r <= q
    return sum(1 for mask in range(1 << q) if all(mask & (1 << i) for i in range(r)))


def main():
    # Nontrivial finite action: S_3 on {0,1,2}.
    S3 = list(permutations(range(3)))
    for k in range(1, 7):
        q1 = orbit_count_direct(3, S3, k)
        q2 = orbit_count_burnside(3, S3, k)
        assert q1 == q2
        # Test support enumeration at small q only.
        if q1 <= 20:
            r = min(2, q1)
            assert support_count(q1, r) == 2 ** (q1-r)

    # Mayr--Ruskuc Example 1.2: |A|=2, Aut(A)=1, r=2.
    expected_b = [
        1,
        4,
        64,
        16384,
        1073741824,
        4611686018427387904,
    ]
    expected_a = [
        1,
        3,
        54,
        16038,
        1073580048,
        4611686002322639760,
    ]
    b = {}
    a = {}
    for k in range(1, 7):
        q = 2 ** k
        b[k] = 2 ** (q - 2)
        a[k] = sum(stirling1_signed(k, j) * b[j] for j in range(1, k+1))
        assert b[k] == expected_b[k-1]
        assert a[k] == expected_a[k-1]
        # Reconstruct all-tuple count from injective counts.
        assert sum(stirling2(k, j) * a[j] for j in range(1, k+1)) == b[k]
        if q <= 20:
            assert support_count(q, 2) == b[k]

    print('VERIFY_OK')


if __name__ == '__main__':
    main()
