"""Finite cross-checks for distributed-knowledge rare-defect bounds.

Uses direct partition enumeration and an independent signed-Stirling formula.
No asymptotic conclusion is inferred from finite checks.
"""
from itertools import product
from math import comb


def partitions(n):
    if n == 0:
        yield ()
        return
    for p in partitions(n - 1):
        yield p + (max(p, default=-1) + 1,)
        for block in range(max(p, default=-1) + 1):
            yield p + (block,)


def bells(n):
    b = [1]
    for k in range(1, n + 1):
        b.append(sum(comb(k - 1, j) * b[j] for j in range(k)))
    return b


def signed_first_kind(n):
    rows = [[1]]
    for k in range(1, n + 1):
        prev = rows[-1]
        row = [0] * (k + 1)
        for j, v in enumerate(prev):
            row[j] -= (k - 1) * v
            row[j + 1] += v
        rows.append(row)
    return rows[-1]


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def failure_polynomial(n, r):
    B = bells(n)
    triv = []
    for k in range(n + 1):
        row = signed_first_kind(k)
        triv.append(sum(row[j] * B[j] ** r for j in range(k + 1)))
    result = [0] * (n + 1)
    for part in partitions(n):
        blocks = {}
        for v, b in enumerate(part):
            blocks[b] = blocks.get(b, 0) + 1
        poly = [1]
        for size in blocks.values():
            phi = [2] + [comb(size, t) for t in range(1, size)]
            poly = poly_mul(poly, phi)
        for i, coeff in enumerate(poly):
            result[i] += triv[len(blocks)] * coeff
    return result


def check_one(n, r):
    parts = list(partitions(n))
    B = bells(n)
    assert len(parts) == B[n]
    N = comb(n, 2)
    success, one_pair, bad_valuations = 0, 0, 0
    actual_hist = [0] * (n + 1)
    for tuple_parts in product(parts, repeat=r):
        equiv_pairs = [
            (a, b)
            for a in range(n) for b in range(a + 1, n)
            if all(part[a] == part[b] for part in tuple_parts)
        ]
        if equiv_pairs:
            success += 1
            if len(equiv_pairs) == 1:
                one_pair += 1
        for mask in range(1 << n):
            invalid_worlds = set()
            for a, b in equiv_pairs:
                a_true = (mask >> a) & 1
                b_true = (mask >> b) & 1
                if a_true and not b_true:
                    invalid_worlds.add(a)
                if b_true and not a_true:
                    invalid_worlds.add(b)
            actual_hist[len(invalid_worlds)] += 1
            if invalid_worlds:
                bad_valuations += 1
    den = B[n] ** r
    assert actual_hist == failure_polynomial(n, r), (n, r, actual_hist, failure_polynomial(n, r))
    assert sum(actual_hist) == den * (1 << n)
    signed = signed_first_kind(n)
    minimal_meet_count = sum(signed[j] * B[j] ** r for j in range(n + 1))
    assert den - success == minimal_meet_count
    if n >= 2:
        pnum = B[n - 1]
        qnum = B[n - 2]
        upper_num = N * pnum ** r
        second_num = comb(N, 2) * qnum ** r
        assert upper_num - second_num <= success <= upper_num
        # Every single-doubleton meet corresponds to a chosen pair and
        # a trivial meet of r quotient partitions on n-1 points.
        bs = B[:-1]
        s = signed_first_kind(n - 1)
        minimal_quotient = sum(s[j] * bs[j] ** r for j in range(n))
        assert one_pair == N * minimal_quotient
        # The valuation probability has exact denominator 2^n times den.
        assert (2 * N * pnum ** r - comb(N, 2) * qnum ** r) * (1 << (n - 2)) <= bad_valuations
        assert bad_valuations <= N * pnum ** r * (1 << (n - 1))
    print(f'n={n}, r={r}, total={den}, bad_frames={success}, '
          f'single_doubleton_frames={one_pair}, bad_valuation_pairs={bad_valuations}')


if __name__ == '__main__':
    for n, r in [(2, 3), (3, 3), (4, 3), (5, 3), (3, 4), (4, 4)]:
        check_one(n, r)
    print('ALL_CHECKS_OK')
