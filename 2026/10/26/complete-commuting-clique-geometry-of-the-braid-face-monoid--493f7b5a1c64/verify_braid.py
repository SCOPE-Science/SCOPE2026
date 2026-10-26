#!/usr/bin/env python3
"""Independent finite checks for commuting ordered partitions under the Tits product.

Run with: python verify_braid.py
Uses only the Python standard library.
"""
from itertools import permutations, combinations, product
from math import factorial


def all_faces(n):
    """Enumerate ordered partitions, independently via all surjections."""
    for k in range(1, n + 1):
        for labels in product(range(k), repeat=n):
            if len(set(labels)) == k:
                yield tuple(tuple(i for i, lab in enumerate(labels) if lab == j)
                            for j in range(k))


def multiply(x, y):
    out = []
    for a in x:
        for b in y:
            c = tuple(i for i in a if i in b)
            if c:
                out.append(c)
    return tuple(out)


def fubini(n):
    return sum(factorial(k) * stirling(n, k) for k in range(n + 1))


def stirling(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    if k > n:
        return 0
    v = [[0] * (k + 1) for _ in range(n + 1)]
    v[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            v[i][j] = j * v[i-1][j] + v[i-1][j-1]
    return v[n][k]


def expected_t(n, r):
    return sum(factorial(k) * stirling(n, k) * (2**r-1)**(k-1)
               for k in range(1, n + 1))


def coarsenings(sigma):
    n = len(sigma)
    return frozenset(tuple(tuple(sorted(sigma[a:b])) for a, b in
                           zip((0,) + cuts, cuts + (n,)))
                     for size in range(n)
                     for cuts in combinations(range(1, n), size))


def run():
    operations = 0
    for n in range(1, 6):
        faces = list(all_faces(n))
        expected_total = fubini(n)
        assert len(faces) == expected_total, (n, len(faces), expected_total)
        idx = {face: i for i, face in enumerate(faces)}
        # Direct products by nonempty intersections (no sign-vector shortcut).
        commute = [[False]*len(faces) for _ in faces]
        for i, a in enumerate(faces):
            for j in range(i, len(faces)):
                b = faces[j]
                val = multiply(a, b) == multiply(b, a)
                commute[i][j] = commute[j][i] = val
                operations += 1
        t2 = sum(sum(row) for row in commute)
        assert t2 == expected_t(n, 2), (n, t2, expected_t(n, 2))
        for i, a in enumerate(faces):
            c = sum(commute[i])
            theory = 2**(len(a)-1)
            for block in a:
                theory *= fubini(len(block))
            assert c == theory, (n, a, c, theory)
            operations += 1
        if n <= 3:
            for r in (3, 4):
                tr = sum(1 for indices in product(range(len(faces)), repeat=r)
                         if all(commute[indices[a]][indices[b]]
                                for a in range(r) for b in range(a + 1, r)))
                assert tr == expected_t(n, r), (n, r, tr, expected_t(n, r))
            for k in range(1, 2**(n-1) + 1):
                ck = sum(1 for indices in combinations(range(len(faces)), k)
                         if all(commute[a][b] for a, b in combinations(indices, 2)))
                # Independent falling-factorial basis inversion for the tuple count.
                coeff = [0]*(k+1)
                coeff[0] = 1
                for j in range(k):
                    nxt = [0]*(k+1)
                    for d in range(j+1):
                        nxt[d+1] += coeff[d]
                        nxt[d] -= j*coeff[d]
                    coeff = nxt
                predicted = sum(coeff[j]*expected_t(n,j) for j in range(1,k+1))//factorial(k)
                assert ck == predicted, (n,k,ck,predicted)
                operations += 1
        if n <= 4:
            chambers = list(permutations(range(n)))
            max_sets = [coarsenings(p) for p in chambers]
            assert len(set(max_sets)) == factorial(n)
            for ch, cl in zip(chambers, max_sets):
                assert len(cl) == 2**(n-1)
                assert all(commute[idx[a]][idx[b]] for a in cl for b in cl)
                operations += len(cl)**2
            # Exact criterion: two faces commute iff a common chamber contains both.
            for i, a in enumerate(faces):
                for j, b in enumerate(faces):
                    common = any(a in cl and b in cl for cl in max_sets)
                    assert common == commute[i][j], (n, a, b)
                    operations += 1
            for s, p in enumerate(chambers):
                for t in range(s, len(chambers)):
                    q = chambers[t]
                    shared_prefixes = sum(set(p[:j]) == set(q[:j])
                                          for j in range(1,n))
                    assert len(max_sets[s] & max_sets[t]) == 2**shared_prefixes
                    operations += 1
        print('verified n=', n, 'faces=',len(faces),'commuting pairs=',t2)
    # Complete overlap distribution against direct-sum indecomposables.
    for n in range(1,8):
        inde = [0]*(n+1)
        inde[1] = 1
        for m in range(2,n+1):
            inde[m] = factorial(m)-sum(inde[j]*factorial(m-j) for j in range(1,m))
        predicted = [0]*n
        def compositions(remaining, ways, count):
            if remaining == 0:
                predicted[count-1] += ways
                return
            for block_len in range(1,remaining+1):
                compositions(remaining-block_len, ways*inde[block_len], count+1)
        compositions(n,1,0)
        observed = [0]*n
        for p in permutations(range(n)):
            d = sum(set(p[:j]) == set(range(j)) for j in range(1,n))
            observed[d] += 1
        assert observed == predicted, (n,observed,predicted)
        operations += factorial(n)
    print('VERIFY_OK', operations, 'finite direct product, tuple, centralizer, maximal-clique, and overlap-spectrum checks')


if __name__ == '__main__':
    run()
