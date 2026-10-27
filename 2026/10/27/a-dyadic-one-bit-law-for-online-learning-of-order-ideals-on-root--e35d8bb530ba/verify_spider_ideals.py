"""Independent finite check of the Littlestone dimension of rooted-spider ideals.
Run: python3 spider_verifier.py. No dependencies beyond Python's stdlib.
A spider arm of length ell has ell vertices above a common minimal root.
"""
from functools import lru_cache
from itertools import combinations_with_replacement, product


def direct_ld(arms):
    n = 1 + sum(arms)
    ancestors = [0]
    for length in arms:
        parent = 0
        for _ in range(length):
            i = len(ancestors)
            ancestors.append(ancestors[parent] | (1 << parent))
            parent = i
    concepts = []
    for s in range(1 << n):
        if all((s & (1 << v)) == 0 or (s & ancestors[v]) == ancestors[v]
               for v in range(n)):
            concepts.append(s)
    query_bits = [sum(1 << j for j, ideal in enumerate(concepts)
                      if ideal & (1 << v)) for v in range(n)]
    @lru_cache(None)
    def rank(mask):
        if mask.bit_count() <= 1:
            return 0
        best = 0
        for query in query_bits:
            a = mask & query
            b = mask & ~query
            if a and b:
                cand = 1 + min(rank(a), rank(b))
                if cand > best:
                    best = cand
        return best
    return rank((1 << len(concepts)) - 1), len(concepts)


def predicted(arms):
    counts = [ell + 1 for ell in arms]
    baseline = sum(b.bit_length() - 1 for b in counts)
    bonus = all(b == (1 << b.bit_length()) - 1 for b in counts)
    return baseline + int(bonus), 1 + __import__('math').prod(counts)


def run():
    checks = 0
    examples = []
    for k in range(0, 6):
        for arms in combinations_with_replacement(range(1, 9), k):
            if 1 + sum(arms) > 13:
                continue
            expected, num_ideals = predicted(arms)
            observed, found_ideals = direct_ld(arms)
            assert (observed, found_ideals) == (expected, num_ideals), (
                arms, (observed, found_ideals), (expected, num_ideals))
            checks += 1
            if arms in ((), (1,), (2,), (2, 2), (1, 2), (2, 2, 2), (2, 6), (3, 3), (6,)):
                examples.append((arms, found_ideals, observed))
    print(f'rooted_spiders_checked={checks}')
    for arms, ideals, rank in examples:
        print(f'arms={arms} ideals={ideals} Ldim={rank}')
    print('ALL_FORMULA_CHECKS_PASS')
if __name__ == '__main__':
    run()
