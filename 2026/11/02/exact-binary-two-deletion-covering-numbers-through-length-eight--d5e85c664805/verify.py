"""Independent, exact checks for short binary two-deletion covering numbers.

Run with Python 3 standard library: python verify.py
"""
from itertools import combinations, product

WITNESSES = {
    2: ['00'],
    3: ['110'],
    4: ['1010'],
    5: ['01010', '10101'],
    6: ['001001', '011011', '101010'],
    7: ['0001010', '0111010', '1010010', '1010111'],
    8: ['00010101', '01010000', '01011010', '01101111',
        '10011001', '10100101', '11101010'],
}

# Each entry assigns the stated *integer* weight to the entire orbit
# under reversal and binary complementation of an (n-2)-symbol word.
WEIGHT_ORBITS = {
    6: {'0000': 1, '0001': 1, '0011': 1},
    7: {'00000': 1, '00001': 1, '00011': 1},
    8: {
        '000000': 5, '000001': 2, '000011': 3, '000100': 2,
        '000111': 4, '001100': 1, '001101': 1, '001110': 2,
        '010001': 1, '010110': 1, '011001': 2, '011110': 1,
    },
}

def words(n):
    return [''.join(bits) for bits in product('01', repeat=n)]


def comp(word):
    return ''.join('1' if a == '0' else '0' for a in word)


def orbit(word):
    return {word, word[::-1], comp(word), comp(word)[::-1]}


def descendants(word):
    """All *distinct* words retained after deleting exactly two positions."""
    n = len(word)
    return {''.join(word[i] for i in kept)
            for kept in combinations(range(n), n-2)}


def subseq(target, source):
    """Independently test subsequence inclusion by greedy scanning."""
    i = 0
    for char in source:
        if i < len(target) and char == target[i]:
            i += 1
    return i == len(target)


def weight_vector(n):
    m = n-2
    weight = {w: 0 for w in words(m)}
    seen = set()
    for rep, val in WEIGHT_ORBITS[n].items():
        orb = orbit(rep)
        assert len(rep) == m and val > 0
        assert not (orb & seen), ('repeated orbit', n, rep)
        seen.update(orb)
        for w in orb:
            weight[w] = val
    return weight


def main():
    test_pairs = 0
    for n in range(2, 9):
        targets = set(words(n-2))
        src = words(n)
        all_desc = {w: descendants(w) for w in src}
        assert len(WITNESSES[n]) == len(set(WITNESSES[n]))
        assert all(c in all_desc for c in WITNESSES[n])
        covered = set().union(*(all_desc[c] for c in WITNESSES[n]))
        assert covered == targets, ('uncovered', n, sorted(targets-covered))
        for w in src:
            assert all_desc[w] == {t for t in targets if subseq(t, w)}
            test_pairs += len(targets)
        if n == 5:
            max_ball = max(map(len, all_desc.values()))
            assert max_ball == 7 < len(targets)
            print('n=5: max deletion-ball size 7 < 8 targets')
        if n in WEIGHT_ORBITS:
            weight = weight_vector(n)
            total = sum(weight.values())
            cap = max(sum(weight[d] for d in all_desc[w]) for w in src)
            assert all(sum(weight[d] for d in ds) <= cap
                       for ds in all_desc.values())
            expected = {6: (8, 3), 7: (10, 3), 8: (74, 12)}[n]
            assert (total, cap) == expected, (n, total, cap)
            assert (len(WITNESSES[n])-1) * cap < total
            print('n=%d: %d source words; %d target words; '
                  'dual total=%d, per-source cap=%d; optimum=%d' %
                  (n, len(src), len(targets), total, cap,
                   len(WITNESSES[n])))
        else:
            print('n=%d: %d source words; %d targets; witness size %d' %
                  (n, len(src), len(targets), len(WITNESSES[n])))
    print('independent source/target subsequence decisions:', test_pairs)
    print('ALL_EXACT_CHECKS_PASSED')

if __name__ == '__main__':
    main()
