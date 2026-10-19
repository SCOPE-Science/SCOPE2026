#!/usr/bin/env python3
"""Independent finite checks of cyclic Thue--Morse palindrome-center radii.

Run: python3 verify.py
The exhaustive finite tests complement, but do not replace, the inductive proof.
"""

def thue_morse(k):
    w = [0]
    for _ in range(k):
        w = [x for a in w for x in (a, 1 - a)]
    return w


def independent_digits(k):
    return [i.bit_count() & 1 for i in range(1 << k)]


def radius_direct(w, c):
    n = len(w)
    z = 0
    for j in range(1, n // 2 + 1):
        if w[(c - j) % n] != w[(c + j - 1) % n]:
            break
        z = j
    return z


def radius_formula(k, c):
    n = 1 << k
    if k % 2 == 0 and c in (0, n // 2):
        return n // 2
    if k % 2 == 1 and c in (n // 4, 3 * n // 4):
        return n // 2
    if c == 0:
        return 0
    v = (c & -c).bit_length() - 1
    if v % 2 == 0:
        return 0
    m = k - v
    assert m >= 3
    u = c >> v
    h = (u - 1) // 2
    mask = (1 << (m - 1)) - 1
    left = ((h - 1) & mask).bit_count() & 1
    right = ((h + 1) & mask).bit_count() & 1
    return (1 << v) * (1 + 2 * (left == right))


def test():
    total = 0
    for k in range(4, 17):
        n = 1 << k
        w = thue_morse(k)
        assert w == independent_digits(k)
        radii = []
        for c in range(n):
            actual = radius_direct(w, c)
            predicted = radius_formula(k, c)
            assert actual == predicted, (k, c, actual, predicted)
            radii.append(actual)
            total += 1
        if k % 2 == 0:
            axes = {0, n // 2}
            bound = n // 8
            maximizers = {n // 8, 3*n // 8, 5*n // 8, 7*n // 8}
        else:
            axes = {n // 4, 3*n // 4}
            bound = 3*n // 16
            maximizers = {u*n // 16 for u in (1, 7, 9, 15)}
        assert {c for c, r in enumerate(radii) if r == n // 2} == axes
        assert max(r for c, r in enumerate(radii) if c not in axes) == bound
        assert {c for c, r in enumerate(radii) if r == bound and c not in axes} == maximizers
        for c in range(n):
            assert all(w[(c-j)%n] == w[(c+j-1)%n] for j in range(1, radii[c]+1))
            if radii[c] < n//2:
                j = radii[c] + 1
                assert w[(c-j)%n] != w[(c+j-1)%n]
        # Length-five palindromes are absent even across the cyclic seam.
        assert all(not all(w[(s+j)%n] == w[(s+4-j)%n] for j in range(2)) for s in range(n))
        # For every length above the off-axis threshold only two factors survive.
        sample_lengths = sorted({2*bound + 2, n//2, n-2, n})
        for L in sample_lengths:
            if L % 2 or L > n or L <= 2*bound:
                continue
            factors = {
                tuple(w[(c-L//2+j)%n] for j in range(L))
                for c in range(n) if radii[c] >= L//2
            }
            assert len(factors) == 2, (k,L,len(factors))
    print(f'VERIFY_OK k=4..16 centers={total} four-maximizer and odd-palindrome tests passed')


if __name__ == '__main__':
    test()
