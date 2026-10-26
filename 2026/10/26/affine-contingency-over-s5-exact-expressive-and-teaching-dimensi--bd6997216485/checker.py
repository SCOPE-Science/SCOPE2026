"""Finite checks for affine-contingency normal forms on single S5 clusters.

For k=1,...,4, enumerate all nonempty sets S of valuation vectors in F_2^k,
regard each v in S as a possible distinguished world, and compute the GF(2)
rank of the vector-valued generators 1, v_i, and C_s for s != 0.
The normal-form proof is independent of these finite checks.
"""
from itertools import combinations
from random import Random


def dot(s, v):
    return (s & v).bit_count() & 1


def cluster_generators(k, S, v):
    """Pack generator truth values into one binary row."""
    bits = 1 | (v << 1)
    for s in range(1, 1 << k):
        if len({dot(s, u) for u in S}) > 1:
            bits ^= 1 << (k + s)
    return bits


def rank(rows):
    basis = {}
    for x in rows:
        while x:
            p = x.bit_length() - 1
            if p not in basis:
                basis[p] = x
                break
            x ^= basis[p]
    return len(basis)


def experiments(k):
    vals = range(1 << k)
    generators = k + (1 << k)
    ranks = []
    for nmax in (k, k + 1):
        rows = []
        for r in range(1, nmax + 1):
            for S in combinations(vals, r):
                for v in S:
                    rows.append(cluster_generators(k, S, v))
        ranks.append(rank(rows))
    assert ranks == [generators - 1, generators], (k, ranks)
    for r in range(1, k + 1):
        for S in combinations(vals, r):
            par = sum(len({dot(s, v) for v in S}) > 1
                      for s in range(1, 1 << k)) % 2
            assert par == 0
    full = (0,) + tuple(1 << i for i in range(k))
    assert (sum(len({dot(s, v) for v in full}) > 1
                for s in range(1, 1 << k)) % 2) == 1
    return ranks


def canonical(expr):
    """Normal form as (constant bit, local variable bitmask, contingency bitmask)."""
    typ = expr[0]
    if typ == 'p':
        return 0, 1 << expr[1], 0
    if typ == 'b':
        return expr[1], 0, 0
    if typ == 'xor':
        c1, a1, b1 = canonical(expr[1]); c2, a2, b2 = canonical(expr[2])
        return c1 ^ c2, a1 ^ a2, b1 ^ b2
    if typ == 'C':
        _, a, _ = canonical(expr[1])
        return 0, 0, (1 << (a - 1)) if a else 0
    raise ValueError(typ)


def direct(expr, S, v):
    typ = expr[0]
    if typ == 'p':
        return (v >> expr[1]) & 1
    if typ == 'b':
        return expr[1]
    if typ == 'xor':
        return direct(expr[1], S, v) ^ direct(expr[2], S, v)
    if typ == 'C':
        return int(len({direct(expr[1], S, u) for u in S}) > 1)
    raise ValueError(typ)


def via_normal(expr, S, v):
    c, a, b = canonical(expr)
    z = c ^ dot(a, v)
    for s in range(1, b.bit_length() + 1):
        if (b >> (s-1)) & 1:
            z ^= int(len({dot(s, u) for u in S}) > 1)
    return z


def random_formula(rng, k, depth):
    if depth == 0 or rng.randrange(4) == 0:
        return ('p', rng.randrange(k)) if rng.randrange(3) else ('b', rng.randrange(2))
    if rng.randrange(3) == 0:
        return ('C', random_formula(rng, k, depth-1))
    return ('xor', random_formula(rng, k, depth-1), random_formula(rng, k, depth-1))


def nullspace_basis(dot_vector, k):
    """Produce a basis of the hyperplane of vectors orthogonal to dot_vector."""
    assert dot_vector != 0
    basis = []
    for v in range(1, 1 << k):
        if dot(dot_vector, v) == 0:
            x = v
            for b in basis:
                x = min(x, x ^ b)
            if x:
                basis.append(x)
    assert len(basis) == k - 1
    return tuple(basis)


def teaching_set(k):
    """Exactly k+2**k explicit pointed models; each uses <=k+1 worlds."""
    worlds = [((0,), 0)]
    worlds.extend([((1 << i,), 1 << i) for i in range(k)])
    worlds.append(((0,) + tuple(1 << i for i in range(k)), 0))
    for s in range(1, (1 << k) - 1):
        worlds.append(((0,) + nullspace_basis(s, k), 0))
    assert len(worlds) == k + (1 << k)
    assert max(map(lambda model: len(model[0]), worlds)) == k + 1
    ranks = rank(cluster_generators(k, S, v) for S, v in worlds)
    assert ranks == k + (1 << k), (k, ranks)
    return len(worlds)


def check_random_syntax(k, num=1200):
    rng = Random(491 + k)
    vals = list(range(1 << k))
    for _ in range(num):
        formula = random_formula(rng, k, rng.randrange(1, 7))
        S = tuple(rng.sample(vals, rng.randrange(1, len(vals)+1)))
        v = rng.choice(S)
        assert direct(formula, S, v) == via_normal(formula, S, v), (formula, S, v)


if __name__ == '__main__':
    for k in range(1, 5):
        ranks = experiments(k)
        assert teaching_set(k) == k + (1 << k)
        print('k=%d variables, <=k rank=%d, <=k+1 rank=%d, classes=%d' % (
            k, ranks[0], ranks[1], 1 << ranks[1]))
        if k <= 3:
            check_random_syntax(k)
    print('ALL CHECKS PASSED')
