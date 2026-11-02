"""Exact self-contained string-attractor certificates for two Rudin-Shapiro prefixes.
Requires only Python 3.9+ standard library; all positions are zero based.
The lower bounds are proved by a complete exhaustive exact hitting-set search.
"""

from collections import defaultdict

WITNESSES = {
    128: (32, 47, 56, 69, 75, 82, 91, 100, 107, 118),
    256: (63, 88, 104, 112, 139, 154, 164, 184, 195, 208, 238),
}
EXPECTED = {
    128: (7008, 48, 243, 172),
    256: (28128, 64, 3703, 2169),
}


def rudin_shapiro_prefix(n):
    """Parity of overlapping 11 blocks in the usual base-2 integer expansion."""
    return bytes(
        sum(((i >> j) & (i >> (j + 1)) & 1)
            for j in range(i.bit_length())) & 1
        for i in range(n)
    )


def complete_factor_masks(word):
    """For each nonempty distinct factor, all positions crossed by any occurrence."""
    n = len(word)
    masks = defaultdict(int)
    for length in range(1, n + 1):
        for start in range(n - length + 1):
            factor = word[start:start + length]
            masks[factor] |= ((1 << length) - 1) << start
    return masks


def minimal_constraints(all_masks):
    """Remove a hitting condition when a strictly stronger condition is kept."""
    unique = sorted(set(all_masks), key=lambda x: (x.bit_count(), x))
    minimal = []
    for mask in unique:
        if not any((earlier & mask) == earlier for earlier in minimal):
            minimal.append(mask)
    # Verify reduction is equivalence-preserving.
    assert all(any((r & mask) == r for r in minimal) for mask in all_masks)
    return minimal


def impossible_with_at_most_k_positions(rows, n, k):
    """Exact DFS; symmetric/dominated choices removed, failed states memoized."""
    m = len(rows)
    covering = [sum((1 << r) for r, row in enumerate(rows) if row >> p & 1)
                for p in range(n)]
    full = (1 << m) - 1
    failures = {}
    counter = [0]

    def search(uncovered, budget):
        counter[0] += 1
        if not uncovered:
            return True
        if budget == 0:
            return False
        if failures.get(uncovered, -1) >= budget:
            return False
        candidate_sets = None
        remaining = uncovered
        while remaining:
            one = remaining & -remaining
            r = one.bit_length() - 1
            remaining -= one
            positions = rows[r]
            choices = set()
            while positions:
                bit = positions & -positions
                positions -= bit
                p = bit.bit_length() - 1
                choices.add(covering[p] & uncovered)
            ranked = sorted(choices, key=lambda a: (-a.bit_count(), -a))
            # A choice whose hit set is contained in another can be discarded.
            ranked = [c for j, c in enumerate(ranked)
                      if not any((c | other) == other for other in ranked[:j])]
            if candidate_sets is None or len(ranked) < len(candidate_sets):
                candidate_sets = ranked
            if len(candidate_sets) == 1:
                break
        for covered in candidate_sets:
            if search(uncovered & ~covered, budget - 1):
                return True
        failures[uncovered] = max(budget, failures.get(uncovered, -1))
        return False

    feasible = search(full, k)
    return not feasible, counter[0], len(failures)


def run():
    for n, witness in WITNESSES.items():
        word = rudin_shapiro_prefix(n)
        factor_masks = complete_factor_masks(word)
        rows = minimal_constraints(factor_masks.values())
        expected_factors, expected_rows, expected_nodes, expected_states = EXPECTED[n]
        assert len(factor_masks) == expected_factors
        assert len(rows) == expected_rows
        assert len(set(witness)) == len(witness)
        assert all(0 <= p < n for p in witness)
        choice_mask = sum(1 << p for p in witness)
        assert all(mask & choice_mask for mask in factor_masks.values())
        impossible, nodes, states = impossible_with_at_most_k_positions(rows, n, len(witness) - 1)
        assert impossible
        assert (nodes, states) == (expected_nodes, expected_states), (n, nodes, states)
        print(f'length={n} factors={len(factor_masks)} constraints={len(rows)} '
              f'optimal={len(witness)} lower_bound_nodes={nodes} failed_states={states}')
    print('RUDIN_SHAPIRO_ATTRACTORS_VERIFY_OK')


if __name__ == '__main__':
    run()
