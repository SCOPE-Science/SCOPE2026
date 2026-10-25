#!/usr/bin/env python3
"""Independent finite checks of the modulo-five Fibonacci state-cycle theorem."""
from collections import Counter

Q = ((0, 1), (1, 1))
I = ((1, 0), (0, 1))


def multiply(A, B, modulus):
    return tuple(tuple(sum(A[i][t] * B[t][j] for t in (0, 1)) % modulus
                       for j in (0, 1)) for i in (0, 1))


def power(A, exponent, modulus):
    R, B = I, A
    while exponent:
        if exponent & 1:
            R = multiply(R, B, modulus)
        B = multiply(B, B, modulus)
        exponent >>= 1
    return R


def fixed_count(A, modulus):
    return sum(1 for a in range(modulus) for b in range(modulus)
               if ((A[0][0] - 1) * a + A[0][1] * b) % modulus == 0
               and (A[1][0] * a + (A[1][1] - 1) * b) % modulus == 0)


def expected_histogram(k):
    result = {1: 1, 4: 1}
    for j in range(1, k):
        result[4 * 5**j] = 6 * 5**(j-1)
    result[4 * 5**k] = 5**(k-1)
    return result


def orbit_histogram(modulus):
    marked = bytearray(modulus * modulus)
    counts = Counter()
    for a in range(modulus):
        for b in range(modulus):
            start = a * modulus + b
            if marked[start]:
                continue
            u, v = a, b
            length = 0
            while True:
                at = u * modulus + v
                if marked[at]:
                    if at != start:
                        raise AssertionError('A cycle did not return to its start')
                    break
                marked[at] = 1
                length += 1
                u, v = v, (u + v) % modulus
            counts[length] += 1
    return dict(counts)


def run():
    # Integral base identities for Q^4-I and (Q^20-I)/5.
    assert power(Q, 4, 100000) == ((2, 3), (3, 5))
    B = ((1, 3), (3, 4))
    BB = multiply(B, B, 100000)
    assert BB == ((10, 15), (15, 25))
    assert BB == tuple(tuple(5*(B[i][j]+I[i][j]) for j in (0, 1)) for i in (0, 1))
    Q20 = power(Q, 20, 100000)
    assert Q20 == ((4181, 6765), (6765, 10946))
    C1 = tuple(tuple((Q20[i][j]-I[i][j])//5 for j in (0, 1)) for i in (0, 1))
    assert C1 == ((836, 1353), (1353, 2189))
    assert C1[0][0] * C1[1][1] - C1[0][1] * C1[1][0] == -605
    matrix_checks = 0
    for j in range(0, 9):
        modulus = 5 ** (j+3)
        P = power(Q, 4 * 5**j, modulus)
        D = tuple(tuple((P[i][t]-I[i][t]) % modulus for t in (0, 1)) for i in (0, 1))
        assert all(entry % (5**j) == 0 for row in D for entry in row)
        C = tuple(tuple((D[i][t] // (5**j)) % 25 for t in (0, 1)) for i in (0, 1))
        if j >= 1:
            assert C == tuple(tuple(x % 25 for x in row) for row in C1)
        else:
            assert C == tuple(tuple(x % 25 for x in row) for row in B)
        determinant = D[0][0] * D[1][1] - D[0][1] * D[1][0]
        assert determinant % (5 ** (2*j+1)) == 0
        assert determinant % (5 ** (2*j+2)) != 0
        assert any(x % (5**(j+1)) for row in D for x in row)
        matrix_checks += 1

    state_checks = 0
    fixed_checks = 0
    for k in range(1, 5):
        modulus = 5**k
        hist = orbit_histogram(modulus)
        assert hist == expected_histogram(k), (k, hist, expected_histogram(k))
        assert sum(length*count for length, count in hist.items()) == modulus**2
        assert sum(hist.values()) == (modulus+1)//2
        state_checks += modulus**2
        for j in range(0, k+1):
            A = power(Q, 4 * 5**j, modulus)
            actual = fixed_count(A, modulus)
            expected = 5 ** (min(j, k) + min(j+1, k))
            assert actual == expected, (k,j,actual,expected)
            fixed_checks += 1
    print(f'VERIFY_OK: {state_checks} enumerated states; {fixed_checks} fixed-point checks; {matrix_checks} lift checks')


if __name__ == '__main__':
    run()
