from itertools import combinations


def rank(rows, n):
    rows = list(rows)
    r = 0
    for bit in range(n - 1, -1, -1):
        pivot = next((i for i in range(r, len(rows)) if (rows[i] >> bit) & 1), None)
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i] >> bit) & 1):
                rows[i] ^= rows[r]
        r += 1
    return r


def span(basis):
    out = {0}
    for v in basis:
        out |= {x ^ v for x in tuple(out)}
    return frozenset(out)


def all_subspaces(n, k):
    seen = set()
    nonzero = range(1, 1 << n)
    for basis in combinations(nonzero, k):
        if rank(basis, n) != k:
            continue
        c = span(basis)
        if c not in seen:
            seen.add(c)
            yield c


def wt(x):
    return x.bit_count()


checked = 0
gap_hits = 0
for n in range(1, 7):
    for k in range(1, min(3, n) + 1):
        for C in all_subspaces(n, k):
            checked += 1
            ws = [wt(c) for c in C if c]
            d = min(ws)
            M = n - k + 1
            if any(d < w <= M for w in ws):
                continue
            gap_hits += 1
            assert all(w % d == 0 for w in ws)
            if d > 1 and d % 2 == 1:
                assert k <= 2
                if k == 2:
                    assert n == 2 * d
print(f"PASS checked {checked} codes; full-gap cases {gap_hits}")
