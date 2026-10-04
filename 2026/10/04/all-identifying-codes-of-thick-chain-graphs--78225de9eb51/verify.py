#!/usr/bin/env python3
from itertools import product


def build_chain(a_sizes, b_sizes):
    p = len(a_sizes)
    vertices = []
    classes = []
    for i, size in enumerate(a_sizes):
        for k in range(size):
            vertices.append(("A", i, k))
            classes.append(("A", i))
    for j, size in enumerate(b_sizes):
        for k in range(size):
            vertices.append(("B", j, k))
            classes.append(("B", j))
    adjacency = [set() for _ in vertices]
    for u, vertex in enumerate(vertices):
        if vertex[0] != "A":
            continue
        i = vertex[1]
        for v, other in enumerate(vertices):
            if other[0] == "B" and other[1] <= i:
                adjacency[u].add(v)
                adjacency[v].add(u)
    return vertices, classes, adjacency


def is_identifying_code(mask, adjacency):
    n = len(adjacency)
    traces = []
    for v in range(n):
        trace = frozenset(u for u in adjacency[v] | {v} if (mask >> u) & 1)
        if not trace:
            return False
        traces.append(trace)
    return len(set(traces)) == n


def theorem_predicts(mask, classes, a_sizes, b_sizes):
    by_class = {}
    for index, cls in enumerate(classes):
        by_class.setdefault(cls, []).append(index)
    for members in by_class.values():
        omitted = sum(1 for v in members if not ((mask >> v) & 1))
        if omitted > 1:
            return False
    if len(a_sizes) == 1 and a_sizes[0] == 2 and b_sizes[0] == 2:
        return mask.bit_count() >= 3
    return True


def predicted_polynomial(a_sizes, b_sizes):
    n = sum(a_sizes) + sum(b_sizes)
    coeff = [0] * (n + 1)
    if len(a_sizes) == 1 and a_sizes[0] == 2 and b_sizes[0] == 2:
        coeff[3] = 4
        coeff[4] = 1
        return coeff
    coeff[0] = 1
    degree = 0
    for size in tuple(a_sizes) + tuple(b_sizes):
        nxt = [0] * (n + 1)
        for d in range(degree + 1):
            if coeff[d]:
                nxt[d + size] += coeff[d]
                nxt[d + size - 1] += size * coeff[d]
        coeff = nxt
        degree += size
    return coeff


def brute_polynomial(adjacency):
    n = len(adjacency)
    coeff = [0] * (n + 1)
    for mask in range(1 << n):
        if is_identifying_code(mask, adjacency):
            coeff[mask.bit_count()] += 1
    return coeff


def main():
    profiles = 0
    subset_checks = 0
    coefficient_checks = 0
    max_order = 0
    for p in range(1, 4):
        for sizes in product((2, 3), repeat=2 * p):
            a_sizes = sizes[:p]
            b_sizes = sizes[p:]
            n = sum(sizes)
            if n > 14:
                continue
            _, classes, adjacency = build_chain(a_sizes, b_sizes)
            profiles += 1
            max_order = max(max_order, n)
            actual = [0] * (n + 1)
            for mask in range(1 << n):
                observed = is_identifying_code(mask, adjacency)
                predicted = theorem_predicts(mask, classes, a_sizes, b_sizes)
                subset_checks += 1
                if observed != predicted:
                    raise AssertionError((a_sizes, b_sizes, mask, observed, predicted))
                if observed:
                    actual[mask.bit_count()] += 1
            expected = predicted_polynomial(a_sizes, b_sizes)
            for k, (x, y) in enumerate(zip(actual, expected)):
                coefficient_checks += 1
                if x != y:
                    raise AssertionError((a_sizes, b_sizes, k, x, y))
    # Extra larger complete-bipartite boundary profiles.
    for a in range(2, 6):
        for b in range(2, 6):
            if a + b > 12:
                continue
            _, classes, adjacency = build_chain((a,), (b,))
            n = a + b
            for mask in range(1 << n):
                subset_checks += 1
                if is_identifying_code(mask, adjacency) != theorem_predicts(mask, classes, (a,), (b,)):
                    raise AssertionError(((a,), (b,), mask))
            profiles += 1
            expected = predicted_polynomial((a,), (b,))
            actual = brute_polynomial(adjacency)
            coefficient_checks += n + 1
            if actual != expected:
                raise AssertionError(((a,), (b,), actual, expected))
            max_order = max(max_order, n)
    print(f"VERIFY_OK profiles={profiles} subset_checks={subset_checks} coefficient_checks={coefficient_checks} max_order={max_order}")


if __name__ == "__main__":
    main()
