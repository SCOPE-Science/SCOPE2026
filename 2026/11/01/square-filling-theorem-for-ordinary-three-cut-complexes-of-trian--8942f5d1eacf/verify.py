"""Finite checks for the square-filling collapse of ordinary three-cut Alexander duals.

Requires Python 3.10+ and SymPy for exact integer Smith forms.
No result for untested graphs is inferred from these computations.
"""
from itertools import combinations
from collections import deque
from math import comb
from sympy import SparseMatrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def cube(d):
    return ({tuple(sorted((x, x ^ (1 << j)))) for x in range(1 << d) for j in range(d)}, 1 << d)


def glued_cubes():
    base, _ = cube(3)
    edges = set(base)
    mapping = {0: 0, 1: 1, 2: 2, 3: 3, 4: 8, 5: 9, 6: 10, 7: 11}
    edges.update(tuple(sorted((mapping[a], mapping[b]))) for a, b in base)
    return edges, 12


def grid(m, n, periodic=False, twist=False):
    def v(i, j): return i * n + j
    edges = set()
    for i in range(m):
        for j in range(n):
            if i + 1 < m: edges.add(tuple(sorted((v(i, j), v(i + 1, j)))))
            elif periodic: edges.add(tuple(sorted((v(i, j), v(0, n - 1 - j if twist else j)))))
            if j + 1 < n: edges.add(tuple(sorted((v(i, j), v(i, j + 1)))))
            elif periodic: edges.add(tuple(sorted((v(i, j), v(i, 0)))))
    return edges, m * n


def book(pages=3):
    edges = {(0, 1)}
    for k in range(pages):
        u, v = 2 + 2 * k, 3 + 2 * k
        edges.update((tuple(sorted(z)) for z in [(0, u), (u, v), (v, 1)]))
    return edges, 2 + 2 * pages


def graph_data(edges, n):
    nb = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < v < n
        nb[u].add(v); nb[v].add(u)
    assert all(not nb[u].intersection(nb[v]) for u, v in edges), 'Graph has a triangle'
    assert all(len(nb[u].intersection(nb[v])) <= 2 for u in range(n) for v in range(u + 1, n) if v not in nb[u]), 'Codegree exceeds two'
    visited = {0}; todo = [0]
    for u in todo:
        for v in nb[u]:
            if v not in visited: visited.add(v); todo.append(v)
    assert len(visited) == n, 'Graph disconnected'
    return nb


def simplices_and_squares(nb):
    n = len(nb)
    cells = {k: set() for k in range(1, 5)}
    cells[1] = {(i,) for i in range(n)}
    cells[2] = set(combinations(range(n), 2))
    cells[3] = {t for t in combinations(range(n), 3)
                if sum(v in nb[u] for u, v in combinations(t, 2)) >= 2}
    squares = set()
    for s in combinations(range(n), 4):
        if all(t in cells[3] for t in combinations(s, 3)):
            cells[4].add(s)
            squares.add(s)
    assert not any(all(t in cells[3] for t in combinations(s, 3)) for s in combinations(range(n), 5))
    return cells, squares


def square_order(square, nb):
    a = min(square)
    b, d = sorted(set(square).intersection(nb[a]))
    c = next(x for x in square if x not in (a, b, d))
    assert b in nb[c] and d in nb[c] and c not in nb[a] and d not in nb[b]
    return a, b, c, d


def remove_free_pair(cells, low, high):
    low = tuple(sorted(low)); high = tuple(sorted(high))
    assert len(high) == len(low) + 1 and low in cells[len(low)] and high in cells[len(high)]
    containing = []
    for dim in range(len(low) + 1, 5):
        for s in cells[dim]:
            if set(low).issubset(s): containing.append(s)
    assert containing == [high], ('Nonfree incidence', low, high, containing)
    cells[len(low)].remove(low)
    cells[len(high)].remove(high)


