"""Finite combinatorial checks for the codimension-one support-transition graph.

This checks graph enumeration, not the topological Hopf-bundle argument.
Run with: python3 verify_graph.py
"""
from itertools import permutations
from math import factorial


def graph_stats(n):
    r = n - 1
    vertices = list(permutations(range(n), r))
    positions = {v: i for i, v in enumerate(vertices)}
    neighbors = [set() for _ in vertices]
    for i, v in enumerate(vertices):
        missing, = set(range(n)) - set(v)
        for j in range(r):
            other = list(v)
            other[j] = missing
            k = positions[tuple(other)]
            assert k != i
            neighbors[i].add(k)
            neighbors[k].add(i)
    assert all(len(adj) == r for adj in neighbors)
    reachable = {0}
    todo = [0]
    while todo:
        i = todo.pop()
        for j in neighbors[i] - reachable:
            reachable.add(j)
            todo.append(j)
    v_count = len(vertices)
    e_count = sum(len(a) for a in neighbors) // 2
    assert len(reachable) == v_count
    assert v_count == factorial(n)
    assert 2 * e_count == (n - 1) * factorial(n)
    cycle_rank = e_count - v_count + 1
    assert 2 * (cycle_rank - 1) == (n - 3) * factorial(n)
    return v_count, e_count, cycle_rank


def main():
    expected = [0, 1, 13, 121, 1081, 10081]
    for n, rank in zip(range(2, 8), expected):
        vertices, edges, computed = graph_stats(n)
        assert computed == rank
        print(f"n={n}: vertices={vertices}, edges={edges}, free_rank={computed}, connected=True")
    print("All finite combinatorial assertions passed.")


if __name__ == "__main__":
    main()
