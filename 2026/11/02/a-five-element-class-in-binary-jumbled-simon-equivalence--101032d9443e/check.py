#!/usr/bin/env python3
"""Check the finite binary 4,1-jumbled scattered-factor class directly."""
from itertools import combinations, product

ALPHABET = '01'
K = 4
ELL = 1


def subsequence(u, w):
    iterator = iter(w)
    return all(any(c == target for c in iterator) for target in u)


def signature_direct(w):
    observed = []
    for bits in product(ALPHABET, repeat=K):
        u = ''.join(bits)
        if any(u.count(bit) > w.count(bit) for bit in ALPHABET):
            continue
        if any(subsequence(''.join(u[i] for i in indices), w)
               for indices in combinations(range(K), K - ELL)):
            observed.append(u)
    return tuple(observed)


def lcs(u, w):
    state = [0] * (len(w) + 1)
    for a in u:
        new = [0]
        for j, b in enumerate(w, 1):
            new.append(state[j - 1] + 1 if a == b else max(new[-1], state[j]))
        state = new
    return state[-1]


def signature_dp(w):
    return tuple(''.join(t) for t in product(ALPHABET, repeat=K)
                 if all(t.count(x) <= w.count(x) for x in ALPHABET)
                 and lcs(''.join(t), w) >= K - ELL)


def main():
    expected = {
        '00011': ('1010', '1100'),
        '00101': ('1100',),
        '00110': (),
        '01001': (),
        '01010': (),
        '01100': (),
        '10001': ('0110',),
        '10010': (),
        '10100': ('0011',),
        '11000': ('0011', '0101'),
    }
    admissible = {'0001','0010','0100','1000','0011','0101','0110','1001','1010','1100'}
    signatures = {}
    for w, missing_expected in expected.items():
        observed = signature_direct(w)
        assert observed == signature_dp(w), ('algorithm disagreement', w)
        missing = tuple(sorted(admissible.difference(observed)))
        assert missing == missing_expected, (w, missing, missing_expected)
        signatures[w] = observed
        print(w, 'missing:', ','.join(missing) if missing else '(none)')
    class_five = tuple(sorted(w for w in expected
                              if signatures[w] == signatures['00110']))
    assert class_five == ('00110','01001','01010','01100','10010')
    # Corroborate the global-class restriction by checking longer strings;
    # the mathematical proof of the restriction is in RESULT.md.
    for n in range(0, 11):
        for bits in product(ALPHABET, repeat=n):
            w = ''.join(bits)
            if signature_direct(w) == signatures['00110']:
                assert w in class_five, ('unexpected equivalent word', w)
    assert len({signatures[w] for w in expected}) == 6
    # Explicitly check every shorter layer; do not assume a layer-reduction lemma.
    for t in range(1, K):
        profiles = []
        for w in class_five:
            profiles.append(tuple(''.join(bits) for bits in product(ALPHABET, repeat=t)
                if all(bits.count(c) <= w.count(c) for c in ALPHABET)
                and any(subsequence(''.join(bits[i] for i in indices), w)
                        for indices in combinations(range(t), t-1))))
        assert len(set(profiles)) == 1, ('shorter layer mismatch', t)
        print('shared layer', t, 'size:', len(profiles[0]))
    print('PASS: direct enumerator, independent LCS dynamic program, and finite-length cross-check.')
    print('Exact class:', ', '.join(class_five))
    print('Six equivalence classes among ten anagrams: one size five, five singleton.')


if __name__ == '__main__':
    main()
