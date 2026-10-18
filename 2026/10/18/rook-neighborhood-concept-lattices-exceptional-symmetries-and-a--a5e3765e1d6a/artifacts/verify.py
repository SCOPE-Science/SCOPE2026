"""Finite corroboration of the rook-board neighborhood-closure theorem.
All checks are finite and do not replace the general proof.
"""
from itertools import combinations, permutations, product
from math import comb, factorial


def masks(m, n):
    V = [(i, j) for i in range(m) for j in range(n)]
    cross = [sum(1 << k for k, (r, c) in enumerate(V) if r == i or c == j)
             for i, j in V]
    return V, cross


def expected_family(m, n):
    V, cross = masks(m, n)
    U = (1 << len(V)) - 1
    F = {0, U}
    F.update(cross)
    for i in range(m):
        F.add(sum(1 << k for k, (r, c) in enumerate(V) if r == i))
    for j in range(n):
        F.add(sum(1 << k for k, (r, c) in enumerate(V) if c == j))
    F.update(1 << k for k in range(len(V)))
    for i, h in combinations(range(m), 2):
        for j, k in combinations(range(n), 2):
            F.add((1 << (i*n+j)) | (1 << (h*n+k)))
            F.add((1 << (i*n+k)) | (1 << (h*n+j)))
    return F


def make_closure(cross, bits):
    U = (1 << bits) - 1
    def closure(x):
        out = U
        for c in cross:
            if x & c == x:
                out &= c
        return out
    return closure


def saturate(S, m, n, k):
    U = (1 << (m*n)) - 1
    if k == 0:
        return S
    rows = [sum(1 << (i*n+j) for j in range(n)) for i in range(m)]
    cols = [sum(1 << (i*n+j) for i in range(m)) for j in range(n)]
    triples = []
    if k >= 3:
        for t in combinations(range(m*n), 3):
            if len({a//n for a in t}) == 3 and len({a%n for a in t}) == 3:
                triples.append(sum(1 << a for a in t))
    while True:
        out = S
        if k >= 2:
            for r in rows:
                if (S&r).bit_count() >= 2: out |= r
            for c in cols:
                if (S&c).bit_count() >= 2: out |= c
        if k >= 3 and any(S&t == t for t in triples):
            out = U
        if out == S:
            return S
        S = out


def verify(m, n, check_horn=True):
    V, cross = masks(m, n)
    f = make_closure(cross, m*n)
    expected = expected_family(m, n)
    predicted = 2 + 2*m*n + m + n + 2*comb(m, 2)*comb(n, 2)
    assert len(expected) == predicted, (m, n, len(expected), predicted)
    generated = set()
    for S in range(1 << (m*n)):
        C = f(S)
        assert C in expected, (m, n, S, C)
        generated.add(C)
        if check_horn:
            w = 0 if m == n == 2 else (2 if min(m, n) == 2 else 3)
            assert saturate(S, m, n, w) == C, (m, n, S, C)
    assert generated == expected
    if min(m, n) >= 3:
        # Four cells in a 2 x 2 rectangle, a target outside both selected rows and columns.
        S = (1 << 0) | (1 << 1) | (1 << n) | (1 << (n+1))
        target = 2*n+2
        assert f(S) & (1 << target)
        for bit in range(m*n):
            if S >> bit & 1:
                assert not (f(S ^ (1 << bit)) & (1 << target))
        # Any three-cell partial matching is inert under binary inference.
        M = (1 << 0) | (1 << (n+1)) | (1 << (2*n+2))
        assert f(M) == (1 << (m*n)) - 1
        assert saturate(M, m, n, 2) == M
    elif m*n > 4:
        S = (1 << 0) | (1 << 1)
        assert f(S) != S
        assert all(f(1 << t) == 1 << t for t in range(m*n))
    print('CASE', m, n, 'concepts', len(generated), 'subsets', 1 << (m*n),
          'iterative', (0 if m == n == 2 else (2 if min(m,n) == 2 else 3)),
          'PASS')


def check_thin_symmetries(n):
    V, cross = masks(2, n)
    f = make_closure(cross, 2*n)
    for p in permutations(range(n)):
        for q in permutations(range(n)):
            for flip in (0, 1):
                def perm(S):
                    out = 0
                    for i in range(2):
                        for j in range(n):
                            if S >> (i*n+j) & 1:
                                out |= 1 << (((i ^ flip) * n) + (p[j] if i == 0 else q[j]))
                    return out
                for S in range(1 << (2*n)):
                    assert perm(f(S)) == f(perm(S))
    print('THIN_WREATH', n, 'elements', 2*factorial(n)**2, 'PASS')


if __name__ == '__main__':
    for m,n in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
        verify(m,n,check_horn=m*n <= 12)
    for n in (3,4):
        check_thin_symmetries(n)
    print('VERIFY_OK closure_family=PASS concept_counts=PASS arity_bounds=PASS thin_symmetry=PASS')
