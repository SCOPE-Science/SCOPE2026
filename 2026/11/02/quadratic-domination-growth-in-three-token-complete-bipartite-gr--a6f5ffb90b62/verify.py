"""Direct finite checks of an extremal set construction and triangle deletion inequality.
Run: python verify.py  (Python standard library only).
This is not an infinite-proof certificate: the proof is in RESULT.md.
"""
from itertools import combinations
from math import comb


def q(n):
    return comb(n, 2) - n*n//4


def witness(m, n):
    assert 2 <= m <= n and n >= 4
    A = tuple(range(m))
    B = tuple(range(m, m+n))
    left = B[:n//2]
    right = B[n//2:]
    R = set(left[:2] + right[:1])
    assert len(R) == 3
    D = {tuple(sorted((0, i, j))) for part in (left, right)
         for i,j in combinations(part, 2)}
    D.update((a,b,i) for a,b in combinations(A[1:], 2) for i in B)
    D.update((0,1,i) for i in B if i not in R)
    D.add(tuple(sorted(R)))
    return D


def dominates_directly(D, m, n):
    nodes = set(range(m+n))
    for v in combinations(range(m+n), 3):
        if v in D:
            continue
        s = set(v)
        adjacent_to_chosen = any(
            tuple(sorted((s - {u}) | {w})) in D
            for u in v for w in nodes - s if (u < m) != (w < m)
        )
        if not adjacent_to_chosen:
            raise AssertionError((m,n,v))


def test_construction():
    count = 0
    for m in range(2, 9):
        for n in range(max(m, 4), 19):
            D = witness(m,n)
            target = q(n) + (comb(m-1,2)+1)*n - 2
            assert len(D) == target, (m,n,len(D),target)
            dominates_directly(D,m,n)
            count += 1
    print('ORIGINAL_THREE_TOKEN_GRAPH_DOMINATION_OK', count)


def test_triangle_lemma():
    # Enumerate all graphs on n vertices (through n=6), use the actual
    # triangle set and verify the edge-deletion budget before Mantel.
    count = 0
    for n in range(3, 7):
        pairs = list(combinations(range(n),2))
        triples = list(combinations(range(n),3))
        for mask in range(1<<len(pairs)):
            edges = {pairs[i] for i in range(len(pairs)) if mask>>i & 1}
            triangles = [T for T in triples if all(e in edges for e in combinations(T,2))]
            deleted = {next(e for e in combinations(T,2) if e in edges) for T in triangles}
            residual = edges - deleted
            assert not any(all(e in residual for e in combinations(T,2)) for T in triples)
            assert len(residual) <= n*n//4
            assert len(edges)-len(triangles) <= n*n//4
            count += 1
    print('ALL_GRAPH_TRIANGLE_DELETION_AND_MANTEL_OK', count)


def test_small_optimum():
    # Exact direct enumeration of all sets smaller than 4 for F3(K2,4).
    m,n = 2,4
    V = list(combinations(range(m+n),3))
    idx = {x:i for i,x in enumerate(V)}
    closed = []
    for v in V:
        s = set(v); mask = 1<<idx[v]
        for u in v:
            for w in set(range(m+n))-s:
                if (u<m)!=(w<m):
                    mask |= 1<<idx[tuple(sorted(s-{u}|{w}))]
        closed.append(mask)
    full = (1<<len(V))-1
    for t in range(4):
        for inds in combinations(range(len(V)),t):
            cover = 0
            for i in inds: cover |= closed[i]
            assert cover != full, (m,n,inds)
    assert len(witness(m,n)) == 4
    print('EXHAUSTIVE_MINIMUM_K24_OK', len(V))


def test_limits():
    for m in range(2, 30):
        for n in (max(4,m), 2*m, 10*m):
            low=q(n)
            up=q(n)+(comb(m-1,2)+1)*n-2
            assert 0<=low<=up
    print('ASYMPTOTIC_BOUNDS_ARITHMETIC_OK')

if __name__ == '__main__':
    test_construction()
    test_triangle_lemma()
    test_small_optimum()
    test_limits()
    print('VERIFY_OK')
