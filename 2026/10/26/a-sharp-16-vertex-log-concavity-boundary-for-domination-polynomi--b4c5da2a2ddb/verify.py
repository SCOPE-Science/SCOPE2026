#!/usr/bin/env python3
"""Exact census of domination-polynomial log-concavity in trivially perfect graphs.

The recurrence exhausts unlabelled rooted-forest shapes. The transitive closure
of every rooted forest is trivially perfect, and every trivially perfect graph
has such a representation. The proof of exhaustive generation is in RESULT.md.
"""
from math import comb


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return tuple(out)


def violations(a):
    return tuple(k for k in range(1, len(a)-1)
                 if a[k]*a[k] < a[k-1]*a[k+1])


def exact_forest_census():
    rooted = []  # (order, domination polynomial) for rooted-tree shapes
    forests = [{(): (1,)}]  # canonical sorted multisets of rooted-tree indices
    connected_counts, forest_counts = [], [1]
    failed_connected, failed_forests = [], []
    for n in range(1, 17):
        num_before = len(rooted)
        # Root a forest of order n-1; root belongs to every graph component.
        for components, p in forests[n-1].items():
            if n == 1:
                poly = (0, 1)
            else:
                poly = tuple((comb(n-1,k-1) if k else 0)
                             + (p[k] if k < len(p) else 0)
                             for k in range(n+1))
            rooted.append((n, poly))
            for k in violations(poly):
                failed_connected.append((n, components, k, poly))
        connected_counts.append(len(rooted)-num_before)
        # Every forest is a unique multiset of rooted trees. The newly
        # appended tree index must be >= the last previous index.
        all_forests = {}
        for typ, (size, p) in enumerate(rooted):
            for old, q in forests[n-size].items():
                if old and old[-1] > typ:
                    continue
                choice = old + (typ,)
                all_forests[choice] = multiply(q, p)
        forests.append(all_forests)
        forest_counts.append(len(all_forests))
        for components, p in all_forests.items():
            for k in violations(p):
                failed_forests.append((n, components, k, p))
    assert connected_counts == [1,1,2,4,9,20,48,115,286,719,1842,
                                4766,12486,32973,87811,235381]
    assert forest_counts == [1,1,2,4,9,20,48,115,286,719,1842,
                             4766,12486,32973,87811,235381,634847]
    assert len(failed_connected) == len(failed_forests) == 1
    nc, fc, ix, poly = failed_connected[0]
    nf, ff, jx, fpoly = failed_forests[0]
    assert nc == nf == 16 and ix == jx == 2 and poly == fpoly
    assert poly[:5] == (0, 1, 15, 230, 1205)
    assert len(ff) == 1 and rooted[ff[0]][1] == poly
    assert len(fc) == 3 and len(set(fc)) == 1
    assert rooted[fc[0]][0] == 5
    assert rooted[fc[0]][1] == (0, 5, 10, 10, 5, 1)
    return poly, connected_counts, forest_counts


def brute_bouquet():
    n = 16
    nbr = [0]*n
    for block in range(3):
        members = list(range(1+5*block, 6+5*block))
        for v in members:
            for w in members + [0]:
                if v != w:
                    nbr[v] |= 1 << w
                    nbr[w] |= 1 << v
    closed = [nbr[v] | (1<<v) for v in range(n)]
    count = [0]*(n+1)
    for mask in range(1<<n):
        if all(mask & N for N in closed):
            count[bin(mask).count("1")] += 1
    assert count[:5] == [0, 1, 15, 230, 1205]
    return tuple(count)


def main():
    a, connected, forests = exact_forest_census()
    assert a == brute_bouquet()
    assert a[2]*a[2] == 225 < a[1]*a[3] == 230
    print('VERIFY_OK connected_through_16=%d forests_through_16=%d bad_at_16=1' %
          (sum(connected), sum(forests[1:])))
    print('CONNECTED_BY_ORDER=' + repr(connected))
    print('FORESTS_BY_ORDER=' + repr(forests[1:]))
    print('WITNESS_POLYNOMIAL=' + repr(a))


if __name__ == '__main__':
    main()
