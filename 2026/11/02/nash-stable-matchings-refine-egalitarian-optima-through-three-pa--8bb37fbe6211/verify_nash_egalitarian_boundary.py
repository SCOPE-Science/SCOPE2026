#!/usr/bin/env python3
"""Exact census of Nash-product and egalitarian stable-marriage choices.

The finite theorem is exhaustively certified over all strict complete profiles
of market size at most three. The four-pair counterexample is independently
checked against every perfect matching. Requires only Python 3 standard library.
"""
from collections import Counter
from itertools import permutations, product, combinations


PREFS4_M = (
    (1, 3, 2, 0),
    (2, 0, 1, 3),
    (1, 0, 3, 2),
    (0, 3, 2, 1),
)
PREFS4_W = (
    (3, 1, 0, 2),
    (3, 1, 0, 2),
    (3, 0, 2, 1),
    (2, 3, 1, 0),
)


def rank_table(orders):
    n = len(orders)
    table = []
    for order in orders:
        row = [0] * n
        for rank, option in enumerate(order):
            row[option] = rank
        table.append(tuple(row))
    return tuple(table)


def all_stable(men, women):
    n = len(men)
    rm = rank_table(men)
    rw = rank_table(women)
    stable = []
    for matching in permutations(range(n)):
        inverse = [0] * n
        for man, woman in enumerate(matching):
            inverse[woman] = man
        # Criterion A: all possible unmatched blocking pairs by rank.
        blocks_by_rank = False
        for man in range(n):
            for woman in range(n):
                if (rm[man][woman] < rm[man][matching[man]]
                        and rw[woman][man] < rw[woman][inverse[woman]]):
                    blocks_by_rank = True
                    break
            if blocks_by_rank:
                break
        # Criterion B: separately use direct preference-order positions.
        blocks_by_orders = any(
            woman in men[man][:men[man].index(matching[man])]
            and man in women[woman][:women[woman].index(inverse[woman])]
            for man in range(n) for woman in range(n)
        )
        assert blocks_by_rank == blocks_by_orders
        if blocks_by_rank:
            continue
        ranks = tuple(rm[m][matching[m]] for m in range(n)) + tuple(
            rw[w][inverse[w]] for w in range(n)
        )
        cost = sum(ranks)
        nash = 1
        for rank in ranks:
            nash *= n - rank
        stable.append((matching, cost, nash, ranks))
    assert stable, 'Gale-Shapley existence should ensure nonempty stable set'
    return stable


def main():
    profile_counts = {}
    for n in (1, 2, 3):
        permutations_n = tuple(permutations(range(n)))
        hist = Counter()
        stable_marginal = Counter()
        pair_types = Counter()
        sum_pairs = Counter()
        gap_min = {}
        n_profiles = 0
        for prefs_index in product(range(len(permutations_n)), repeat=2*n):
            men = tuple(permutations_n[i] for i in prefs_index[:n])
            women = tuple(permutations_n[i] for i in prefs_index[n:])
            solutions = all_stable(men, women)
            stable_marginal[len(solutions)] += 1
            n_profiles += 1
            best_cost = min(x[1] for x in solutions)
            best_nash = max(x[2] for x in solutions)
            egal = {x[0] for x in solutions if x[1] == best_cost}
            nash = {x[0] for x in solutions if x[2] == best_nash}
            if egal == nash:
                hist['equal'] += 1
            elif nash < egal:
                hist['nash_strict_subset'] += 1
            else:
                raise AssertionError(('noncontained-optimal', n, prefs_index,
                                      sorted(nash), sorted(egal)))
            for x, y in combinations(solutions, 2):
                smaller, larger = sorted((x, y), key=lambda a: a[1])
                if smaller[1] < larger[1]:
                    pair_types['strict_cost'] += 1
                    assert smaller[2] > larger[2], (
                        'pairwise-order-failure', prefs_index, smaller, larger)
                    key = (smaller[1], larger[1])
                    sum_pairs[key] += 1
                    gap = smaller[2] - larger[2]
                    gap_min[key] = min(gap_min.get(key, gap), gap)
                elif smaller[2] == larger[2]:
                    pair_types['same_cost_same_product'] += 1
                else:
                    pair_types['same_cost_different_product'] += 1
        assert n_profiles == (len(permutations_n)**(2*n))
        assert sum(hist.values()) == n_profiles
        profile_counts[n] = hist
        print('SIZE', n, 'PROFILES', n_profiles, 'OPTIMUM_RELATIONS', dict(hist),
              'STABLE_COUNTS', dict(sorted(stable_marginal.items())),
              'PAIR_TYPES', dict(pair_types))
        if n == 3:
            assert hist == {'equal': 43728, 'nash_strict_subset': 2928}, hist
            assert stable_marginal == {1: 34080, 2: 11484, 3: 1092}, stable_marginal
            assert pair_types == {
                'strict_cost': 8304,
                'same_cost_same_product': 2760,
                'same_cost_different_product': 3696,
            }, pair_types
            print('DIFFERENT_EGALITARIAN_COST_PAIRS: (cost_low, cost_high, number, min_nash_gap)')
            for key in sorted(sum_pairs):
                print(key[0], key[1], sum_pairs[key], gap_min[key])
    assert profile_counts[1] == {'equal': 1}
    assert profile_counts[2] == {'equal': 16}
    found = all_stable(PREFS4_M, PREFS4_W)
    assert len(found) == 2, found
    witness = {x[0]:x for x in found}
    egal_choice = (1, 2, 3, 0)
    nash_choice = (2, 1, 3, 0)
    assert set(witness) == {egal_choice, nash_choice}
    assert witness[egal_choice][1:3] == (7, 4096)
    assert witness[nash_choice][1:3] == (8, 4608)
    assert witness[egal_choice][3] == (0, 0, 2, 0, 0, 2, 3, 0)
    assert witness[nash_choice][3] == (2, 2, 2, 0, 0, 1, 1, 0)
    print('FOUR_PAIR_WITNESS', witness)
    print('VERIFY_OK exact_profiles_3=46656 pairwise_stable_comparisons_3=14760')


if __name__ == '__main__':
    main()
