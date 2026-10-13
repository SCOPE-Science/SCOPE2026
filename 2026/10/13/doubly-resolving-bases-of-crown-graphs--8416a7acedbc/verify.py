from itertools import combinations
from math import comb
from collections import deque


def crown_graph(n):
    vertices = list(range(2 * n))
    adjacency = [set() for _ in vertices]
    for i in range(n):
        for j in range(n):
            if i != j:
                adjacency[i].add(n + j)
                adjacency[n + j].add(i)
    return vertices, adjacency


def all_pairs_distances(adjacency):
    order = len(adjacency)
    distances = []
    for source in range(order):
        dist = [None] * order
        dist[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if dist[v] is None:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        assert all(x is not None for x in dist)
        distances.append(dist)
    return distances


def is_doubly_resolving(selected, distances):
    selected = tuple(selected)
    if len(selected) < 2:
        return False
    order = len(distances)
    for u in range(order):
        for v in range(u + 1, order):
            values = {distances[u][s] - distances[v][s] for s in selected}
            if len(values) < 2:
                return False
    return True


def predicted_basis(n, selected):
    selected = set(selected)
    occupancy = []
    side = []
    for i in range(n):
        has_a = i in selected
        has_b = n + i in selected
        occupancy.append(int(has_a) + int(has_b))
        if has_a and not has_b:
            side.append("A")
        elif has_b and not has_a:
            side.append("B")
        elif has_a and has_b:
            side.append("X")
        else:
            side.append("-")

    if 3 <= n <= 6:
        if len(selected) != n:
            return False
        if occupancy.count(0) == 1 and occupancy.count(2) == 1 and occupancy.count(1) == n - 2:
            return True
        if occupancy.count(0) == 0 and occupancy.count(2) == 0:
            b_count = sum(x == "B" for x in side)
            return b_count not in {2, n - 2}
        return False

    if len(selected) != n - 1:
        return False
    if occupancy.count(0) != 1 or occupancy.count(1) != n - 1 or occupancy.count(2) != 0:
        return False
    a_count = sum(x == "A" for x in side)
    b_count = sum(x == "B" for x in side)
    return a_count >= 3 and b_count >= 3


def predicted_count(n):
    if 3 <= n <= 6:
        excluded_weight_layers = (2 - int(n == 4)) * comb(n, 2)
        transversals = 2**n - excluded_weight_layers
        one_hole_one_double = n * (n - 1) * 2 ** (n - 2)
        return one_hole_one_double + transversals
    m = n - 1
    return n * (2**m - 2 * (1 + m + comb(m, 2)))


def main():
    total_subset_checks = 0
    total_basis_checks = 0
    total_bases = 0

    for n in range(3, 10):
        vertices, adjacency = crown_graph(n)
        distances = all_pairs_distances(adjacency)
        optimum = n if n <= 6 else n - 1

        for size in range(2, optimum):
            for selected in combinations(vertices, size):
                total_subset_checks += 1
                assert not is_doubly_resolving(selected, distances), (n, size, selected)

        bases = 0
        for selected in combinations(vertices, optimum):
            total_subset_checks += 1
            actual = is_doubly_resolving(selected, distances)
            predicted = predicted_basis(n, selected)
            total_basis_checks += 1
            assert actual == predicted, (n, selected, actual, predicted)
            bases += int(actual)

        assert bases == predicted_count(n), (n, bases, predicted_count(n))
        total_bases += bases

    print(
        "VERIFY_OK n_range=3..9 "
        f"subset_checks={total_subset_checks} "
        f"basis_checks={total_basis_checks} "
        f"bases={total_bases} max_order=18"
    )


if __name__ == "__main__":
    main()
