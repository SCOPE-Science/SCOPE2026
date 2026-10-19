"""Finite cross-checks of the Zimin periodic privileged/palindrome theorem.

Usage: python verify.py
The unrestricted theorem is supplied by the mathematical proof, not these checks.
"""
from functools import lru_cache


def zimin(n):
    assert n >= 1
    z = (1,)
    for k in range(2, n + 1):
        z = z + (k,) + z
    return z


def predicted(n, length):
    assert length >= 1
    return 1 if length % 2 == 0 else max(1, n - (length.bit_length() - 1))


def brute_palindromes(w, length):
    n = len(w)
    periodic = w * (length // n + 2)
    return {periodic[i:i + length] for i in range(n)
            if periodic[i:i + length] == periodic[i:i + length][::-1]}


def center_palindromes(w, max_length):
    """Independent palindrome enumeration by outward center expansion."""
    n = len(w)
    periodic = w * (max_length // n + 6)
    answer = {length: set() for length in range(1, max_length + 1)}
    for i in range(n):
        for parity in (0, 1):
            # Centers at 2*n+i (odd, parity=0) or immediately before (even, parity=1).
            left = 2 * n + i - parity
            right = 2 * n + i
            while left >= 0 and right < len(periodic) and periodic[left] == periodic[right]:
                length = right - left + 1
                if length > max_length:
                    break
                answer[length].add(periodic[left:right + 1])
                left -= 1
                right += 1
    return answer


@lru_cache(maxsize=None)
def privileged(w):
    if len(w) <= 1:
        return True
    n = len(w)
    for p in range(1, n):
        border = w[:p]
        if border != w[-p:] or not privileged(border):
            continue
        occ = 0
        for i in range(n - p + 1):
            if w[i:i + p] == border:
                occ += 1
                if occ > 2:
                    break
        if occ == 2:
            return True
    return False


def check():
    palindrome_cases = 0
    privileged_cases = 0
    for n in range(1, 9):
        w = zimin(n)
        N = len(w)
        bound = 3 * N
        by_center = center_palindromes(w, bound)
        for L in range(1, bound + 1):
            direct = brute_palindromes(w, L)
            assert direct == by_center[L], (n, L, 'center/direct disagree')
            assert len(direct) == predicted(n, L), (n, L, len(direct), predicted(n, L))
            palindrome_cases += 1
        if n <= 7:
            doubled = w + w
            all_circular = {doubled[i:i + L] for L in range(1, N + 1)
                            for i in range(N)}
            palindromes = {u for u in all_circular if u == u[::-1]}
            privileges = {u for u in all_circular if privileged(u)}
            assert palindromes == privileges, (n, 'privileged mismatch')
            assert len(palindromes) == (3 * N - 1) // 2, n
            privileged_cases += len(all_circular)
    print('VERIFY_OK orders=1..8 full_palindromic_profiles_through_three_periods',
          'tested_length_levels=' + str(palindrome_cases),
          'independent_palindrome_methods=2',
          'privileged_factor_equality_orders=1..7',
          'distinct_circular_factors_checked=' + str(privileged_cases),
          'periodic_complexity_formula=True',
          'circular_total_formula=True')


if __name__ == '__main__':
    check()
