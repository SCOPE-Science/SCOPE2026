#!/usr/bin/env python3
"""Independent finite-census reconstruction using composition breakpoints."""
from itertools import combinations
from math import comb


def partitions_via_breakpoints(n):
    # Every ordered composition corresponds to a subset of the n-1 cut positions.
    # Sorting its parts creates every integer partition, with no missing partition.
    output = set()
    for mask in range(1 << (n - 1)):
        parts, piece = [], 1
        for pos in range(n - 1):
            if (mask >> pos) & 1:
                parts.append(piece)
                piece = 1
            else:
                piece += 1
        parts.append(piece)
        output.add(tuple(sorted(parts, reverse=True)))
    return output


def rich_numer(profile, n, k):
    return sum(v * (comb(n-v, k-1) if k-1 <= n-v else 0) for v in profile)


def comparison(a, b, n):
    signs = []
    for k in range(1, n + 1):
        delta = rich_numer(b, n, k) - rich_numer(a, n, k)
        if delta != 0:
            signs.append(1 if delta > 0 else -1)
    return sum(signs[t] != signs[t+1] for t in range(len(signs)-1))


def is_majorized(a, b):
    ca, cb = 0, 0
    for i in range(len(a) - 1):
        ca += a[i]; cb += b[i]
        if ca < cb:
            return False
    return a != b


def main():
    critical=[]
    pairs = 0
    for n in range(2,18):
        p = partitions_via_breakpoints(n)
        groups = {}
        for x in p:
            groups.setdefault(len(x), []).append(x)
        for group in groups.values():
            for x,y in combinations(group,2):
                if is_majorized(x,y): u,v = x,y
                elif is_majorized(y,x): u,v = y,x
                else: continue
                pairs += 1
                t = comparison(u,v,n)
                if t > 1:
                    critical.append((n,u,v,t))
    assert critical==[(17,(9,4,3,1),(7,6,2,2),3)], critical
    print('Breakpoints-derived partition enumeration: PASS; comparable pairs:',pairs)
    print('Unique multi-reversal:',critical[0])

if __name__=='__main__':main()
