"""Independent finite checks for a base-b palindrome difference classification.

No external dependencies. Finite tests complement, but do not replace, the proof.
"""
from itertools import product
from math import isqrt


def digits_base(n, b):
    assert n >= 0 and b >= 2
    if n == 0:
        return (0,)
    out = []
    while n:
        out.append(n % b)
        n //= b
    return tuple(out)


def is_palindrome(n, b):
    d = digits_base(n, b)
    return d == d[::-1]


def palindromes_to_length(b, max_length):
    """Construct every palindrome directly, length by length."""
    for length in range(1, max_length + 1):
        half_len = (length + 1) // 2
        for leading in range(1, b):
            for tail in product(range(b), repeat=half_len-1):
                first_half = (leading,) + tail
                sequence = first_half + (first_half[-2::-1] if length % 2 else first_half[::-1])
                n = 0
                for d in sequence:
                    n = b * n + d
                assert is_palindrome(n, b)
                yield n


def classified_pairs(b, k):
    out = set()
    for a in range(1, k + 1):
        if k % a == 0:
            n = sum(b ** (j*a) for j in range(k//a))
            out.add((n, n + b**k))
    for n in palindromes_to_length(b, 2*k+1):
        d = digits_base(n, b)
        if len(d) == 2*k+1 and d[k] <= b-2:
            out.add((n, n+b**k))
    return out


def divisors_count(k):
    return sum(k % a == 0 for a in range(1, k + 1))


def check(b, k):
    predicted = classified_pairs(b, k)
    direct = {(n, n + b**k) for n in palindromes_to_length(b, 2*k+1)
              if is_palindrome(n + b**k, b)}
    expected = (b-1)**2 * b**(k-1) + divisors_count(k)
    assert predicted == direct, (b, k, len(predicted), len(direct), (direct-predicted), (predicted-direct))
    assert len(direct) == expected, (b, k, len(direct), expected)
    # For small parameters also rule out palindromic solutions above the proved cutoff.
    if b == 3 and k <= 4 or b == 4 and k <= 3:
        beyond = [n for n in palindromes_to_length(b, 2*k+3)
                  if len(digits_base(n, b)) > 2*k+1 and is_palindrome(n+b**k, b)]
        assert not beyond, (b, k, beyond)
    return len(direct)


def main():
    checks = [(b, k) for b in range(3, 7) for k in range(1, 5)]
    checks += [(3, 5), (3, 6), (7, 1), (7, 2), (7, 3)]
    pairs = 0
    for b, k in checks:
        count = check(b, k)
        pairs += count
        print(f'base={b} power={k} exact_pairs={count}')
    print(f'CHECKED {len(checks)} base-exponent instances, {pairs} matching ordered palindrome pairs')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
