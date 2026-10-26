"""Finite checks for the golden-integer first-order limit spectrum."""
from itertools import product
from math import sqrt

PHI = (1 + sqrt(5)) / 2


def words(n):
    return [''.join(b) for b in product('01', repeat=n) if '11' not in ''.join(b)]


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def scale_pair(m, n, k):
    """Return integer a,b satisfying (m+n*phi)*phi**(k+1)=a*phi+b."""
    a, b = m + n, n
    for _ in range(k):
        a, b = a + b, a
    return a, b


checks = 0
for size in range(1, 14):
    ensemble = words(size)
    assert len(ensemble) == fibonacci(size + 2)
    checks += 1
    for k in range(1, min(size, 6) + 1):
        for s in words(k):
            actual = sum(w.startswith(s) for w in ensemble)
            expected = fibonacci(size-k+2) if s[-1] == '0' else fibonacci(size-k+1)
            assert actual == expected, (size, k, s, actual, expected)
            checks += 1
    for left in words(min(size // 2, 3)) if size >= 2 else []:
        for right in words(min(size // 2, 3)):
            if len(left) + len(right) > size:
                continue
            actual = sum(w.startswith(left) and w.endswith(right) for w in ensemble)
            # Bridge count from last state of left to first state of right.
            gap = size - len(left) - len(right) + 1
            transition = ((1, 1), (1, 0))
            matrix = [[1, 0], [0, 1]]
            for _ in range(gap):
                matrix = [[sum(matrix[i][j] * transition[j][k] for j in range(2)) for k in range(2)] for i in range(2)]
            expected = matrix[int(left[-1])][int(right[0])]
            assert actual == expected, (size, left, right, actual, expected)
            checks += 1

representations = 0
for m in range(-16, 17):
    for n in range(-16, 17):
        alpha = m + n * PHI
        if 1e-9 < alpha < 1 - 1e-9:
            k = next((k for k in range(1, 60) if 0 <= scale_pair(m,n,k)[0] <= fibonacci(k+1) and 0 <= scale_pair(m,n,k)[1] <= fibonacci(k)), None)
            assert k is not None, (m, n, alpha)
            a, b = scale_pair(m,n,k)
            assert abs(a*PHI**(-k) + b*PHI**(-k-1) - alpha) < 1e-7
            representations += 1

print('GOLDEN_FO_EXACT_OK', checks, representations)
