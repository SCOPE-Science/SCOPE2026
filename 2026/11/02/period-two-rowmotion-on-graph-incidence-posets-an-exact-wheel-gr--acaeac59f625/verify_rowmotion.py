"""Exhaustive ideal-level verification of wheel incidence-poset rowmotion."""
from collections import Counter


def wheel(r):
    n = r + 1
    edges = [(i, (i + 1) % r) for i in range(r)]
    edges += [(i, r) for i in range(r)]
    return n, edges


def row(state, n, edges):
    vertices, selected_edges = state
    enabled = 0
    for j, (u, v) in enumerate(edges):
        if (vertices >> u) & 1 and (vertices >> v) & 1:
            enabled |= 1 << j
    newly_enabled = enabled ^ selected_edges
    next_vertices = ((1 << n) - 1) ^ vertices
    for j, (u, v) in enumerate(edges):
        if (newly_enabled >> j) & 1:
            next_vertices |= (1 << u) | (1 << v)
    return next_vertices, newly_enabled


def all_ideals(n, edges):
    for vertices in range(1 << n):
        enabled = 0
        for j, (u, v) in enumerate(edges):
            if ((vertices >> u) & 1) and ((vertices >> v) & 1):
                enabled |= 1 << j
        selected = enabled
        while True:
            yield vertices, selected
            if selected == 0:
                break
            selected = (selected - 1) & enabled


def lucas(r):
    a, b = 2, 1
    for _ in range(r):
        a, b = b, a + b
    return a


def check():
    for r in range(3, 9):
        n, edges = wheel(r)
        count = 0
        total = 0
        for state in all_ideals(n, edges):
            total += 1
            image = row(state, n, edges)
            if image != state and row(image, n, edges) == state:
                count += 1
                assert state[0] == (1 << n) - 1
        assert count % 2 == 0
        answer = (3**r + (-1)**r - 2 * lucas(r)) // 2
        assert count // 2 == answer, (r, count, answer)
        print(f'r={r} ideals={total} points_period_2={count} orbits={count//2} expected={answer}')
    print('WHEEL_IDEAL_ROWMOTION_EXHAUSTIVE_PASS')


if __name__ == '__main__':
    check()
