"""Independent finite spanning-tree comparisons for a one-hub p-transport formula.

This checks selected finite cases, not the general theorem. Run with Python 3.
"""

from itertools import product
from math import isclose


def prufer_edges(code, size):
    deg = [1] * size
    for v in code:
        deg[v] += 1
    edges = []
    for v in code:
        leaf = next(i for i in range(size) if deg[i] == 1)
        edges.append((leaf, v))
        deg[leaf] -= 1
        deg[v] -= 1
    leaves = [i for i in range(size) if deg[i] == 1]
    assert len(leaves) == 2
    edges.append(tuple(leaves))
    return edges


def tree_cost(edges, masses, exponent, radius):
    # Root 0 is the unique sink, vertex 1 is the zero-mass hub.
    size = len(masses) + 2
    graph = [[] for _ in range(size)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    def branch(v, parent):
        mass = 0.0 if v < 2 else masses[v - 2]
        cost = 0.0
        for w in graph[v]:
            if w == parent:
                continue
            child_mass, child_cost = branch(w, v)
            length = radius if v == 1 or w == 1 else 1.0
            cost += child_cost + length ** exponent * abs(child_mass) ** exponent
            mass += child_mass
        return mass, cost

    return branch(0, -1)[1]


def all_tree_minimum(masses, exponent, radius):
    size = len(masses) + 2
    return min(
        tree_cost(prufer_edges(code, size), masses, exponent, radius)
        for code in product(range(size), repeat=size - 2)
    )


def subset_formula(masses, exponent, radius):
    n = len(masses)
    values = []
    for bitset in range(1 << n):
        chosen = [masses[i] for i in range(n) if bitset & (1 << i)]
        other = [masses[i] for i in range(n) if not (bitset & (1 << i))]
        values.append(
            sum(c ** exponent for c in other)
            + radius ** exponent * (sum(c ** exponent for c in chosen) + sum(chosen) ** exponent)
        )
    return min(values)


def run():
    tested = 0
    for exponent in (0.25, 0.5, 0.8):
        for radius in (0.5, 0.7, 1.0):
            for masses in ((1.0, 1.0), (1.0, 2.0, 4.0), (1.0, 3.0, 2.0, 7.0)):
                exact = subset_formula(masses, exponent, radius)
                tree = all_tree_minimum(masses, exponent, radius)
                assert isclose(exact, tree, rel_tol=3e-12, abs_tol=3e-12), (masses, exponent, radius, exact, tree)
                tested += 1
    assert 5 < (2 ** 0.5 - 1) ** (-2) < 6
    tested += 1
    masses = (1.0,) * 10 + (10000.0,)
    e_none = 110.0
    e_small = 100 + (10 + 10 ** 0.5) / 2 ** 0.5
    e_big = 10 + 200 / 2 ** 0.5
    e_all = (110 + 10010 ** 0.5) / 2 ** 0.5
    assert e_small < min(e_none, e_big, e_all)
    tested += 1
    print(f"PASS: {tested} finite comparisons, including the selective-routing witness")


if __name__ == "__main__":
    run()
