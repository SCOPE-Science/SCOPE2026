"""Independent finite checks for two-occurrence consecutive-pattern packings.

Only Python 3 standard library is needed. This checks finite cases; the
all-m statement follows from the mathematical two-chain interleaving proof.
"""
from functools import lru_cache
from math import comb


def patterns(m):
    assert m >= 4
    odds = list(range(1, 2*m, 2))
    evens = list(range(2, 2*m+1, 2))
    prefix = [1, 3, 4, 7] + list(range(9, 2*m, 2))
    suffix = sorted(set(range(1, 2*m+1)).difference(prefix))
    assert len(prefix) == len(suffix) == m
    assert sorted(prefix + suffix) == list(range(1, 2*m+1))
    return tuple(prefix + suffix), tuple(odds + evens)


def order_type(seq):
    order = {v: i for i, v in enumerate(sorted(seq))}
    return tuple(order[v] for v in seq)


def count_by_gap_formula(pattern, m):
    K = len(pattern)
    assert K == 2*m
    P = sorted(pattern[:m])
    S = sorted(pattern[m:])
    assert pattern[:m] == tuple(P) and pattern[m:] == tuple(S)
    assert len(set(P+S)) == K
    def gaps(shared):
        bounds = [0] + shared + [K+1]
        return [sum(lo < value < hi for value in range(1, K+1)
                    if value not in shared)
                for lo, hi in zip(bounds, bounds[1:])]
    a, b = gaps(S), gaps(P)
    assert sum(a) == sum(b) == m
    return __import__('math').prod(comb(x+y,x) for x,y in zip(a,b)), tuple(a), tuple(b)


def chain_constraints(pattern, m):
    K = len(pattern)
    n = K + (K-m)
    before = [0]*n
    for shift in (0, K-m):
        positions = sorted(range(K), key=lambda i: pattern[i])
        for u, v in zip(positions, positions[1:]):
            before[shift + v] |= 1 << (shift + u)
    return before


def count_by_independent_poset_dp(pattern, m):
    prerequisites = chain_constraints(pattern,m)
    n = len(prerequisites)
    all_mask = (1<<n)-1
    @lru_cache(None)
    def count(mask):
        if mask == all_mask:
            return 1
        return sum(count(mask | (1<<v)) for v in range(n)
                   if (mask & (1<<v)) == 0 and
                   (mask & prerequisites[v]) == prerequisites[v])
    return count(0)


def list_actual_permutations(pattern,m):
    prerequisites = chain_constraints(pattern,m)
    n = len(prerequisites)
    ranks = []
    def recurse(mask,order):
        if len(order)==n:
            sigma = [0]*n
            for value, position in enumerate(order,1):
                sigma[position] = value
            sigma=tuple(sigma)
            assert order_type(sigma[:2*m]) == order_type(pattern)
            assert order_type(sigma[m:]) == order_type(pattern)
            ranks.append(sigma)
            return
        for v in range(n):
            if (mask & (1<<v)) == 0 and (mask & prerequisites[v]) == prerequisites[v]:
                recurse(mask|(1<<v),order+[v])
    recurse(0,[])
    assert len(set(ranks)) == len(ranks)
    return ranks


def main():
    a4, b4 = patterns(4)
    assert a4 == (1,3,4,7,2,5,6,8)
    assert b4 == (1,3,5,7,2,4,6,8)
    direct_a = list_actual_permutations(a4,4)
    direct_b = list_actual_permutations(b4,4)
    assert len(direct_a) == 9 and len(direct_b) == 8
    print('ALL_PRESCRIBED_OCCURRENCES_DIRECTLY_RECONSTRUCTED 4 9 8')
    for m in range(4,11):
        family, alternate = patterns(m)
        for kind, pattern, expected in (
            ('family',family, 9*2**(m-4)),
            ('interleaved',alternate,2**(m-1))):
            formula, gaps_a, gaps_b = count_by_gap_formula(pattern,m)
            independently = count_by_independent_poset_dp(pattern,m)
            assert formula == expected == independently, (m,kind,formula,independently)
            if kind == 'family':
                assert gaps_a == (1,2,0) + (1,)*(m-3) + (0,)
                assert gaps_b == (0,1,0,2) + (1,)*(m-3)
            else:
                assert gaps_a == (1,)*m + (0,)
                assert gaps_b == (0,) + (1,)*m
        print('INDEPENDENT_CHAIN_DP_AND_GAPS_OK', m, 9*2**(m-4), 2**(m-1))
    print('VERIFY_OK')

if __name__=='__main__':
    main()
