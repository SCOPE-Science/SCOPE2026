#!/usr/bin/env python3
"""Exact combinatorial verification of strand-symmetric four-base deletion codes.

Python standard library only. Run from the directory containing the two TSV files.
"""
from collections import Counter
from itertools import permutations, product
from pathlib import Path

ALPHABET = "ACGT"
COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}


def reverse_complement(word):
    return "".join(COMPLEMENT[x] for x in reversed(word))


def descendants(word):
    return frozenset(word[:i] + word[i + 1:] for i in range(len(word)))


def orbit_data():
    words = ("".join(t) for t in product(ALPHABET, repeat=4))
    seen = set()
    orbits = []
    for word in words:
        if word in seen:
            continue
        orbit = tuple(sorted({word, reverse_complement(word)}))
        seen.update(orbit)
        sets = [descendants(x) for x in orbit]
        if len(sets) == 2 and sets[0].intersection(sets[1]):
            continue
        orbits.append((orbit, frozenset().union(*sets)))
    assert len(seen) == 256
    assert len(orbits) == 136
    assert Counter(len(x[0]) for x in orbits) == {1: 16, 2: 120}
    return orbits


ORBITS = orbit_data()
N = len(ORBITS)
OUTPUTS = ["".join(t) for t in product(ALPHABET, repeat=3)]
INDEX = {word: i for i, word in enumerate(OUTPUTS)}
MASKS = [sum(1 << INDEX[y] for y in ds) for _, ds in ORBITS]
WEIGHTS = [len(orbit) for orbit, _ in ORBITS]
COMPAT = [
    sum(1 << j for j in range(N) if j != i and not MASKS[i] & MASKS[j])
    for i in range(N)
]
ALL = (1 << N) - 1
NO_SELF = sum(1 << i for i, w in enumerate(WEIGHTS) if w == 2)


def colored_bound_and_order(candidate):
    """Greedy independent-set partition of the compatibility graph.

    Each graph color class is independent, so a clique uses at most one
    vertex per class. The accumulated maximum vertex weights are valid
    upper bounds for every successive prefix of the returned order.
    """
    remaining = candidate
    order = []
    bounds = []
    cumulative = 0
    while remaining:
        independent = remaining
        vertices = []
        max_weight = 0
        while independent:
            bit = independent & -independent
            vertex = bit.bit_length() - 1
            remaining ^= bit
            independent &= ~(bit | COMPAT[vertex])
            vertices.append(vertex)
            max_weight = max(max_weight, WEIGHTS[vertex])
        cumulative += max_weight
        for vertex in vertices:
            order.append(vertex)
            bounds.append(cumulative)
    return order, bounds


def exact_maximum(allowed):
    best = 0
    node_count = 0

    def recurse(candidate, weight):
        nonlocal best, node_count
        node_count += 1
        if not candidate:
            best = max(best, weight)
            return
        order, bounds = colored_bound_and_order(candidate)
        for k in range(len(order) - 1, -1, -1):
            if weight + bounds[k] <= best:
                return
            vertex = order[k]
            next_candidate = candidate & COMPAT[vertex]
            if next_candidate:
                recurse(next_candidate, weight + WEIGHTS[vertex])
            else:
                best = max(best, weight + WEIGHTS[vertex])
            candidate &= ~(1 << vertex)

    recurse(allowed, 0)
    return best, node_count


def exact_optima(allowed, target):
    solutions = set()
    node_count = 0

    def recurse(candidate, weight, selected):
        nonlocal node_count
        node_count += 1
        if not candidate:
            return
        order, bounds = colored_bound_and_order(candidate)
        for k in range(len(order) - 1, -1, -1):
            if weight + bounds[k] < target:
                return
            vertex = order[k]
            new_weight = weight + WEIGHTS[vertex]
            new_selected = selected + (vertex,)
            if new_weight == target:
                solutions.add(tuple(sorted(new_selected)))
            elif new_weight < target:
                recurse(candidate & COMPAT[vertex], new_weight, new_selected)
            candidate &= ~(1 << vertex)

    recurse(allowed, 0, ())
    return solutions, node_count


def words_of(selected):
    return tuple(sorted(word for i in selected for word in ORBITS[i][0]))


def check_code(words, expect_no_self=False):
    assert len(set(words)) == len(words)
    assert all(len(w) == 4 and set(w) <= set(ALPHABET) for w in words)
    assert {reverse_complement(w) for w in words} == set(words)
    if expect_no_self:
        assert all(w != reverse_complement(w) for w in words)
    used = set()
    for word in words:
        deletions = descendants(word)
        assert used.isdisjoint(deletions)
        used.update(deletions)


def verify_inventory(name, optima, size, no_self=False):
    actual = sorted(words_of(c) for c in optima)
    for words in actual:
        assert len(words) == size
        check_code(words, expect_no_self=no_self)
    expected = sorted(tuple(line.strip().split("\t")) for line in
                      (Path(__file__).parent / name).read_text(encoding="utf-8").splitlines())
    assert actual == expected, f"Complete optimizer inventory mismatch: {name}"
    return actual


def symmetry_orbits(codebooks):
    complement_commuting = [p for p in permutations(ALPHABET) if
        all(p[ALPHABET.index(COMPLEMENT[c])] == COMPLEMENT[p[ALPHABET.index(c)]]
            for c in ALPHABET)]
    assert len(complement_commuting) == 8
    maps = [dict(zip(ALPHABET, p)) for p in complement_commuting]
    universe = set(codebooks)
    classes = []
    while universe:
        representative = min(universe)
        transformed = {
            tuple(sorted("".join(m[c] for c in w) for w in representative))
            for m in maps
        }
        assert transformed <= set(codebooks)
        classes.append((len(transformed), sum(w == reverse_complement(w)
                                             for w in representative)))
        universe.difference_update(transformed)
    return classes


def main():
    assert len(OUTPUTS) == 64
    assert all((mask.bit_count() == len(ORBITS[i][1])) for i, mask in enumerate(MASKS))
    optimum, max_nodes = exact_maximum(ALL)
    assert optimum == 24, (optimum, max_nodes)
    optima, count_nodes = exact_optima(ALL, optimum)
    assert len(optima) == 160
    codebooks = verify_inventory("optimal_rc24.tsv", optima, 24)
    by_fixed = Counter(sum(w == reverse_complement(w) for w in c) for c in codebooks)
    assert by_fixed == {2: 4, 4: 44, 6: 76, 8: 36}
    classes = symmetry_orbits(codebooks)
    assert len(classes) == 28
    assert Counter(classes) == {(4, 2): 1, (4, 4): 5, (4, 6): 7, (4, 8): 3,
                                (8, 4): 3, (8, 6): 6, (8, 8): 3}
    palindrome_free_max, no_self_nodes = exact_maximum(NO_SELF)
    assert palindrome_free_max == 22
    no_self_optima, no_self_count_nodes = exact_optima(NO_SELF, palindrome_free_max)
    assert len(no_self_optima) == 44
    verify_inventory("optimal_rc22_no_self.tsv", no_self_optima, 22, no_self=True)
    print("VERIFY_OK")
    print("eligible_orbits=136; fixed=16; pairs=120; deletion_outputs=64")
    print(f"strand_closed_max=24; max_search_nodes={max_nodes}; optimizer_count=160; count_search_nodes={count_nodes}")
    print("fixed_word_distribution=2:4,4:44,6:76,8:36; symmetry_classes=28")
    print(f"no_self_max=22; max_search_nodes={no_self_nodes}; optimizer_count=44; count_search_nodes={no_self_count_nodes}")


if __name__ == "__main__":
    main()
