"""Finite checks for the two-agent strong-disagreement depth-one theorem.

Run with Python 3.10+; no third-party packages are needed.
"""
from itertools import product


def d_signature(m, x, y):
    universe = (1 << m) - 1
    return bytes(
        int(((x & (universe ^ p)) == 0 and (y & p) == 0)
            or ((y & (universe ^ p)) == 0 and (x & p) == 0))
        for p in range(1 << m)
    )


def check_quotients():
    for m in (1, 2, 3, 4, 8):
        buckets = {}
        for x, y in product(range(1, 1 << m), repeat=2):
            sig = d_signature(m, x, y)
            canonical = None if (x & y) else tuple(sorted((x, y)))
            if sig in buckets:
                assert buckets[sig] == canonical, (m, x, y, buckets[sig])
            else:
                buckets[sig] = canonical
        predicted = (3 ** m - 2 ** (m + 1) + 3) // 2
        assert len(buckets) == predicted, (m, len(buckets), predicted)
        assert len([a for a in buckets.values() if a is None]) == 1
        print(f"m={m}: {len(buckets)} support signatures; formula exponent={m*predicted}")


def kd45(rows):
    n = len(rows)
    assert all(len(a) > 0 for a in rows)
    for x in range(n):
        for y in rows[x]:
            assert rows[y] == rows[x], (x, y, rows)


def disagree(values, rel1, rel2, event):
    return [
        (all(event[v] for v in rel1[u]) and all(not event[v] for v in rel2[u]))
        or (all(not event[v] for v in rel1[u]) and all(event[v] for v in rel2[u]))
        for u in range(len(values))
    ]


def check_depth_two():
    vals = (True, False)
    rel2 = ((1,), (1,))
    first1 = ((0,), (1,))
    first2 = ((0,), (0,))
    for rel1 in (first1, first2):
        kd45(rel1)
        kd45(rel2)
    d_one = disagree(vals, first1, rel2, vals)
    d_two = disagree(vals, first2, rel2, vals)
    assert d_one[0] and d_two[0]
    assert disagree(vals, first1, rel2, d_one)[0]
    assert not disagree(vals, first2, rel2, d_two)[0]
    for p in (False, True):
        assert not disagree((p,), ((0,),), ((0,),), (p,))[0]
    print("two-world depth-two separation verified")


if __name__ == '__main__':
    check_quotients()
    check_depth_two()
    print("ALL_CHECKS_OK")
