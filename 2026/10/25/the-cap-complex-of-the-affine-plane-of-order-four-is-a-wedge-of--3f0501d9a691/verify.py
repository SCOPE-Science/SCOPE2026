#!/usr/bin/env python3
"""Finite certificate checker for the AG(2,4) cap complex.

Usage: python3 verify.py [directory containing MATCHING.csv]
Only Python 3 standard-library modules are required.
"""
import collections
import itertools
import pathlib
import sys

POWER = {1: 0, 2: 1, 3: 2}

def mul(a, b):
    if a == 0 or b == 0:
        return 0
    return (1, 2, 3)[(POWER[a] + POWER[b]) % 3]

def points():
    return tuple(itertools.product(range(4), repeat=2))

def lines(ps):
    # The unique degree-one polynomials and vertical lines in F_4^2.
    out = []
    for slope in range(4):
        for intercept in range(4):
            out.append(tuple(i for i, (x, y) in enumerate(ps)
                             if y == (mul(slope, x) ^ intercept)))
    for xval in range(4):
        out.append(tuple(i for i, (x, y) in enumerate(ps) if x == xval))
    assert len(out) == 20 and len(set(out)) == 20
    assert all(len(line) == 4 for line in out)
    # Each two points determine exactly one line.
    pair_counts = collections.Counter(
        pair for line in out for pair in itertools.combinations(line, 2))
    assert len(pair_counts) == 120 and set(pair_counts.values()) == {1}
    return out

def forbidden_triples(ps, ls):
    from_lines = {
        sum(1 << i for i in t)
        for line in ls for t in itertools.combinations(line, 3)
    }
    # Separate determinant collinearity calculation.
    from_det = set()
    for a, b, c in itertools.combinations(range(16), 3):
        x1, y1 = ps[a]
        x2, y2 = ps[b]
        x3, y3 = ps[c]
        if mul(x2 ^ x1, y3 ^ y1) == mul(x3 ^ x1, y2 ^ y1):
            from_det.add((1 << a) | (1 << b) | (1 << c))
    assert from_lines == from_det and len(from_lines) == 80
    return frozenset(from_lines)

def face_set(forbidden):
    good = set()
    for mask in range(1, 1 << 16):
        if not any(mask & t == t for t in forbidden):
            good.add(mask)
    return good

def matching(faces):
    rem = set(faces)
    pairs = []
    for v in range(16):
        bit = 1 << v
        for low in sorted(rem):
            high = low | bit
            if (low & bit) or high not in rem:
                continue
            rem.remove(low)
            rem.remove(high)
            pairs.append((low, high))
    return pairs, rem

def check_acyclic(faces, pairs):
    # Hasse graph orientation: unmatched cover edges point downwards,
    # matched edges point upwards. Topological sort decides acyclicity.
    low_to_high = dict(pairs)
    assert len(low_to_high) == len(pairs)
    matched = set(pairs)
    indeg = dict.fromkeys(faces, 0)
    arcs = {face: [] for face in faces}
    incidences = 0
    for hi in faces:
        for i in range(16):
            bit = 1 << i
            if not hi & bit:
                continue
            lo = hi ^ bit
            if lo == 0:
                continue
            incidences += 1
            assert lo in faces
            if (lo, hi) in matched:
                start, end = lo, hi
            else:
                start, end = hi, lo
            arcs[start].append(end)
            indeg[end] += 1
    queue = collections.deque(s for s in faces if indeg[s] == 0)
    reached = 0
    while queue:
        s = queue.popleft()
        reached += 1
        for t in arcs[s]:
            indeg[t] -= 1
            if indeg[t] == 0:
                queue.append(t)
    assert reached == len(faces), (reached, len(faces))
    return incidences

def main():
    ps = points()
    ls = lines(ps)
    tris = forbidden_triples(ps, ls)
    faces = face_set(tris)
    vector = tuple(sum(mask.bit_count() == k for mask in faces) for k in range(1, 7))
    assert vector == (16, 120, 480, 840, 288, 48)
    assert len(faces) == 1792
    facet_counts = collections.Counter(
        mask.bit_count() for mask in faces
        if all((mask | (1 << i)) not in faces
               for i in range(16) if not mask & (1 << i)))
    assert facet_counts == {4: 120, 6: 48}, facet_counts
    pairs, critical = matching(faces)
    assert len(pairs) == 783
    assert len(critical) == 226
    counts = collections.Counter(mask.bit_count()-1 for mask in critical)
    assert counts == {0: 1, 3: 225}, counts
    actual_csv = ''.join(f'{lo},{hi}\n' for lo, hi in pairs)
    path = (pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(__file__).parent) / 'MATCHING.csv'
    expected_csv = path.read_text(encoding='utf8')
    assert actual_csv == expected_csv, 'embedded matching certificate differs'
    assert all(hi.bit_count() == lo.bit_count()+1 and lo & hi == lo for lo,hi in pairs)
    assert len(set(s for pair in pairs for s in pair)) == 2 * len(pairs)
    ninc = check_acyclic(faces, pairs)
    assert ninc == 6768
    chi = sum((-1)**d * vector[d] for d in range(6))
    assert chi == 1 - 225
    print('POINTS=16 LINES=20 FORBIDDEN_TRIPLES=80')
    print('F_VECTOR=16,120,480,840,288,48 FACETS_4=120 FACETS_6=48')
    print('FACES=1792 MATCHED_PAIRS=783 CRITICAL_0=1 CRITICAL_3=225')
    print('INCIDENCES=6768 MATCHING_ACYCLIC=TRUE EULER_CHARACTERISTIC=-224')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
