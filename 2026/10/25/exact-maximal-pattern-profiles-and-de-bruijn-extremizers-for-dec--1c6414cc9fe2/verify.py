"""Exact finite checks for the necklace-profile theorem; Python 3 standard library only.

The universal result is established analytically; finite checks test the
finite combinatorial invariants and explicit de Bruijn constructions.
"""
from itertools import product


def debruijn(q, order):
    """Return a cyclic q-ary de Bruijn word of order `order`."""
    a = [0] * (q * order + 1)
    out = []
    def db(t, p):
        if t > order:
            if order % p == 0:
                out.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, q):
                a[t] = j
                db(t + 1, t)
    db(1, 1)
    assert len(out) == q ** order
    cyc = out + out[:order - 1]
    assert len({tuple(cyc[i:i + order]) for i in range(q ** order)}) == q ** order
    return out


def signature_count(c, positions):
    m = len(c) + 1
    seen = set()
    for r in range(m):
        if all((r + s) % m != 0 for s in positions):
            seen.add(tuple(c[(r + s) % m - 1] for s in positions))
    return len(seen)


def max_for_c(c):
    m = len(c) + 1
    by_size = [0] * (m + 1)
    for mask in range(1, 1 << m):
        S = tuple(j for j in range(m) if mask >> j & 1)
        by_size[len(S)] = max(by_size[len(S)], signature_count(c, S))
    return by_size


def threshold(m, q):
    return next(s for s in range(1, m + 1) if q ** s >= m - s)


def target(m, q, k):
    return min(q ** k, m - threshold(m, q))


def check():
    cases = 0
    for q, lastm in ((2, 9), (3, 7), (4, 6)):
        for m in range(2, lastm + 1):
            observed = [0] * (m + 1)
            for c in product(range(q), repeat=m - 1):
                counts = max_for_c(c)
                for k in range(1, m + 1):
                    observed[k] = max(observed[k], max(counts[1:k + 1]))
            for k in range(1, m + 1):
                assert observed[k] == target(m, q, k), (q, m, k, observed[k])
                # Witness by a length-(m-1) prefix of an order-t de Bruijn necklace.
                t = min(k, threshold(m, q))
                cyc = debruijn(q, t)
                c = tuple(cyc[i % len(cyc)] for i in range(m - 1))
                assert signature_count(c, range(t)) == min(m - t, q ** t)
                assert min(m - t, q ** t) == target(m, q, k)
                cases += 1
    # Non-extremal decoration: fully enumerate its all-sample residue signature profile.
    assert max(max_for_c((0, 1, 1, 0))[1:]) == 3
    # A four-letter length-12 example saturates 2k+8 for every k>=3.
    m, q, k = 12, 2, 3
    c = tuple((debruijn(q, k) * 2)[:m - 1])
    assert signature_count(c, range(k)) == 8
    assert target(m, q, k) == 8
    print('VERIFY_OK finite_extremal_instances=' + str(cases))

if __name__ == '__main__':
    check()
