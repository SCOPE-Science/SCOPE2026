"""Self-contained finite verification for optimal attractors of three-run binary words."""
from itertools import product
from math import comb


def factor_coverage_masks(word):
    result = {}
    for i in range(len(word)):
        mask = 0
        for j in range(i, len(word)):
            mask |= 1 << j
            factor = word[i:j + 1]
            result[factor] = result.get(factor, 0) | mask
    return tuple(result.values())


def brute_pairs(a, b, c):
    word = '0' * a + '1' * b + '0' * c
    masks = factor_coverage_masks(word)
    return {(i + 1, j + 1) for i in range(len(word)) for j in range(i + 1, len(word))
            if all(mask & ((1 << i) | (1 << j)) for mask in masks)}


def theorem_pairs(a, b, c):
    if b == 1:
        zero_positions = []
        if a >= c:
            zero_positions.extend(range(1, a + 1))
        if c >= a:
            zero_positions.extend(range(a + b + 1, a + b + c + 1))
        return {tuple(sorted((a + 1, z))) for z in zero_positions}
    result = set()
    if a >= c:
        result.add((a, a + b))
    if c >= a:
        result.add((a + 1, a + b + 1))
    return result


def count_formula(a, b, c):
    if b == 1:
        return max(a, c) + (a if a == c else 0)
    return 1 + (a == c)


def polynomial_mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def rational_coefficients(N):
    denominator = polynomial_mul(polynomial_mul([1,-1], [1,-1]),
                   polynomial_mul([1,-1], polynomial_mul([1,1], [1,1])))
    numerator = [0,0,0,2,4,4]
    ans = [0] * (N + 1)
    for n in range(N + 1):
        ans[n] = (numerator[n] if n < len(numerator) else 0) - sum(
            denominator[j] * ans[n-j] for j in range(1, min(n, len(denominator)-1)+1))
    return ans


def main():
    tested = 0
    for a,b,c in product(range(1,15), repeat=3):
        expected = theorem_pairs(a,b,c)
        actual = brute_pairs(a,b,c)
        assert actual == expected, (a,b,c, actual,expected)
        assert len(expected) == count_formula(a,b,c)
        assert not any(all(m & (1 << i) for m in factor_coverage_masks('0'*a+'1'*b+'0'*c))
                       for i in range(a+b+c))
        tested += 1

    coefficients = rational_coefficients(40)
    for n in range(3,41):
        aggregate = sum(count_formula(a,b,n-a-b) for a in range(1,n-1)
                        for b in range(1,n-a))
        assert aggregate == coefficients[n], (n,aggregate,coefficients[n])
        unique = sum(count_formula(a,b,n-a-b) == 1 for a in range(1,n-1)
                     for b in range(1,n-a))
        assert unique == comb(n-1,2) - (n-2) - (n-2)//2
    print(f'VERIFY_OK exhaustive_triplets={tested} maximum_single_run=14 enumerator_coefficients=38 unique_counts=38')

if __name__ == '__main__':
    main()
