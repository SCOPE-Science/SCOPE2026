#!/usr/bin/env python3
"""Exact finite regression checks for paperfolding initial non-repetitive complexity.

The mathematical proof of the infinite theorem is in RESULT.md; this verifier
checks a large finite range by an independent exhaustive factor comparison.
"""

def oddpart_bit(i):
    t = i + 1
    while t % 2 == 0:
        t //= 2
    return int(t % 4 == 3)


def recursive_prefix(length):
    out = bytearray(length)
    for i in range(length):
        if i % 2 == 0:
            out[i] = (i // 2) % 2
        else:
            out[i] = out[i // 2]
    return bytes(out)


def first_collision(seq, length, bound):
    """Use exact Python integers encoding all length-bit windows; no hashes."""
    mask = (1 << length) - 1
    w = 0
    for x in seq[:length]:
        w = (w << 1) | x
    seen = {}
    for i in range(bound + 1):
        previous = seen.get(w)
        if previous is not None:
            return i, previous
        seen[w] = i
        w = ((w << 1) & mask) | seq[i + length]
    raise AssertionError('no collision by specified bound')


def predicted(n):
    short = {1: (1,0), 2: (3,0), 3:(3,0), 4:(8,3), 5:(8,3),
             6:(12,4), 7:(12,4)}
    if n <= 7:
        return short[n]
    m = 1 << (n.bit_length() - 1)
    return 3*m, m


def run():
    limit = 25000
    seq = recursive_prefix(limit)
    assert all(seq[i] == oddpart_bit(i) for i in range(limit))
    assert len({seq[i:i+8] for i in range(24)}) == 24
    assert seq[8:23] == seq[24:39]
    assert all(seq[i:i+4] not in (bytes((0,1,0,1)),bytes((1,0,1,0))) for i in range(5000))
    # Exhaustive first-repetition comparison at EVERY length through 320.
    lengths = set(range(1,321))
    # Extra scale and transition tests through 4096.
    for k in range(9,13):
        m = 1 << k
        lengths.update([m - 1, m, m + 1, 3*m//2, 2*m - 1])
    for n in sorted(lengths):
        want = predicted(n)
        got = first_collision(seq, n, want[0])
        assert got == want, (n, got, want)
    print('VERIFY_OK', 'lengths_checked', len(lengths), 'max_n', max(lengths),
          'prefix_bits', limit)


if __name__ == '__main__':
    run()
