#!/usr/bin/env python3
"""Exact rational certificate for the centered graph-ball maximal norm on K(3,3).

Only Python's standard library is needed. Vertex labels are 0,1,2 and 3,4,5;
choice 0 is the singleton ball, 1 is the closed-neighborhood ball,
and 2 is the whole six-vertex graph.
"""
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product


def determinant(rows):
    """Fractional Gaussian elimination with tracked row-swap sign."""
    a = [list(row) for row in rows]
    size = len(a)
    answer = Q(1)
    for j in range(size):
        pivot = next((k for k in range(j, size) if a[k][j]), None)
        if pivot is None:
            return Q(0)
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            answer = -answer
        c = a[j][j]
        answer *= c
        for k in range(j + 1, size):
            factor = a[k][j] / c
            if factor:
                for ell in range(j + 1, size):
                    a[k][ell] -= factor * a[j][ell]
            a[k][j] = Q(0)
    return answer


def averaging_row(vertex, choice):
    row = [Q(0) for _ in range(6)]
    if choice == 0:
        row[vertex] = Q(1)
    elif choice == 1:
        row[vertex] = Q(1, 4)
        for other in range(6):
            if (vertex < 3) != (other < 3):
                row[other] = Q(1, 4)
    elif choice == 2:
        row = [Q(1, 6) for _ in range(6)]
    else:
        raise ValueError(choice)
    assert sum(row) == 1
    return row


def averaging_matrix(choices):
    return [averaging_row(i, choices[i]) for i in range(6)]


def gram(rows):
    return [[sum(rows[k][i] * rows[k][j] for k in range(6))
             for j in range(6)] for i in range(6)]


def sylvester(choices):
    g = gram(averaging_matrix(choices))
    gap = [[Q(39, 25) * (i == j) - g[i][j] for j in range(6)]
           for i in range(6)]
    return [determinant([row[:j] for row in gap[:j]])
            for j in range(1, 7)]


def canonical(choices):
    a = tuple(sorted(choices[:3]))
    b = tuple(sorted(choices[3:]))
    return tuple(sorted((a, b)))


def main():
    patterns = list(combinations_with_replacement(range(3), 3))
    keys = list(combinations_with_replacement(patterns, 2))
    assert len(patterns) == 10 and len(keys) == 55
    winner = ((0, 0, 0), (1, 1, 1))
    expected_minima = [
        Q(1141, 3600),
        Q(1631, 22500),
        Q(2989, 93750),
        Q(12691, 390625),
        Q(357749, 9765625),
        Q(7529536, 244140625),
    ]
    mins = [None] * 6
    for a, b in keys:
        if (a, b) == winner:
            continue
        d = sylvester(a + b)
        assert min(d) > 0, (a, b, d)
        for k, value in enumerate(d):
            if mins[k] is None or value < mins[k]:
                mins[k] = value
    assert mins == expected_minima, (mins, expected_minima)

    all_keys = set()
    winner_count = 0
    for choices in product(range(3), repeat=6):
        key = canonical(choices)
        all_keys.add(key)
        if key == winner:
            winner_count += 1
        else:
            assert min(sylvester(choices)) > 0, choices
    assert all_keys == set(keys)
    assert winner_count == 2

    # Explicit exceptional block: on the mean-zero subspaces, the squared
    # singular values are 1 (twice) and 1/16 (twice). On class constants,
    # the averaging matrix is [[1/4,3/4],[0,1]] up to class interchange.
    # Its Gram has entries [[1,3],[3,25]] /16; trace is 26/16 and
    # determinant 1/16, giving 16 z*z - 26 z + 1 = 0.
    s = [[Q(1, 4), Q(3, 4)], [Q(0), Q(1)]]
    block = [[sum(s[k][i] * s[k][j] for k in range(2))
              for j in range(2)] for i in range(2)]
    assert block == [[Q(1, 16), Q(3, 16)],
                     [Q(3, 16), Q(25, 16)]]
    assert sum(block[i][i] for i in range(2)) == Q(26, 16)
    assert determinant(block) == Q(1, 16)
    assert 16*Q(13,16)**2 + 16*Q(3,16)**2 * 17 -26*Q(13,16) + 1 == 0
    assert 32*Q(13,16)*Q(3,16) - 26*Q(3,16) == 0
    # sqrt(17)>4 implies (13+3sqrt(17))/16>25/16>39/25.
    assert Q(25, 16) > Q(39, 25)
    print("CERTIFICATE_OK canonical=55 strict=54 raw=729 winning_raw=2")
    print("leading_Sylvester_minima", ', '.join(str(x) for x in mins))
    print("winning_squared_norm = (13+3*sqrt(17))/16")


if __name__ == '__main__':
    main()
