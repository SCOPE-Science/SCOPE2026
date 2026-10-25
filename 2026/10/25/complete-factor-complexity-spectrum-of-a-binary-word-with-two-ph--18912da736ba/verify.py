#!/usr/bin/env python3
"""Direct finite checks for a two-defect binary factor-complexity formula."""
from itertools import product


def diagonal_rectangle(x, y, k):
    return max(0, min(x - 1, k) - max(0, k - y + 1) + 1)


def predicted(a, b, c, length):
    A, B, C = 2 * a + 1, 2 * b + 1, 2 * c
    T = max(A, B, C)
    base = (2 if 1 <= length < T else 1 if length == T else 0)
    return (base + diagonal_rectangle(A, B, length - 2)
            + diagonal_rectangle(B, C, length - 2)
            - diagonal_rectangle(min(A, B), min(B, C), length - 2)
            + diagonal_rectangle(A, C, length - B - 2))


def main():
    cases = 0
    for a, b, c in product(range(1, 10), repeat=3):
        word = '01' * a + '0' + '01' * b + '0' + '01' * c
        A, B, C = 2*a+1, 2*b+1, 2*c
        expected_total = (2*max(A,B,C)-1 + A*B+B*C
                          - min(A,B)*min(B,C) + A*C)
        seen = set()
        for ell in range(1, len(word)+1):
            factors = {word[i:i+ell] for i in range(len(word)-ell+1)}
            assert len(factors) == predicted(a,b,c,ell), (a,b,c,ell)
            seen.update(factors)
        assert len(seen) == expected_total, (a,b,c)
        cases += 1
    print(f'VERIFY_OK {cases} triples')

if __name__ == '__main__':
    main()
