"""Exact arithmetic tests of spanning-tree Minkowski-center formula.

Run: python3 verify.py
Uses only Python standard library; finite enumeration supplements a universal proof.
"""
from fractions import Fraction as F
from itertools import product, combinations
from heapq import heapify, heappop, heappush


def prufer_edges(sequence, n):
    degrees = [1] * n
    for v in sequence:
        degrees[v] += 1
    leaves = [v for v in range(n) if degrees[v] == 1]
    heapify(leaves)
    out = []
    for v in sequence:
        u = heappop(leaves)
        out.append((min(u, v), max(u, v)))
        degrees[u] -= 1
        degrees[v] -= 1
        if degrees[v] == 1:
            heappush(leaves, v)
    u, v = leaves
    out.append((min(u, v), max(u, v)))
    return out


def masks_and_edges(n, edges):
    return [(mask, [i for i, (u, v) in enumerate(edges)
                    if (mask >> u) & 1 and (mask >> v) & 1], mask.bit_count())
            for mask in range(1, (1 << n)-1) if mask.bit_count() >= 2]


def verify_centers():
    all_count = 0
    comparisons = 0
    for n in range(3, 8):
        edges = list(combinations(range(n), 2))
        index = {e: j for j, e in enumerate(edges)}
        subset_edges = masks_and_edges(n, edges)
        signs = [0] * len(edges)
        if n >= 4:
            # Signed four-cycle has zero vertex degree and zero total.
            for (u, v), s in [((0, 1), +1), ((1, 2), -1),
                              ((2, 3), +1), ((0, 3), -1)]:
                signs[index[(u, v)]] = s
        for choice in (0, 1) if n >= 4 else (0,):
            # Four times (n*c_e) is an integer, equal to 8 plus perturbation.
            q = [8 + choice * s for s in signs]
            assert sum(q) == 4*n*(n-1)
            assert all(sum(q[i] for i, (u, v) in enumerate(edges)
                           if u == vertex or v == vertex) == 8*(n-1)
                       for vertex in range(n))
            for seq in product(range(n), repeat=n-2):
                tree = set(prufer_edges(seq, n))
                assert len(tree) == n-1
                # Numerator of reflected point in units 4*(n-1).
                numerators = [q[i] - 4*int(e in tree) for i, e in enumerate(edges)]
                assert min(numerators) >= 0
                assert sum(numerators) == 4 * (n-1) * (n-1)
                for mask, subset, s in subset_edges:
                    assert sum(numerators[i] for i in subset) <= 4*(n-1)*(s-1), (n, choice, mask)
                    comparisons += 1
                all_count += 1
        print(f"n={n}: checked {n**(n-2)} distinct labeled trees and {2 if n >= 4 else 1} centers")
    print(f"checked {all_count} reflected spanning trees, {comparisons} subset constraints")


def verify_exception():
    n = 6
    edges = list(combinations(range(n), 2))
    # Two disjoint weighted triangles, regular degree five.
    z = {e: (F(5, 2) if (e[0] < 3) == (e[1] < 3) else F(0)) for e in edges}
    assert all(sum(v for e, v in z.items() if i in e) == 5 for i in range(n))
    assert all(F(0) <= v <= 4 for v in z.values())
    S = {0, 1, 2}
    cut = sum(v for (u, w), v in z.items() if (u in S) != (w in S))
    assert cut == 0
    c = {e: (1+v)/6 for e, v in z.items()}
    # Star at vertex 3 avoids the edges induced by S.
    star = {(min(3, i), max(3, i)) for i in range(n) if i != 3}
    reflected = {e: (6*c[e] - int(e in star))/5 for e in edges}
    assert sum(reflected[e] for e in edges if e[0] in S and e[1] in S) == F(21, 10)
    print('n=6: uncapped triangle-cut counterexample has reflected internal mass 21/10 > 2')


def verify_seven_split():
    n = 7
    edges = list(combinations(range(n), 2))
    A = set(range(3))
    z = {}
    for e in edges:
        if all(v in A for v in e): z[e] = F(3)
        elif all(v not in A for v in e): z[e] = F(2)
        else: z[e] = F(0)
    assert all(sum(z[e] for e in edges if v in e) == 6 for v in range(n))
    assert all(0 <= z[e] <= 5 for e in edges)
    assert sum(z[e] for e in edges if (e[0] in A) != (e[1] in A)) == 0
    for s in range(2, n):
        for subset in combinations(range(n), s):
            S = set(subset)
            assert sum(z[e] for e in edges if e[0] in S and e[1] in S) <= (s-1)*(n-1)-s*(s-1)//2
    q = [4*(1+z[e]) for e in edges]
    subset_edges = masks_and_edges(n, edges)
    for seq in product(range(n), repeat=n-2):
        tree = set(prufer_edges(seq, n))
        nums = [q[i]-4*int(e in tree) for i,e in enumerate(edges)]
        assert min(nums) >= 0
        assert sum(nums) == 4*(n-1)*(n-1)
        for mask, ids, size in subset_edges:
            assert sum(nums[i] for i in ids) <= 4*(n-1)*(size-1)
    print('n=7: disconnected (3+4) regular weighting passes every reflected-tree inequality')


def verify_cut_threshold():
    for n in range(7, 200):
        for s in range(3, n-2):
            assert s*s - n*s + 2*n-2 <= 0
    print('n>=7: arithmetic cut-threshold checked for n=7,...,199')


def verify_rank():
    # Gaussian elimination with rational entries on unsigned incidence matrices.
    for n in range(3, 11):
        edges = list(combinations(range(n), 2))
        rows = [[F(int(v in e)) for e in edges] for v in range(n)]
        pivot = 0
        for col in range(len(edges)):
            found = next((i for i in range(pivot, n) if rows[i][col]), None)
            if found is None:continue
            rows[found], rows[pivot] = rows[pivot], rows[found]
            k=rows[pivot][col]
            rows[pivot]=[e/k for e in rows[pivot]]
            for j in range(n):
                if j!=pivot and rows[j][col]:
                    k=rows[j][col]
                    rows[j]=[a-k*b for a,b in zip(rows[j], rows[pivot])]
            pivot+=1
            if pivot == n:break
        assert pivot == n
    print('unsigned incidence rank equals n for n=3,...,10')

if __name__ == '__main__':
    verify_centers()
    verify_exception()
    verify_seven_split()
    verify_cut_threshold()
    verify_rank()
    print('VERIFICATION_OK')
