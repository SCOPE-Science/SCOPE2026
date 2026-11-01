"""Exact finite-field checks for nearest-neighbor binary coupled cat maps.

Run with: python3 verify_binary_cycles.py
Uses only the Python standard library. Finite checks corroborate, but do not
replace, the all-size algebraic proof.
"""

def rotate(mask, delta, n):
    delta %= n
    bits = (1 << n) - 1
    if not delta:
        return mask & bits
    return ((mask << delta) | (mask >> (n - delta))) & bits


def couple(mask, n):
    return rotate(mask, 1, n) ^ rotate(mask, n - 1, n)


def advance(q, p, n):
    cp = couple(p, n)
    return q ^ cp, p ^ couple(q, n) ^ couple(cp, n)


def common_spatial_period(q, p, n):
    d = 1
    while d <= n:
        if rotate(q, d, n) == q and rotate(p, d, n) == p:
            return d
        d *= 2
    raise AssertionError("missing spatial period")


def orbit_period(q, p, n):
    init = (q, p)
    for t in range(1, n // 2 + 1):
        q, p = advance(q, p, n)
        if (q, p) == init:
            return t
    raise AssertionError("missing temporal return")


def rank_binary_rows(rows):
    pivots = {}
    for r in rows:
        while r:
            j = r.bit_length() - 1
            if j in pivots:
                r ^= pivots[j]
            else:
                pivots[j] = r
                break
    return len(pivots)


def fixed_count_by_rank(n, steps):
    dim = 2 * n
    rows = [0] * dim
    for column in range(dim):
        q = (1 << column) if column < n else 0
        p = (1 << (column - n)) if column >= n else 0
        initial = q | (p << n)
        for _ in range(steps):
            q, p = advance(q, p, n)
        diff = (q | (p << n)) ^ initial
        for i in range(dim):
            if (diff >> i) & 1:
                rows[i] |= 1 << column
    return 1 << (dim - rank_binary_rows(rows))


def run():
    for n in (4, 8):
        census = {}
        for q in range(1 << n):
            for p in range(1 << n):
                spatial = common_spatial_period(q, p, n)
                temporal = orbit_period(q, p, n)
                assert temporal == max(1, spatial // 2)
                census[temporal] = census.get(temporal, 0) + 1
        assert sum(census.values()) == 1 << (2 * n)
        print("exhaustive", n, "states", 1 << (2 * n), "period census", sorted(census.items()))
    for n in (4, 8, 16, 32):
        fixed_previous = 0
        for j in range(n.bit_length() - 1):
            k = 1 << j
            observed = fixed_count_by_rank(n, k)
            expected = 1 << min(2 * n, 1 << (j + 2))
            assert observed == expected, (n, k, observed, expected)
            if j == n.bit_length() - 2:
                assert observed == 1 << (2 * n)
                assert fixed_previous < observed
            fixed_previous = observed
        print("rank-and-order", n, "passed; order", n // 2)
    print("ALL CHECKS PASSED")


if __name__ == '__main__':
    run()
