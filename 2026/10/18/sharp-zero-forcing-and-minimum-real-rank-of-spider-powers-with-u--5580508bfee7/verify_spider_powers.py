#!/usr/bin/env python3
"""Self-contained exact checks for powers of subdivided stars.

Usage: python spider_power_check.py
Only Python's standard library is required.
"""
from itertools import combinations
from fractions import Fraction


def build_tree(lengths):
    """Hub is 0; each arm is indexed outward from the hub."""
    arms = []
    idx = 1
    for length in lengths:
        arms.append(list(range(idx, idx + length)))
        idx += length
    adj = [set() for _ in range(idx)]
    for arm in arms:
        prev = 0
        for vertex in arm:
            adj[prev].add(vertex)
            adj[vertex].add(prev)
            prev = vertex
    return adj, arms


def power_adj(tree, k):
    n = len(tree)
    result = [set() for _ in range(n)]
    for u in range(n):
        current = {u}
        explored = {u}
        for _ in range(k):
            current = {w for v in current for w in tree[v]} - explored
            explored |= current
        result[u] = explored - {u}
    return result


def zero_force_closure(adj, blue):
    blue = set(blue)
    while True:
        forced = set()
        for u in blue:
            w = adj[u] - blue
            if len(w) == 1:
                forced |= w
        if not forced:
            return blue
        blue |= forced


def forcing_sequence(arms, k):
    assert len(arms) >= 2 and min(map(len, arms)) >= k + 1
    steps = []
    for arm in arms[:-1]:
        for t in range(len(arm) - k, 0, -1):
            steps.append((arm[t + k - 1], arm[t - 1]))
    steps.append((arms[0][k - 1], 0))
    for j in range(1, k):
        steps.append((arms[0][k - j - 1], arms[-1][j - 1]))
    steps.append((0, arms[-1][k - 1]))
    for t in range(k + 1, len(arms[-1]) + 1):
        steps.append((arms[-1][t - k - 1], arms[-1][t - 1]))
    return set(v for arm in arms[:-1] for v in arm[-k:]), steps


def matrix_witness(lengths, k):
    """The integer symmetric matrix [0,h^T U^T; Uh, diag(C_i^T C_i)+UBU^T]."""
    _, arms = build_tree(lengths)
    n = 1 + sum(lengths)
    matrix = [[0] * n for _ in range(n)]
    for arm in arms:
        ell = len(arm)
        for start in range(ell - k):
            for p in arm[start:start + k + 1]:
                for q in arm[start:start + k + 1]:
                    matrix[p][q] += 1
        for j, v in enumerate(arm, start=1):
            if j <= k:
                matrix[0][v] = matrix[v][0] = 1
    for arm in arms:
        for other in arms:
            for i in range(1, min(k, len(arm)) + 1):
                for j in range(1, min(k, len(other)) + 1):
                    if i + j <= k:
                        matrix[arm[i-1]][other[j-1]] += 1
    return matrix, arms


def kernel_basis(lengths, k):
    """(m-1)*k explicit independent kernel vectors from first-k coordinates."""
    _, arms = build_tree(lengths)
    n = 1 + sum(lengths)
    vectors = []
    for s in range(len(arms) - 1):
        for coord in range(k):
            vec = [0] * n
            for arm, sign in ((arms[s], 1), (arms[-1], -1)):
                x = [int(t == coord) for t in range(k)]
                for t in range(k, len(arm)):
                    x.append(-sum(x[t-k:t]))
                for vertex, value in zip(arm, x):
                    vec[vertex] = sign * value
            vectors.append(vec)
    return vectors


def rational_rank(a):
    """Exact row rank, not floating-point rank."""
    a = [[Fraction(y) for y in row] for row in a]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivotrow = 0
    for j in range(cols):
        i = next((i for i in range(pivotrow, rows) if a[i][j]), None)
        if i is None:
            continue
        a[i], a[pivotrow] = a[pivotrow], a[i]
        coeff = a[pivotrow][j]
        a[pivotrow] = [v / coeff for v in a[pivotrow]]
        for t in range(pivotrow + 1, rows):
            factor = a[t][j]
            if factor:
                a[t] = [x - factor * y for x, y in zip(a[t], a[pivotrow])]
        pivotrow += 1
        if pivotrow == rows:
            break
    return pivotrow


def verify_one(lengths, k, rank_check=True, brute_force=False):
    tree, arms = build_tree(lengths)
    adj = power_adj(tree, k)
    matrix, _ = matrix_witness(lengths, k)
    n = len(tree)
    target = (len(lengths) - 1) * k
    for i in range(n):
        for j in range(n):
            assert matrix[i][j] == matrix[j][i]
            if i != j:
                assert (matrix[i][j] != 0) == (j in adj[i]), (lengths,k,i,j)
    basis = kernel_basis(lengths, k)
    assert len(basis) == target
    for v in basis:
        assert all(sum(matrix[i][j] * v[j] for j in range(n)) == 0 for i in range(n))
    # Independence follows from the disjoint first k coordinates of arms 1..m-1.
    blue, moves = forcing_sequence(arms, k)
    assert len(blue) == target
    for u, v in moves:
        assert u in blue and v not in blue and adj[u] - blue == {v}, (lengths,k,u,v)
        blue.add(v)
    assert len(blue) == n
    if rank_check:
        assert n - rational_rank(matrix) == target, (lengths,k)
    if brute_force:
        tested = 0
        for size in range(target):
            for selection in combinations(range(n), size):
                assert len(zero_force_closure(adj, selection)) < n
                tested += 1
        return tested
    return 0


def main():
    matrix_cases = 0
    brute_count = 0
    for k in range(1, 5):
        for m in range(2, 6):
            cases = [tuple([k+1]*m), tuple(k+1+(i%3) for i in range(m)), tuple(k+1+(i%2) for i in range(m))]
            for lengths in cases:
                verify_one(lengths, k, rank_check=True)
                matrix_cases += 1
    for lengths, k in [((2,2,2),1), ((3,3,3),2), ((4,4,4),3), ((4,5,4),3), ((3,4,4,3),2)]:
        brute_count += verify_one(lengths, k, rank_check=True, brute_force=True)
    print(f"PASS: {matrix_cases+5} independent exact matrix/forcing comparisons")
    print(f"PASS: {brute_count} direct lower-cardinality seed tests (all nonforcing)")
    print("PASS: exact support, symmetry, kernel vectors, rational nullity, chronological forces")

if __name__ == '__main__':
    main()
