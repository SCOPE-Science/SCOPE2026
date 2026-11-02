#!/usr/bin/env python3
"""Exact finite checks of coordinate covariance for directed Hamiltonian tours.

Only Python's standard library is required. This checks finite instances;
the stated all-order and all-measure theorems require their separate proofs.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial
from random import Random


def arcs(n):
    return [(i, j) for i in range(n) for j in range(n) if i != j]


def tours(n):
    # Unique canonical listing: start every directed cycle at zero.
    for order in permutations(range(1, n)):
        cyc = (0,) + order
        yield frozenset((cyc[k], cyc[(k + 1) % n]) for k in range(n))


def moments(n, weights=None):
    ee = arcs(n)
    tt = list(tours(n))
    assert len(tt) == factorial(n - 1)
    if weights is None:
        weights = [1] * len(tt)
    assert len(weights) == len(tt) and all(w > 0 for w in weights)
    wtot = sum(weights)
    a = [0] * len(ee)
    b = [[0] * len(ee) for _ in ee]
    for T, w in zip(tt, weights):
        idx = [k for k, e in enumerate(ee) if e in T]
        for k in idx:
            a[k] += w
            for j in idx:
                b[k][j] += w
    # N = wtot^2 times the probability-normalized covariance.
    N = [[wtot * b[i][j] - a[i] * a[j]
          for j in range(len(ee))] for i in range(len(ee))]
    return ee, tt, wtot, a, b, N


def bareiss(A):
    A = [list(r) for r in A]
    n = len(A)
    if n == 0:
        return 1
    den, sg = 1, 1
    for k in range(n - 1):
        if A[k][k] == 0:
            piv = next((j for j in range(k + 1, n) if A[j][k] != 0), None)
            if piv is None:
                return 0
            A[k], A[piv] = A[piv], A[k]
            sg = -sg
        z = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                v = A[i][j] * z - A[i][k] * A[k][j]
                assert v % den == 0
                A[i][j] = v // den
            A[i][k] = 0
        den = z
    return sg * A[-1][-1]


def components(n, idx_set):
    ee = arcs(n)
    parent = list(range(2 * n))
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for k in idx_set:
        i, j = ee[k]
        ri, rj = root(i), root(n + j)
        parent[ri] = rj
    return len({root(i) for i in range(2 * n)})


def expected_spectrum(n):
    return {
        Fraction(0): 2 * n - 1,
        Fraction(1, n - 1): n * (n - 3) // 2,
        Fraction(n, (n - 1) * (n - 2)): (n - 1) * (n - 2) // 2,
    }


def check_uniform_moments():
    tests = 0
    for n in range(3, 8):
        ee, tt, W, a, b, N = moments(n)
        p = Fraction(1, n - 1)
        q = Fraction(1, (n - 1) * (n - 2))
        for i, (x, y) in enumerate(ee):
            assert Fraction(a[i], W) == p
            for j, (u, v) in enumerate(ee):
                pair = (p if i == j else q if x != u and y != v and (x, y) != (v, u) else 0)
                assert Fraction(b[i][j], W) == pair
                assert N[i][j] == W * W * (pair - p * p)
                tests += 1
        # The crown-graph incidence kernel has a fundamental-cycle basis.
        m = len(ee)
        parent = list(range(2 * n))
        def root(x):
            while parent[x] != x:
                x = parent[x]
            return x
        tree, chords = [], []
        for k, (x, y) in enumerate(ee):
            a0, b0 = root(x), root(n + y)
            if a0 != b0:
                parent[a0] = b0
                tree.append(k)
            else:
                chords.append(k)
        assert len(tree) == 2 * n - 1
        for chord in chords:
            x, y = ee[chord]
            start, goal = x, n + y
            adj = [[] for _ in range(2 * n)]
            for k in tree:
                i, j = ee[k]
                adj[i].append((n + j, k))
                adj[n + j].append((i, k))
            queue, seen = [start], {start:(-1,-1)}
            for node in queue:
                for nb, k in adj[node]:
                    if nb not in seen:
                        seen[nb]=(node,k)
                        queue.append(nb)
            vec = [0]*m
            vec[chord]=1
            cur, sign = goal, -1
            while cur != start:
                prev, k = seen[cur]
                vec[k]=sign
                sign=-sign
                cur=prev
            assert sign == 1  # path has odd length
            assert all(sum(vec[k] for k,(i,j) in enumerate(ee) if i == z) == 0 for z in range(n))
            assert all(sum(vec[k] for k,(i,j) in enumerate(ee) if j == z) == 0 for z in range(n))
            transpose = [vec[ee.index((y, x))] for x,y in ee]
            for sym, lam in ((True,p),(False,p+2*q)):
                v = [vec[k]+transpose[k] if sym else vec[k]-transpose[k] for k in range(m)]
                for k in range(m):
                    assert Fraction(sum(N[k][j]*v[j] for j in range(m)), W*W) == lam*v[k]
        print('n=', n, 'tours=', len(tt), 'moments=', m * m,
              'predicted positive ranks=', sum(k for v,k in expected_spectrum(n).items() if v))
    return tests


def check_complete_determinant_enumeration(n, weights=None):
    ee, tt, W, a, b, N = moments(n, weights)
    m, d = len(ee), n * (n - 3) + 1
    tree_count = (n - 1) * n ** (n - 2) * (n - 2) ** (n - 1)
    positive = 0
    common = None
    for S in combinations(range(m), d):
        complement = set(range(m)) - set(S)
        conn = components(n, complement) == 1
        val = bareiss([[N[i][j] for j in S] for i in S])
        assert (val > 0) == conn, (n, S, val, conn)
        if val:
            positive += 1
            if common is None:
                common = val
            assert val == common, (n, S, val, common)
    assert positive == tree_count
    if weights is None and n == 4:
        assert Fraction(4 ** d * common, W ** (2 * d)) == Fraction(64, 729)
    if weights is not None and n == 4:
        assert Fraction(common, W ** (2 * d)) == Fraction(5, 221184)
    print('EXHAUSTIVE n=', n, 'weights=',weights, 'positive=',positive,
          'subsets=',comb(m,d), 'common covariance determinant=', Fraction(common, W**(2*d)))
    return positive


def check_random_designs(n=5, trials=120):
    ee, tt, W, a, b, N = moments(n)
    m, d = len(ee), n * (n - 3) + 1
    rng = Random(314159)
    value = None
    positives = 0
    negatives = 0
    for _ in range(trials):
        S = sorted(rng.sample(range(m), d))
        F = set(range(m)) - set(S)
        conn = components(n, F) == 1
        det = bareiss([[N[i][j] for j in S] for i in S])
        assert (det > 0) == conn
        if conn:
            positives += 1
            if value is None: value = det
            assert det == value
        else: negatives += 1
    assert positives > 0 and negatives > 0
    print('RANDOM n=5 designs=',trials,'trees=',positives,'disconnected=',negatives)
    return trials


if __name__ == '__main__':
    c = check_uniform_moments()
    check_complete_determinant_enumeration(3)
    check_complete_determinant_enumeration(4)
    check_complete_determinant_enumeration(4, [1, 2, 3, 4, 5, 9])
    check_random_designs()
    print('CHECKER PASS:', c, 'exact edge-pair moment comparisons plus determinant tests')
