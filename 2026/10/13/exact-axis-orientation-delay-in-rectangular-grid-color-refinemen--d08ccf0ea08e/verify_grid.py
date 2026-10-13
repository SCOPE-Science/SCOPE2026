"""Finite spot checks for the pointed-grid colour-refinement theorem.

Run: python verify_grid.py
No external packages are needed. Exhaustive over the finite parameter range
below; infinite validity is established by the separate mathematical proof.
"""
from collections import Counter


def build(m, n):
    vertices = [(i, j) for i in range(m) for j in range(n)]
    nbr = {}
    for i, j in vertices:
        nbr[(i, j)] = tuple(
            (a, b) for a, b in ((i-1, j), (i+1, j), (i, j-1), (i, j+1))
            if 0 <= a < m and 0 <= b < n
        )
    return vertices, nbr


def check(m, n):
    vertices, nbr = build(m, n)
    u, v = (1, 0), (0, 1)
    colors = {x: 0 for x in vertices}
    deficit = {x: 4-len(nbr[x]) for x in vertices}
    for r in range(m):
        # The first split should be precisely at r=m-1.
        assert (colors[u] != colors[v]) == (r == m-1), (m, n, r)
        # Color after r>=1 determines the previous defect-walk moments.
        if r <= m-2:
            diff = deficit[u] - deficit[v]
            assert diff == (1 if r == m-2 else 0), (m, n, r, diff)
        if r == m-1:
            break
        signatures = {
            x: (colors[x], tuple(sorted(Counter(colors[y] for y in nbr[x]).items())))
            for x in vertices
        }
        palette = {s: k for k, s in enumerate(sorted(set(signatures.values())))}
        colors = {x: palette[signatures[x]] for x in vertices}
        deficit = {x: sum(deficit[y] for y in nbr[x]) for x in vertices}


def main():
    checked = 0
    for m in range(2, 19):
        for n in range(m+1, 23):
            check(m, n)
            checked += 1
    print("VERIFY_OK pointed rectangular grids:", checked, "instances (2<=m< n<=22)")


if __name__ == '__main__':
    main()
