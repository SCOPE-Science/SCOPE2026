"""Exact finite certificate for GC-balanced, strand-closed tetranucleotide comma-free codes.

Python 3.9+; standard library only.  Run `python verify.py` in this directory.
The search uses exact integer bitsets and a proved weighted-coloring bound.
"""
import itertools
import json
from pathlib import Path

ALPHABET = 'ACGT'
COMPLEMENT = dict(zip('ACGT', 'TGCA'))
TARGETS = {1: (21, 136, 3, 17), 2: (17, 16, 1, 2), 3: (7, 72, 1, 9)}


def revcomp(word):
    return ''.join(COMPLEMENT[x] for x in reversed(word))


def gc_count(word):
    return sum(x in 'CG' for x in word)


def direct_check(code, minimum_distance):
    words = set(code)
    if len(words) != len(code):
        return False
    if any(len(x) != 4 or gc_count(x) != 2 for x in words):
        return False
    if {revcomp(x) for x in words} != words:
        return False
    if any(sum(x != y for x, y in zip(a, b)) < minimum_distance
           for a, b in itertools.combinations(sorted(words), 2)):
        return False
    return not any(a[k:] + b[:k] in words
                   for a in words for b in words for k in (1, 2, 3))


WORDS = sorted(''.join(letters) for letters in itertools.product(ALPHABET, repeat=4)
               if gc_count(letters) == 2)
ORBITS = sorted({tuple(sorted((word, revcomp(word))))
                 if word != revcomp(word) else (word,) for word in WORDS})
INDEX = {w: i for i, orbit in enumerate(ORBITS) for w in orbit}
WEIGHTS = tuple(map(len, ORBITS))
V = len(ORBITS)
assert len(WORDS) == 96 and V == 52
assert sum(len(o) == 1 for o in ORBITS) == 8


def make_constraints(distance):
    """All forbidden supports of size one, two or three (possibly redundant)."""
    forbidden = set()
    # Every possible middle 4-mer of every concatenation of two selected words.
    for i, first in enumerate(ORBITS):
        for j, second in enumerate(ORBITS):
            for x in first:
                for y in second:
                    for offset in (1, 2, 3):
                        middle = x[offset:] + y[:offset]
                        if middle in INDEX:
                            forbidden.add(tuple(sorted({i, j, INDEX[middle]})))
    # Every forbidden distinct-word pair under the chosen Hamming requirement.
    for i, first in enumerate(ORBITS):
        for j in range(i, V):
            second = ORBITS[j]
            if any(sum(a != b for a, b in zip(x, y)) < distance
                   for x in first for y in second if x != y):
                forbidden.add(tuple(sorted({i, j})))
    return forbidden


class ExactSearch:
    def __init__(self, minimum_distance):
        constraints = make_constraints(minimum_distance)
        self.constraint_count = len(constraints)
        self.singleton_count = sum(len(t) == 1 for t in constraints)
        self.pair_count = sum(len(t) == 2 for t in constraints)
        self.triple_count = sum(len(t) == 3 for t in constraints)
        banned = {t[0] for t in constraints if len(t) == 1}
        self.full = sum(1 << i for i in range(V) if i not in banned)
        self.compatible = [self.full & ~(1 << i) for i in range(V)]
        self.third_forbidden = [[0] * V for _ in range(V)]
        for support in constraints:
            if len(support) == 2:
                a, b = support
                self.compatible[a] &= ~(1 << b)
                self.compatible[b] &= ~(1 << a)
            elif len(support) == 3:
                a, b, c = support
                for i, j, k in ((a, b, c), (b, a, c),
                                (a, c, b), (c, a, b),
                                (b, c, a), (c, b, a)):
                    self.third_forbidden[i][j] |= 1 << k
        self.nodes_bound = 0
        self.nodes_census = 0

    def color_bound(self, remaining):
        """Create conflict classes: chosen codes take at most one member per class.

        A class is constructed greedily from vertices pairwise incompatible
        in the *pairwise* compatibility graph.  Consequently its maximum
        selectable weight is the maximum weight of any class member.
        The sum of these maxima bounds each consecutive prefix of `order`.
        """
        order, bounds = [], []
        total = 0
        while remaining:
            available = remaining
            class_maximum = 0
            group = []
            while available:
                bit = available & -available
                i = bit.bit_length() - 1
                group.append(i)
                remaining ^= bit
                available ^= bit
                available &= ~self.compatible[i]
                class_maximum = max(class_maximum, WEIGHTS[i])
            total += class_maximum
            for i in group:
                order.append(i)
                bounds.append(total)
        return order, bounds

    def descend(self, candidate, choice):
        new_candidate = candidate & self.compatible[choice]
        for earlier in self.chosen:
            new_candidate &= ~self.third_forbidden[choice][earlier]
        return new_candidate

    def prove_no_larger(self, target):
        def rec(candidates, score):
            self.nodes_bound += 1
            if score > target:
                return False
            if not candidates:
                return True
            order, bounds = self.color_bound(candidates)
            for p in range(len(order) - 1, -1, -1):
                if score + bounds[p] <= target:
                    return True
                choice = order[p]
                bit = 1 << choice
                if candidates & bit:
                    new_candidate = self.descend(candidates, choice)
                    self.chosen.append(choice)
                    successful = rec(new_candidate, score + WEIGHTS[choice])
                    self.chosen.pop()
                    if not successful:
                        return False
                    candidates &= ~bit
            return True
        self.chosen = []
        return rec(self.full, 0)

    def enumerate_exact(self, target):
        found = set()
        def rec(candidates, score):
            self.nodes_census += 1
            if score == target:
                found.add(tuple(sorted(self.chosen)))
                return
            if not candidates:
                return
            order, bounds = self.color_bound(candidates)
            for p in range(len(order) - 1, -1, -1):
                if score + bounds[p] < target:
                    return
                choice = order[p]
                bit = 1 << choice
                if candidates & bit:
                    if score + WEIGHTS[choice] <= target:
                        new_candidate = self.descend(candidates, choice)
                        self.chosen.append(choice)
                        rec(new_candidate, score + WEIGHTS[choice])
                        self.chosen.pop()
                    candidates &= ~bit
        self.chosen = []
        rec(self.full, 0)
        return found


