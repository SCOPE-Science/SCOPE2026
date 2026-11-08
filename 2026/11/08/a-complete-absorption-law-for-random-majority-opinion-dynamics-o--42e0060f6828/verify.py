"""Independent exact finite-state checks of the book-network absorption theorem.

Run with Python 3.9 or newer: python verify.py
Uses only the Python standard library. These finite checks supplement the proof.
"""
from fractions import Fraction
from itertools import product
from math import comb


def solve(matrix, rhs):
    """Gauss-Jordan elimination for rational matrix and multiple right sides."""
    n = len(matrix)
    k = len(rhs[0])
    a = [[Fraction(x) for x in row] + [Fraction(x) for x in b]
         for row, b in zip(matrix, rhs)]
    for col in range(n):
        pivot = next(i for i in range(col, n) if a[i][col] != 0)
        a[col], a[pivot] = a[pivot], a[col]
        v = a[col][col]
        a[col] = [x / v for x in a[col]]
        for i in range(n):
            if i == col:
                continue
            mult = a[i][col]
            if mult:
                a[i] = [x - mult*y for x, y in zip(a[i], a[col])]
    return [row[n:n+k] for row in a]


def transition(m, u, v, x):
    r = m//2
    up = int(x+v >= r+1)
    vp = int(x+u >= r+1)
    if u == v:
        return {(up, vp, m*u): Fraction(1)}
    return {(up, vp, y): Fraction(comb(m, y), 2**m)
            for y in range(m+1)}


def claimed(m, u, v, x):
    r = m//2
    c = Fraction(comb(m, r), 2**m)
    delta = Fraction(2, 2**m)
    q = (1+c)/2
    if u == v:
        if u == 0:
            cls = 0 if x <= r else 2
        else:
            cls = 1 if x >= r else 2
        probabilities = [Fraction(int(cls == i)) for i in range(3)]
        is_terminal = x in (0, m)
        expected = Fraction(0 if is_terminal else 1)
        second_moment = expected
        return probabilities, expected, second_moment
    if x < r:
        probs = [q, Fraction(0), 1-q]
    elif x > r:
        probs = [Fraction(0), q, 1-q]
    else:
        probs = [q/2, q/2, 1-q]
    h_mean = 2-delta
    h_second = 4-3*delta
    if x != r:
        return probs, h_mean, h_second
    p = 1-c
    g_mean = 1/p
    g_second = (1+c)/(p*p)
    return probs, g_mean + h_mean, g_second + 2*g_mean*h_mean + h_second


def test(m):
    assert m >= 2 and m % 2 == 0
    states = list(product((0, 1), (0, 1), range(m+1)))
    terminals = {(0, 0, 0): 0, (1, 1, m): 1,
                 (0, 0, m): 2, (1, 1, 0): 2}
    nonterm = [s for s in states if s not in terminals]
    idx = {s: i for i, s in enumerate(nonterm)}
    n = len(nonterm)
    mat = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    rhs = [[Fraction(0) for _ in range(4)] for _ in range(n)]
    for i, state in enumerate(nonterm):
        tr = transition(m, *state)
        assert sum(tr.values()) == 1
        for nxt, probability in tr.items():
            if nxt in terminals:
                rhs[i][terminals[nxt]] += probability
            else:
                mat[i][idx[nxt]] -= probability
        rhs[i][3] = Fraction(1)
    sol = solve(mat, rhs)
    # E[T^2] = 1 + 2*sum Q_ij E[T_j] + sum Q_ij E[T_j^2].
    rhs2 = []
    for state in nonterm:
        expr = Fraction(1)
        for nxt, probability in transition(m, *state).items():
            if nxt not in terminals:
                expr += 2*probability*sol[idx[nxt]][3]
        rhs2.append([expr])
    seconds = solve(mat, rhs2)
    checks = 0
    for state in states:
        p_expected, t_expected, s_expected = claimed(m, *state)
        if state in terminals:
            observed = [Fraction(int(terminals[state] == j))
                        for j in range(3)] + [Fraction(0)]
            second = Fraction(0)
        else:
            observed = sol[idx[state]]
            second = seconds[idx[state]][0]
        assert observed[:3] == p_expected, (m, state, 'class')
        assert observed[3] == t_expected, (m, state, 'time')
        assert second == s_expected, (m, state, 'second moment')
        checks += 5
    return checks


if __name__ == '__main__':
    total = sum(test(m) for m in (2, 4, 6, 8))
    print('VERIFY_OK', total, 'exact-rational state identities')
