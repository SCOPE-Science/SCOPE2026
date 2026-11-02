"""Independent graph-level enumeration for minimal defensive alliances of crown graphs.

Run with Python 3.8 or later: python verify.py
All vertex subsets are checked for each n in the stated finite verification range.
"""
from collections import Counter
from math import comb


def expected(n):
    t = (n - 1) // 2
    s = t + 1
    d = comb(n, t) * comb(n - t, t)
    h = lambda r: comb(n, s) * comb(s, r) * (comb(n-s, s-r) if 0 <= s-r <= n-s else 0)
    local = Counter({2*t: d, 2*s: sum(h(r) for r in range(2, s+1))})
    global_min = Counter({2*t: d, 2*s: sum(h(r) for r in range(3, s+1))})
    return +local, +global_min, h(2), t, s


def actual(n):
    order = 2*n
    adjacency = [0] * order
    for i in range(n):
        for j in range(n):
            if i != j:
                adjacency[i] |= 1 << (n+j)
                adjacency[n+j] |= 1 << i
    assert all(mask.bit_count() == n-1 for mask in adjacency)

    limit = 1 << order
    alliances = bytearray(limit)
    has_proper_alliance = bytearray(limit)
    locally = Counter()
    globally_min = Counter()
    local_not_global = 0

    for mask in range(1, limit):
        remainder = mask
        valid = True
        while remainder:
            bit = remainder & -remainder
            vertex = bit.bit_length() - 1
            if 2 * (adjacency[vertex] & mask).bit_count() + 1 < n - 1:
                valid = False
                break
            remainder -= bit
        if valid:
            alliances[mask] = 1

    # Proper-subset existence is computed only from smaller masks.
    # Unlike local minimality, global minimality must inspect all proper subsets.
    for mask in range(1, limit):
        remainder = mask
        removable = False
        nested = False
        while remainder:
            bit = remainder & -remainder
            child = mask ^ bit
            if alliances[child]:
                removable = True
                nested = True
            if has_proper_alliance[child]:
                nested = True
            remainder -= bit
        has_proper_alliance[mask] = nested
        if alliances[mask] and not removable:
            locally[mask.bit_count()] += 1
            x = mask & ((1 << n) - 1)
            y = mask >> n
            r = (x & y).bit_count()
            lx, ly = x.bit_count(), y.bit_count()
            t, s = (n - 1)//2, (n + 1)//2
            assert (r == 0 and lx == ly == t) or (r >= 2 and lx == ly == s)
            if not nested:
                globally_min[mask.bit_count()] += 1
                assert r == 0 or r >= 3
            else:
                local_not_global += 1
                assert r == 2 and lx == ly == s
    return +locally, +globally_min, local_not_global, limit-1


def main():
    total = 0
    for n in range(3, 11):
        local, global_min, difference, tested = actual(n)
        el, eg, ed, t, s = expected(n)
        assert local == el, (n, 'local', local, el)
        assert global_min == eg, (n, 'global', global_min, eg)
        assert difference == ed, (n, 'difference', difference, ed)
        central = comb(n, s)
        if n % 2:
            assert sum(local.values()) == central**2
        else:
            assert 2*sum(local.values()) == 2*central**2 - central*(2 + (n//2)**2)
        print(f'n={n} locally={dict(local)} globally={dict(global_min)} local_only={difference}')
        total += tested
    print(f'VERIFY_OK graph_orders=8 tested_nonempty_subsets={total} all_formulas_agree=true')


if __name__ == '__main__':
    main()
