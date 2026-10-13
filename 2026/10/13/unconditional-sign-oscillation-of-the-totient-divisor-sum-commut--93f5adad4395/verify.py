"""Finite arithmetic checks for the composition-commutator theorem.

The unrestricted sign assertions follow from the proof in RESULT.md;
finite evaluation supplies reproducible numerical spot checks.
"""


def factor_powers(n):
    """Return (prime, exponent) pairs by deterministic trial division."""
    assert n >= 1
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            factors.append((d, a))
        d = 3 if d == 2 else d + 2
    if n > 1:
        factors.append((n, 1))
    return factors


def phi(n):
    r = n
    for p, _ in factor_powers(n):
        r = r // p * (p - 1)
    return r


def sigma(n):
    r = 1
    for p, a in factor_powers(n):
        r *= (p ** (a + 1) - 1) // (p - 1)
    return r


def is_prime(n):
    return n > 1 and factor_powers(n) == [(n, 1)]


def check():
    positives, negatives = [], []
    for k in range(2, 37):
        n = 1 << (k - 1)
        m = (1 << k) - 1
        difference = sigma(phi(n)) - phi(sigma(n))
        assert difference == (m - 1) // 2 - phi(m)
        if difference > 0:
            positives.append(k)
        if difference < 0:
            negatives.append(k)
        if is_prime(k):
            assert difference < 0, (k, difference)
        if k % 12 == 0:
            assert difference > 0, (k, difference)
    assert min(positives) == 12
    assert phi(4095) == 1728
    assert sigma(phi(2048)) - phi(sigma(2048)) == 319
    assert positives == [12, 20, 24, 28, 30, 36]
    assert all(k in negatives for k in [2, 3, 5, 7, 11])
    print('VERIFY_OK k=2..36', 'positive_indices=', positives,
          'first_positive_n=2048', 'C_2048=319',
          'prime_indices_negative=', sum(map(is_prime, range(2, 37))))


if __name__ == '__main__':
    check()
