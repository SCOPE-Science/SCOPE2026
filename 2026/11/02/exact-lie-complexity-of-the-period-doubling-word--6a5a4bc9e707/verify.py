#!/usr/bin/env python3
"""Finite independent checks for a period-doubling conjugacy-class formula.

The proof in RESULT.md is valid for all positive lengths. This executable
checks finite prefix computations and is not used to infer infinite cases.
"""


def substitution_prefix(level):
    w = '0'
    for _ in range(level):
        w = ''.join('01' if a == '0' else '00' for a in w)
    return w


def arithmetic_prefix(length):
    def parity_of_v2(k):
        j = 0
        while k % 2 == 0:
            k //= 2
            j += 1
        return str(j % 2)
    return ''.join(parity_of_v2(i + 1) for i in range(length))


def necklace_root(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def accepted_classes(factors, n):
    result = set()
    for w in factors:
        if w in result:
            continue
        if all(w[i:] + w[:i] in factors for i in range(n)):
            result.add(necklace_root(w))
    return result


def predicted(n):
    while n % 2 == 0:
        n //= 2
    return 2 if n in (1, 3) else 0


def run():
    long_word = substitution_prefix(17)
    shorter_word = substitution_prefix(15)
    assert len(long_word) == 131072
    assert long_word == arithmetic_prefix(len(long_word))
    assert '11' not in long_word and '0000' not in long_word
    for n in range(1, 121):
        factors = {long_word[i:i+n] for i in range(len(long_word)-n+1)}
        short_factors = {shorter_word[i:i+n] for i in range(len(shorter_word)-n+1)}
        assert factors == short_factors, ('prefix stability', n)
        accepted = accepted_classes(factors, n)
        assert len(accepted) == predicted(n), ('exact class count', n, accepted)
        if n >= 4 and n % 2 == 0:
            # Class-by-class desubstitution, independently of just counts.
            shorter = {long_word[i:i+n//2] for i in range(len(long_word)-n//2+1)}
            decoded = {necklace_root(''.join('01' if c == '0' else '00' for c in v))
                       for v in accepted_classes(shorter, n//2)}
            assert decoded == accepted, ('class identity', n)
    for n in range(1, 14):
        factors = {long_word[i:i+n] for i in range(len(long_word)-n+1)}
        candidates = set()
        for mask in range(1 << n):
            w = format(mask, f'0{n}b')
            if all(w[i:] + w[:i] in factors for i in range(n)):
                candidates.add(necklace_root(w))
        assert candidates == accepted_classes(factors, n), ('brute classes', n)
    print('VERIFY_OK: independent 2-adic construction, 120 exact factor lengths, '
          'class-level desubstitution, 13 complete binary necklace censuses')


if __name__ == '__main__':
    run()
