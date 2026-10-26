#!/usr/bin/env python3
"""Exact finite checks of cardinality spectrum for square units modulo p^2.

Works solely with integer bit masks; no external packages.
"""

def isprime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


def spectrum(p):
    m = p * p
    A = sorted({x * x % m for x in range(1, m) if x % p})
    N = len(A)
    assert N == p * (p - 1) // 2
    bits = [0] * (N + 1)
    bits[0] = 1
    mask = (1 << m) - 1
    for x in A:
        for k in range(N, 0, -1):
            b = bits[k - 1]
            bits[k] |= (b << x | b >> (m - x)) & mask
    return N, bits, mask


def predicted(p, N):
    if p == 3:
        return set()
    if p == 5:
        return {4, 6}
    out = set(range(3, N - 2))
    if p % 4 == 1:
        out.update({2, N - 2})
    return out


def main():
    for p in [3, 5, 7, 11, 13, 17, 19, 23]:
        assert isprime(p)
        N, bits, mask = spectrum(p)
        got = {i for i, x in enumerate(bits) if x == mask}
        assert got == predicted(p, N), (p, got, predicted(p, N))
        if p == 5:
            missing = {j for j in range(25) if not ((bits[5] >> j) & 1)}
            assert missing == {0, 10, 15}, missing
        print(f"p={p} N={N} universal_k_count={len(got)}: OK")
    print("VERIFY_OK")


if __name__ == '__main__':
    main()
