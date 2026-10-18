"""Check the finite path-neighborhood approximation census and transfer certificate.

Uses only Python's standard library. Execution: python verify.py
"""
from collections import deque

# A state records surviving ordered pairs of consecutive truth bits.
PAIRS = ((0, 0), (0, 1), (1, 0), (1, 1))
START = frozenset(((0, 0), (1, 1)))
FINAL = set(START)


def local_symbol(a, b, c):
    if (a, b, c) == (0, 0, 0):
        return 0
    if (a, b, c) == (1, 1, 1):
        return 2
    return 1


def advance(state, symbol):
    return frozenset(
        (b, c)
        for (a, b) in state
        for c in (0, 1)
        if local_symbol(a, b, c) == symbol
    )


def deterministic_states():
    found = {START: 0}
    todo = deque((START,))
    transitions = []
    while todo:
        state = todo.popleft()
        row = []
        for symbol in (0, 1, 2):
            new = advance(state, symbol)
            if new not in found:
                found[new] = len(found)
                todo.append(new)
            row.append(found[new])
        transitions.append(tuple(row))
    accept = [int(bool(set(state) & FINAL)) for state in found]
    return found, transitions, accept


# The output-side deterministic automaton. Vertex order is breadth-first.
EXPECTED_ROWS = (
    (1, 2, 3), (1, 4, 5), (5, 6, 5), (5, 7, 3),
    (5, 8, 5), (5, 5, 5), (1, 6, 3), (5, 9, 5),
    (5, 10, 3), (1, 11, 5), (1, 6, 5), (5, 6, 3),
)
EXPECTED_ACCEPT = (1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1)


def trim(poly):
    poly = list(poly)
    while poly and poly[-1] == 0:
        poly.pop()
    return tuple(poly)


def add(*polys):
    n = max((len(p) for p in polys), default=0)
    return trim(sum((p[j] if j < len(p) else 0) for p in polys) for j in range(n))


def multiply(a, b):
    v = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            v[i + j] += x * y
    return trim(v)


def scale(c, p):
    return trim(c * x for x in p)


# Numerators G_i(z)=P_i(z)/(1-z-z^2-z^3), one for each DFA state.
NUMERATORS = (
    (1, 1, 0, 1, 1), (1,), (0, 1, 2, 1), (1,),
    (0, 1, 1), (), (1, 2, 1), (0, 1, 1),
    (1, 1), (1, 1), (1, 1, 1), (1, 1, 1),
)
DENOMINATOR = (1, -1, -1, -1)


def check_certificate():
    states, rows, acc = deterministic_states()
    assert len(states) == len(EXPECTED_ROWS) == 12
    assert tuple(rows) == EXPECTED_ROWS
    assert tuple(acc) == EXPECTED_ACCEPT
    # The 12 polynomial identities ensure exact transfer counting for all n.
    for i, row in enumerate(rows):
        rhs = add(scale(acc[i], DENOMINATOR),
                  multiply((0, 1), add(*(NUMERATORS[j] for j in row))))
        assert trim(NUMERATORS[i]) == trim(rhs), (i, rhs)


def path_signature(mask, n):
    lower = upper = 0
    for i in range(n):
        bits = [int(bool(mask & (1 << j)))
                for j in range(max(0, i-1), min(n, i+2))]
        if all(bits):
            lower |= 1 << i
        if any(bits):
            upper |= 1 << i
    return lower, upper


def counts(nmax=15):
    a = [1]
    for n in range(1, nmax+1):
        signatures = {path_signature(mask, n) for mask in range(1 << n)}
        a.append(len(signatures))
    assert a[:6] == [1, 2, 3, 7, 13, 23]
    for n in range(5, nmax+1):
        assert a[n] == a[n-1] + a[n-2] + a[n-3], n
    return a


if __name__ == '__main__':
    check_certificate()
    a = counts()
    print('VERIFY_OK: exact transfer polynomial identities; direct subset enumeration n=1..15; counts', a)
