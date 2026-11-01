#!/usr/bin/env python3
"""Exact integer, standalone verification for the cap complex of PG(3,2).

Usage: python3 verify_cap.py
Requires only Python 3 standard library and morse_certificate.json.
"""
import collections
import functools
import json
import math
from pathlib import Path


def faces_and_lines():
    lines = set()
    for a in range(1, 16):
        for b in range(a + 1, 16):
            c = a ^ b
            lines.add((1 << (a - 1)) | (1 << (b - 1)) | (1 << (c - 1)))
    assert len(lines) == 35
    faces = [m for m in range(1, 1 << 15) if all((m & L) != L for L in lines)]
    assert collections.Counter(m.bit_count() - 1 for m in faces) == {
        0: 15, 1: 105, 2: 420, 3: 945, 4: 1008, 5: 420, 6: 120, 7: 15
    }
    assert len(faces) == 3048
    return faces, lines


def oriented_boundary(m):
    i = 0
    y = m
    while y:
        b = y & -y
        y -= b
        yield m - b, 1 if i % 2 == 0 else -1
        i += 1


def verify():
    faces, lines = faces_and_lines()
    face_set = set(faces)
    data = json.loads((Path(__file__).resolve().parent / 'morse_certificate.json').read_text(encoding='utf-8'))
    assert data['vertex_encoding'] == 'integer i in 1..15 corresponds to nonzero vector i in F_2^4, face mask bit (i-1)'
    pairs = [tuple(p) for p in data['pairs']]
    critical = data['critical']
    assert len(pairs) == 1484 and len(critical) == 80
    assert all(isinstance(p, tuple) and len(p) == 2 for p in pairs)
    assert all(a in face_set and b in face_set and b.bit_count() == a.bit_count()+1 and (a & b) == a for a,b in pairs)
    matched = [v for p in pairs for v in p]
    assert len(set(matched)) == len(matched)
    assert len(set(critical)) == len(critical) and not(set(critical) & set(matched))
    assert set(critical).union(matched) == face_set
    assert collections.Counter(m.bit_count()-1 for m in critical) == {0: 1, 3: 1, 4: 78}
    pair_edges = set(pairs)
    arrows = collections.defaultdict(list)
    indeg = dict.fromkeys(faces,0)
    num_arrows = 0
    for hi in faces:
        for lo,_ in oriented_boundary(hi):
            if lo == 0:
                continue
            if (lo,hi) in pair_edges:
                src,dst=lo,hi
            else:
                src,dst=hi,lo
            arrows[src].append(dst)
            indeg[dst]+=1
            num_arrows+=1
    assert num_arrows == 13770
    queue=collections.deque(f for f in faces if indeg[f]==0)
    visited=0
    while queue:
        u=queue.popleft()
        visited+=1
        for v in arrows[u]:
            indeg[v]-=1
            if indeg[v] == 0:
                queue.append(v)
    assert visited == len(faces), f'Gradient cycle found; visited {visited}'

    critical_set = set(critical)
    lower_to_upper=dict(pairs)
    upper_set={v for _,v in pairs}
    c3=[f for f in critical if f.bit_count() == 4]
    c4=[f for f in critical if f.bit_count() == 5]
    assert len(c3)==1 and len(c4)==78
    c3_mask=c3[0]

    @functools.lru_cache(maxsize=None)
    def to_critical3(face):
        """Algebraic Morse projection of a 3-cell to the unique critical 3-cell."""
        assert face.bit_count() == 4
        if face in critical_set:
            return int(face == c3_mask)
        if face in upper_set:
            return 0
        assert face in lower_to_upper
        upper=lower_to_upper[face]
        faces4=dict(oriented_boundary(upper))
        incidence=faces4.pop(face)
        assert abs(incidence)==1
        return -incidence*sum(sign*to_critical3(other) for other,sign in faces4.items())

    coeffs=[sum(sign*to_critical3(face) for face,sign in oriented_boundary(c)) for c in c4]
    histogram=collections.Counter(coeffs)
    expected={0:32, 2:20, -2:18, 4:4, -4:3, 6:1}
    assert histogram == expected, (histogram,expected)
    assert math.gcd(*coeffs)==2
    # No other differential is possible in the Morse complex. 1-dimensional
    # CW in degree 3 and 78 cells in degree 4, attached by these degrees.
    assert sum(histogram.values())==78
    print('POINTS=15 LINES=35 F_VECTOR=15,105,420,945,1008,420,120,15')
    print(f'FACES={len(faces)} ARROWS={num_arrows} ACYCLIC_VISITED={visited}')
    print(f'PAIRS={len(pairs)} CRITICAL_0=1 CRITICAL_3=1 CRITICAL_4=78')
    print('SIGNED_MORSE_BOUNDARY_HISTOGRAM='+str(sorted(histogram.items())))
    print('MORSE_BOUNDARY_GCD=2')
    print('REDUCED_INTEGRAL_H3=Z/2 REDUCED_INTEGRAL_H4=Z^77')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
