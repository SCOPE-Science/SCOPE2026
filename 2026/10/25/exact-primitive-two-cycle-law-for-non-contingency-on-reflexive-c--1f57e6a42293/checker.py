"""Exact, dependency-free verification of the non-contingency two-cycle formula.
Run: python3 checker.py
"""
from itertools import product


def local(a, b, c):
    return int(a == b == c)


def double_local(a, b, c, d, e):
    return int(c == local(local(a, b, c), local(b, c, d), local(c, d, e)))


states = list(product((0, 1), repeat=4))
position = {state: i for i, state in enumerate(states)}
N = len(states)
M = [[0] * N for _ in range(N)]
for i, (a, b, c, d) in enumerate(states):
    for e in (0, 1):
        if double_local(a, b, c, d, e):
            M[i][position[(b, c, d, e)]] += 1


def multiply(A, B):
    size = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(size))
             for j in range(size)] for i in range(size)]


def polynomial_multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            out[i + j] += u * v
    return out


# Newton identities reconstruct det(lambda I-M) solely from exact traces.
P = [[int(i == j) for j in range(N)] for i in range(N)]
traces = [0]
for k in range(1, N + 1):
    P = multiply(P, M)
    traces.append(sum(P[i][i] for i in range(N)))
coefficients = [1]
for k in range(1, N + 1):
    numerator = -sum(coefficients[k-i] * traces[i] for i in range(1, k+1))
    assert numerator % k == 0
    coefficients.append(numerator // k)
expected_ascending = polynomial_multiply(
    polynomial_multiply([0] * 9 + [1], [-1, 1]),
    polynomial_multiply([-1, -1, 0, 1], [1, 1, 0, 1])
)
assert coefficients == expected_ascending[::-1], (coefficients, expected_ascending)


def update(mask, n):
    result = 0
    for i in range(n):
        bits = ((mask >> ((i-1) % n)) & 1,
                (mask >> i) & 1,
                (mask >> ((i+1) % n)) & 1)
        result |= local(*bits) << i
    return result


# Independent global enumeration, no transfer-matrix use here.
known = {3: 0, 4: 2, 5: 5, 6: 3, 7: 0, 8: 2, 9: 9, 10: 15,
         11: 11, 12: 5, 13: 13, 14: 35}
sequence = [0] * 15
for n in range(3, 15):
    fixed_first = fixed_second = 0
    for mask in range(1 << n):
        successor = update(mask, n)
        fixed_first += successor == mask
        fixed_second += update(successor, n) == mask
    assert fixed_first == 1, (n, fixed_first)
    assert (fixed_second - fixed_first) % 2 == 0
    sequence[n] = (fixed_second - 1) // 2
    assert sequence[n] == known[n], (n, sequence[n], known[n])
    if n >= 7:
        assert sequence[n] == sequence[n-4] + 2 * sequence[n-5] + sequence[n-6]
    assert traces[n] == fixed_second if n <= N else True

# Independent trace recurrence from characteristic factors for sizes >= 17.
for n in range(17, 101):
    predicted = traces[n-4] + 2 * traces[n-5] + traces[n-6] - 3
    traces.append(predicted)
    assert (predicted - 1) % 2 == 0
    c = (predicted - 1) // 2
    if n < 23:
        assert c > 0

print('ALL_CHECKS_OK; characteristic polynomial, 12 full ring enumerations, recurrence validated')
