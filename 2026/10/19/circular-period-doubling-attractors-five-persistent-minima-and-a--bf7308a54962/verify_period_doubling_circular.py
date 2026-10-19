"""Exact finite certificates for circular attractors of period-doubling words.

Only Python's standard library is required. Indexing is zero-based.
"""


def word(order):
    s = '0'
    for _ in range(order):
        s = ''.join('01' if a == '0' else '00' for a in s)
    return s


def proposed_pairs(order):
    q = 1 << (order - 3)
    return {(2*q-1, 4*q-1), (2*q-1, 5*q-1),
            (3*q-1, 6*q-1), (4*q-1, 6*q-1),
            (4*q-1, 8*q-1)}


def factor_coverage(word_text, length):
    """Return exact factor-ID masks per selected position; no hashing."""
    size = len(word_text)
    repeated = word_text + word_text
    identifiers = {}
    starting_factors = []
    for beginning in range(size):
        fragment = repeated[beginning:beginning+length]
        if fragment not in identifiers:
            identifiers[fragment] = len(identifiers)
        starting_factors.append(1 << identifiers[fragment])
    covers = []
    for position in range(size):
        cover = 0
        for distance in range(length):
            cover |= starting_factors[(position - distance) % size]
        covers.append(cover)
    return covers, (1 << len(identifiers)) - 1, len(identifiers)


def necessary_candidates(word_text, lengths):
    size = len(word_text)
    candidates = [(a, b) for a in range(size) for b in range(a+1, size)]
    trajectory = []
    for length in lengths:
        masks, complete, variety = factor_coverage(word_text, length)
        candidates = [(a, b) for a, b in candidates
                      if (masks[a] | masks[b]) == complete]
        trajectory.append([length, variety, len(candidates)])
    return set(candidates), trajectory


def cyclic_rotations_lcp(word_text):
    size = len(word_text)
    doubled = word_text + word_text
    rotation_order = sorted(range(size), key=lambda i: doubled[i:i+size])
    adjacent_lcp = [0]
    for j in range(1, size):
        a, b = rotation_order[j-1], rotation_order[j]
        length = 0
        while length < size and doubled[a+length] == doubled[b+length]:
            length += 1
        adjacent_lcp.append(length)
    return rotation_order, adjacent_lcp


def verify_complete_attractors(word_text, pairs):
    """Exact all-length check via equivalence classes of sorted rotations.

    At a fixed length, two cyclic factors coincide iff their rotations have
    common prefix at least that length. This check uses no fingerprints.
    """
    size = len(word_text)
    order, adjacent_lcp = cyclic_rotations_lcp(word_text)
    max_length = max(max(b-a, size-(b-a)) for a,b in pairs)
    for length in range(1, max_length):
        factor_class = [0] * size
        class_id = 0
        for j, start in enumerate(order):
            if j and adjacent_lcp[j] < length:
                class_id += 1
            factor_class[start] = class_id
        all_classes = class_id + 1
        for a, b in pairs:
            observed = set()
            for offset in range(length):
                observed.add(factor_class[(a-offset) % size])
                observed.add(factor_class[(b-offset) % size])
            if len(observed) != all_classes:
                raise AssertionError((size, length, a, b, all_classes, len(observed)))
    # At length >= max(d, size-d), any cyclic interval meets a or b.


def main():
    import time
    started = time.monotonic()
    total_necessary_tests = 0
    for order in range(3, 14):
        size = 1 << order
        necessary_lengths = sorted({1, 2, 3} | {2**j + 1 for j in range(2, order-1)})
        if order <= 11:
            actual, stages = necessary_candidates(word(order), necessary_lengths)
        else:
            # The longest required length alone rejects nearly all pairs.
            # Scan pairs once without materializing the complete pair list.
            wd = word(order)
            cover, complete, variety = factor_coverage(wd, necessary_lengths[-1])
            shortlist = [(a, b) for a in range(size) for b in range(a+1, size)
                         if (cover[a] | cover[b]) == complete]
            stages = [[necessary_lengths[-1], variety, len(shortlist)]]
            for length in necessary_lengths[:-1]:
                cover, complete, variety = factor_coverage(wd, length)
                shortlist = [(a, b) for a, b in shortlist
                             if (cover[a] | cover[b]) == complete]
                stages.append([length, variety, len(shortlist)])
            actual = set(shortlist)
        expected = proposed_pairs(order)
        assert actual == expected, (order, sorted(actual), sorted(expected))
        assert len(actual) == 5
        total_necessary_tests += sum(x[2] for x in stages)
        print(f'order={order} size={size} exact_candidate_pairs=5 stages={stages}')
    # Independent all-length check on largest certified word via suffix rotations.
    verify_complete_attractors(word(11), sorted(proposed_pairs(11)))
    print('Independent cyclic-rotation all-factor-length check: order 11 PASS')
    # Independent brute-force base check: no length is omitted.
    all_base, _ = necessary_candidates(word(3), range(1, 9))
    assert all_base == proposed_pairs(3)
    print('Eight-letter base exhaustive all-length check: PASS')
    # The all-order assertion comes from the mathematical morphism lemma,
    # not from this finite experiment.
    print(f'Finite tests and exact candidate-set comparisons: PASS; elapsed={time.monotonic()-started:.2f}s')


if __name__ == '__main__':
    main()
