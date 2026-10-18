"""Independently enumerate binary and quaternary palindrome-race signs."""
from collections import Counter


def is_palindrome(n, base):
    digits = []
    while n:
        n, digit = divmod(n, base)
        digits.append(digit)
    return digits == digits[::-1]


def expected_by_region(h):
    B, q = 4**h, 2**h
    return [
        ((B*B-4*B)//8, (B*B+4*B)//8, 3*B*B//4),
        (1, 2*B*B-B-2, B+1),
        (0, 4*B*B-2*B+1, 2*B-1),
        ((8*B*B+7*B-q)//14, (8*B*B-7*B-q)//14, (48*B*B+q)//7),
    ]


def expected_total(h):
    B, q = 4**h, 2**h
    numerators = (39*B*B+56-4*q, 375*B*B-168*B-56-4*q,
                  213*B*B+84*B+4*q)
    assert numerators[0] % 56 == numerators[1] % 56 == 0
    assert numerators[2] % 28 == 0
    return numerators[0]//56, numerators[1]//56, numerators[2]//28


def main():
    for h in range(1, 5):
        X = 16**h
        a2 = sum(is_palindrome(n, 2) for n in range(1, X))
        a4 = sum(is_palindrome(n, 4) for n in range(1, X))
        observed_regions = []
        for ra, rb in ((1, 2), (2, 4), (4, 8), (8, 16)):
            signs = Counter()
            for n in range(ra*X, rb*X):
                a2 += is_palindrome(n, 2)
                a4 += is_palindrome(n, 4)
                signs[(a2 > a4) - (a2 < a4)] += 1
            observed_regions.append(tuple(signs[v] for v in (1, -1, 0)))
        assert observed_regions == expected_by_region(h), (h, observed_regions)
        counts = tuple(sum(region[j] for region in observed_regions)
                       for j in range(3))
        assert counts == expected_total(h), (h, counts)
        print('h', h, 'positive negative tied:', counts)
    print('ALL_EXACT_CHECKS_PASS')


if __name__ == '__main__':
    main()
