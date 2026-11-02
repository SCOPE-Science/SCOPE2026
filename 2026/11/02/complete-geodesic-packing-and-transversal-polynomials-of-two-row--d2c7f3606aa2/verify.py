#!/usr/bin/env python3
"""Exact independent finite checks for a theorem on vertex-disjoint maximal geodesics.
Run: python3 verify.py . Only the Python 3 standard library is required.
"""
from collections import deque
from functools import lru_cache
from math import comb, factorial


def product_graph(n):
    vertices = [(r, c) for r in range(2) for c in range(n)]
    adjacency = [[j for j in range(2*n) if i != j and
                  (vertices[i][0] == vertices[j][0] or vertices[i][1] == vertices[j][1])]
                 for i in range(2*n)]
    dist = []
    for src in range(2*n):
        distances = [-1] * (2*n)
        distances[src] = 0
        todo = deque([src])
        while todo:
            u = todo.popleft()
            for v in adjacency[u]:
                if distances[v] == -1:
                    distances[v] = distances[u] + 1
                    todo.append(v)
        assert -1 not in distances
        dist.append(distances)
    return dist


def maximal_geodesic_masks(n):
    dist = product_graph(n)
    diameter = max(max(row) for row in dist)
    assert diameter == 2
    paths = set()
    for u in range(2*n):
        for v in range(2*n):
            if dist[u][v] != 2:
                continue
            for w in range(2*n):
                if dist[u][w] == 1 and dist[w][v] == 1:
                    paths.add((1 << u) | (1 << w) | (1 << v))
    # Every edge extends to a length-2 shortest path in this product.
    for u in range(2*n):
        for v in range(2*n):
            if dist[u][v] == 1:
                assert any((p & (1 << u)) and (p & (1 << v)) for p in paths)
    assert len(paths) == 2*n*(n-1)
    return tuple(sorted(paths))


def predicted_packings(n):
    m = (2*n)//3
    return [factorial(n)//factorial(n-k)*comb(2*(n-k),k) for k in range(m+1)]


def observed_packings(n, paths):
    @lru_cache(None)
    def walk(index, used):
        if index == len(paths):
            return (1,)
        excluded = walk(index+1, used)
        if used & paths[index]:
            return excluded
        included = walk(index+1, used | paths[index])
        total = [0]*(max(len(excluded),len(included)+1))
        for k, value in enumerate(excluded):
            total[k] += value
        for k, value in enumerate(included):
            total[k+1] += value
        while len(total) > 1 and total[-1] == 0:
            total.pop()
        return tuple(total)
    return list(walk(0,0))


def observed_transversals(n, paths):
    # F(S): does no maximal geodesic lie completely inside S?
    free_coeff = [0]*(2*n+1)
    maximal_free = []
    for subset in range(1 << (2*n)):
        if all((subset & triple) != triple for triple in paths):
            free_coeff[subset.bit_count()] += 1
            if all((subset & (1 << x)) or any(((subset | (1 << x)) & triple) == triple
                       for triple in paths) for x in range(2*n)):
                maximal_free.append(subset)
    trans_coeff = list(reversed(free_coeff))
    return free_coeff, trans_coeff, maximal_free


def predicted_transversals(n):
    free_coeff = [comb(n,k)*2**k for k in range(n+1)]
    free_coeff[2] += n
    return free_coeff + [0]*n, [0]*n + list(reversed(free_coeff))


def num_max_packings(n):
    q, r = divmod(n,3)
    return (factorial(n)//factorial(q))*({0:1,1:2*q+1,2:2}[r])


def main():
    for n in range(2,9):
        paths = maximal_geodesic_masks(n)
        observed = observed_packings(n,paths)
        predicted = predicted_packings(n)
        assert observed == predicted, (n, observed, predicted)
        assert observed[-1] == num_max_packings(n)
        assert len(observed)-1 == (2*n)//3
        assert all(observed[k]**2 > observed[k-1]*observed[k+1] for k in range(1,len(observed)-1))
        free_coeff, trans_coeff, maximal_free = observed_transversals(n,paths)
        expected_free, expected_trans = predicted_transversals(n)
        assert free_coeff == expected_free, (n,free_coeff,expected_free)
        assert trans_coeff == expected_trans, (n,trans_coeff,expected_trans)
        assert len(maximal_free) == 2**n + n
        assert {v.bit_count() for v in maximal_free} == {n, 2}
        assert sum(v.bit_count() == n for v in maximal_free) == 2**n + (n if n==2 else 0)
        print('n=%d geodesics=%d pack_coeff=%s min_transv=%d min_transv_count=%d' %
              (n,len(paths),observed,2*n-max(map(int.bit_count,maximal_free)),
               sum(v.bit_count()==n for v in maximal_free)))
    for n in range(2,151):
        p=predicted_packings(n)
        assert len(p)-1 == 2*n//3
        assert p[-1] == num_max_packings(n)
        assert all(p[k]*p[k] > p[k-1]*p[k+1] for k in range(1,len(p)-1))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
