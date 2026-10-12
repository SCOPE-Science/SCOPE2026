"""Finite corroboration for dyadic abelian complexity of the Baum–Sweet word.

The mathematical proof is symbolic; this executable does not certify infinite cases.
Run with Python 3.9 or later: python verify.py
"""

SUBSTITUTION = {'A': 'AB', 'B': 'CB', 'C': 'BD', 'D': 'DD'}
CODING = {'A': 1, 'B': 1, 'C': 0, 'D': 0}


def baum_sweet_by_digits(n):
    assert n >= 0
    if n == 0:
        return 1
    return int(all(len(run) % 2 == 0 for run in bin(n)[2:].split('1')))


def morphic_states(level):
    states = 'A'
    for _ in range(level):
        states = ''.join(SUBSTITUTION[s] for s in states)
    return states


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def coded_block(letter, level):
    symbols = letter
    for _ in range(level):
        symbols = ''.join(SUBSTITUTION[s] for s in symbols)
    return [CODING[s] for s in symbols]


def verify():
    max_level = 16
    states = morphic_states(max_level + 1)
    word = [CODING[s] for s in states]
    assert len(word) == (1 << (max_level + 1))
    for n, actual in enumerate(word):
        assert actual == baum_sweet_by_digits(n), ('binary digit mismatch', n)

    symbolic_blocks = 0
    for k in range(max_level + 1):
        a, b, c, d = [coded_block(s, k) for s in ('A', 'B', 'C', 'D')]
        assert all(x + y == z for x, y, z in zip(b, c, a))
        assert not any(d)
        assert sum(a) == fibonacci(k + 2)
        symbolic_blocks += 1

    # Compare all possible starts within the finite independently digit-checked
    # prefix, not only block-aligned starts.
    window_cases = 0
    full_spectrum_levels = 0
    L = len(word)
    for k in range(max_level + 1):
        window_length = 1 << k
        weight = sum(word[:window_length])
        max_weight = weight
        seen = {weight}
        for start in range(1, L - window_length + 1):
            weight += word[start + window_length - 1] - word[start - 1]
            max_weight = max(max_weight, weight)
            if k <= 12:
                seen.add(weight)
            window_cases += 1
        expected = fibonacci(k + 2)
        assert max_weight == expected, ('window maximum mismatch', k, max_weight, expected)
        if k <= 12:
            assert seen == set(range(expected + 1)), ('Parikh spectrum mismatch', k)
            full_spectrum_levels += 1
    print('VERIFY_OK digit_positions={} substitution_levels={} dyadic_window_cases={} full_parikh_levels={} last_maximum={}'.format(
        L, symbolic_blocks, window_cases, full_spectrum_levels, fibonacci(max_level + 2)))


if __name__ == '__main__':
    verify()
