#!/usr/bin/env python3
"""Standalone exact finite consistency checks for evil-integer tail semigroups."""
from collections import Counter

def verify(r):
    q = 1 << r
    m = 2 * q + 1
    limit = 6 * q + 3
    generators = [k for k in range(m, limit + 1) if k.bit_count() % 2 == 0]
    reachable = bytearray(limit + 1)
    reachable[0] = 1
    for g in generators:
        for x in range(g, limit + 1):
            if reachable[x - g]:
                reachable[x] = 1
    actual = [n for n in range(1, limit + 1) if not reachable[n]]
    predicted = list(range(1, 2*q + 1)) + [n for n in range(2*q+1, 4*q+1) if n.bit_count() % 2]
    assert actual == predicted, (r, set(actual) ^ set(predicted))
    assert len(actual) == 3*q and max(actual) == 4*q
    runs = []
    lo = prev = actual[0]
    for n in actual[1:]:
        if n > prev + 1:
            runs.append((lo, prev))
            lo = n
        prev = n
    runs.append((lo, prev))
    assert runs[0] == (1, 2*q)
    counts = Counter(hi-lo+1 for lo,hi in runs[1:])
    assert counts == Counter({1:(q+2*(-1)**r)//3, 2:(q-(-1)**r)//3}), (r,counts)
    assert all(reachable[n] for n in range(4*q+1,limit+1))
    return len(actual),len(generators),counts

if __name__ == '__main__':
    gaps=generators=0
    for r in range(2,11):
        ng,nc,counts = verify(r)
        gaps+=ng;generators+=nc
        print(f'r={r} q={1<<r} gaps={ng} generators={nc} singleton_runs={counts[1]} double_runs={counts[2]} PASS')
    print(f'ALL PASS: 9 families, {gaps} gaps, {generators} candidate generators.')
