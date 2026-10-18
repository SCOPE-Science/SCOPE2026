"""Independent finite checks for the generalized Cantor factor-spectrum theorem.

Run with Python 3: python verify.py
Finite tests illustrate, but do not replace, the all-parameter proof.
"""


def substitution_prefix(base, depth):
    word = '1'
    for _ in range(depth):
        word = ''.join(('1' + '0' * (base - 2) + '1') if x == '1'
                       else '0' * base for x in word)
    return word


def digit_prefix(base, length):
    """Independent digit representation: all base-q digits are 0 or q-1."""
    ans = []
    for n in range(length):
        a = n
        good = True
        while a:
            if a % base not in (0, base - 1):
                good = False
                break
            a //= base
        ans.append('1' if good else '0')
    return ''.join(ans)


def predicted_factors(base, W):
    L = len(W)
    family = {'0' * (2 * L)}
    family.update('0' * j + W + '0' * (L - j) for j in range(L + 1))
    family.update(W[r:] + '0' * (L + r) for r in range(1, L))
    family.update('0' * (2 * L - r) + W[:r] for r in range(1, L))
    if base == 3:
        family.update(W[r:] + '0' * L + W[:r] for r in range(1, L))
    return family


def run():
    cases = 0
    for base in range(3, 9):
        for depth in range(4):
            L = base ** depth
            block = substitution_prefix(base, depth)
            source = substitution_prefix(base, max(depth + 3, 5))
            assert source == digit_prefix(base, len(source))
            factors_L = {source[i:i+L] for i in range(len(source) - L + 1)}
            factors_2L = {source[i:i+2*L] for i in range(len(source) - 2*L + 1)}
            predicted = predicted_factors(base, block)
            assert factors_2L == predicted, (base, depth, 'factor spectrum')
            assert len(predicted) == (4 * L - 1 if base == 3 else 3 * L)
            maximum_L = max(w.count('1') for w in factors_L)
            maximum_2L = max(w.count('1') for w in factors_2L)
            assert (maximum_L, maximum_2L) == (2 ** depth, 2 ** depth)
            assert {w for w in factors_L if w.count('1') == maximum_L} == {block}
            extrema = {w for w in factors_2L if w.count('1') == maximum_2L}
            expected = {'0' * j + block + '0' * (L-j) for j in range(L + 1)}
            if base == 3:
                expected.update(block[r:] + '0' * L + block[:r] for r in range(1, L))
            assert extrema == expected, (base, depth, 'extremal class')
            assert len(extrema) == (2 * L if base == 3 else L + 1)
            cases += 1
    print(f'VERIFY_OK cases={cases}; substitutions and digit formula agree; '
          f'exact factors, maxima, and all extremizers agree')


if __name__ == '__main__':
    run()
