"""Exact integer verification for ternary four-window cyclic-permutation balls.

Run with Python 3.9+ (standard library only): python verify.py
All finite checks are exhaustive over the stated finite sets.
"""
from itertools import product
from collections import Counter, defaultdict

ALPHABET = (0, 1, 2)


def rotate4(word, start, amount):
    t = word[start:start + 4]
    return word[:start] + t[amount:] + t[:amount] + word[start + 4:]


def ball(word):
    result = {word}
    for i in range(len(word) - 3):
        for r in (1, 2, 3):
            result.add(rotate4(word, i, r))
    return result


def incremental_six(six):
    """Contribution of the final four-window in a six-symbol context."""
    assert len(six) == 6
    old = {w + six[-1:] for w in ball(six[:-1])}
    new = {rotate4(six, 2, r) for r in (1, 2, 3)}
    return len(new - old)


def canonical(word):
    names = {}
    out = []
    for x in word:
        if x not in names:
            names[x] = len(names)
        out.append(names[x])
    return tuple(out)


def direct_counts(n):
    histogram = Counter()
    for word in product(ALPHABET, repeat=n):
        histogram[len(ball(word))] += 1
    return histogram


def construct_graph():
    """Alphabet-relabelling quotient of all maximal five-letter centers."""
    valid_five = [w for w in product(ALPHABET, repeat=5)
                  if len(ball(w)) == 7]
    states = sorted({canonical(w) for w in valid_five})
    assert len(states) == 21
    assert all(len(set(s)) in (2, 3) for s in states)
    assert len(valid_five) == 126
    assert all(sum(canonical(w) == s for w in valid_five) == 6 for s in states)

    index = {s: i for i, s in enumerate(states)}
    A = [[0] * len(states) for _ in states]
    for i, state in enumerate(states):
        for a in ALPHABET:
            ext = state + (a,)
            if incremental_six(ext) == 3:
                target = canonical(ext[1:])
                assert target in index
                A[i][index[target]] += 1
    assert all(A[i][j] <= 1 for i in range(len(states))
               for j in range(len(states)))
    assert sum(sum(row) for row in A) == 41
    return states, A


def matmul(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if A[i][k]:
                a = A[i][k]
                for j in range(n):
                    C[i][j] += a * B[k][j]
    return C


def char_det_I_minus_zA(A):
    """Newton identities compute det(I-zA) in exact integer arithmetic."""
    n = len(A)
    I = [[int(i == j) for j in range(n)] for i in range(n)]
    P = I
    traces = [0]
    for k in range(1, n + 1):
        P = matmul(P, A)
        traces.append(sum(P[i][i] for i in range(n)))
    coefficients = [1]
    for k in range(1, n + 1):
        neg = -sum(coefficients[k - j] * traces[j]
                   for j in range(1, k + 1))
        assert neg % k == 0
        coefficients.append(neg // k)
    return coefficients


def rowmul(v, A):
    return [sum(v[i] * A[i][j] for i in range(len(v)))
            for j in range(len(v))]


def reachable(A, s):
    found = {s}
    todo = [s]
    while todo:
        i = todo.pop()
        for j, v in enumerate(A[i]):
            if v and j not in found:
                found.add(j)
                todo.append(j)
    return found


def verify():
    # This is the complete, independently enumerated 4--9 population check.
    maxima = {4: (4, 72), 5: (7, 126), 6: (10, 246),
              7: (13, 474), 8: (16, 930), 9: (19, 1770)}
    for n, expected in maxima.items():
        h = direct_counts(n)
        found = (max(h), h[max(h)])
        assert found == expected, (n, found, expected)
        assert sum(h.values()) == 3 ** n
    print('DIRECT_COUNTS_OK', maxima)

    # Suffix locality can be checked against independent direct full balls.
    # Its all-length validity is established by the changed-support argument.
    for n in (7, 8, 9):
        for w in product(ALPHABET, repeat=n):
            old = {z + w[-1:] for z in ball(w[:-1])}
            new = {rotate4(w, n - 4, r) for r in (1, 2, 3)}
            observed = len(new - old)
            assert observed == incremental_six(w[-6:])
    print('LOCALITY_CHECK_OK: all ternary words of lengths 7, 8, 9')

    states, A = construct_graph()
    assert len(states) == 21
    for s in range(len(states)):
        assert len(reachable(A, s)) == len(states)
    assert A[states.index((0, 1, 2, 0, 1))][states.index((0, 1, 2, 0, 1))] == 1
    print('QUOTIENT_GRAPH_OK: 21 states; 41 edges; primitive')

    target_d = [1, -1, -1, -2, -2, 4, 2, 3, -1, -4, 4] + [0] * 11
    computed_d = char_det_I_minus_zA(A)
    assert computed_d == target_d, computed_d
    print('DETERMINANT_OK', computed_d[:11])

    # The 10th-order operator annihilates the initial row vector exactly.
    # This is stronger than fitting a recurrence to finitely many terms.
    annihilator_ascending = [4, -4, -1, 3, 2, 4, -2, -2, -1, -1, 1]
    v = [6] * len(states)
    annih = [0] * len(states)
    counts = []
    for j in range(35):
        if j < 11:
            annih = [annih[k] + annihilator_ascending[j] * v[k]
                     for k in range(len(states))]
        counts.append(sum(v))
        v = rowmul(v, A)
    assert all(x == 0 for x in annih), annih
    print('ANNIHILATOR_OK: exact row-vector identity')

    num = [126, 120, 102, -42, -378, -192, -156, 120, 168, -288]
    for k in range(len(counts)):
        convolution = sum(target_d[j] * counts[k - j]
                          for j in range(min(k, 10) + 1))
        assert convolution == (num[k] if k < 10 else 0), (k, convolution)
    print('GENERATING_FUNCTION_OK: numerator', num)
    print('FIRST_COUNTS', counts[:15])

    period = tuple(int(c) for c in '000121')
    assert all(incremental_six(tuple((period * 2)[j:j + 6])) == 3
               for j in range(6))
    seed = period * 8
    for n in range(4, 41):
        assert len(ball(seed[:n])) == 3 * n - 8
    print('PERIODIC_WITNESS_OK: first forty lengths')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()
