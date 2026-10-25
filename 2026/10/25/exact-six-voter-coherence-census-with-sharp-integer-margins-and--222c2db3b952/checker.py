"""Exact six-point majority-frame enumeration; Python 3, standard library only.

The computation is finite, uses integer arithmetic throughout, and checks
both obstruction enumeration and explicit weight representations.
"""
from itertools import combinations, product, permutations

U = tuple(range(6))
FULL = (1 << 6) - 1
TRIPLES = tuple(sum(1 << i for i in c) for c in combinations(U, 3))
PAIRS = tuple(sorted((s, FULL ^ s) for s in TRIPLES if s < (FULL ^ s)))
assert len(TRIPLES) == 20 and len(PAIRS) == 10
pair_index = {a: j for j, pair in enumerate(PAIRS) for a in pair}


def chosen(mask):
    return {pair[(mask >> j) & 1] for j, pair in enumerate(PAIRS)}


def balance(family):
    n = len(family)
    return n % 2 == 0 and all(
        sum(bool(s & (1 << i)) for s in family) * 2 == n
        for i in U
    )


def demands(family):
    take, omit = 0, 0
    for s in family:
        j = pair_index[s]
        if s == PAIRS[j][1]:
            take |= 1 << j
        else:
            omit |= 1 << j
    return take, omit


# Any four-balanced family containing complementary triples is inadmissible.
BLOCKERS = set()
for four in combinations(TRIPLES, 4):
    if not balance(four):
        continue
    take, omit = demands(four)
    if not (take & omit):
        assert (take | omit).bit_count() == 4
        BLOCKERS.add((take, omit))
assert len(BLOCKERS) == 30, len(BLOCKERS)


def has_four_obstruction(mask):
    return any((mask & take) == take and (((1 << 10) - 1) ^ mask) & omit == omit
               for take, omit in BLOCKERS)


GOOD = {a for a in range(1024) if not has_four_obstruction(a)}
BAD = set(range(1024)) - GOOD
assert (len(GOOD), len(BAD)) == (332, 692)


def weight_masks(bound):
    result = {}
    for first_five in product(range(-bound, bound + 1), repeat=5):
        last = -sum(first_five)
        if abs(last) > bound:
            continue
        w = first_five + (last,)
        orientation = 0
        for j, (a, b) in enumerate(PAIRS):
            score = sum(w[i] for i in U if a & (1 << i))
            if score == 0:
                break
            if score < 0:
                orientation |= 1 << j
        else:
            result.setdefault(orientation, w)
    return result


weights1, weights2, weights3 = (weight_masks(k) for k in (1, 2, 3))
assert len(weights1) == 20 and len(weights2) == 20
assert len(weights3) == 332
assert set(weights3) == GOOD

# Check the prescribed full majority rule at quota 21, not just triples.
for mask, perturbation in weights3.items():
    integer_weights = [7 + v for v in perturbation]
    assert min(integer_weights) >= 4 and sum(integer_weights) == 42
    positives = chosen(mask)
    for set_mask in range(1 << 6):
        actual = sum(integer_weights[i] for i in U if set_mask & (1 << i)) > 21
        expected = (set_mask.bit_count() > 3 or
                    (set_mask.bit_count() == 3 and set_mask in positives))
        assert actual == expected, (mask, perturbation, set_mask)

PERMS = tuple(permutations(U))


def transported_orientation(mask, permutation):
    value = 0
    for subset in chosen(mask):
        new_subset = sum(1 << permutation[i] for i in U if subset & (1 << i))
        j = pair_index[new_subset]
        if new_subset == PAIRS[j][1]:
            value |= 1 << j
    return value


def orbits(family):
    pending = set(family)
    result = []
    while pending:
        seed = min(pending)
        orb = {transported_orientation(seed, permutation) for permutation in PERMS}
        assert orb <= family
        result.append((seed, len(orb)))
        pending -= orb
    return result


coherent_orbits = orbits(GOOD)
incoherent_orbits = orbits(BAD)
assert sorted(size for _, size in coherent_orbits) == [6, 6, 20, 60, 60, 180]
assert sorted(size for _, size in incoherent_orbits) == [12, 20, 90, 90, 120, 180, 180]

# Check a published six-point construction directly; do not rely on citations.
example = ({1, 2, 3}, {1, 2, 4}, {1, 2, 6}, {1, 3, 5}, {1, 4, 5},
           {1, 4, 6}, {1, 5, 6}, {2, 4, 5}, {2, 5, 6}, {3, 4, 6})
example_masks = {sum(1 << (i - 1) for i in group) for group in example}
assert len(example_masks) == 10 and all(len(set(pair) & example_masks) == 1 for pair in PAIRS)
witness = ({1, 2, 3}, {1, 4, 5}, {2, 5, 6}, {3, 4, 6})
witness_masks = [sum(1 << (i - 1) for i in group) for group in witness]
assert set(witness_masks) <= example_masks and balance(witness_masks)

print('ALL_CHECKS_OK')
print('admissible_four_block_patterns:', len(BLOCKERS))
print('coherent_and_incoherent:', len(GOOD), len(BAD))
print('integer_weight_radius_1_2_3:',len(weights1),len(weights2),len(weights3))
print('coherent_orbits:', sorted(coherent_orbits))
print('incoherent_orbits:', sorted(incoherent_orbits))
print('explicit_four_block_witness:', [sorted(s) for s in witness])
