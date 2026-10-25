#!/usr/bin/env python3
"""Exact arithmetic checks for dyadic translation periods of central Delannoy numbers."""

def v2(x):
    return 10**9 if x == 0 else (x & -x).bit_length() - 1

def main():
    N = 640
    seq = [1, 3]
    for n in range(2, N):
        numerator = 3 * (2 * n - 1) * seq[-1] - (n - 1) * seq[-2]
        assert numerator % n == 0
        seq.append(numerator // n)
    assert seq[:9] == [1, 3, 13, 63, 321, 1683, 8989, 48639, 265729]
    comparisons = 0
    for m in range(1, 161):
        s = v2(m)
        needed = 1 if s == 0 else 2 if s == 1 else s + 2
        assert v2(seq[m+1] - seq[1]) == needed, (m, needed)
        for n in range(0, 321):
            assert v2(seq[n+m] - seq[n]) >= needed, (m, n, needed)
            comparisons += 1
    period_tests = 0
    for h in range(1, 11):
        p = 1 if h == 1 else 2 if h == 2 else 4 if h in (3,4) else 2**(h-2)
        modulus = 2**h
        assert all((seq[n+p] - seq[n]) % modulus == 0 for n in range(N-p))
        if p > 1:
            assert any((seq[n+p//2] - seq[n]) % modulus for n in range(N-p//2))
        period_tests += 1
    conjecture_checks = 0
    for s in range(2, 8):
        for a in range(1, 9, 2):
            if a*(2**(s+1))+1 >= N:
                continue
            assert v2(seq[a*2**(s+1)+1] - seq[a*2**s+1]) == s+2
            conjecture_checks += 1
    print('VERIFY_OK exact_translation_checks', comparisons, 'dyadic_period_moduli', period_tests,
          'published_offset_checks', conjecture_checks)

if __name__ == '__main__':
    main()
