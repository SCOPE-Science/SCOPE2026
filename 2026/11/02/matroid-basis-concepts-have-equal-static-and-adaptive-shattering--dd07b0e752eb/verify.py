"""Standalone finite corroboration of matroid-basis shattering formulas.
Run with: python3 verify.py (Python 3.9+, standard library only).
"""
import itertools
import random
from functools import lru_cache


def gf2_rank(values):
    pivots = {}
    for x in values:
        while x:
            j = x.bit_length() - 1
            if j in pivots:
                x ^= pivots[j]
            else:
                pivots[j] = x
                break
    return len(pivots)


def analyze(columns):
    n = len(columns)
    rank = [gf2_rank([columns[j] for j in range(n) if s >> j & 1])
            for s in range(1 << n)]
    r = rank[-1]
    bases = tuple(s for s in range(1 << n) if s.bit_count() == r and rank[s] == r)
    key = tuple(bases)
    return rank, bases, key


def checks(rank, bases):
    n = (len(rank) - 1).bit_length()
    r = rank[-1]
    full = (1 << n) - 1
    nu = min(2 * rank[a] + n - a.bit_count() - r for a in range(1 << n))
    feasible = [a for a in range(1 << n)
                if rank[a] == a.bit_count() and rank[full ^ a] == r]
    vc = max(a.bit_count() for a in feasible)
    # independent coordinate-split recursion for the Littlestone dimension
    concepts = (1 << len(bases)) - 1
    positive = tuple(sum(1 << j for j, b in enumerate(bases) if b >> i & 1)
                     for i in range(n))
    @lru_cache(None)
    def ldim(active):
        answer = 0
        for p_all in positive:
            p, q = active & p_all, active & (concepts ^ p_all)
            if p and q:
                answer = max(answer, 1 + min(ldim(p), ldim(q)))
        return answer
    actual = ldim(concepts)
    assert vc == nu == actual, (rank, bases, vc, nu, actual)
    for p_all in positive:
        p, q = concepts & p_all, concepts & (concepts ^ p_all)
        if p and q:
            assert 1 + min(ldim(p), ldim(q)) == nu
    return nu


def main():
    distinct = set()
    tally = {}
    for n in range(1, 6):
        for ambient in range(1, 4):
            for columns in itertools.product(range(1 << ambient), repeat=n):
                ranks, bases, key = analyze(columns)
                if (n, key) in distinct:
                    continue
                distinct.add((n, key))
                d = checks(ranks, bases)
                tally[(n, d)] = tally.get((n, d), 0) + 1
    rng = random.Random(20261026)
    for n in (6, 7):
        for ambient in (2, 3, 4):
            for _ in range(160):
                columns = tuple(rng.randrange(1 << ambient) for _ in range(n))
                ranks, bases, key = analyze(columns)
                if (n, key) in distinct:
                    continue
                distinct.add((n, key))
                d = checks(ranks, bases)
                tally[(n, d)] = tally.get((n, d), 0) + 1
    # A concrete imbalanced matroid with rank and corank both five.
    # U_{1,5} direct sum U_{4,5}; VC/Littlestone dimension is 1+1=2.
    n = 10
    rank = []
    for a in range(1 << n):
        k1 = (a & 31).bit_count()
        k2 = (a >> 5).bit_count()
        rank.append(min(k1, 1) + min(k2, 4))
    bases = tuple(a for a in range(1 << n) if a.bit_count() == 5 and rank[a] == 5)
    assert checks(rank, bases) == 2
    print('MATROID_BASIS_SHATTERING_CHECKS_PASS')
    print('distinct_binary_matroids', len(distinct))
    print('per_size', [(n, sum(v for (k, d), v in tally.items() if k == n)) for n in range(1, 8)])
    print('imbalanced_U1_5_plus_U4_5', len(bases), 'VC=Ldim=2', 'rank=corank=5')


if __name__ == '__main__':
    main()
