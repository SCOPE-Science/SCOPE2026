"""Reproduce exact finite edge-geodesic covers of Fibonacci cubes.

Usage: python verify_fibonacci_geodesics.py fibonacci_geodesic_certificate.json
Dependencies: Python >= 3.8 standard library only.
"""
import itertools
import json
import sys


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def graph(n):
    vertices = {
        ''.join(bits)
        for bits in itertools.product('01', repeat=n)
        if all(not (bits[i] == bits[i+1] == '1') for i in range(n-1))
    }
    edges = set()
    for u in vertices:
        for i in range(n):
            v = u[:i] + ('1' if u[i] == '0' else '0') + u[i+1:]
            if v in vertices:
                edges.add(tuple(sorted((u, v))))
    return vertices, edges


def check(certificate):
    assert set(certificate) == {'6', '7', '8'}, 'Unexpected dimension keys'
    for n in (6, 7, 8):
        vertices, edges = graph(n)
        paths = certificate[str(n)]
        assert len(paths) == fibonacci(n), 'Wrong number of geodesics'
        assert all(isinstance(path, list) for path in paths)
        covered = set()
        for path in paths:
            assert 2 <= len(path) <= n + 1, 'Invalid path length'
            assert all(isinstance(v, str) and len(v) == n and v in vertices for v in path), 'Bad vertex'
            assert len(set(path)) == len(path), 'Repeated vertex'
            # Each edge is checked independently against the regenerated graph.
            for a, b in zip(path, path[1:]):
                edge = tuple(sorted((a, b)))
                assert edge in edges, 'Non-edge in path'
                covered.add(edge)
            distance = sum(a != b for a, b in zip(path[0], path[-1]))
            assert distance == len(path) - 1, 'Path not geodesic'
        assert covered == edges, 'A graph edge is not covered'
        outer_0 = {e for e in edges if e[0][0] != e[1][0]}
        outer_n = {e for e in edges if e[0][-1] != e[1][-1]}
        assert len(outer_0) == len(outer_n) == fibonacci(n)
        assert not (outer_0 & outer_n)
        # Any geodesic changes each coordinate at most once, hence an
        # edge-general-position set can contain both outer classes.
        print('n={} vertices={} edges={} geodesics={} covered={} outer_edges={}'.format(
            n, len(vertices), len(edges), len(paths), len(covered),
            len(outer_0 | outer_n)))
    print('VERIFICATION_OK dimensions=6,7,8')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python verify_fibonacci_geodesics.py PATH_TO_CERTIFICATE')
    with open(sys.argv[1], encoding='utf-8') as source:
        check(json.load(source))
