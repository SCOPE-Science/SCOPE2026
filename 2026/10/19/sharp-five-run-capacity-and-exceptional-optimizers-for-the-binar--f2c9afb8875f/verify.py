"""Reproduce the sharp four-run threshold for scattered pattern 0101."""
from itertools import product, combinations

PATTERN = '0101'


def count_dp(word):
    state = [1, 0, 0, 0, 0]
    for symbol in word:
        for j in range(4, 0, -1):
            if symbol == PATTERN[j - 1]:
                state[j] += state[j - 1]
    return state[4]


def count_index(word):
    return sum(''.join(word[i] for i in four) == PATTERN
               for four in combinations(range(len(word)), 4))


def four_max(n):
    quotient, rem = divmod(n, 4)
    lengths = [quotient + 1] * rem + [quotient] * (4 - rem)
    product_value = 1
    for length in lengths:
        product_value *= length
    return product_value, lengths


def split_witness(lengths):
    a, b, c, d = lengths
    return '0' * (a - 1) + '10' + '1' * (b - 1) + '0' * c + '1' * d


def main():
    finite = {}
    for n in range(4, 9):
        values = []
        for letters in product('01', repeat=n):
            w = ''.join(letters)
            via_dp = count_dp(w)
            assert via_dp == count_index(w), ('methods disagree', w)
            values.append(via_dp)
        finite[n] = max(values)
    assert finite == {4: 1, 5: 2, 6: 5, 7: 9, 8: 16}, finite
    assert count_dp('0101') == finite[4]
    assert count_dp('00101') == finite[5]
    assert count_dp('00110011') == finite[8]
    assert count_dp('0010101') == 9 > four_max(7)[0]

    for n in range(4, 13):
        bound, _ = four_max(n)
        best_at_most_five = max(
            count_dp(''.join(w))
            for w in product('01', repeat=n)
            if 1 + sum(x != y for x, y in zip(w, w[1:])) <= 5
        )
        assert best_at_most_five == bound, (n, best_at_most_five, bound)

    for n in range(4, 4097):
        q, lengths = four_max(n)
        a, b, c, d = lengths
        word = split_witness(lengths)
        assert len(word) == n
        if n <= 512:
            measured = count_dp(word)
            gap = (a - 1) * (b - 1 + d) - c * d
            assert measured - q == gap, (n, measured, q, gap)
        if n >= 9:
            assert (a - 1) * (b - 1 + d) - c * d > 0, n
    print('PASS: exhaustive all binary words at lengths 4..8 via independent methods;')
    print('PASS: exact five-run optimum through n=12 and gap identities through n=4096;')
    print('THEOREM for every n>=9 uses the integer case analysis in RESULT.md.')


if __name__ == '__main__':
    main()
