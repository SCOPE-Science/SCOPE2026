#!/usr/bin/env python3
"""Exact all-length four-symbol cyclic-rotation ball bound.

Only Python's standard library is required. All comparisons are integer or
finite-set operations; the 32-state recurrence proves the universal claim.
"""
from itertools import product

BITS = tuple(''.join(x) for x in product('01', repeat=5))


def local_out(z, j):
    """Nonidentity length-four rotations beginning at j."""
    b = z[j:j+4]
    return {z[:j] + b[t:] + b[:t] + z[j+4:]
            for t in (1, 2, 3)} - {z}


def first(z):
    assert len(z) == 4
    return len(local_out(z, 0))


def second(z):
    assert len(z) == 5
    return len(local_out(z, 1) - local_out(z, 0))


def reward(z):
    assert len(z) == 6
    return len(local_out(z, 2) - local_out(z, 1) - local_out(z, 0))


def initial():
    return {z: first(z[:4]) + second(z) for z in BITS}


def update(v):
    w = {z: -1000000 for z in BITS}
    for z in BITS:
        for b in '01':
            t = z[1:] + b
            w[t] = max(w[t], v[z] + reward(z + b))
    assert all(x > -1000000 for x in w.values())
    return w


def recurrence_counts(N):
    v = initial()
    d = {5: v}
    for n in range(6, N + 1):
        v = update(v)
        d[n] = v
    return d


def direct(s):
    # Separate tuple-based full-word enumeration for independent local-check.
    x = tuple(int(b) for b in s)
    seen = {x}
    for i in range(len(x) - 3):
        t = x[i:i+4]
        for j in range(1, 4):
            seen.add(x[:i] + t[j:] + t[:j] + x[i+4:])
    return len(seen)


def local_total(s):
    if len(s) == 4:
        return 1 + first(s)
    r = 1 + first(s[:4]) + second(s[:5])
    for i in range(2, len(s) - 3):
        r += reward(s[i-2:i+4])
    return r


def main():
    d = recurrence_counts(16)
    targets = {4: 4, 5: 7, 6: 9, 7: 11, 8: 13,
               9: 15, 10: 18}
    for n, expected in targets.items():
        got = (1 + max(d[n].values()) if n >= 5
               else max(direct(''.join(t)) for t in product('01', repeat=4)))
        assert got == expected, (n, got, expected)
    # The pivotal componentwise equality: by update(v+c)=update(v)+c,
    # it rigorously propagates to every larger length.
    for state in BITS:
        assert d[11][state] == d[6][state] + 11, state
    for n in range(5, 17):
        assert 1 + max(d[n].values()) == (11*n - 20)//5, n
    # Independent brute-force reconstruction of every DP terminal-state value,
    # including both sides of the five-step translation certificate.
    for n in range(5, 12):
        terminal = {z: -1000000 for z in BITS}
        for t in product('01', repeat=n):
            s = ''.join(t)
            terminal[s[-5:]] = max(terminal[s[-5:]], direct(s) - 1)
        assert terminal == d[n], n
    # Exhaustive independent comparison of local and full-word constructions.
    for n in range(4, 12):
        for t in product('01', repeat=n):
            s = ''.join(t)
            assert direct(s) == local_total(s), (n, s)
    for n in range(4, 101):
        witness = ('01110' * ((n + 4)//5))[:n]
        assert direct(witness) == (11*n - 20)//5, n
    print('VERIFY_OK')
    print('v6 (lexicographic five-bit states):')
    print(' '.join(str(d[6][s]) for s in BITS))
    print('max volumes n=4..16:', [4] + [1+max(d[n].values()) for n in range(5,17)])


if __name__ == '__main__':
    main()
