"""Independent finite checks for the Christoffel conjugate Abelian-border theorem.

Run with Python 3.10 or later: python check.py
The infinite theorem rests on the arithmetic proof, not these tests.
"""
from math import gcd


def prefix_ones(word):
    out = [0]
    for symbol in word:
        out.append(out[-1] + symbol)
    return out


def abelian_borders(word):
    n = len(word)
    pref = prefix_ones(word)
    return tuple(ell for ell in range(1, n)
                 if pref[ell] == pref[n] - pref[n - ell])


def predicted_borders(n, b, shift):
    j = (shift * b) % n
    lo = min(j, n - 1 - j)
    hi = max(j, n - 1 - j)
    return tuple(ell for ell in range(1, n)
                 if (r := (ell * b) % n) <= lo or r > hi)


def run():
    verified = 0
    checked_lengths = 0
    checked_border_decisions = 0
    for n in range(2, 81):
        for b in range(1, n):
            if gcd(n, b) != 1:
                continue
            lower = [(i + 1) * b // n - i * b // n for i in range(n)]
            assert len(lower) == n and sum(lower) == b
            counts = []
            for s in range(n):
                rotation = lower[s:] + lower[:s]
                observed = abelian_borders(rotation)
                expected = predicted_borders(n, b, s)
                assert observed == expected, (n, b, s, observed, expected)
                j = s * b % n
                assert len(observed) == 2 * min(j, n - 1 - j)
                counts.append(len(observed))
                checked_border_decisions += n - 1
                verified += 1
            expected_counts = sorted(2 * min(j, n - 1 - j)
                                     for j in range(n))
            assert sorted(counts) == expected_counts
            assert counts.count(0) == 2
            if n % 2:
                assert counts.count(n - 1) == 1
            else:
                assert counts.count(n - 2) == 2
            checked_lengths += 1
    print('PASS_CHRISTOFFEL_ABELIAN_BORDER n=2..80'
          f' coprime_length_slope_pairs={checked_lengths}'
          f' rotations={verified}'
          f' border_decisions={checked_border_decisions}')


if __name__ == '__main__':
    run()
