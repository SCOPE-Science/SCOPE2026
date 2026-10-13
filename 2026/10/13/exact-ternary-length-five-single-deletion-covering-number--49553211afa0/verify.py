#!/usr/bin/env python3
"""Exact verification of a ternary single-deletion covering certificate."""
from collections import Counter
from itertools import permutations, product

ALPHABET = "012"
WEIGHT_NUMERATORS = {
    "0000": 10, "0001": 8, "0010": 5, "0011": 7, "0012": 6,
    "0101": 3, "0102": 4, "0110": 7, "0112": 6, "0120": 4,
}
EXPECTED_ORBITS = {
    "0000": 3, "0001": 12, "0010": 12, "0011": 6, "0012": 12,
    "0101": 6, "0102": 12, "0110": 6, "0112": 6, "0120": 6,
}
# Each three-word block is obtained by adding 0, 1, 2 modulo three.
PROTOTYPES = (
    "00121", "00200", "01010", "01022", "01112", "02120", "02221"
)
EXPECTED_CENTER_SCORES = {
    10: 3, 15: 12, 18: 12, 19: 36, 20: 18, 21: 12, 22: 24, 23: 126
}


def words(length):
    return ("".join(t) for t in product(ALPHABET, repeat=length))


def deletions(word):
    # A set is essential: deleting different positions may give the same word.
    return {word[:i] + word[i+1:] for i in range(len(word))}


def orbit(word):
    variants = set()
    for p in permutations(ALPHABET):
        translate = str.maketrans(ALPHABET, "".join(p))
        transformed = word.translate(translate)
        variants.add(transformed)
        variants.add(transformed[::-1])
    return variants


def verify():
    universe4 = set(words(4))
    # Build the dual weights directly from orbit generation, without assuming
    # the canonicalization shortcut used to discover the rational certificate.
    weights = {}
    orbit_count = 0
    for representative, numerator in WEIGHT_NUMERATORS.items():
        assert representative == min(orbit(representative))
        block = orbit(representative)
        assert len(block) == EXPECTED_ORBITS[representative]
        assert not block.intersection(weights), representative
        weights.update({w: numerator for w in block})
        orbit_count += 1
    assert orbit_count == 10
    assert set(weights) == universe4
    assert sum(weights.values()) == 468

    # All 243 possible five-symbol centers have rational shadow weight <= 1.
    center_score_histogram = Counter()
    centers_by_orbit = {}
    for center in words(5):
        score = sum(weights[y] for y in deletions(center))
        assert score <= 23, (center, score)
        center_score_histogram[score] += 1
        canonical = min(orbit(center))
        if canonical in centers_by_orbit:
            assert centers_by_orbit[canonical] == score
        else:
            centers_by_orbit[canonical] = score
    assert dict(center_score_histogram) == EXPECTED_CENTER_SCORES
    assert len(centers_by_orbit) == 25

    # Expand seven blocks of cyclic alphabet translations, checking distinctness
    # and full coverage of every possible four-symbol target.
    selected = set()
    for prototype in PROTOTYPES:
        assert len(prototype) == 5
        for increment in range(3):
            center = "".join(str((int(d) + increment) % 3) for d in prototype)
            assert center not in selected
            selected.add(center)
    assert len(selected) == 21
    target_multiplicity = Counter(y for center in selected for y in deletions(center))
    assert set(target_multiplicity) == universe4
    assert set(target_multiplicity.values()) == {1}

    # Weak unweighted sphere bound 81/5 < 21; the sharper fractional dual gives
    # the exact integer lower bound ceil(468/23) = 21.
    assert (468 + 23 - 1) // 23 == 21
    print("VERIFY_OK")
    print("targets=81 centers=243 four_word_orbits=10 five_word_orbits=25")
    print("dual_numerator_sum=468 denominator=23 maximum_shadow_numerator=23")
    print("code_size=21 coverage_size=81 target_multiplicity=1")


if __name__ == "__main__":
    verify()
