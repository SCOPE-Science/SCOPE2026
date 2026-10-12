"""Exact residue-certificate verifier for length-three mixed binary patterns."""
from collections import Counter
from fractions import Fraction

PATTERNS = ('001', '010', '011', '100', '101', '110')
EXPECTED = {
    '001': {1: Fraction(3,32), 3: Fraction(1,32), 5: Fraction(1,32), 6: Fraction(1,64), 7: Fraction(1,16), 8: Fraction(1,64)},
    '010': {1: Fraction(7,32), 2: Fraction(13,64), 4: Fraction(5,128), 5: Fraction(3,128), 6: Fraction(1,128), 7: Fraction(1,128)},
    '011': {1: Fraction(3,32), 2: Fraction(7,64), 3: Fraction(3,32), 4: Fraction(3,128), 5: Fraction(5,128), 7: Fraction(1,128), 8: Fraction(1,128)},
}
EXPECTED['100'] = EXPECTED['011']
EXPECTED['101'] = EXPECTED['010']
EXPECTED['110'] = EXPECTED['001']
EXTRA = {'001': 9, '010': 10, '011': 11}
ODD_RESIDUES = {0: (1, 3, 5, 7), 16: (1, 5), 32: (1, 3, 5, 7), 48: (3, 7)}


def parity_count(digits, word):
    return sum(digits[i:i+3] == word for i in range(len(digits)-2)) & 1


def symbol(n, word):
    return parity_count(bin(n)[2:], word)


def jump(n, word):
    return symbol(n, word) ^ symbol(n + 1, word)


def trailing_zeroes(n):
    return (n & -n).bit_length() - 1


def local_jump(q, t, word):
    assert q >= 5 and q % 2 == 1 and t >= 0
    prefix = bin((q - 1) // 2)[2:]
    return parity_count(prefix + '0' + '1' * t, word) ^ parity_count(prefix + '1' + '0' * t, word)


def exotic_jump(q, t, word):
    assert q in (1, 3)
    return jump((q << t)-1, word)


def certificates(word):
    # Every q>=5 has a prefix of at least two binary digits. Only the
    # last two prefix digits and the first three suffix digits matter.
    for t in range(9):
        for q in range(5, 71, 2):
            representative = 16 + q % 8
            assert local_jump(q, t, word) == local_jump(representative, t, word)
    for q in (17, 19, 21, 23):
        assert all(local_jump(q, t, word) == local_jump(q, 4, word)
                   for t in range(4, 12))
    for q in (1, 3):
        assert all(exotic_jump(q, t, word) == exotic_jump(q, 6, word)
                   for t in range(6, 12))

    # Fixed positions: s=n+1, s mod 64 != 0,16,32,48.
    T = {}
    for r in range(1, 64):
        if r % 16 == 0:
            continue
        t = trailing_zeroes(r)
        residue_q = (r >> t) % 8
        T[r] = local_jump(16 + residue_q, t, word)
    E = {q: local_jump(16 + q, 4, word) for q in (1, 3, 5, 7)}
    unusual = {q: exotic_jump(q, 6, word) for q in (1, 3)}
    candidates = {r: set(E[q] for q in allowed) for r, allowed in ODD_RESIDUES.items()}
    candidates[0].update(unusual.values())

    # Finite consistency of the 2-adic/local rule, not used as proof.
    for n in range(128, 12000):
        r = (n + 1) % 64
        assert jump(n, word) in ({T[r]} if r % 16 else candidates[r]), (word, n)

    # Exact interval certificate. The sole exceptional position in each
    # 14-window is specialized to every allowed q mod 8; all other positions
    # are fixed by the residue table. Also check anomalous q=1,3 choices.
    density = Counter()
    ordinary = set()
    for r in range(64):
        specials = [j for j in range(14) if (r + j) % 16 == 0]
        assert len(specials) <= 1
        if specials:
            j0 = specials[0]
            exceptional_class = (r + j0) % 64
            opts = [(E[q], Fraction(1, len(ODD_RESIDUES[exceptional_class])))
                    for q in ODD_RESIDUES[exceptional_class]]
            possible_values = candidates[exceptional_class]
        else:
            j0 = None
            opts = [(0, Fraction(1, 1))]
            possible_values = {0}

        def next_jump_value(e):
            sequence = [e if j0 == j else T[(r+j)%64] for j in range(14)]
            if sequence[0] == 0:
                return None
            offsets = [j for j in range(1, 14) if sequence[j]]
            assert offsets, (word, r, e, 'no next change within 13')
            return offsets[0]

        for e, weight in opts:
            length = next_jump_value(e)
            if length is not None:
                density[length] += weight / 64
        for e in possible_values:
            length = next_jump_value(e)
            if length is not None:
                ordinary.add(length)

    assert dict(density) == EXPECTED[word], (word, density, EXPECTED[word])
    assert ordinary == set(EXPECTED[word]), (word, ordinary)
    assert sum(length * proportion for length, proportion in density.items()) == 1

    # All starts s<128 are determined by 145 directly calculated symbols.
    values = [symbol(n, word) for n in range(145)]
    first_runs = []
    s = 0
    for n in range(1, len(values)):
        if values[n] != values[n-1]:
            if s < 128:
                first_runs.append((s, n-s))
            s = n
    assert first_runs and s >= 128, (word, s)
    exceptional = [(s, length) for s, length in first_runs
                   if length not in EXPECTED[word]]
    assert exceptional == ([(0, EXTRA[word])] if word in EXTRA else []), (word, exceptional)
    assert max(EXPECTED[word]) <= 8

    # Independent direct prefix cross-check and run frequencies.
    total = 1 << 17
    begins = Counter()
    last = symbol(0, word)
    s = 0
    for n in range(1, total):
        cur = symbol(n, word)
        if cur != last:
            begins[n-s] += 1
            s = n
        last = cur
    possible_lengths = set(EXPECTED[word]) | ({EXTRA[word]} if word in EXTRA else set())
    assert set(begins) == possible_lengths, (word, begins)
    for length, proportion in density.items():
        assert abs(begins[length] - proportion * total) <= 75, (word, length)
    return density, exceptional


def main():
    for word in PATTERNS:
        density, exceptional = certificates(word)
        print(word, 'densities', ','.join(f'{k}:{v}' for k, v in sorted(density.items())),
              'exceptional', exceptional)
    print('VERIFY_OK six_patterns=6 phase_classes=64 odd_residue_cases=all symbolic_window_bound=13'
          ' mixed_pattern_critical_boundary=checked direct_n=131072')

if __name__ == '__main__':
    main()
