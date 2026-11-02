#!/usr/bin/env python3
"""Finite exhaustive certificate for the order-five binary de Bruijn
periodic-autocorrelation extrema distribution. Uses only Python 3 stdlib.
"""
from collections import Counter
from hashlib import sha256

N = 32
TARGET = {
    -24: (0, 0, 4, 0, 8),
    -20: (0, 0, 44, 36, 8),
    -16: (0, 100, 140, 22, 6),
    -12: (0, 214, 612, 32, 6),
     -8: (4, 356, 404, 24, 8),
     -4: (0, 12, 8, 0, 0),
}
COLS = (0, 4, 8, 12, 16)

def feedback_words():
    """Enumerate all 2^16 nonsingular five-bit shift feedback maps.

    Each map has a freely chosen four-bit Boolean component g, and
    successor s -> 2s mod 32 plus (high_bit(s) xor g(low_four(s))).
    A full orbit of state zero yields one and only one rooted de Bruijn word.
    """
    out = set()
    full = (1 << N) - 1
    for truth_table in range(1 << 16):
        state, seen, letters = 0, 0, []
        for _ in range(N):
            if (seen >> state) & 1:
                break
            seen |= 1 << state
            letters.append(str(state >> 4))
            b = (state >> 4) ^ ((truth_table >> (state & 15)) & 1)
            state = ((state << 1) & 31) | b
        if state == 0 and seen == full and len(letters) == N:
            word = ''.join(letters)
            assert word.startswith('00000')
            out.add(word)
    return out

def euler_words():
    """Independently enumerate rooted words by forbidden-repeat DFS.

    Start with 00000 as the first five-letter window and add bits
    without repeating a five-letter window. At length 32, test the four
    missing cyclic wrap-around windows, which all append initial zeros.
    """
    out = set()
    full = (1 << N) - 1
    def extend(state, used, word):
        if len(word) == N:
            for _ in range(4):
                state = (state << 1) & 31
                if (used >> state) & 1:
                    return
                used |= 1 << state
            if used == full:
                out.add(word)
            return
        for bit in (0, 1):
            new_state = ((state << 1) & 31) | bit
            if not ((used >> new_state) & 1):
                extend(new_state, used | (1 << new_state), word + str(bit))
    extend(0, 1, '00000')
    return out

def cyclic_five_windows(word):
    return {''.join(word[(i+j) % N] for j in range(5)) for i in range(N)}

def signed_correlations(word):
    """Direct sign-vector dot products: one score for each nonzero shift."""
    s = tuple(1 if x == '1' else -1 for x in word)
    return tuple(sum(s[i] * s[(i+t) % N] for i in range(N)) for t in range(1, N))

def xor_correlations(word):
    """Independent cyclic bit rotation and Hamming-distance evaluation."""
    x = int(word, 2)
    out = []
    for t in range(1, N):
        rotated = (x >> t) | ((x & ((1 << t) - 1)) << (N - t))
        out.append(N - 2 * (x ^ rotated).bit_count())
    return tuple(out)

def certify():
    a = feedback_words()
    b = euler_words()
    assert len(a) == len(b) == 2048 and a == b
    tab = Counter()
    for word in sorted(a):
        assert len(cyclic_five_windows(word)) == 32
        c1 = signed_correlations(word)
        c2 = xor_correlations(word)
        assert c1 == c2
        assert all(c1[t-1] == 0 for t in range(1, 5))
        assert min(c1) < 0 and max(c1) >= 0
        tab[min(c1), max(c1)] += 1
    assert sum(tab.values()) == 2048
    for m, vals in TARGET.items():
        assert tuple(tab[m, p] for p in COLS) == vals
    assert set(tab) == {(m,p) for m,vals in TARGET.items() for p,x in zip(COLS,vals) if x}
    # Published controls: worst two negative levels and selected peak sizes;
    # the low-sidelobe subsets in Spinsante et al. (2011).
    assert sum(tab[-24,p] for p in COLS) == 12
    assert sum(tab[-20,p] for p in COLS) == 88
    assert sum(tab[m,16] for m in TARGET) == 36
    assert sum(x for (m,p),x in tab.items() if max(-m,p) <= 4) == 12
    assert sum(x for (m,p),x in tab.items() if max(-m,p) <= 8) == 784
    digest = sha256(('\n'.join(sorted(a))+'\n').encode('ascii')).hexdigest()
    print('word_count=2048')
    print('rows=(minimum offpeak correlation), columns=(maximum offpeak correlation)')
    print('columns=', COLS)
    for m in TARGET:
        print(m, TARGET[m])
    print('canonical_word_set_sha256=', digest)
    print('VERIFY_OK')

if __name__ == '__main__':
    certify()
