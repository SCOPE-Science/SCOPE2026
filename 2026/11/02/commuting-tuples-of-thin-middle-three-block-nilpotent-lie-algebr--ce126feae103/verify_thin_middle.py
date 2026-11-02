#!/usr/bin/env python3
"""Independent exhaustive finite-field checks of thin-middle commuting loci.
Run with Python 3; uses only the standard library.
"""
from itertools import product


def field(q):
    if q in (2, 3):
        return (lambda x, y: (x + y) % q), (lambda x, y: (x * y) % q)
    if q == 4:
        def mul(x, y):
            z = 0
            for i in range(2):
                if (y >> i) & 1:
                    z ^= x << i
            if z & 8:
                z ^= 0b1110
            if z & 4:
                z ^= 0b111
            return z
        return (lambda x, y: x ^ y), mul
    raise ValueError('unsupported test field')


def commute(v, w, a, c, mul):
    u, b, up, bp = v[:a], v[a:], w[:a], w[a:]
    return all(mul(u[i], bp[j]) == mul(up[i], b[j]) for i in range(a) for j in range(c))


def rank_at_most_one(vecs, add, mul):
    m = len(vecs)
    if not m:
        return True
    d = len(vecs[0])
    return all(mul(vecs[j][i], vecs[k][h]) == mul(vecs[k][i], vecs[j][h])
               for i in range(d) for h in range(i + 1, d)
               for j in range(m) for k in range(j + 1, m))


def predicted(q, a, c, m):
    return q ** (a * m) + q ** (c * m) - 1 + ((q ** a - 1) * (q ** c - 1) * (q ** m - 1)) // (q - 1)


def verify_points(q, a, c, m):
    add, mul = field(q)
    d = a + c
    got = 0
    for z in product(range(q), repeat=d * m):
        vecs = [z[j*d:(j+1)*d] for j in range(m)]
        cc = all(commute(vecs[j], vecs[k], a, c, mul) for j in range(m) for k in range(j+1, m))
        pure_u = all(all(x == 0 for x in v[a:]) for v in vecs)
        pure_b = all(all(x == 0 for x in v[:a]) for v in vecs)
        determinantal = rank_at_most_one(vecs, add, mul)
        assert cc == (pure_u or pure_b or determinantal), ('component disagreement', q,a,c,m,vecs)
        got += cc
    want = predicted(q, a, c, m)
    assert got == want, (q,a,c,m,got,want)
    return got


def max_abelian(q, a, c):
    add, mul = field(q)
    d = a + c
    zero = tuple([0] * d)
    ambient = list(product(range(q), repeat=d))
    spaces = {frozenset([zero])}
    todo = [frozenset([zero])]
    while todo:
        U = todo.pop()
        for v in ambient:
            if v in U:
                continue
            new = frozenset(tuple(add(u[i], mul(t, v[i])) for i in range(d)) for u in U for t in range(q))
            if new not in spaces:
                spaces.add(new)
                todo.append(new)
    abelian = [U for U in spaces if all(commute(x,y,a,c,mul) for x in U for y in U)]
    maximal = [U for U in abelian if not any(U < W for W in abelian)]
    pure_u = frozenset(v for v in ambient if all(x == 0 for x in v[a:]))
    pure_b = frozenset(v for v in ambient if all(x == 0 for x in v[:a]))
    mixed = []
    for v in ambient:
        if not any(v[:a]) or not any(v[a:]):
            continue
        L = frozenset(tuple(mul(t, v[i]) for i in range(d)) for t in range(q))
        if L not in mixed:
            mixed.append(L)
    want = set(mixed + [pure_u,pure_b])
    assert set(maximal) == want, ('max abelian mismatch',q,a,c,len(maximal),len(want))
    assert len(maximal) == 2 + ((q ** a - 1) * (q ** c - 1)) // (q - 1)
    return len(spaces), len(maximal)


def run():
    configs = [(2,1,1,1),(2,1,1,3),(2,1,2,2),(2,2,2,2),
               (2,2,2,3),(2,3,1,3),(2,2,3,2),
               (3,1,1,4),(3,2,1,3),(3,2,2,2),
               (4,1,1,3),(4,2,1,2),(4,2,2,2)]
    for q,a,c,m in configs:
        got = verify_points(q,a,c,m)
        print('CHECK',q,a,c,m,got)
    for q,a,c in [(2,2,2),(3,1,2)]:
        n, ab = max_abelian(q,a,c)
        print('SUBSPACES',q,a,c,n,ab)
    print('THIN_MIDDLE_COMMUTING_GEOMETRY_OK',len(configs),2)

if __name__ == '__main__':
    run()
