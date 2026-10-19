"""Exact finite combinatorial verification of three-tap prime cyclic STFT support."""
from itertools import combinations
from collections import Counter, defaultdict


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p**0.5) + 1))


def same_translate(A, B, p):
    return any({(x + t) % p for x in B} == set(A) for t in range(p))


def arithmetic_progression(A, p):
    return any((a + c - 2*b) % p == 0
               for a in A for b in A for c in A if len({a, b, c}) == 3)


def exact_support_signature(A, B, p):
    pairs = defaultdict(list)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            pairs[(a - b) % p].append((i, j))
    assert max(map(len, pairs.values())) <= 2
    rows = []
    for cells in pairs.values():
        if len(cells) == 2:
            (i, j), (k, l) = cells
            assert i != k and j != l
            rows.append((1 << i) ^ (1 << k) ^ (1 << (j + 3)) ^ (1 << (l + 3)))
    rank = {}
    for value in rows:
        v, right = value, 1
        while v:
            pivot = v.bit_length() - 1
            if pivot not in rank:
                rank[pivot] = (v, right)
                break
            base, base_right = rank[pivot]
            v ^= base
            right ^= base_right
        if not v and right:
            return len(rows), 1
    return len(rows), 0


def verify(p):
    assert is_prime(p) and p >= 5
    subsets = tuple(combinations(range(p), 3))
    cases = Counter()
    for A in subsets:
        for B in subsets:
            if same_translate(A, B, p):
                continue
            e, obstruction = exact_support_signature(A, B, p)
            assert (e == 4 and obstruction == 0) if p == 5 else (e <= 3)
            predicted = int(p >= 7 and e == 3
                            and not arithmetic_progression(A, p)
                            and same_translate(A, tuple(-x % p for x in B), p))
            assert obstruction == predicted, (p, A, B, e, obstruction, predicted)
            support_min = p * (9 - e) - e + obstruction
            assert support_min >= (5*p - 4 if p == 5 else 6*p - 3)
            cases[(e, obstruction)] += 1
    nonap = sum(not arithmetic_progression(A, p) for A in subsets)
    expected_bad = 0 if p == 5 else p * nonap
    assert sum(n for (e, obs), n in cases.items() if obs) == expected_bad
    assert sum(cases.values()) == len(subsets) * (len(subsets) - p)
    if p == 5:
        assert cases == {(4, 0): 50}
    if p == 7:
        assert cases == {(3, 0): 588, (2, 0): 294, (3, 1): 98}
    if p == 11:
        assert cases == {(2, 0): 10890, (1, 0): 9680, (3, 0): 2420,
                         (0, 0): 1210, (3, 1): 1210}
    if p == 13:
        assert cases == {(1, 0): 36504, (2, 0): 26364, (0, 0): 8450,
                         (3, 0): 4056, (3, 1): 2704}
    print('p=%d: %s; exceptional=%d' % (p, dict(sorted(cases.items())), expected_bad))




def exact_stft_size_for_signs(p, A, B, signs_a, signs_b):
    # Cyclotomic minimal polynomial of a primitive p-th root is 1+x+...+x^(p-1).
    # An integer polynomial of degree <= p-1 vanishes at that root iff its
    # coefficient vector is constant, a criterion requiring no floating point.
    zeros = 0
    for t in range(p):
        for k in range(p):
            coefficients = [0] * p
            for i, a in enumerate(A):
                for j, b in enumerate(B):
                    if (a - b) % p == t:
                        coefficients[(-k * a) % p] += signs_a[i] * signs_b[j]
            if all(c == coefficients[0] for c in coefficients):
                zeros += 1
    return p*p - zeros


def verify_direct_examples():
    examples = [
        (5, (0, 1, 2), (0, 1, 3), 21),
        (7, (0, 1, 2), (0, 1, 3), 39),
        (7, (0, 1, 3), (0, 4, 6), 40),
        (11, (0, 1, 2), (0, 1, 3), 63),
    ]
    for p, A, B, expected in examples:
        best = p*p + 1
        for u in range(8):
            signs_a = tuple(1 if (u >> i) & 1 == 0 else -1 for i in range(3))
            for v in range(8):
                signs_b = tuple(1 if (v >> i) & 1 == 0 else -1 for i in range(3))
                best = min(best, exact_stft_size_for_signs(p, A, B, signs_a, signs_b))
        assert best == expected, (p, A, B, best, expected)
    print('exact cyclotomic-sign STFT examples passed')

if __name__ == '__main__':
    for prime in (5, 7, 11, 13):
        verify(prime)
    verify_direct_examples()
    print('CHECK_PASS')
