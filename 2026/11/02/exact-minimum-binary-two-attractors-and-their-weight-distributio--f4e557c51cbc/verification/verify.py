"""Independent exhaustive check for the minimum binary 2-attractor classification.

Run: python3 verify.py
Only Python's standard library is required.
"""
from collections import Counter
from itertools import combinations, product


def minimum_two_attractor(word):
    """Cover the actual distinct length-1/2 factors using selected positions."""
    n = len(word)
    distinct = {word[i:i+width] for width in (1, 2)
                for i in range(n-width+1)}
    labels = sorted(distinct)
    index = {factor: bit for bit, factor in enumerate(labels)}
    target = (1 << len(labels)) - 1
    by_position = [0] * n
    for width in (1, 2):
        for start in range(n-width+1):
            factor = word[start:start+width]
            bit = 1 << index[factor]
            for pos in range(start,start+width):
                by_position[pos] |= bit
    if len(set(word)) == 1:
        assert any(mask == target for mask in by_position)
        return 1
    # Two letters require at least two distinct selected positions.
    for a, b in combinations(range(n), 2):
        if (by_position[a] | by_position[b]) == target:
            return 2
    for selected in combinations(range(n), 3):
        if (by_position[selected[0]] | by_position[selected[1]] |
                by_position[selected[2]]) == target:
            return 3
    raise AssertionError('minimum > 3')


def predicted(word):
    if len(set(word)) == 1:
        return 1
    n = len(word)
    for a in range(2, n + 1):
        for b in range(1, (n - a)//2 + 1):
            c = n - a - 2*b
            if c < 2:
                continue
            x = '0'*a + '10'*b + '1'*c
            y = '1'*a + '01'*b + '0'*c
            if word == x or word == y:
                return 3
    return 2


def weight_count(n, t):
    return 2 * max(0, min(t-2, n-t-2))


def closed_total(n):
    return sum(weight_count(n, t) for t in range(n+1))


def main():
    checked = 0
    for n in range(1, 16):
        tally = Counter()
        by_weight = Counter()
        for digits in product('01', repeat=n):
            word = ''.join(digits)
            obtained = minimum_two_attractor(word)
            forecast = predicted(word)
            assert obtained == forecast, (word, obtained, forecast)
            tally[obtained] += 1
            if obtained == 3:
                by_weight[word.count('1')] += 1
            checked += 1
        assert tally[1] == 2
        assert tally[3] == closed_total(n)
        assert tally[2] == 2**n - 2 - closed_total(n)
        for t in range(n+1):
            assert by_weight[t] == weight_count(n, t), (n, t)
        print(f'n={n:2d}: 1:{tally[1]}, 2:{tally[2]}, 3:{tally[3]}')
    # An independently evaluated coefficient formula from the rational OGF.
    for n in range(1, 300):
        direct_coeff = 2 * sum(n-2*b-3 for b in range(1, (n-4)//2 + 1)) if n >= 6 else 0
        assert direct_coeff == closed_total(n), n
    print(f'VERIFY_OK exhaustive_words={checked} coefficients_through_n=299')

if __name__ == '__main__':
    main()
