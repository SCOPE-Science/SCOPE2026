#!/usr/bin/env python3
"""Independent layer-plug transfer enumeration of local flip degrees in 2x2xn boxes.
No external libraries. Run: python3 verify_transfer.py
"""
from collections import Counter
import json

RING = frozenset(range(4))
EMPTY = frozenset()
ARCS = [frozenset({j, (j + 1) % 4}) for j in range(4)]


def ring_edge(s):
    assert s in ARCS
    return next(i for i, arc in enumerate(ARCS) if arc == RING - s)


# Layer record: (incoming vertical plug, outgoing plug,
#                ring-edge indices used within layer, cap flip count).
LAYERS = [
    (EMPTY, EMPTY, frozenset({0, 2}), 1),
    (EMPTY, EMPTY, frozenset({1, 3}), 1),
]
for arc in ARCS:
    e = ring_edge(arc)
    LAYERS.extend([
        (EMPTY, arc, frozenset({e}), 0),
        (arc, EMPTY, frozenset({e}), 0),
        (arc, RING - arc, EMPTY, 0),
    ])
LAYERS.extend([(EMPTY, RING, EMPTY, 0), (RING, EMPTY, EMPTY, 0)])
assert len(LAYERS) == 16

TRANSITIONS = []
for i, left in enumerate(LAYERS):
    for j, right in enumerate(LAYERS):
        if left[1] != right[0]:
            continue
        plug = left[1]
        vertical_face_count = sum(arc <= plug for arc in ARCS)
        horizontal_face_count = len(left[2] & right[2])
        TRANSITIONS.append((i, j, vertical_face_count + horizontal_face_count))


def degree_poly(n):
    d = Counter()
    for i, layer in enumerate(LAYERS):
        if layer[0] == EMPTY:
            d[(i, layer[3])] += 1
    for _ in range(1, n):
        nxt = Counter()
        for i, j, boundary_degree in TRANSITIONS:
            for (state, degree), count in d.items():
                if state == i:
                    nxt[(j, degree + boundary_degree + LAYERS[j][3])] += count
        d = nxt
    answer = Counter()
    for (i, degree), count in d.items():
        if LAYERS[i][1] == EMPTY:
            answer[degree] += count
    return dict(sorted(answer.items()))


def main():
    profiles = {}
    for n in range(1, 16):
        p = degree_poly(n)
        assert min(p) == (2*n+2)//3
        assert max(p) == 3*n-2
        assert p[max(p)] == (3 if n == 2 else 2)
        if n%3 == 0:
            assert p[min(p)] == 4*3**(n//3-1)
        if n <= 8:
            profiles[str(n)] = {str(d): count for d, count in p.items()}
    print(json.dumps(profiles, sort_keys=True, separators=(',', ':')))
    print('TRANSFER_VERIFY_OK')


if __name__ == '__main__':
    main()
