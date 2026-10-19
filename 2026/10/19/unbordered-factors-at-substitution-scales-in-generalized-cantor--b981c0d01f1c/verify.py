#!/usr/bin/env python3
"""Independent finite checks for Cantor-word unbordered-factor formula.
Scientific verification only; no certification of infinite claims.
"""

def substitution(q, height):
    w = '1'
    for _ in range(height):
        w = ''.join(('1' + '0' * (q-2) + '1') if c == '1'
                    else '0' * q for c in w)
    return w


def digit_sequence(q, length):
    bits = bytearray(length)
    for i in range(length):
        v = i
        while v and v % q in (0, q-1):
            v //= q
        bits[i] = (49 if v == 0 else 48)
    return bits.decode('ascii')


def unbordered(w):
    # KMP prefix function: final value zero iff w has no nonempty border.
    lps = [0] * len(w)
    j = 0
    for i in range(1, len(w)):
        while j and w[i] != w[j]:
            j = lps[j-1]
        if w[i] == w[j]:
            j += 1
        lps[i] = j
    return lps[-1] == 0


def predicted(q, k):
    n = q ** k
    m = n // q
    a = substitution(q, k-1)
    assert len(a) == m
    out = set()
    for r, c in enumerate(a):
        if c == '1':
            word = a[r:] + '0' * ((q-1)*m+r)
            assert len(word) == n
            out.add(word)
            out.add(word[::-1])
    return out


def check(q, k):
    n = q**k
    src = digit_sequence(q, q**(k+2))
    assert src[:q**(k+1)] == substitution(q, k+1)
    factors = {src[i:i+n] for i in range(len(src)-n+1)}
    actual = {w for w in factors if w[0] != w[-1] and unbordered(w)}
    want = predicted(q, k)
    if actual != want:
        raise AssertionError((q, k, len(actual), len(want),
                              list(actual-want)[:2], list(want-actual)[:2]))
    if len(want) != 2**k:
        raise AssertionError((q, k, len(want)))
    return len(factors)


def main():
    cases = [(q, k) for q in range(3, 8) for k in range(1,5)]
    cases += [(3,5),(3,6),(4,5),(5,5)]
    for q,k in cases:
        nfac=check(q,k)
        print(f'CHECK q={q} k={k} n={q**k} distinct_factors={nfac} unbordered={2**k}')
    print('VERIFY_OK independent_digit_vs_substitution cases=%s complete_borders=yes' % len(cases))

if __name__ == '__main__':
    main()
