#!/usr/bin/env python3
"""Exact enumeration of alphabet-symmetric ternary one-insertion covers."""
from itertools import product, permutations, combinations

ALPHABET = tuple(range(3))
PERMUTATIONS = tuple(permutations(ALPHABET))
WITNESS_31 = (
    '0000','0011','0012','0021','0022','0100','0111','0122','0210','0220',
    '1000','1011','1022','1100','1102','1111','1120','1122','1201','1220',
    '2001','2002','2110','2112','2120','2121','2200','2211','2212','2221','2222'
)

def words(n):
    return list(product(ALPHABET, repeat=n))

def delete_one(word):
    return {word[:i] + word[i + 1:] for i in range(len(word))}

def orbits(n):
    remaining = set(words(n)); output = []
    while remaining:
        seed = min(remaining)
        block = {tuple(perm[x] for x in seed) for perm in PERMUTATIONS}
        assert block <= remaining
        remaining -= block
        output.append(tuple(sorted(block)))
    return output

def main():
    blocks = orbits(4)
    assert len(blocks) == 14
    assert [len(block) for block in blocks] == [3] + [6] * 13
    word_to_block = {word: i for i, block in enumerate(blocks) for word in block}
    assert len(word_to_block) == 81
    targets = orbits(5)
    assert len(targets) == 41
    masks = []
    for target_block in targets:
        rep = target_block[0]
        mask = sum(1 << i for i in {word_to_block[child] for child in delete_one(rep)})
        for word in target_block:
            assert mask == sum(1 << i for i in {word_to_block[child] for child in delete_one(word)})
        masks.append(mask)
    assert any(m == 1 for m in masks)

    def covers(mask):
        return all(mask & target_mask for target_mask in masks)

    for size in range(6):
        assert sum(covers(1 | sum(1 << j for j in chosen))
                   for chosen in combinations(range(1, 14), size)) == 0
    choices = [1 | sum(1 << j for j in chosen)
               for chosen in combinations(range(1, 14), 6)
               if covers(1 | sum(1 << j for j in chosen))]
    assert len(choices) == 37
    assert all(mask.bit_count() == 7 for mask in choices)
    all_solutions = set(choices)
    reverse_orbit = [word_to_block[block[0][::-1]] for block in blocks]
    def reverse_mask(mask):
        return sum((1 << reverse_orbit[i]) for i in range(14) if mask & (1 << i))
    assert all(reverse_mask(mask) in all_solutions for mask in choices)
    fixed = sum(reverse_mask(mask) == mask for mask in choices)
    assert fixed == 5
    assert (len(choices) - fixed) // 2 == 16
    witness = {tuple(map(int, word)) for word in WITNESS_31}
    assert len(witness) == 31
    assert all(delete_one(target) & witness for target in words(5))
    assert any(tuple(perm[x] for x in word) not in witness
               for word in witness for perm in PERMUTATIONS)

    print('alphabet_size=3 source_length=4 target_length=5')
    print('source_orbits=14 source_orbit_sizes=3+13*6')
    print('target_orbits=41')
    print('covers_with_at_most_5_nonconstant_orbits=0')
    print('covers_with_6_nonconstant_orbits=37')
    print('minimum_symmetric_cover_size=39')
    print('reversal_fixed_optima=5 reversal_pairs=16 reversal_classes=21')
    print('asymmetric_witness_size=31 target_words_verified=243')
    print('verification=PASS')

if __name__ == '__main__':
    main()
