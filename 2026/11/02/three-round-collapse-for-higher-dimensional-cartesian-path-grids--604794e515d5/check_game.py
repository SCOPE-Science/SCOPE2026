#!/usr/bin/env python3
"""Independent nested Hintikka-type computation for three-round graph games."""
from functools import lru_cache
from itertools import product


def make_path_product(sides):
    verts = list(product(*[range(a) for a in sides]))
    edges = set()
    for i, a in enumerate(verts):
        for j, b in enumerate(verts):
            if i < j and sum(abs(x - y) for x, y in zip(a, b)) == 1:
                edges.add((i, j))
    return len(verts), edges


def make_cycle(n):
    return n, {(min(i, (i + 1) % n), max(i, (i + 1) % n)) for i in range(n)}


def three_type(graph):
    size, edges = graph

    @lru_cache(None)
    def T(chosen, rem):
        if rem == 0:
            return tuple((int(chosen[i] == chosen[j]),
                          int((min(chosen[i], chosen[j]), max(chosen[i], chosen[j])) in edges))
                         for i in range(len(chosen)) for j in range(i + 1, len(chosen)))
        return frozenset(T(chosen + (v,), rem - 1) for v in range(size))
    return T((), 3)


def main():
    c7 = three_type(make_cycle(7))
    for sides in ((2, 2, 3), (2, 3, 3), (3, 3, 3), (2, 2, 2, 2),
                  (2, 2, 4), (2, 3, 4), (2, 2, 2, 2, 2)):
        assert three_type(make_path_product(sides)) == c7, sides
    q3 = three_type(make_path_product((2, 2, 2)))
    assert q3 != c7
    print('CHECK_GAME_OK')
    print('complete_three_round_types: 7 stable grids plus 7-cycle')
    print('three_cube_separated: true')


if __name__ == '__main__':
    main()
