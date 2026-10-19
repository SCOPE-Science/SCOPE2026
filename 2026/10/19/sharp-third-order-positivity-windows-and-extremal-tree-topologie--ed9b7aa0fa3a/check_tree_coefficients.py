"""Exact finite checks for the cubic graph-heat positivity formulas.

No third-party dependencies.  All tests use integer arithmetic.
The finite enumeration is an illustration, not a proof for all trees.
"""

from itertools import product


def prufer_edges(sequence):
    n = len(sequence) + 2
    deg = [1] * n
    for vertex in sequence:
        deg[vertex] += 1
    edges = []
    for vertex in sequence:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, vertex))
        deg[leaf] -= 1
        deg[vertex] -= 1
    u, v = (i for i in range(n) if deg[i] == 1)
    edges.append((u, v))
    return edges


def multiply(left, right):
    n = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def check_tree(n, edges):
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)
    degrees = [len(row) for row in neighbors]
    delta = max(degrees)
    laplacian = [[degrees[i] if i == j else
                  (-1 if j in neighbors[i] else 0)
                  for j in range(n)] for i in range(n)]
    square = multiply(laplacian, laplacian)
    cube = multiply(laplacian, square)
    for u in range(n):
        distance = {u: 0}
        frontier = [u]
        while frontier:
            following = []
            for vertex in frontier:
                for next_vertex in neighbors[vertex]:
                    if next_vertex not in distance:
                        distance[next_vertex] = distance[vertex] + 1
                        following.append(next_vertex)
            frontier = following
        for v in range(n):
            r = distance[v]
            du, dv = degrees[u], degrees[v]
            if r == 0:
                assert square[u][v] == du * du + du
                assert cube[u][v] == du ** 3 + 2 * du ** 2 + sum(
                    degrees[z] for z in neighbors[u])
            elif r == 1:
                assert square[u][v] == -(du + dv)
                assert cube[u][v] == -(
                    du * du + du * dv + dv * dv + du + dv - 1)
            elif r == 2:
                midpoint = next(w for w in neighbors[u] if v in neighbors[w])
                assert square[u][v] == 1
                assert cube[u][v] == du + degrees[midpoint] + dv
            elif r == 3:
                assert square[u][v] == 0
                assert cube[u][v] == -1
            else:
                assert square[u][v] == 0
                assert cube[u][v] == 0

            # Six times delta cubed times P(1/delta)_{uv}, an exact integer.
            numerator = (6 * delta ** 3 * (u == v)
                         - 6 * delta ** 2 * laplacian[u][v]
                         + 3 * delta * square[u][v] - cube[u][v])
            assert numerator >= 0
            if r == 2:
                midpoint = next(w for w in neighbors[u] if v in neighbors[w])
                assert (numerator == 0) == (
                    du == degrees[midpoint] == dv == delta)


def main():
    grand_total = 0
    for n in range(2, 8):
        count = 0
        for sequence in product(range(n), repeat=n - 2):
            check_tree(n, prufer_edges(sequence))
            count += 1
        grand_total += count
        print(f"n={n}: {count} labeled trees passed exact coefficient and positivity tests")
    print(f"Total checked: {grand_total} labeled trees")


if __name__ == "__main__":
    main()