def perform_collapses(edges, n, exact=False):
    nb = graph_data(edges, n)
    cells, squares = simplices_and_squares(nb)
    counts_before = [len(cells[k]) for k in range(1, 5)]
    square_triangles = {t for s in squares for t in combinations(s, 3)}
    non_square = sorted(cells[3].difference(square_triangles))
    for t in non_square:
        ends = [(u, v) for u, v in combinations(t, 2) if v not in nb[u]]
        assert len(ends) == 1
        remove_free_pair(cells, ends[0], t)
    coresquares = []
    for s in sorted(squares):
        a, b, c, d = square_order(s, nb)
        remove_free_pair(cells, (a, b, c), s)
        remove_free_pair(cells, (a, c), (a, c, d))
        coresquares.append(((a, b, d), (b, c, d)))
    assert not cells[4]
    expected_triangles = {tuple(sorted(t)) for two in coresquares for t in two}
    assert cells[3] == expected_triangles
    core_edges = set(edges)
    for two in coresquares:
        for t in two: core_edges.update(combinations(sorted(t), 2))
    lengths = []
    for a in range(n):
        dist = {a: 0}; todo = [a]
        for u in todo:
            for v in nb[u]:
                if v not in dist: dist[v] = dist[u] + 1; todo.append(v)
        lengths.append(dist)
    long_edges = {e for e in combinations(range(n), 2) if lengths[e[0]][e[1]] >= 3}
    assert cells[2] == core_edges.union(long_edges)
    assert not core_edges.intersection(long_edges)
    assert len(cells[2]) == len(core_edges) + len(long_edges)
    # Integral Smith form of the square-completion core, independently of the dual collapse.
    b1 = b2 = None; torsion = []
    if exact:
        edge_list = sorted(core_edges); tri_list = sorted(expected_triangles)
        edge_index = {e: i for i, e in enumerate(edge_list)}
        data = {}
        for j, (a,b,c) in enumerate(tri_list):
            for edge, coeff in [((b,c),1),((a,c),-1),((a,b),1)]:
                data[(edge_index[edge],j)] = coeff
        mat = SparseMatrix(len(edge_list),len(tri_list),data)
        sm = smith_normal_form(mat, domain=ZZ)
        nz = [abs(int(sm[i,i])) for i in range(min(sm.rows,sm.cols)) if sm[i,i]]
        torsion = [v for v in nz if v>1]
        rank2 = len(nz)
        b2 = len(tri_list)-rank2
        b1 = len(edge_list)-(n-1)-rank2
        assert n - len(edge_list) + len(tri_list) == 1 - b1 + b2
    return dict(vertices=n, edges=len(edges), pre_faces=counts_before,
                four_cycles=len(squares), nonsquare_paths=len(non_square),
                collapsed_pairs=len(non_square)+2*len(squares),
                core_edges=len(core_edges), core_triangles=len(expected_triangles),
                long_edges=len(long_edges), core_b1=b1, core_b2=b2,
                core_H1_torsion=torsion)


def main():
    cases = [
        ('square_book_3', *book(3)),
        ('cube_3', *cube(3)),
        ('cube_4', *cube(4)),
        ('two_cubes_common_face', *glued_cubes()),
        ('rectangular_3x3', *grid(3,3)),
        ('toroidal_5x5', *grid(5,5,periodic=True)),
        ('klein_5x5', *grid(5,5,periodic=True,twist=True)),
    ]
    for name, edges, n in cases:
        data = perform_collapses(edges, n, exact=True)
        print(name, data)
        if name == 'cube_3':
            assert (data['core_b1'], data['core_b2'], data['long_edges'], data['core_H1_torsion']) == (0,1,4,[])
        if name == 'cube_4':
            assert (data['core_b1'], data['core_b2'], data['long_edges']) == (0, 7, 40)
        if name == 'two_cubes_common_face':
            assert (data['core_b1'], data['core_b2']) == (0, 2)
        if name == 'toroidal_5x5':
            assert (data['core_b1'], data['core_b2'], data['long_edges'], data['core_H1_torsion']) == (2,1,150,[])
        if name == 'klein_5x5':
            assert (data['core_b1'], data['core_b2'], data['long_edges'], data['core_H1_torsion']) == (1,0,150,[2])
        if name == 'square_book_3':
            assert (data['core_b1'], data['core_b2'], data['four_cycles']) == (0,0,3)
    print('SQUARE_FILLING_THREE_CUT_COLLAPSE_AND_INTEGRAL_CHECK_OK')

if __name__ == '__main__':
    main()
