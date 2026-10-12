#!/usr/bin/env python3
"""Independent finite checks for the all-ones block-parity run theorem.

No external packages or data files are needed. Executable: python3 verify.py
The exhaustive checks are finite tests; the manuscript supplies the infinite proof.
"""
from collections import Counter
from fractions import Fraction


def valuation2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def spectrum(k):
    assert k >= 2
    H = 1 << k
    return ({1} | {1 << j for j in range(1, k + 1)}
            | {H - (1 << j) for j in range(k - 1)}
            | {H // 2 + 1})


def mass(k):
    """Rational run counts per block of H=2**k indices; add collisions."""
    H = 1 << k
    p = Fraction(2, H)
    rho = (2 - p) / 3
    c = Counter()
    c[1] += Fraction(1, 2) + rho
    for j in range(1, k - 1):
        c[1 << j] += Fraction(1, 1 << (j + 1))
    for j in range(1, k):
        c[H - (1 << j)] += Fraction(1, 1 << (j + 1))
    c[H // 2 + 1] += Fraction(1, H)
    c[H - 1] += (1 + p) / 6
    c[H] += (2 - p) / 6
    return c


def direct_word(N, k):
    H = 1 << k
    word = bytearray(N + 1)
    for n in range(1, N + 1):
        word[n] = word[n >> 1] ^ (1 if (n & (H - 1)) == H - 1 else 0)
    return word


def direct_bit_word(n, k):
    s = bin(n)[2:]
    pat = '1' * k
    return sum(s[i:i+k] == pat for i in range(max(0, len(s)-k+1))) & 1


def delta_predicted(n, k):
    t = valuation2(n+1)
    m = n >> (t+1)
    r = valuation2(m+1)
    return ((max(0, t-k+1) + (r >= k-1)) & 1)


def events_by_block(B, k):
    H = 1 << k
    for j in range(B):
        s = valuation2(j + 1)
        m = min(s, k-1)
        for t in range(m, -1, -1):
            yield j*H + H - (1 << t) - 1
        q = (j+1) >> s
        c = (s+1 + (q % H == H-1)) & 1
        if c:
            yield (j+1)*H-1


def check():
    for k in range(2, 11):
        H = 1 << k
        c = mass(k)
        assert set(c) == spectrum(k), (k, set(c) ^ spectrum(k))
        assert all(v > 0 for v in c.values())
        p = Fraction(2, H)
        Lambda = Fraction(4, 3)*(2-p)
        assert sum(c.values()) == Lambda
        assert Lambda/H == Fraction(8*(H-1), 3*H*H)
        assert sum(ell*v for ell,v in c.items()) == H

        N = 1 << 21
        w = direct_word(N, k)
        for n in range(0, min(N, 1 << 14)):
            assert w[n] == direct_bit_word(n, k), (k, n)
        for n in range(0, min(N, 1 << 17)):
            assert (w[n] ^ w[n+1]) == delta_predicted(n, k), (k, n)

        seen = set()
        prev = None
        num_changes = 0
        for n in range(N):
            if w[n] != w[n+1]:
                num_changes += 1
                if prev is not None:
                    d = n-prev
                    assert d in spectrum(k), (k, d, n)
                    seen.add(d)
                prev = n
        assert seen == spectrum(k), (k, seen, spectrum(k))
        assert abs(Fraction(num_changes, N) - Lambda/H) < Fraction(5*H, N)

        Bsmall = min(4096, N // H)
        actual = [n for n in range(Bsmall*H) if w[n] != w[n+1]]
        predicted = list(events_by_block(Bsmall, k))
        assert actual == predicted, (k, 'event-placement', Bsmall)

        B = 1 << 15
        hist = Counter()
        previous = None
        for n in events_by_block(B, k):
            if previous is not None:
                hist[n-previous] += 1
            previous = n
        assert set(hist) == set(c), (k, 'constructed-spectrum')
        for ell, mass_value in c.items():
            assert abs(Fraction(hist[ell],B)-mass_value) < Fraction(3,1000), (k,ell,hist[ell],mass_value)
        print(f'k={k} H={H} types={len(c)} changes={num_changes} block_events={len(predicted)} histogram_total={sum(hist.values())}')
    print('VERIFY_OK k=2..10 direct_N=2097152 bitcount_prefix=16384 delta_prefix=131072 exact_direct_spectra=yes event_blocks<=4096 frequency_blocks=32768 normalized_mass_and_mean_length=yes')


if __name__ == '__main__':
    check()
