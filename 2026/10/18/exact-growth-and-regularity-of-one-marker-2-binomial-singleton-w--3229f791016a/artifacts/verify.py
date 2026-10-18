"""Independent finite and formal-series checks for one-marker 2-binomial singleton theorem."""
from collections import Counter
from itertools import product
from math import comb

# Two independent routes: direct ternary signature enumeration and exact
# integer generating-function coefficient arithmetic.

def signature(word):
    counts = [0, 0, 0]
    pairs = [[0] * 3 for _ in range(3)]
    for symbol in word:
        for previous_symbol in range(3):
            pairs[previous_symbol][symbol] += counts[previous_symbol]
        counts[symbol] += 1
    return tuple(counts) + tuple(pairs[x][y] for x in range(3) for y in range(3))

def direct_singletons(length):
    frequencies = Counter()
    for marker_position in range(length):
        for binary_part in product((0, 1), repeat=length - 1):
            word = binary_part[:marker_position] + (2,) + binary_part[marker_position:]
            frequencies[signature(word)] += 1
    return sum(frequency == 1 for frequency in frequencies.values())

def rational_coefficient(length):
    # z*(1+2*z^2+4*z^3+3*z^4-4*z^5-4*z^6)/(1-z)^4.
    numerator = {1: 1, 3: 2, 4: 4, 5: 3, 6: -4, 7: -4}
    return sum(c * comb(length - degree + 3, 3)
               for degree, c in numerator.items() if length >= degree)

def composition_singletons(a, b, c, d):
    A, B = a*b, c*d
    if A and B:
        return 2
    if not (A or B):
        return 1
    x, y = (a, b) if A else (c, d)
    return x*y + 1 if min(x, y) == 1 else 4

def composition_sum(length):
    total = 0
    for a in range(length):
        for b in range(length - a):
            for c in range(length - a - b):
                d = length - 1 - a - b - c
                total += composition_singletons(a, b, c, d)
    return total

def check_formal_series(limit=200):
    # Compare coefficient convolution z*(A*A+2*A*T+2*B*B)
    # against the claimed rational expression, using arithmetic only.
    A = [1] + [2]*limit  # (1+z)/(1-z)
    B = [0, 0] + [k-1 for k in range(2, limit+1)]  # z^2/(1-z)^2
    # T = 2 z^2(1+z+z^2)/(1-z)^2, built separately below.
    T = [0]*(limit+1)
    for k in range(2, limit+1):
        T[k] = 2 * sum(k-j+1 for j in (2, 3, 4) if j <= k)
    def conv(x, y, i):
        return sum(x[j]*y[i-j] for j in range(i+1))
    for n in range(1, limit+1):
        target = conv(A, A, n-1) + 2*conv(A, T, n-1) + 2*conv(B, B, n-1)
        assert target == rational_coefficient(n), (n, target, rational_coefficient(n))
        if n >= 7:
            assert 3*target == n**3 + 27*n*n - 178*n + 312

if __name__ == '__main__':
    check_formal_series(200)
    expected = [1, 4, 12, 32, 74, 144, 244, 376, 542, 744, 984, 1264]
    for n, e in enumerate(expected, 1):
        actual = direct_singletons(n)
        assert actual == e, (n, actual, e)
        assert actual == composition_sum(n)
        assert actual == rational_coefficient(n)
    print('ALL_CHECKS_PASS', 'direct_lengths=1..12', 'formal_series=1..200')
