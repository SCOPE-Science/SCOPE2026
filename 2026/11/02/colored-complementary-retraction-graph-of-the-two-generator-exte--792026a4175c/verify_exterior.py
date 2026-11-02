"""Exhaustive idempotent and commutation checks for exterior algebras on two generators."""
from itertools import product
from collections import Counter


def field(q):
    if q in (2, 3, 5):
        add = lambda a, b: (a + b) % q
        neg = lambda a: (-a) % q
        mul = lambda a, b: (a * b) % q
    elif q in (4, 8):
        k = (q.bit_length() - 1)
        irr = 0b111 if q == 4 else 0b1011
        add = lambda a, b: a ^ b
        neg = lambda a: a
        def mul(a, b):
            c = 0
            while b:
                if b & 1:
                    c ^= a
                b >>= 1
                a <<= 1
                if a & q:
                    a ^= irr
            return c
    else:
        raise ValueError('unsupported finite-field order')
    sub = lambda a, b: add(a, neg(b))
    return add, mul, sub


def compose(F, G, add, mul, sub):
    a, b, c, d, e, f = F
    u, v, w, r, s, t = G
    det = sub(mul(a, e), mul(b, d))
    return (
        add(mul(a, u), mul(d, v)),
        add(mul(b, u), mul(e, v)),
        add(add(mul(c, u), mul(f, v)), mul(det, w)),
        add(mul(a, r), mul(d, s)),
        add(mul(b, r), mul(e, s)),
        add(add(mul(c, r), mul(f, s)), mul(det, t)),
    )


def check(q):
    add, mul, sub = field(q)
    maps = list(product(range(q), repeat=6))
    # Every map x -> ax+by+cz, y -> dx+ey+fz satisfies the exterior relations.
    for a,b,c,d,e,f in maps:
        assert sub(mul(a,b), mul(b,a)) == 0
        assert sub(mul(d,e), mul(e,d)) == 0
        assert add(sub(mul(a,e),mul(b,d)), sub(mul(d,b),mul(e,a))) == 0
    identity = (1,0,0,0,1,0)
    augmentation = (0,0,0,0,0,0)
    E = [F for F in maps if compose(F, F, add, mul, sub) == F]
    assert identity in E and augmentation in E
    assert len(E) == 2 + q*q*(q+1), (q, len(E))
    S = [F for F in E if F not in (identity, augmentation)]
    assert len(S) == q*q*(q+1)
    assert all(sub(mul(F[0],F[4]),mul(F[1],F[3])) == 0 for F in S)
    # Multiplication is evaluated on the generators, not using a precomputed graph.
    commutes = lambda F,G: compose(F,G,add,mul,sub) == compose(G,F,add,mul,sub)
    adj = {F:set() for F in S}
    for i,F in enumerate(S):
        for G in S[i+1:]:
            if commutes(F,G):
                adj[F].add(G)
                adj[G].add(F)
                assert compose(F,G,add,mul,sub) == augmentation
    assert all(len(adj[F]) == q for F in S)
    remaining = set(S)
    comp_sizes = []
    while remaining:
        root = remaining.pop()
        cluster = {root}
        todo = [root]
        while todo:
            v = todo.pop()
            for w in adj[v]:
                if w in remaining:
                    remaining.remove(w)
                    cluster.add(w)
                    todo.append(w)
        assert len(cluster) == 2*q
        assert sum(len(adj[F]) for F in cluster) == 2*q*q
        # The graph induced by each cluster is complete bipartite K_{q,q}.
        side1 = adj[root]
        side2 = cluster-side1
        assert len(side1) == len(side2) == q
        assert all(adj[F] == side1 for F in side2)
        assert all(adj[F] == side2 for F in side1)
        comp_sizes.append(len(cluster))
    expected_components = q*(q+1)//2
    assert len(comp_sizes) == expected_components
    maximal_families = sum(len(adj[F]) for F in S)//2
    assert maximal_families == q**3*(q+1)//2
    total_commuting = sum(commutes(F,G) for F in E for G in E)
    assert total_commuting == q*q*(q+1)*(q+5)+4
    assert all(commutes(identity,F) and commutes(augmentation,F) for F in E)
    print(f'q={q} maps={len(maps)} idempotents={len(E)} components={len(comp_sizes)} maximal_families={maximal_families} commuting_ordered={total_commuting}')


if __name__ == '__main__':
    for q in (2,3,4,5,8):
        check(q)
    print('VERIFY_OK exterior retraction commutation census')
