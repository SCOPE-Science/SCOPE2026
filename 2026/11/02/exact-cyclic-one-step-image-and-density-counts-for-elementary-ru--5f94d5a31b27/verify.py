#!/usr/bin/env python3
"""Independent finite checks for exact one-step Rule 18 image enumeration.

Only the Python standard library is required. Run: python verify.py
This verifier checks finite cases; the all-length argument is in RESULT.md.
"""
from math import comb


def update(word):
    """Synchronous Rule 18 on a periodic binary tuple, including tiny rings."""
    n = len(word)
    return tuple((1 - word[i]) * (word[(i - 1) % n] ^ word[(i + 1) % n])
                 for i in range(n))


def bits(v, n):
    return tuple((v >> i) & 1 for i in range(n))


def encoded(word):
    return sum(b << i for i, b in enumerate(word))


def matching_and_predecessor(y):
    """Construct explicit preimage from the alternating positive-gap rule.

    Return None for unreachable outputs. A predecessor is returned for every
    other output by filling the intervals between paired 1s with 0 and
    all intervening separation intervals with 1.
    """
    n = len(y)
    pos = [i for i in range(n) if y[i]]
    m = len(pos)
    if m == 0:
        return tuple(0 for _ in range(n))
    if m % 2:
        return None
    gaps = [(pos[(i + 1) % m] - pos[i] - 1) % n for i in range(m)]
    shift = None
    for s in (0, 1):
        if all(gaps[(s + 2*j + 1) % m] >= 1 for j in range(m // 2)):
            shift = s
            break
    if shift is None:
        return None
    x = [1] * n
    for j in range(m // 2):
        a = pos[(shift + 2*j) % m]
        b = pos[(shift + 2*j + 1) % m]
        for t in range((b - a) % n + 1):
            x[(a + t) % n] = 0
    return tuple(x)


def choose(n, k):
    return comb(n, k) if n >= 0 and 0 <= k <= n else 0


def fixed_density(n, k):
    """Number with exactly 2*k output 1s, for positive k."""
    if k < 1:
        raise ValueError('k must be positive')
    numer = n * (2 * choose(n-k-1, 2*k-1) - choose(n-2*k-1, 2*k-1))
    assert numer % (2*k) == 0
    return numer // (2*k)


def neg_z_log_derivative_coeffs(q, degree):
    """Coefficients of -z Q'(z)/Q(z), with Q(0)=1."""
    assert q[0] == 1
    vals = [0] * (degree + 1)
    for n in range(1, degree + 1):
        result = -n * (q[n] if n < len(q) else 0)
        result -= sum(q[j] * vals[n-j] for j in range(1, min(n, len(q)-1)+1))
        vals[n] = result
    return vals


def gf_counts(degree):
    # Q_B = (1-z)^2-z^3; Q_C=(1-z)^2-z^4.
    sb = neg_z_log_derivative_coeffs([1, -2, 1, -1], degree)
    sc = neg_z_log_derivative_coeffs([1, -2, 1, 0, -1], degree)
    assert all(x % 2 == 0 for x in sc[1:])
    return [0] + [sb[n] - sc[n] // 2 for n in range(1, degree + 1)]


def main():
    gf = gf_counts(70)
    for n in range(1, 19):
        image = {encoded(update(bits(i, n))) for i in range(1 << n)}
        matched = set()
        counts = {}
        for i in range(1 << n):
            y = bits(i, n)
            pred = matching_and_predecessor(y)
            if pred is not None:
                assert update(pred) == y, (n, i, 'constructive predecessor failed')
                matched.add(i)
                counts[sum(y)] = counts.get(sum(y), 0) + 1
        assert image == matched, (n, len(image), len(matched))
        assert counts.get(0) == 1
        assert all((j & 1) == 0 for j in counts)
        for k in range(1, n//2 + 1):
            assert counts.get(2*k, 0) == fixed_density(n, k), (n,k)
        assert len(image) == gf[n], (n, len(image), gf[n])
        print(f'n={n}: reachable={len(image)}, weights={counts}')
    for n in range(1, 71):
        assert 1 + sum(fixed_density(n,k) for k in range(1, n//2+1)) == gf[n]
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
