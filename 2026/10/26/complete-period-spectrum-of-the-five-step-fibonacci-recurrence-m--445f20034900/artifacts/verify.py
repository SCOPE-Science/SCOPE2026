"""Independent integer checks for the five-step recurrence cycle theorem.
Runs with Python 3 standard library and no input files.
"""
from collections import Counter
from itertools import combinations
from math import gcd

D = 5
T = [[0] * D for _ in range(D)]
for i in range(D - 1):
    T[i][i + 1] = 1
T[-1] = [1] * D
I = [[int(i == j) for j in range(D)] for i in range(D)]


def multiply(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(D))
             for j in range(D)] for i in range(D)]


def power(n):
    acc = [row[:] for row in I]
    cur = [row[:] for row in T]
    while n:
        if n & 1:
            acc = multiply(acc, cur)
        cur = multiply(cur, cur)
        n >>= 1
    return acc


def difference(n, divisor=1):
    W = power(n)
    assert all((W[i][j] - I[i][j]) % divisor == 0 for i in range(D) for j in range(D))
    return [[(W[i][j] - I[i][j]) // divisor for j in range(D)] for i in range(D)]


def determinant(M):
    # Exact Bareiss elimination with row pivots.
    A = [row[:] for row in M]
    n = len(A)
    if n == 0:
        return 1
    denom = 1
    sign = 1
    for k in range(n - 1):
        p = next((i for i in range(k, n) if A[i][k]), None)
        if p is None:
            return 0
        if p != k:
            A[p], A[k] = A[k], A[p]
            sign *= -1
        piv = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = A[i][j] * piv - A[i][k] * A[k][j]
                assert num % denom == 0
                A[i][j] = num // denom
            A[i][k] = 0
        denom = piv
    return sign * A[-1][-1]


def smith_v2(A):
    gvals = []
    for d in range(1, D + 1):
        g = 0
        for rows in combinations(range(D), d):
            for cols in combinations(range(D), d):
                g = gcd(g, determinant([[A[i][j] for j in cols] for i in rows]))
        assert g
        v = (g & -g).bit_length() - 1
        gvals.append(v)
    return [gvals[0]] + [gvals[i] - gvals[i - 1] for i in range(1, D)]


def A(j, k):
    return 2 ** min(k, j + 2)


def B(j, k):
    if j == 0:
        return 2 ** (2 * min(k, 1) + min(k, 2))
    return 2 ** (4 * min(k, j) + min(k, j + 2))


def predicted(k):
    found = {1: A(0, k)}
    assert (B(0, k) - A(0, k)) % 3 == 0
    found[3] = (B(0, k) - A(0, k)) // 3
    for j in range(1, k + 1):
        pure = A(j, k) - A(j - 1, k)
        mix = B(j, k) - B(j - 1, k) - pure
        assert pure % (2**j) == 0
        assert mix % (3 * 2**j) == 0
        if pure:
            found[2**j] = pure // (2**j)
        if mix:
            found[3 * 2**j] = mix // (3 * 2**j)
    assert sum(length * count for length, count in found.items()) == 2**(5 * k)
    return found


def directly_count(k):
    n = 2**k
    space = n**D
    seen = bytearray(space)
    cycles = Counter()
    def next_state(x):
        parts = []
        y = x
        for _ in range(D):
            parts.append(y % n)
            y //= n
        return x // n + (sum(parts) % n) * n**(D - 1)
    for x in range(space):
        if seen[x]:
            continue
        first = x
        y = x
        length = 0
        while True:
            assert not seen[y]  # All states lie on genuine disjoint cycles.
            seen[y] = 1
            length += 1
            y = next_state(y)
            if y == first:
                break
        cycles[length] += 1
    return dict(cycles)


def main():
    assert smith_v2(difference(1)) == [0, 0, 0, 0, 2]
    assert smith_v2(difference(3)) == [0, 0, 1, 1, 2]
    assert smith_v2(difference(6, 2)) == [0, 0, 0, 0, 2]
    assert smith_v2(difference(12, 4)) == [0, 0, 0, 0, 2]
    for k in range(1, 4):
        got = directly_count(k)
        target = predicted(k)
        assert got == target, (k, got, target)
    expected = (8, 96, 1468, 23400, 374292)
    for k, count in enumerate(expected, 1):
        assert sum(predicted(k).values()) == count
    for k in range(2, 12):
        assert sum(predicted(k).values()) == (257 * 16**k + 960*k + 1408) // 720
    print('VERIFY_OK: four exact 5x5 Smith-gcd certificates; complete cycle enumerations k=1,2,3; eleven symbolic-level distributions; OEIS first five orbit totals')

if __name__ == '__main__':
    main()
