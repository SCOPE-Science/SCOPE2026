#!/usr/bin/env python3
"""Independent finite tests of palindromic factor complexity in Cantor-like words.

Run: python verify_pal.py
Finite tests corroborate; they do not prove the unbounded theorem.
"""
from itertools import product

def iterate(q, minimum):
    word = '1'
    while len(word) < minimum:
        word = ''.join(('1' + '0' * (q-2) + '1') if ch == '1' else '0' * q for ch in word)
    return word

def by_digits(q, length):
    out = []
    for i in range(length):
        j = i
        b = '1'
        while j:
            d = j % q
            if d not in (0, q - 1):
                b = '0'
                break
            j //= q
        out.append(b)
    return ''.join(out)

def formula(q, n):
    if n == 0:
        return 1
    v = 1 + int(n % 2 == 1 and n <= 2 * (q - 2) + 1)
    j = 0
    while (q - 2) * q**j + 2 <= n:
        gap = (q - 2) * q**j
        stop = (2*q - 3) * q**(j+1)
        if (n-gap) % 2 == 0 and n <= stop:
            v += 1
        j += 1
    return v

def main():
    cases = 0
    for q in range(3, 10):
        w = iterate(q, 1200)
        assert w == by_digits(q, len(w)), (q, 'digit morphism mismatch')
        assert formula(q, 0) == 1
        for n in range(1, 81):
            pal = set()
            for i in range(len(w) - n + 1):
                s = w[i:i+n]
                if s == s[::-1]:
                    pal.add(s)
            assert len(pal) == formula(q, n), (q,n,len(pal),formula(q,n),sorted(pal))
            cases += 1
    print('VERIFY_OK independent_base_digit_and_substitution q=3..9 palindromes_n=0..80 cases='+str(cases))
if __name__ == '__main__':
    main()
