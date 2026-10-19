"""Finite exact-state checks for dyadic-successor Thue--Morse shifts.

All arithmetic is integer-valued; exhaustive low residues and four high
Thue--Morse adjacent-value pairs cover every possible prefix integer.
"""
from collections import Counter


def t(n):
    assert n >= 0
    return n.bit_count() & 1


def offsets(c):
    assert c >= 1
    vals = {c}
    power = 2
    while power <= c * 2:
        q, r = divmod(c, power)
        vals.add(q)
        vals.add(q + (r != 0))
        power *= 2
    return tuple(sorted(vals))


def fingerprint(n, os):
    return tuple(t(n + j) for j in os)


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def exact_fingerprints(c):
    # Set B > c and n=h*B+r. Every t(n+j) depends only on
    # r, t(h), t(h+1). The four pairs appear for h=0,1,2,5.
    B = 1 << (c.bit_length() + 1)
    pairs = {h: (t(h), t(h+1)) for h in (0, 1, 2, 5)}
    assert len(set(pairs.values())) == 4, pairs
    os = offsets(c)
    all_fps = set()
    even_fps = set()
    odd_fps = set()
    for h in pairs:
        for r in range(B):
            n = h * B + r
            f = fingerprint(n, os)
            all_fps.add(f)
            (odd_fps if n & 1 else even_fps).add(f)
    return all_fps, even_fps, odd_fps


def brute_suffix_signature(n, c, ell_max):
    out = []
    for ell in range(ell_max + 1):
        for u in range(1 << ell):
            out.append(t((n << ell) + u + c))
    return tuple(out)


def main():
    assert offsets(2) == (0, 1, 2)
    assert len(exact_fingerprints(2)[0]) == 6
    print('base c=2: six distinct length-three Thue--Morse factors: OK')
    for k in range(1, 9):
        c = (1 << k) + 1
        all_fps, even_fps, odd_fps = exact_fingerprints(c)
        a = 2 * fib(k + 2)
        b = 2 * fib(k + 3)
        expected = 2 * fib(k + 4)
        assert not even_fps.intersection(odd_fps)
        assert len(even_fps) == a, (k, len(even_fps), a)
        assert len(odd_fps) == b, (k, len(odd_fps), b)
        assert len(all_fps) == expected, (k, len(all_fps), expected)
        print(f'k={k:2d} c={c:3d} offsets={len(offsets(c)):2d} even={len(even_fps):3d} odd={len(odd_fps):3d} total={len(all_fps):3d}: OK')
    for c in range(1, 41):
        os = offsets(c)
        seen = {}
        for n in range(70):
            fp = fingerprint(n, os)
            sig = brute_suffix_signature(n, c, c.bit_length() + 1)
            if fp in seen:
                assert seen[fp] == sig, (c, n)
            else:
                seen[fp] = sig
        assert len(set(seen.values())) == len(seen), (c, len(seen))
    print('MSD-first residual/fingerprint equivalence verified for 40 shifts, 70 prefix values each: OK')
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
