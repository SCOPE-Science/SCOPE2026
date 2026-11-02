"""Reproduce the finite certificates for circular palindromes of Rudin-Shapiro prefixes.

The infinite claims also use the substitution and two-block arguments in RESULT.md.
No third-party libraries or external input are needed.
"""

from collections import Counter

RHO = {'0': '01', '1': '02', '2': '31', '3': '32'}
B = {'01', '02', '10', '13', '20', '23', '31', '32'}
BLOCKS = {
    '0': '0001001000011101',
    '1': '0001001011100010',
    '2': '1110110100011101',
    '3': '1110110111100010',
}
COUNTS_BY_LENGTH = {1: 2, 2: 2, 3: 4, 4: 4, 5: 4, 6: 4,
                    7: 4, 8: 4, 10: 4, 12: 2, 14: 2}
COUNTS_BY_RANK = [1, 2, 5, 12, 18, 23, 31, 34, 36]


def morph(word, repetitions=1):
    for _ in range(repetitions):
        word = ''.join(RHO[c] for c in word)
    return word


def code(word):
    return ''.join('0' if c in '01' else '1' for c in word)


def pal(w):
    return w == w[::-1]


def circular_palindromes(w):
    n = len(w)
    w2 = w + w
    return {w2[i:i+ell] for i in range(n)
            for ell in range(1, n + 1) if pal(w2[i:i+ell])}


def finite_certificate():
    q4 = morph('0', 4)
    assert {q4[i:i+2] for i in range(len(q4)-1)} == B
    in_images = {RHO[a] for a in RHO}
    crossing_images = {RHO[a][-1] + RHO[b][0] for a,b in B}
    assert in_images | crossing_images == B
    assert {'01', '10'} <= B
    trigrams = {q4[i:i+3] for i in range(len(q4)-2)}
    assert {'010', '101'} <= trigrams

    blocks = {a: code(morph(a, 4)) for a in RHO}
    assert blocks == BLOCKS
    pals = {w for a,b in B for i in range(16)
            for ell in range(1, 17)
            if len(w := (blocks[a] + blocks[b])[i:i+ell]) == ell and pal(w)}
    assert len(pals) == 36
    assert dict(Counter(map(len, pals))) == COUNTS_BY_LENGTH
    assert not any(len(w) in (15, 16) for w in pals)

    for k, count in enumerate(COUNTS_BY_RANK):
        coded = code(morph('0', k))
        n = len(coded)
        assert n == 2**k
        by_bits = ''.join(str(sum(((j >> t) & 3) == 3
                                  for t in range(k)) % 2) for j in range(n))
        assert coded == by_bits
        circ = circular_palindromes(coded)
        assert len(circ) == count, (k, len(circ), count)
        assert circ <= pals
        if k == 8:
            assert circ == pals
            linear = {coded[j:j+ell] for j in range(n)
                      for ell in range(1, 15)
                      if len(w := coded[j:j+ell]) == ell and pal(w)}
            assert linear == pals
        if 1 <= k <= 8:
            grown = (code(morph('010', k-1)), code(morph('101', k-1)))
            for ell in range(1, n + 1):
                admissible = {g[i:i+ell] for g in grown
                              for i in range(len(g)-ell+1)}
                assert {(coded+coded)[i:i+ell] for i in range(n)} <= admissible

    for k in range(9, 12):
        coded = code(morph('0', k)); n = len(coded)
        w2 = coded + coded
        short_pals = {w2[i:i+ell] for i in range(n)
                      for ell in range(1, 17)
                      if pal(w2[i:i+ell])}
        assert short_pals == pals

    print('CHECK_OK: exact digram closure, 4 supertiles, 36-word language,')
    print('no 15/16 palindromes, complete ranks 0..8,')
    print('full-cycle containment ranks 1..8, stabilization samples 9..11.')


if __name__ == '__main__':
    finite_certificate()
