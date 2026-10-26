"""Exhaustive designated-truth entailment certificate for 24 FDE S5 operators.

The input is one arbitrary formula. An atomic valuation realizes every
four-valued pointed support profile, so the finite scan is complete.
"""
from itertools import combinations, product

VALUES = ('t', 'b', 'n', 'f')
# The two last sets test membership of positive and negative evidence.
TESTS = {
    't': frozenset(('t',)),
    'b': frozenset(('b',)),
    'n': frozenset(('n',)),
    'f': frozenset(('f',)),
    'T': frozenset(('t', 'b')),
    'F': frozenset(('b', 'f')),
}
KINDS = ('circ', 'bullet', 'negcirc', 'negbullet')
OPERATORS = tuple((kind, name) for name in TESTS for kind in KINDS)


def actual_truth(kind, name, local, domain):
    """Direct reading of positive-truth clauses in Petrukhin, Definition 6."""
    Q = TESTS[name]
    if kind == 'circ':
        return local not in Q or all(s in Q for s in domain)
    if kind == 'bullet':
        return local in Q and any(s not in Q for s in domain)
    if kind == 'negcirc':
        return local in Q or all(s not in Q for s in domain)
    if kind == 'negbullet':
        return local not in Q and any(s in Q for s in domain)
    raise ValueError(kind)


def closed_truth(kind, name, local, support):
    """Separate support-based Boolean evaluation."""
    Q = TESTS[name]
    u = local in Q
    has_inside = bool(support & Q)
    has_outside = bool(support - Q)
    return {
        'circ': not (u and has_outside),
        'bullet': u and has_outside,
        'negcirc': not ((not u) and has_inside),
        'negbullet': (not u) and has_inside,
    }[kind]


def criterion(left, right):
    """Three possible strict implication families; identity otherwise."""
    k, i = left
    h, j = right
    Q, R = TESTS[i], TESTS[j]
    if left == right:
        return True
    if k == 'bullet' and h == 'circ':
        return not Q.intersection(R)
    if k == 'bullet' and h == 'negcirc':
        return Q.issubset(R)
    if k == 'negbullet' and h == 'circ':
        return R.issubset(Q)
    return False


def main():
    all_profiles = [(x, frozenset(s))
                    for m in range(1, 5)
                    for s in combinations(VALUES, m)
                    for x in s]
    assert len(all_profiles) == 32
    # Each profile appears as a pointed finite S5 model of the atom p.
    # Comparing 1..4 labelled worlds separately guards against a mistake
    # in support compression or in the model-size certificate.
    minimal = {}
    for size in range(1, 5):
        for assignment in product(VALUES, repeat=size):
            local = assignment[0]
            support = frozenset(assignment)
            for op in OPERATORS:
                assert actual_truth(*op, local, assignment) == closed_truth(*op, local, support)
            truths = {op: actual_truth(*op, local, assignment) for op in OPERATORS}
            for left in OPERATORS:
                if not truths[left]:
                    continue
                for right in OPERATORS:
                    if not truths[right]:
                        minimal.setdefault((left, right), size)
    distinct_signatures = {op: tuple(closed_truth(*op, x, s)
                                      for x, s in all_profiles) for op in OPERATORS}
    assert len(set(distinct_signatures.values())) == 24
    implication_count = 0
    strict_implications = 0
    for left in OPERATORS:
        for right in OPERATORS:
            semantically_implies = (left, right) not in minimal
            assert semantically_implies == criterion(left, right), (left, right)
            if semantically_implies:
                implication_count += 1
                if left != right:
                    strict_implications += 1
    assert implication_count == 64
    assert strict_implications == 40
    size_histogram = {size: sum(v == size for v in minimal.values()) for size in (1, 2, 3, 4)}
    assert size_histogram == {1: 144, 2: 340, 3: 28, 4: 0}, size_histogram
    # Optimality: local n needs two distinct witnesses t and b.
    witness = ('n', 't', 'b')
    assert actual_truth('negbullet', 't', witness[0], witness)
    assert not actual_truth('negcirc', 'b', witness[0], witness)
    for size in (1, 2):
        for assignment in product(VALUES, repeat=size):
            assert not (actual_truth('negbullet', 't', assignment[0], assignment)
                        and not actual_truth('negcirc', 'b', assignment[0], assignment))
    print('BELNAP_24_IMPLICATIONS_OK 24 40 512 144 340 28')


if __name__ == '__main__':
    main()
