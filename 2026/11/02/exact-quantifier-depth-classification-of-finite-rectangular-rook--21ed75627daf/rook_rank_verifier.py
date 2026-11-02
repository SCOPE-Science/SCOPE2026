"""Exact finite-type checks for rectangular rook graphs (Python 3, stdlib only).

Computes quantifier-rank types by recursion over every one-point extension.
The orbit implementation uses first-appearance row/column patterns.  A
second implementation uses the actual vertices without orbit compression.
Neither finite check substitutes for the uniform Ehrenfeucht-Fraisse proof.
"""
from functools import lru_cache
from itertools import combinations


def signature(pairs):
    return tuple((int(pairs[i] == pairs[j]),
                  int(pairs[i] != pairs[j] and
                      (pairs[i][0] == pairs[j][0] or
                       pairs[i][1] == pairs[j][1])))
                 for i in range(len(pairs)) for j in range(i))


def canonical(rows, cols, m, n):
    if m == n and (cols, rows) < (rows, cols):
        return cols, rows
    return rows, cols


def orbit_types(maxrank, maxside):
    intern = {}
    def number(key):
        if key not in intern:
            intern[key] = len(intern)
        return intern[key]

    @lru_cache(None)
    def typ(m, n, rows, cols, left):
        atoms = signature(tuple(zip(rows, cols)))
        if not left:
            return number((0, len(rows), atoms))
        nr, nc = len(set(rows)), len(set(cols))
        children = set()
        for rr in range(nr + (nr < m)):
            for cc in range(nc + (nc < n)):
                ar, ac = canonical(rows + (rr,), cols + (cc,), m, n)
                children.add(typ(m, n, ar, ac, left-1))
        return number((left, len(rows), atoms, tuple(sorted(children))))

    out = {}
    cases = [(m, n) for m in range(2, maxside+1)
                     for n in range(m, maxside+1)]
    for rank in range(2, maxrank+1):
        out[rank] = {case: typ(*case, (), (), rank) for case in cases}
        predicted = {case: (min(case[0], rank), min(case[1], rank))
                     for case in cases}
        for a in cases:
            for b in cases:
                assert (out[rank][a] == out[rank][b]) == (predicted[a] == predicted[b]), (rank,a,b)
        nc = len(set(out[rank].values()))
        assert nc == rank * (rank-1)//2
        print(f"ORBIT_TYPES_OK rank={rank} sides=2..{maxside} classes={nc} graphs={len(cases)}")
    return out


def direct_types(maxrank, maxside):
    intern = {}
    def number(key):
        if key not in intern:
            intern[key] = len(intern)
        return intern[key]

    @lru_cache(None)
    def typ(m, n, verts, left):
        atoms = signature(verts)
        if not left:
            return number((0, len(verts), atoms))
        children = set()
        for x in range(m):
            for y in range(n):
                children.add(typ(m, n, verts + ((x,y),), left-1))
        return number((left, len(verts), atoms, tuple(sorted(children))))

    cases = [(m,n) for m in range(2,maxside+1) for n in range(m,maxside+1)]
    for rank in range(2,maxrank+1):
        types = {case: typ(*case, (), rank) for case in cases}
        for a in cases:
            for b in cases:
                expected = (min(a[0],rank),min(a[1],rank)) == (min(b[0],rank),min(b[1],rank))
                assert (types[a] == types[b]) == expected, (rank,a,b)
        print(f"DIRECT_TYPES_OK rank={rank} sides=2..{maxside} graphs={len(cases)}")


def clique_independence():
    for m in range(2,5):
        for n in range(m,5):
            vs = [(x,y) for x in range(m) for y in range(n)]
            def adj(a,b): return a != b and (a[0] == b[0] or a[1] == b[1])
            # Explicitly enumerate all candidate sets up through one past each predicted maximum.
            for kind, best in [('clique',n),('independent',m)]:
                def ok(chosen):
                    return all(adj(a,b) == (kind == 'clique') for a,b in combinations(chosen,2))
                assert any(ok(c) for c in combinations(vs,best))
                assert not any(ok(c) for c in combinations(vs,best+1))
    print('DIRECT_CLIQUE_INDEPENDENCE_OK sides=2..4')


if __name__ == '__main__':
    orbit_types(5, 7)
    direct_types(4, 4)
    clique_independence()
    print('VERIFY_OK')
