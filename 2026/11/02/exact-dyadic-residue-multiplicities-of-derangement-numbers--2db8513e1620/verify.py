"""Standalone exact checks for the dyadic derangement residue theorem.

Run: python3 verify.py. Python standard library only.
Finite tests corroborate, but do not replace, the infinite proof.
"""
from collections import Counter
from math import prod


def derangements_mod(modulus):
    vals = [1]
    for n in range(1, modulus):
        vals.append((n * vals[-1] + (-1 if n % 2 else 1)) % modulus)
    return vals


def falling(n, j):
    r = 1
    for h in range(j):
        r *= n - h
    return r


def signed_falling_sum(n):
    return sum((-1)**j * falling(n, j) for j in range(n + 1))


def derivative_falling(n, j):
    if not j:
        return 0
    return sum(prod(n - h for h in range(j) if h != i)
               for i in range(j))


def main():
    # Independence of the standard recurrence from the inclusion-exclusion sum.
    exact = 1
    for n in range(0, 121):
        if n:
            exact = n * exact + (-1 if n % 2 else 1)
        assert exact == (-1)**n * signed_falling_sum(n), n

    # The derivative is stable modulo 4 once j >= 6.
    for x in range(32):
        deriv = sum((-1)**j * derivative_falling(x, j)
                    for j in range(0, 20))
        if x % 2:
            assert deriv % 2 == 1, ('odd derivative', x, deriv % 2)
        else:
            assert deriv % 4 == 2, ('even derivative', x, deriv % 4)

    tested = 0
    for k in range(1, 16):
        modulus = 1 << k
        vals = derangements_mod(modulus)
        c = Counter(vals)
        if k == 1:
            expected = {0: 1, 1: 1}
        elif k == 2:
            expected = {0: 1, 1: 2, 2: 1}
        else:
            expected = {y: 1 for y in range(0, modulus, 2)}
            expected.update({y: 4 for y in range(1, modulus, 8)})
        assert c == expected, (k, sorted((c - Counter(expected)).items())[:5],
                               sorted((Counter(expected) - c).items())[:5])
        if k >= 2:
            assert vals[1] != vals[1 + modulus // 2]
        tested += modulus
        print(f'LEVEL_OK k={k} support={len(c)} even_values={modulus//2} '
              f'fibers={modulus}')
    print(f'VERIFY_OK exhaustive_fibers={tested} levels=1..15 '
          f'derivative_mod4_test_points=32 exact_formula_n=0..120')


if __name__ == '__main__':
    main()