def to_code(indices):
    return tuple(sorted(w for i in indices for w in ORBITS[i]))


def nucleotide_symmetries():
    """Eight nucleotide permutations commuting with Watson--Crick complementation."""
    pairs = (('A', 'T'), ('C', 'G'))
    for pairing in itertools.permutations(range(2)):
        for flips in itertools.product((0, 1), repeat=2):
            mapping = {}
            for i, (a, b) in enumerate(pairs):
                to = pairs[pairing[i]]
                mapping[a], mapping[b] = to[flips[i]], to[1 - flips[i]]
            yield mapping


def symmetry_orbits(all_codes):
    unused = set(all_codes)
    sizes = []
    for code in all_codes:
        if code not in unused:
            continue
        orbit = {
            tuple(sorted(''.join(mapping[letter] for letter in word) for word in code))
            for mapping in nucleotide_symmetries()
        }
        assert orbit <= unused
        unused -= orbit
        sizes.append(len(orbit))
    assert not unused
    return sorted(sizes)


def calculate_all():
    output = {}
    for d, (maximum, expected_count, fixed_count, classes) in TARGETS.items():
        search = ExactSearch(d)
        assert search.prove_no_larger(maximum), f'Upper bound failed at d={d}'
        indexed = search.enumerate_exact(maximum)
        all_codes = sorted(to_code(c) for c in indexed)
        assert len(all_codes) == expected_count, (d, len(all_codes))
        class_sizes = symmetry_orbits(all_codes)
        assert len(class_sizes) == classes and all(x == 8 for x in class_sizes)
        for code in all_codes:
            assert len(code) == maximum
            assert sum(word == revcomp(word) for word in code) == fixed_count
            assert direct_check(code, d)
        output[str(d)] = {
            'minimum_distance': d,
            'maximum_size': maximum,
            'number_of_maximizers': len(all_codes),
            'number_of_nucleotide_symmetry_classes': len(class_sizes),
            'symmetry_class_sizes': class_sizes,
            'self_reverse_complementary_words_in_each_maximizer': fixed_count,
            'number_of_candidate_words': len(WORDS),
            'number_of_reverse_complement_orbits': V,
            'forbidden_supports_total': search.constraint_count,
            'forbidden_supports_by_size': {
                str(k): getattr(search, {1:'singleton_count',2:'pair_count',3:'triple_count'}[k])
                for k in (1, 2, 3)
            },
            'upper_search_nodes': search.nodes_bound,
            'census_search_nodes': search.nodes_census,
            'maximizers': [list(code) for code in all_codes]
        }
    return output


if __name__ == '__main__':
    obtained = calculate_all()
    stored = json.loads(Path(__file__).with_name('optimal_codebooks.json').read_text(encoding='utf-8'))
    assert obtained == stored, 'Computed optimum inventory differs from included certificate'
    for d, row in obtained.items():
        print(f"distance={d}: max={row['maximum_size']}, count={row['number_of_maximizers']}, "
              f"fixed={row['self_reverse_complementary_words_in_each_maximizer']}, "
              f"upper_nodes={row['upper_search_nodes']}, census_nodes={row['census_search_nodes']}")
    print('VERIFY_OK')
