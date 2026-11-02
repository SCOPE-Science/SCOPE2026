"""Exact independent enumerations of binary linear Hamming anticodes of diameter at most four."""
from collections import Counter
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial

EXPECTED = {
    0: (1, 0, 0, 0, 0),
    1: (0, 1, 0, 0, 0),
    2: (0, 1, 1, 0, 0),
    3: (0, 1, 4, 1, 0),
    4: (0, 1, 13, 11, 1),
    5: (0, 0, 25, 55, 11),
    6: (0, 0, 15, 75, 10),
    7: (0, 0, 0, 30, 0),
}


def rref_tally(s):
    """All subspaces exactly once, via pivot-fixed reduced row-echelon bases."""
    out = [0] * 5
    for k in range(min(s, 4) + 1):
        subspace_total = 0
        for piv in combinations(range(s), k):
            free = [j for j in range(s) if j not in piv]
            opts = []
            for p in piv:
                right = [j for j in free if j > p]
                opts.append([(1 << p) | sum(((z >> t) & 1) << j
                                              for t, j in enumerate(right))
                             for z in range(1 << len(right))])
            for basis in product(*opts):
                subspace_total += 1
                words = [0]
                for v in basis:
                    words += [v ^ w for w in words]
                if any(w.bit_count() > 4 for w in words):
                    continue
                support = 0
                for v in basis:
                    support |= v
                if support == (1 << s) - 1:
                    out[k] += 1
        # Each RREF matrix must appear exactly once: compare against the
        # closed Gaussian-binomial count of all k-subspaces of F_2^s.
        numerator = 1
        denominator = 1
        for j in range(k):
            numerator *= (1 << (s-j)) - 1
            denominator *= (1 << (k-j)) - 1
        assert subspace_total == numerator // denominator, (s,k,subspace_total)
    return tuple(out)


def binary_rank(columns):
    pivots = {}
    for x in columns:
        while x:
            j = x.bit_length() - 1
            if j in pivots:
                x ^= pivots[j]
            else:
                pivots[j] = x
                break
    return len(pivots)


def multiset_tally(s):
    """Independent generator-column classification, quotient by GL(k,2)."""
    answer = [0] * 5
    if s == 0:
        return (1, 0, 0, 0, 0)
    for k in range(1, min(s, 4) + 1):
        basis_count = 1
        for i in range(k):
            basis_count *= (1 << k) - (1 << i)
        matrix_count = 0
        for entries in combinations_with_replacement(range(1, 1 << k), s):
            distinct = set(entries)
            if binary_rank(distinct) != k:
                continue
            if any(sum(((u & v).bit_count() & 1) for v in entries) > 4
                   for u in range(1, 1 << k)):
                continue
            multiplicities = Counter(entries)
            permutations = factorial(s)
            for v in multiplicities.values():
                permutations //= factorial(v)
            matrix_count += permutations
        assert matrix_count % basis_count == 0, (s,k,matrix_count,basis_count)
        answer[k] = matrix_count // basis_count
    return tuple(answer)


def main():
    for s in range(8):
        a = rref_tally(s)
        b = multiset_tally(s)
        assert a == b == EXPECTED[s], (s,a,b,EXPECTED[s])
        print('SUPPORT',s,'BY_DIM',','.join(map(str,a)))
    for n in (0,1,2,3,4,5,7,8,12,30):
        exact = sum(comb(n,s)*sum(v) for s,v in EXPECTED.items() if s<=n)
        by_dimension = [sum(comb(n,s)*EXPECTED[s][k] for s in range(min(n,7)+1))
                        for k in range(5)]
        assert exact == sum(by_dimension)
        print('LENGTH',n,'TOTAL',exact)
    print('VERIFY_OK')


if __name__=='__main__':
    main()
