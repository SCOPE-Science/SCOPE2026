#!/usr/bin/env python3
"""Independent finite literal-factor checks for periodic run-cycle attractors."""
from itertools import product


def factor_occurrence_masks(word):
    """A factor's bit mask is the union of all of its literal occurrence intervals."""
    n = len(word)
    occurrences = {}
    for lo in range(n):
        for hi in range(lo + 1, n + 1):
            factor = word[lo:hi]
            positions = ((1 << hi) - 1) ^ ((1 << lo) - 1)
            occurrences[factor] = occurrences.get(factor, 0) | positions
    return occurrences


def formula(lens, copies):
    q = len(lens)
    edges = range(q)
    total = 0
    for flags in product((0, 1), repeat=q):
        ways = 1
        for j, r in enumerate(lens):
            before, after = (j - 1) % q, j
            incoming = copies - (before == q - 1)
            outgoing = copies - (after == q - 1)
            common = (copies - (j in (0, q - 1))) if r == 1 else 0
            available = (copies * r - flags[before] * incoming
                         - flags[after] * outgoing
                         + flags[before] * flags[after] * common)
            assert available >= 0
            ways *= available
        total += (-1) ** sum(flags) * ways
    return total


def check_family(lens, k):
    q = len(lens)
    word = ''.join(str(j) * r for j, r in enumerate(lens)) * k
    all_occ = factor_occurrence_masks(word)
    small = {f: mask for f, mask in all_occ.items() if len(f) <= 2}
    options = [[p for p, letter in enumerate(word) if letter == str(j)] for j in range(q)]
    literal_total = 0
    transition_total = 0
    total_checked = 0
    for positions in product(*options):
        chosen = sum(1 << p for p in positions)
        literal = all(chosen & mask for mask in all_occ.values())
        local = all(chosen & mask for mask in small.values())
        assert literal == local, ('local equivalence failed', lens, k, positions)
        literal_total += literal
        transition_total += local
        total_checked += 1
    predicted = formula(lens, k)
    assert literal_total == predicted == transition_total, (lens, k, literal_total, predicted)
    if all(r >= 2 for r in lens):
        assert literal_total == 2 * (k ** (q - 1)) * (k - 1), lens
    if all(r == 1 for r in lens):
        assert literal_total == k ** q - k ** (q - 2), lens
    return total_checked, len(all_occ)


def run():
    families = 0
    trials = 0
    literal_factors = 0
    for q in (2, 3, 4, 5):
        side = 3 if q <= 4 else 2
        for lens in product(range(1, side + 1), repeat=q):
            for copies in (2, 3, 4):
                if (copies * sum(lens) > 24 or
                    (q == 5 and copies == 4 and sum(lens) > 6)):
                    continue
                tested, distinct = check_family(lens, copies)
                families += 1
                trials += tested
                literal_factors += distinct
    print('VERIFY_OK', 'families='+str(families),
          'candidate_sets='+str(trials),
          'distinct_factor_profiles='+str(literal_factors),
          'literal_vs_local_and_IE=TRUE',
          'all_long_runs=TRUE', 'all_singletons=TRUE')


if __name__ == '__main__':
    run()
