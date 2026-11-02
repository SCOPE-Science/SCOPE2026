#!/usr/bin/env python3
"""Complete certificate for Nash loss from lexicographic rank-maximal stable matching."""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product

EXPECTED = {
    Fraction(1, 1): 42756,
    Fraction(4, 3): 2484,
    Fraction(16, 9): 432,
    Fraction(64, 27): 12,
    Fraction(8, 3): 828,
    Fraction(32, 9): 72,
    Fraction(16, 3): 72,
}


def complete_census(n):
    preferences = tuple(permutations(range(n)))
    counts = Counter()
    stable_sizes = Counter()
    rank_maximality = Counter()
    first_worst = None
    for profile in product(preferences, repeat=2*n):
        male_rank = [[pref.index(w) + 1 for w in range(n)] for pref in profile[:n]]
        female_rank = [[pref.index(m) + 1 for m in range(n)] for pref in profile[n:]]
        options = []
        for matching in permutations(range(n)):
            woman_partner = [matching.index(w) for w in range(n)]
            blocked = any(male_rank[m][w] < male_rank[m][matching[m]] and
                          female_rank[w][m] < female_rank[w][woman_partner[w]]
                          for m in range(n) for w in range(n) if matching[m] != w)
            if blocked:
                continue
            selected_ranks = ([male_rank[m][matching[m]] for m in range(n)] +
                              [female_rank[w][woman_partner[w]] for w in range(n)])
            count_vector = tuple(selected_ranks.count(r) for r in range(1, n+1))
            welfare_product = 1
            for rank in selected_ranks:
                welfare_product *= n + 1 - rank
            options.append((matching, count_vector, welfare_product))
        assert options
        stable_sizes[len(options)] += 1
        lex_best = max(entry[1] for entry in options)
        max_welfare = max(entry[2] for entry in options)
        lex_welfares = {entry[2] for entry in options if entry[1] == lex_best}
        assert len(lex_welfares) == 1
        lex_welfare = next(iter(lex_welfares))
        q = Fraction(max_welfare, lex_welfare)
        counts[q] += 1
        nash_best = {entry[0] for entry in options if entry[2] == max_welfare}
        lex_best_set = {entry[0] for entry in options if entry[1] == lex_best}
        relation = 'identical' if nash_best == lex_best_set else ('disjoint' if not (nash_best & lex_best_set) else 'partial_overlap')
        rank_maximality[relation] += 1
        if n == 3 and q == Fraction(16, 3) and first_worst is None:
            first_worst = (profile, options)
    return counts, stable_sizes, rank_maximality, first_worst


def main():
    c2, _, r2, _ = complete_census(2)
    c3, sizes3, relations3, witness = complete_census(3)
    assert c2 == {Fraction(1): 16}, c2
    assert r2 == {'identical': 16}, r2
    assert c3 == EXPECTED, c3
    assert sizes3 == {1: 34080, 2: 11484, 3: 1092}, sizes3
    assert relations3 == {'identical': 42756, 'disjoint': 3900}, relations3
    print('VERIFIED n2:', sorted(c2.items()))
    print('VERIFIED n3 ratios:', [(str(r), c) for r, c in sorted(c3.items())])
    print('VERIFIED n3 optimal-set relations:', dict(relations3))
    print('VERIFIED n3 stable matching counts:', dict(sizes3))
    print('VERIFIED first maximum-ratio witness:', witness)

if __name__ == '__main__':
    main()
