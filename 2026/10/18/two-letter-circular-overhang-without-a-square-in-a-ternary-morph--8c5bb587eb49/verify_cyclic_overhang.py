"""Finite cross-checks for cyclic two-letter overhang on the ternary fixed point.

The infinite statement is established by the proof in RESULT.md; these checks
only corroborate initial cases and verify the finite base certificates.
"""

H = {'0': '01', '1': '21', '2': '0'}


def morph(word):
    return ''.join(H[c] for c in word)


def iterate(a, k):
    for _ in range(k):
        a = morph(a)
    return a


def cyclic_windows(u, extra=2):
    return [(u * 3)[i:i + len(u) + extra] for i in range(len(u))]


def main():
    p6 = iterate('0', 6)
    assert p6 == '0121021010210121010210121021012101021'
    certificates = {
        '0': (0, 22, 23, 8, 18, 19, 20),
        '1': (7, 3, 4, 5, 6),
    }
    for a, offsets in certificates.items():
        u = iterate(a, 3)
        words = cyclic_windows(u)
        assert len(words) == len(offsets)
        for phase, (w, j) in enumerate(zip(words, offsets)):
            assert p6[j:j+len(w)] == w, (a, phase, j, w)
        assert u + u not in p6
    p_long = iterate('0', 17)
    # Full occurrence checks are feasible for these initial lengths.
    for k in range(3, 9):
        for a in ('0', '1'):
            u = iterate(a, k)
            assert '22' not in u+u
            missing = [i for i, w in enumerate(cyclic_windows(u)) if w not in p_long]
            assert not missing, (a, k, missing)
            assert u+u not in p_long, (a, k)
    # Check the forbidden length-two factors in a long prefix.
    assert all(w not in p_long for w in ('00', '11', '20', '22'))
    print('PASS: 12 base two-letter-overhang certificates and all phases for k=3..8')
    print('PASS: tested candidate-root square absence for k=3..8 in a length-%d prefix' % len(p_long))
    print('Finite checks corroborate, but do not establish, the all-k theorem.')


if __name__ == '__main__':
    main()
