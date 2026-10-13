#!/usr/bin/env python3
"""Exact integral incidence-matrix tests for rooted-tree order polytopes.

Run with Python 3.9+ and the standard library: python3 CHECKER.py.
The general theorem is proved separately; these are finite regression tests.
"""
from collections import Counter
from itertools import product
from heapq import heapify, heappop, heappush


def rooted_tree_from_prufer(code, n):
    if n == 1:
        return [-1]
    degree = [1] * n
    for a in code:
        degree[a] += 1
    leaves = [v for v in range(n) if degree[v] == 1]
    heapify(leaves)
    edges = []
    for a in code:
        v = heappop(leaves)
        edges.append((v, a))
        degree[v] -= 1
        degree[a] -= 1
        if degree[a] == 1:
            heappush(leaves, a)
    u = heappop(leaves)
    v = heappop(leaves)
    edges.append((u, v))
    adjacency = [[] for _ in range(n)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    parent = [-2] * n
    parent[0] = -1
    stack = [0]
    for u in stack:
        for v in adjacency[u]:
            if v != parent[u]:
                assert parent[v] == -2
                parent[v] = u
                stack.append(v)
    assert len(stack) == n
    return parent


def children_of(parent):
    children = [[] for _ in parent]
    for v in range(1, len(parent)):
        children[parent[v]].append(v)
    return children


def determinant_bareiss(matrix):
    n = len(matrix)
    a = [row[:] for row in matrix]
    if n == 0:
        return 1
    sign = 1
    previous = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((j for j in range(k + 1, n) if a[j][k] != 0), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = a[i][j] * p - a[i][k] * a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = p
    return sign * a[-1][-1]


def polynomial_distribution(children, u=0):
    if not children[u]:
        return Counter({0: 2}), 1
    parts = [polynomial_distribution(children, v) for v in children[u]]
    poly = Counter({0: 1})
    for other, _ in parts:
        out = Counter()
        for a, va in poly.items():
            for b, vb in other.items():
                out[a + b] += va * vb
        poly = out
    number_leaves = sum(count for _, count in parts)
    poly[number_leaves - 1] += 1
    return poly, number_leaves


def smooth_count_from_tails(children, parent):
    leaves = [v for v in range(len(parent)) if not children[v]]
    if len(leaves) == 1:
        return len(parent) + 1
    answer = 1
    for leaf in leaves:
        v = leaf
        tail_length = 0
        while parent[v] != -1:
            tail_length += 1
            if len(children[parent[v]]) >= 2:
                break
            v = parent[v]
        else:
            raise AssertionError('tree with multiple leaves lacks a branching ancestor')
        answer *= tail_length + 1
    return answer


def active_facets(parent, children, mask):
    n = len(parent)
    rows = []
    edges = []
    # The extra vertex n joins the two virtual order bounds.
    if not (mask & 1):
        row = [0] * n
        row[0] = 1
        rows.append(row)
        edges.append((0, n))
    for v in range(1, n):
        p = parent[v]
        if bool(mask & (1 << p)) == bool(mask & (1 << v)):
            row = [0] * n
            row[p] = -1
            row[v] = 1
            rows.append(row)
            edges.append((p, v))
    for v in range(n):
        if not children[v] and mask & (1 << v):
            row = [0] * n
            row[v] = 1
            rows.append(row)
            edges.append((v, n))
    return rows, edges


def spanning_tree_minor(rows, edges, n):
    ds = list(range(n + 1))
    def root(a):
        while ds[a] != a:
            ds[a] = ds[ds[a]]
            a = ds[a]
        return a
    chosen = []
    for row, (u, v) in zip(rows, edges):
        a, b = root(u), root(v)
        if a != b:
            ds[a] = b
            chosen.append(row)
    assert len(chosen) == n, ('active graph not connected', edges)
    det = determinant_bareiss(chosen)
    assert abs(det) == 1, ('nonunimodular spanning minor', rows, chosen, det)


def check_tree(parent):
    n = len(parent)
    children = children_of(parent)
    predicted, L = polynomial_distribution(children)
    observed = Counter()
    checked_filters = 0
    for mask in range(1 << n):
        # A characteristic vector of a filter cannot turn from 1 to 0
        # along a directed parent-to-child edge.
        if any(mask & (1 << parent[v]) and not (mask & (1 << v))
               for v in range(1, n)):
            continue
        rows, edges = active_facets(parent, children, mask)
        spanning_tree_minor(rows, edges, n)
        rank = len(rows) - n
        frontier = sum(not (mask & (1 << parent[v])) and bool(mask & (1 << v))
                       for v in range(1, n))
        selected_leaves = sum(bool(mask & (1 << v)) for v in range(n)
                              if not children[v])
        expected = selected_leaves - frontier - bool(mask & 1)
        assert rank == expected >= 0, (parent, mask, rank, expected)
        observed[rank] += 1
        checked_filters += 1
    assert observed == predicted, (parent, observed, predicted)
    smooth = observed[0]
    assert smooth == smooth_count_from_tails(children, parent), parent
    return checked_filters


def full_binary_parent(height):
    # Breadth-first numbering, with root 0.
    n = 2 ** (height + 1) - 1
    return [-1] + [(v - 1) // 2 for v in range(1, n)]


def main():
    grand_trees = 0
    grand_filters = 0
    for n in range(1, 7):
        tree_count = 0
        filter_count = 0
        codes = [()] if n <= 2 else product(range(n), repeat=n - 2)
        for code in codes:
            parent = rooted_tree_from_prufer(code, n)
            filter_count += check_tree(parent)
            tree_count += 1
        grand_trees += tree_count
        grand_filters += filter_count
        print(f'n={n} rooted labeled trees={tree_count} checked filters={filter_count}')
    for height in range(4):
        parent = full_binary_parent(height)
        c = check_tree(parent)
        L = 1 << height
        print(f'full binary height={height} leaves={L} filters={c} smooth={1 << L}')
    print(f'TOTAL rooted labeled trees={grand_trees} checked filters={grand_filters}')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
