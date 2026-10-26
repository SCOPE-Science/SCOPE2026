"""Exhaustively check the recurrent classes of asynchronous minority dynamics on wheels.

Uses only the Python standard library; finite checks are not a proof for all n.
"""
import sys
from collections import Counter
from math import comb

sys.setrecursionlimit(100000)


def moves(n, state):
    hub = (state >> n) & 1
    for i in range(n):
        color = (state >> i) & 1
        same = sum(((state >> j) & 1) == color
                   for j in ((i - 1) % n, (i + 1) % n))
        same += hub == color
        if same >= 2:  # Rim degree is three.
            yield state ^ (1 << i)
    same = sum(((state >> i) & 1) == hub for i in range(n))
    if 2 * same > n - 1:  # Closed-neighborhood minority, tie keeps color.
        yield state ^ (1 << n)


def perrin(n):
    values = [3, 0, 2]
    for i in range(3, n + 1):
        values.append(values[i - 2] + values[i - 3])
    return values[n]


def recurrent_classes(n):
    count = 1 << (n + 1)
    edges = [tuple(moves(n, state)) for state in range(count)]
    index = [-1] * count
    low = [0] * count
    on_stack = [False] * count
    stack = []
    components = []
    clock = 0

    def visit(v):
        nonlocal clock
        index[v] = low[v] = clock
        clock += 1
        stack.append(v)
        on_stack[v] = True
        for w in edges[v]:
            if index[w] == -1:
                visit(w)
                low[v] = min(low[v], low[w])
            elif on_stack[w]:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            component = set()
            while True:
                w = stack.pop()
                on_stack[w] = False
                component.add(w)
                if w == v:
                    break
            components.append(component)

    for v in range(count):
        if index[v] == -1:
            visit(v)
    return [component for component in components
            if all(v in component for u in component for v in edges[u])]


def predicted_weighted(n, z):
    if z < 1 or z > n // 2 or z < (n + 2) // 3:
        return 0
    return n * comb(z, n - 2 * z) // z


def check(n):
    classes = recurrent_classes(n)
    lengths = Counter(map(len, classes))
    fixed = 2 * perrin(n) - (4 if n % 2 == 0 else 0)
    pairs = 2 if n % 2 == 0 else 0
    assert lengths[1] == fixed
    assert lengths[2] == pairs
    assert set(lengths) <= {1, 2}
    assert sum(len(c) for c in classes) == 2 * perrin(n)
    profile = Counter()
    for component in classes:
        if len(component) == 2:
            u, v = tuple(component)
            assert u ^ v == (1 << n)  # Only the hub flips.
        for state in component:
            hub = (state >> n) & 1
            z = sum(((state >> i) & 1) == hub for i in range(n))
            profile[z] += 1
    for z in range(n + 1):
        assert profile[z] == 2 * predicted_weighted(n, z), (n, z, profile[z])
    return len(classes), fixed, pairs


if __name__ == '__main__':
    for n in range(3, 12):
        total, fixed, pairs = check(n)
        print(f'n={n}: recurrent_classes={total}, absorbing_states={fixed}, two_state_classes={pairs}, Perrin={perrin(n)}')
    print('PASS: exhaustive recurrent-class and density-profile checks, n=3..11')
