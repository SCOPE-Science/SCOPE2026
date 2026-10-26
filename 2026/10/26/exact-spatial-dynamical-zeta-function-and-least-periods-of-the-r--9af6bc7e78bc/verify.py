#!/usr/bin/env python3
"""Exact integer certificate for the spatial-periodic image of Rule 110.

No third-party dependencies. Run: python3 verify.py
"""
from collections import deque
from itertools import product

RULE = 110
I = sum(1 << (5 * i) for i in range(4))
DIAGONAL = I


def letter_relations():
    rel = [0, 0]
    for a, b, c in product(range(2), repeat=3):
        bit = (RULE >> (4 * a + 2 * b + c)) & 1
        rel[bit] |= 1 << (4 * (2 * a + b) + (2 * b + c))
    return tuple(rel)


def mul(a, b):
    out = 0
    for i in range(4):
        row = (a >> (4 * i)) & 15
        for j in range(4):
            if (row >> j) & 1:
                out |= ((b >> (4 * j)) & 15) << (4 * i)
    return out


def cycle(a):
    power = a
    for length in range(1, 5):
        if power & DIAGONAL:
            return True
        power = mul(power, a)
    return False


def build_relation_graph():
    letters = letter_relations()
    seen = {I: 0}
    ordered = [I]
    edges = []
    queue = deque([I])
    while queue:
        a = queue.popleft()
        row = []
        for b in letters:
            target = mul(a, b)
            if target not in seen:
                seen[target] = len(ordered)
                ordered.append(target)
                queue.append(target)
            row.append(seen[target])
        edges.append(tuple(row))
    assert len(edges) == len(ordered) == 75
    assert len(set(ordered)) == 75
    return letters, ordered, edges


def transfer(edges, column):
    return [column[j] + column[k] for j, k in edges]


def polynomial_multiply(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            c[i + j] += u * v
    return c


def derivative(a):
    return [i * a[i] for i in range(1, len(a))]


def pad_equal(a, b):
    return a + [0] * max(0, len(b) - len(a)) == b + [0] * max(0, len(a) - len(b))


def ring_outputs(n):
    # Enumerate periodic antecedents with spatial periods n, 2n, 3n, 4n.
    # This is a separate bit-parallel implementation of the local CA rule.
    good = set()
    mask_n = (1 << n) - 1
    for k in range(1, 5):
        m = n * k
        mask = (1 << m) - 1
        pattern_mult = sum(1 << (n * j) for j in range(k))
        for x in range(1 << m):
            left = ((x << 1) & mask) | (x >> (m - 1))
            right = (x >> 1) | ((x & 1) << (m - 1))
            y = ((x | right) & ~(left & x & right)) & mask
            base = y & mask_n
            if y == base * pattern_mult:
                good.add(base)
    return good


def main():
    letters, states, edges = build_relation_graph()
    assert letters == (0x8101, 0x42c2)
    assert all(0 <= s < 65536 for s in states)
    nstates = len(states)
    accept = [int(cycle(s)) for s in states]
    assert accept[0] == 1

    # The exact polynomial-annihilation certificate Q(T) accept = 0.
    # Coefficient C[j] multiplies T^(9-j).
    C = [1, -4, 6, -5, 1, 4, -4, 2, 0, -1]
    vectors = [accept]
    for _ in range(9):
        vectors.append(transfer(edges, vectors[-1]))
    killed = [sum(C[j] * vectors[9 - j][i] for j in range(10))
              for i in range(nstates)]
    assert killed == [0] * nstates

    P = [vec[0] for vec in vectors]
    assert P[:10] == [1, 2, 2, 5, 10, 22, 41, 79, 154, 302]
    col = vectors[-1]
    for _ in range(100):
        col = transfer(edges, col)
        P.append(col[0])
    for n in range(9, len(P)):
        assert sum(C[j] * P[n - j] for j in range(10)) == 0

    # P(z)=sum_{n>=0}P_n z^n = N(z)/Q(z), Q(z)=sum C[j] z^j.
    Q = C
    N = [sum(Q[j] * P[n - j] for j in range(min(n, 9) + 1))
         for n in range(9)]
    assert N == [1, -2, 0, 4, -7, 8, -6, 4, 0]
    numer_zeta = [1, -1, 0, 0, -1]
    factor1 = [1, -1]
    factor2 = [1, -2, 1, -1, -1]
    denom_zeta = polynomial_multiply(factor1, factor2)
    assert pad_equal(Q, polynomial_multiply(numer_zeta, denom_zeta))

    # Formal identity: z Z'(z)/Z(z) = P(z)-1.
    # Clear denominators; no floating-point differentiation/integration.
    L = polynomial_multiply(derivative(numer_zeta), denom_zeta)
    R = polynomial_multiply(numer_zeta, derivative(denom_zeta))
    diff = [a - b for a, b in zip(L + [0] * (max(len(L), len(R)) - len(L)),
                                    R + [0] * (max(len(L), len(R)) - len(R)))]
    left = [0] + polynomial_multiply(diff, Q)
    right = polynomial_multiply([
        (N[i] if i < len(N) else 0) - (Q[i] if i < len(Q) else 0)
        for i in range(max(len(N), len(Q)))],
        polynomial_multiply(numer_zeta, denom_zeta))
    assert pad_equal(left, right)

    # Exact ring-image enumeration independent of relation-semigroup counting.
    for n in range(1, 6):
        good = ring_outputs(n)
        assert len(good) == P[n]
    assert ring_outputs(2) == {0, 3}

    # Every n>=3 has a primitive spatial n-periodic output 1^(n-1)0.
    A = I
    for k in range(1, 7):
        A = mul(A, letters[1])
        if 2 <= k <= 5:
            assert cycle(mul(A, letters[0]))
        if k == 5:
            fixed = A
    assert A == fixed  # multiplication by R_1 stabilizes after five factors
    assert not cycle(mul(letters[1], letters[0]))

    # Entire certificate is exact. The matrix-annihilation identity proves
    # the rational series for all n, not just enumerated test lengths.
    print('VERIFY_OK: 75 Boolean relations; exact ninth-order annihilation on all states;'
          ' rational zeta identity; ring preimage enumeration n<=5;'
          ' primitive output periods exactly 1 and all n>=3')


if __name__ == '__main__':
    main()
