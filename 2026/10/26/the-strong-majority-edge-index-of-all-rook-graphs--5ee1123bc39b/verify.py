#!/usr/bin/env python3
"""Finite exact checks for a strong-majority classification on rook graphs."""
from itertools import combinations


def edges_of_rook(m, n):
    vertices = [(i, j) for i in range(m) for j in range(n)]
    return [(u, v) for u, v in combinations(vertices, 2)
            if (u[0] == v[0]) != (u[1] == v[1])]


def adjacency_masks(edges):
    masks = []
    for k, (u, v) in enumerate(edges):
        mask = 0
        for l, (x, y) in enumerate(edges):
            if k != l and (u == x or u == y or v == x or v == y):
                mask |= (1 << l)
        masks.append(mask)
    return masks


def valid_colors(edges, palette):
    for k, (u, v) in enumerate(edges):
        adjacent = [j for j, (x, y) in enumerate(edges)
                    if k != j and (u == x or u == y or v == x or v == y)]
        counts = [sum(palette[j] == c for j in adjacent) for c in set(palette)]
        if max(counts, default=0) * 2 > len(adjacent):
            return False
    return True


def small_certificate(m, n, edges):
    if (m, n) == (2, 2):
        return [0 if (u[0] == v[0] and u[0] == 0) or
                   (u[1] == v[1] and u[1] == 1) else 1 for u, v in edges]
    if (m, n) in ((2, 3), (3, 3)):
        output = []
        for (i, j), (k, l) in edges:
            if i == k:
                output.append((i + j + l) % 3)
            else:
                output.append((i + k + j) % 3)
        return output
    if (m, n) == (2, 4):
        factor = {(0, 1): 0, (2, 3): 0,
                  (0, 2): 1, (1, 3): 1,
                  (0, 3): 2, (1, 2): 2}
        rungs = (0, 0, 1, 2)
        return [factor[min(u[1], v[1]), max(u[1], v[1])]
                if u[0] == v[0] else rungs[u[1]] for u, v in edges]
    raise ValueError((m, n))


def count_two_colorings(edges):
    masks = adjacency_masks(edges)
    counts = [mask.bit_count() for mask in masks]
    solutions = 0
    for mask in range(1 << len(edges)):
        if all((mask & adj).bit_count() * 2 == d
               for adj, d in zip(masks, counts)):
            solutions += 1
    return solutions


def main():
    expected = {(2, 2): 4, (2, 3): 0, (2, 4): 0, (3, 3): 0}
    for (m, n), count in expected.items():
        edges = edges_of_rook(m, n)
        coloring = small_certificate(m, n, edges)
        assert valid_colors(edges, coloring), ('certificate failed', m, n)
        assert len(set(coloring)) == (2 if (m, n) == (2, 2) else 3)
        observed = count_two_colorings(edges)
        assert observed == count, ((m, n), observed, count)
        print(f'R({m},{n}): edges={len(edges)}, named_two_colorings={observed}, '
              f'certificate_colors={len(set(coloring))}, CHECK_OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
