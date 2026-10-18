#!/usr/bin/env python3
"""Exact finite enumeration of the mod-two Betti spectra of partial AG(2,3) line systems.

Only Python's standard library is required.  Vertex masks have bit index 3*x+y.
Line and face enumeration are exhaustive, including all 2**12 choices of retained lines.
"""
from collections import Counter
from itertools import combinations
import json

V = tuple((x, y) for x in range(3) for y in range(3))
IX = {v: i for i, v in enumerate(V)}
L = tuple(sorted({sum(1 << IX[p] for p in (a, b, ((2*b[0]-a[0]) % 3, (2*b[1]-a[1]) % 3))) for a, b in combinations(V, 2)}))
assert len(L) == 12 and len(set(L)) == 12
assert all(x.bit_count() == 3 for x in L)
assert all(sum(bool(x & (1 << i)) for x in L) == 4 for i in range(9))

EXPECTED = {
  0: {11: 1},
  1: {9: 12},
  2: {7: 54, 9: 12},
  3: {4: 36, 5: 72, 6: 108, 10: 4},
  4: {0: 9, 3: 288, 4: 162, 6: 36},
  5: {0: 72, 1: 108, 2: 468, 3: 144},
  6: {0: 324, 1: 528, 2: 72},
  7: {0: 684, 1: 108},
  8: {0: 495},
  9: {0: 220},
 10: {0: 66},
 11: {0: 12},
 12: {0: 1},
}

def gf2_rank(lower, upper):
    loc = {face: j for j, face in enumerate(lower)}
    pivots = {}
    for t in upper:
        col = 0
        for v in range(9):
            if t & (1 << v):
                col ^= 1 << loc[t ^ (1 << v)]
        while col:
            leading = col.bit_length() - 1
            if leading not in pivots:
                pivots[leading] = col
                break
            col ^= pivots[leading]
    return len(pivots)

def odd_rank(lower, upper, p):
    loc = {face: j for j, face in enumerate(lower)}
    pivots = {}
    for t in upper:
        col = {}
        position = 0
        for v in range(9):
            if t & (1 << v):
                col[loc[t ^ (1 << v)]] = (1 if position % 2 == 0 else p - 1)
                position += 1
        for leading in sorted(pivots):
            if leading not in col:
                continue
            a = col[leading]
            for j, b in pivots[leading].items():
                y = (col.get(j, 0) - a * b) % p
                if y:
                    col[j] = y
                else:
                    col.pop(j, None)
        if col:
            leading = min(col)
            inv = pow(col[leading], -1, p)
            pivots[leading] = {j: a * inv % p for j, a in col.items()}
    return len(pivots)

def betti(remain_lines, p=2):
    faces = [s for s in range(1, 512) if all((s & line) != line for line in remain_lines)]
    levels = [[s for s in faces if s.bit_count() == k] for k in range(1, 10)]
    while levels and not levels[-1]:
        levels.pop()
    f = [len(z) for z in levels]
    ranks = [(gf2_rank if p == 2 else lambda x, y: odd_rank(x, y, p))(levels[i], levels[i+1]) for i in range(len(levels)-1)]
    b = tuple(f[i] - (ranks[i-1] if i else 1) - (ranks[i] if i < len(ranks) else 0) for i in range(len(f)))
    assert all(x >= 0 for x in b)
    assert sum((-1)**k * f[k] for k in range(len(f))) - 1 == sum((-1)**k * b[k] for k in range(len(b)))
    return b

def is_pencil(four):
    return len(four) == 4 and any(all(l & (1 << i) for l in four) for i in range(9))

def is_parallel_class(three):
    return len(three) == 3 and (three[0] & three[1]) == (three[0] & three[2]) == (three[1] & three[2]) == 0

def main():
    spectra = {k: Counter() for k in range(13)}
    pencils = parallels = 0
    total = 0
    for deleted_mask in range(1 << len(L)):
        removed = deleted_mask.bit_count()
        remaining = tuple(line for j, line in enumerate(L) if not (deleted_mask & (1 << j)))
        b = betti(remaining, 2)
        assert b == betti(remaining, 3) == betti(remaining, 101)
        rank3 = b[3] if len(b) > 3 else 0
        spectra[removed][rank3] += 1
        if removed == 0:
            assert tuple(b[:4]) == (0, 0, 1, 11) and not any(b[4:])
        elif 1 <= removed <= 7:
            assert all(v == 0 for k, v in enumerate(b) if k != 3)
        elif removed == 8:
            extraordinary = is_pencil(remaining)
            assert (b[4] if len(b) > 4 else 0) == int(extraordinary)
            assert all(v == 0 for k, v in enumerate(b) if k != 4)
            if extraordinary:
                assert all(not any(betti(tuple(sorted(remaining + (line,))), 2)) for line in L if line not in remaining)
            pencils += extraordinary
        elif removed == 9:
            extraordinary = is_parallel_class(remaining)
            assert (b[5] if len(b) > 5 else 0) == int(extraordinary)
            assert all(v == 0 for k, v in enumerate(b) if k != 5)
            if extraordinary:
                assert all(not any(betti(tuple(sorted(remaining + (line,))), 2)) for line in L if line not in remaining)
            parallels += extraordinary
        else:
            assert not any(b)
        total += 1
    assert spectra == {k: Counter(v) for k, v in EXPECTED.items()}
    assert total == 4096 and pencils == 9 and parallels == 4
    print(json.dumps({"total_line_subsets":total,"pencils":pencils,"parallel_classes":parallels,"betti3_spectrum_by_deleted_count":{str(k):dict(sorted(v.items())) for k,v in spectra.items()},"independent_fields":[2,3,101],"status":"PASS"},indent=2))

if __name__ == '__main__':
    main()
