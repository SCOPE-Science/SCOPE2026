#!/usr/bin/env python3
"""Exact integer certificate for two ternary multiplicative intersections.

No external libraries required. The finite carry graphs are exhaustively built
from their transition rule, and the vector-polynomial identities certify
recurrences at every prefix length, not merely sampled depths.
"""
from collections import deque


def graph(m):
    reached = {0}
    queue = deque([0])
    edges = {}
    while queue:
        carry = queue.popleft()
        out = []
        for digit in (0, 1):
            u = carry + m * digit
            if u % 3 <= 1:
                destination = u // 3
                out.append((digit, destination))
                if destination not in reached:
                    reached.add(destination)
                    queue.append(destination)
        edges[carry] = tuple(out)
    assert all(len(edges[v]) > 0 for v in reached)
    assert all(len({digit for digit, _ in edges[v]}) == len(edges[v])
               for v in reached)
    assert all(v <= m // 2 for v in reached)
    return edges


def transfer(edges, v):
    return {c: sum(v[d] for _, d in edges[c]) for c in edges}


def count_vectors(edges, count):
    v = {c: 1 for c in edges}
    out = [v]
    for _ in range(count):
        v = transfer(edges, v)
        out.append(v)
    return out


def check_vector_relation(vectors, terms, depth):
    """Check A^depth 1 = sum coefficient * A^previous_depth 1."""
    assert all(vectors[depth][c] == sum(coef * vectors[j][c]
                                        for j, coef in terms)
               for c in vectors[depth])


def prefix_counts_bruteforce(m, n):
    """Independent digit-based enumeration, rather than graph traversal."""
    count = 0
    for mask in range(1 << n):
        x = sum((3**j) for j in range(n) if (mask >> j) & 1)
        y = (m * x) % (3**n)
        if all((y // (3**j)) % 3 in (0, 1) for j in range(n)):
            count += 1
    return count


def main():
    g13 = graph(13)
    g85 = graph(85)
    assert sorted(g13) == [0, 1, 4]
    assert sorted(g85) == [0, 1, 3, 4, 9, 10, 11, 13, 14,
                           28, 29, 31, 32, 33, 38, 39, 41, 42]
    assert sum(map(len, g13.values())) == 4
    assert sum(map(len, g85.values())) == 24
    v13 = count_vectors(g13, 30)
    v85 = count_vectors(g85, 30)
    # A_13^3 1 - A_13^2 1 - 1 = 0, on every reachable state.
    check_vector_relation(v13, [(2, 1), (0, 1)], 3)
    # A_85^9 1 - A_85^8 1 - A_85^4 1 - 2 A_85^2 1 - 1 = 0.
    check_vector_relation(v85, [(8, 1), (4, 1), (2, 2), (0, 1)], 9)
    counts13 = [v[0] for v in v13]
    counts85 = [v[0] for v in v85]
    assert counts13[:3] == [1, 2, 3]
    assert counts85[:9] == [1, 2, 3, 5, 8, 11, 16, 22, 32]
    for n in range(12):
        assert prefix_counts_bruteforce(13, n) == counts13[n]
        assert prefix_counts_bruteforce(85, n) == counts85[n]
    # The first nine numerator coefficients for
    # F85(z)=N85(z)/(1-z-z^5-2z^7-z^9).
    coeff = []
    for n in range(9):
        coeff.append(counts85[n]
                     - (counts85[n-1] if n >= 1 else 0)
                     - (counts85[n-5] if n >= 5 else 0)
                     - (2*counts85[n-7] if n >= 7 else 0))
    assert coeff == [1, 1, 1, 2, 3, 2, 3, 1, 1]
    for n in range(9, 31):
        assert counts85[n] == (counts85[n-1] + counts85[n-5]
                               + 2*counts85[n-7] + counts85[n-9])
    # Integer-convolution verification of the denominator factorization:
    # (1-z-z^3)(1+z^3+z^4+z^6) = 1-z-z^5-2z^7-z^9.
    f = [1, -1, 0, -1]
    h = [1, 0, 0, 1, 1, 0, 1]
    conv = [0] * (len(f)+len(h)-1)
    for i, a in enumerate(f):
        for j, b in enumerate(h):
            conv[i+j] += a*b
    assert conv == [1, -1, 0, 0, 0, -1, 0, -2, 0, -1]
    print('VERIFY_OK M13_states=3 M85_states=18 M85_edges=24')
    print('STATEWISE_IDENTITIES A13^3-A13^2-I; A85^9-A85^8-A85^4-2A85^2-I')
    print('FIRST_PREFIX_COUNTS_85', counts85[:16])
    print('GENERATING_NUMERATOR_85', coeff)
    print('DIRECT_DIGIT_COMPARISON depths=0..11 multipliers=13,85')


if __name__ == '__main__':
    main()
