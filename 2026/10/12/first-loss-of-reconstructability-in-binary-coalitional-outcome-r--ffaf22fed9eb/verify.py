#!/usr/bin/env python3
"""Exhaustive finite certificate for three-agent binary game-form exact effectivity.

Only the two labelled outcomes and independently relabelled actions are used.
No external packages or files are needed.
"""
from collections import defaultdict, Counter


def signature(table, players):
    """Table is an integer whose bit at profile j is its outcome in {0,1}."""
    records = []
    for coalition in range(1 << players):
        possible_ranges = set()
        for assignment in range(1 << players):
            if assignment & ~coalition:
                continue
            r = 0
            for full in range(1 << players):
                if (full & coalition) == assignment:
                    outcome = (table >> full) & 1
                    r |= 1 << outcome
            possible_ranges.add(r)
        records.append(tuple(sorted(possible_ranges)))
    return tuple(records)


def canonical_table(table, players):
    """Minimum bit table among independent action-0/action-1 swaps."""
    best = None
    for flips in range(1 << players):
        transformed = 0
        for profile in range(1 << players):
            transformed |= ((table >> (profile ^ flips)) & 1) << profile
        if best is None or transformed < best:
            best = transformed
    return best


def evaluate(players):
    signature_to_tables = defaultdict(list)
    for table in range(1 << (1 << players)):
        signature_to_tables[signature(table, players)].append(table)
    classes = {canonical_table(t, players) for tables in signature_to_tables.values()
               for t in tables}
    ambiguous = []
    for s, ts in signature_to_tables.items():
        orbits = {canonical_table(t, players) for t in ts}
        if len(orbits) > 1:
            ambiguous.append((len(orbits), len(ts), s))
    return len(signature_to_tables), len(classes), sorted(ambiguous)


def run():
    expected = {1: (3, 3), 2: (7, 7), 3: (41, 46)}
    for k in (1, 2, 3):
        count_sig, count_orbits, ambiguous = evaluate(k)
        assert (count_sig, count_orbits) == expected[k], (k, count_sig, count_orbits)
        if k < 3:
            assert ambiguous == []
        else:
            assert [(multiplicity, size) for multiplicity, size, _ in ambiguous] == [
                (2, 12), (2, 12), (4, 32)]
        print(f'{k} agents: {1 << (1 << k)} game forms, '
              f'{count_sig} exact-effectivity signatures, '
              f'{count_orbits} action-relabeling classes; '
              f'{len(ambiguous)} ambiguous signatures')
    f = (1 << 3) | (1 << 5) | (1 << 6)
    g = (1 << 3) | (1 << 4)
    shared = ((3,), (3,), (3,), (1, 3), (3,), (1, 3), (1, 3), (1, 2))
    assert signature(f, 3) == shared == signature(g, 3)
    assert f.bit_count() == 3 and g.bit_count() == 2
    assert canonical_table(f, 3) != canonical_table(g, 3)
    # Independent Burnside orbit totals: identity fixes 2^(2^k) colorings;
    # each of 2^k-1 nonidentity translations has 2^(2^(k-1)) fixed colorings.
    for k in (1, 2, 3):
        burnside = ((1 << (1 << k)) + ((1 << k) - 1) * (1 << (1 << (k - 1)))) // (1 << k)
        assert burnside == expected[k][1], (k, burnside)
    # The output cardinality is invariant even if all players and actions
    # are relabelled. Outcome exchange sends it to 8-cardinality.
    assert f.bit_count() not in (g.bit_count(), 8 - g.bit_count())
    print('PASS: first nonfaithfulness at three players; witness and exact census verified')


if __name__ == '__main__':
    run()
