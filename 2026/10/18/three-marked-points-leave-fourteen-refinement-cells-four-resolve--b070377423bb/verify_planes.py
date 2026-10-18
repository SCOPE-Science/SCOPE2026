#!/usr/bin/env python3
"""Exact independent colour-refinement checks for prime-order projective planes."""
from collections import Counter


def projective_points(p):
    values = set()
    for x in range(p):
        for y in range(p):
            for z in range(p):
                vector = (x, y, z)
                if not any(vector):
                    continue
                inv = pow(next(t for t in vector if t), -1, p)
                values.add(tuple(t * inv % p for t in vector))
    return sorted(values)


def incidence_graph(p):
    pts = projective_points(p)
    n = len(pts)
    graph = [set() for _ in range(2 * n)]
    for i, point in enumerate(pts):
        for j, line in enumerate(pts):
            if sum(a*b for a, b in zip(point, line)) % p == 0:
                graph[i].add(n+j)
                graph[n+j].add(i)
    assert all(len(s) == p+1 for s in graph)
    return pts, graph


def refine(graph, colours):
    colours = list(colours)
    for steps in range(len(colours)+1):
        signature = [(colours[i], tuple(sorted(Counter(colours[j] for j in nbrs).items())))
                     for i, nbrs in enumerate(graph)]
        ids = {key: idx for idx, key in enumerate(sorted(set(signature)))}
        nxt = [ids[sig] for sig in signature]
        if nxt == colours:
            return colours, steps
        colours = nxt
    raise AssertionError('refinement did not stabilize')


def marked_colours(pts, mark_vectors):
    n = len(pts)
    marks = [pts.index(x) for x in mark_vectors]
    assert len(marks) == len(set(marks))
    return [marks.index(i)+1 if i in marks else 0 for i in range(n)] + [len(marks)+1]*n

if __name__ == '__main__':
    triangle = ((1,0,0), (0,1,0), (0,0,1))
    frame = triangle + ((1,1,1),)
    for p in (2,3,5,7,11,13):
        pts, graph = incidence_graph(p)
        n = len(pts)
        c3, rounds3 = refine(graph, marked_colours(pts,triangle))
        count3 = Counter(c3)
        expected = sorted([1]*6 + [p-1]*6 + [(p-1)**2]*2)
        assert len(count3) == 14
        assert sorted(count3.values()) == expected
        assert rounds3 == 2
        c4, rounds4 = refine(graph, marked_colours(pts,frame))
        assert len(set(c4)) == 2*n
        print(f'PASS p={p} points={n} triangle_classes=14 triangle_rounds={rounds3} '
              f'frame_classes={2*n} frame_rounds={rounds4}')
    print('VERIFY_PLANES_OK')
