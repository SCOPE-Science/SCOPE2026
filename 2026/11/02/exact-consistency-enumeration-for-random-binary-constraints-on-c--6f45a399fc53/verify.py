#!/usr/bin/env python3
"""Exact verification of the cyclic random-binary-relation consistency count.

Only Python's standard library is required. No stochastic sampling is used.
"""
from itertools import product

REPS = (0, 1, 3, 5, 6, 7, 15)
TRANSITION = (
    (16, 0, 0, 0, 0, 0, 0),
    (4, 8, 4, 0, 0, 0, 0),
    (1, 6, 9, 0, 0, 0, 0),
    (4, 0, 0, 8, 0, 0, 4),
    (1, 4, 2, 2, 2, 4, 1),
    (1, 2, 1, 4, 0, 4, 4),
    (1, 0, 0, 6, 0, 0, 9),
)
G = (0, 8, 12, 12, 12, 14, 15)


def multiply(a, b):
    """Boolean product of two 2x2 matrices encoded row-major, low bit first."""
    out = 0
    for i in range(2):
        for j in range(2):
            if any((a >> (2*i+k) & 1) and (b >> (2*k+j) & 1) for k in range(2)):
                out |= 1 << (2*i+j)
    return out


def swap_rows(a):
    return (a >> 2) | ((a & 3) << 2)


def swap_cols(a):
    return ((a & 5) << 1) | ((a & 10) >> 1)


def orbit(a):
    found = {a}
    todo = [a]
    while todo:
        b = todo.pop()
        for c in (swap_rows(b), swap_cols(b)):
            if c not in found:
                found.add(c)
                todo.append(c)
    return frozenset(found)


def transition_check():
    orbits = [orbit(a) for a in REPS]
    assert len(set(orbits)) == 7
    assert set().union(*orbits) == set(range(16))
    lookup = {a: i for i, oo in enumerate(orbits) for a in oo}
    assert lookup[9] == 4
    for i, oo in enumerate(orbits):
        for a in oo:
            row = [0] * 7
            for b in range(16):
                row[lookup[multiply(a,b)]] += 1
            assert tuple(row) == TRANSITION[i]
        a = REPS[i]
        assert G[i] == sum(bool(multiply(a,b)&9) for b in range(16))
    return lookup


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def matvec(A, v):
    return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]


def matrix_polynomial_check():
    T = [list(r) for r in TRANSITION]
    eye = [[int(i == j) for j in range(7)] for i in range(7)]
    sub = lambda A, c: [[A[i][j]-c*eye[i][j] for j in range(7)] for i in range(7)]
    T2 = matmul(T, T)
    quad = [[T2[i][j]-17*T[i][j]+48*eye[i][j] for j in range(7)] for i in range(7)]
    annihilator = matmul(matmul(sub(T, 4), sub(T, 2)), quad)
    assert matvec(annihilator, G) == [0]*7


def direct_consistency_count(n):
    """Independent brute force: all edge truth-table choices and all assignments."""
    patterns = []
    for assignment in range(1 << n):
        forbidden_masks = []
        for i in range(n):
            val_i = (assignment >> i) & 1
            val_next = (assignment >> ((i+1) % n)) & 1
            forbidden_masks.append(1 << (2*val_i+val_next))
        patterns.append(tuple(forbidden_masks))
    count = 0
    for edge_tables in product(range(16), repeat=n):
        if any(all(edge_tables[i] & needed[i] for i in range(n)) for needed in patterns):
            count += 1
    return count


def independent_inclusion_exclusion(n):
    """A different exact count: union of 2^n events, one per assignment.

    For a nonempty chosen family S of assignments, each edge table must
    contain every two-bit projection attained by S. Inclusion-exclusion
    adds (-1)^(|S|+1) 2^(4n - sum_e |projection_e(S)|).
    """
    projected = []
    for e in range(n):
        edge_groups = [0] * 4
        for assignment in range(1 << n):
            pair = 2 * ((assignment >> e) & 1) + ((assignment >> ((e+1) % n)) & 1)
            edge_groups[pair] |= 1 << assignment
        projected.extend(edge_groups)
    total = 0
    for family in range(1, 1 << (1 << n)):
        required = sum(bool(family & group) for group in projected)
        contribution = 1 << (4*n - required)
        total += contribution if family.bit_count() & 1 else -contribution
    return total


def predicted_count(n):
    a0, a1 = 2, 17
    if n == 0:
        lucas = a0
    else:
        for _ in range(2, n+1):
            a0, a1 = a1, 17*a1 - 48*a0
        lucas = a1
    return lucas - 4**n - 2**(n-1) if n >= 1 else None


def transfer_count(n):
    row = [0, 0, 0, 0, 1, 0, 0]
    for _ in range(n-1):
        row = [sum(row[i]*TRANSITION[i][j] for i in range(7)) for j in range(7)]
    return sum(row[i]*G[i] for i in range(7))


def run():
    transition_check()
    matrix_polynomial_check()
    for n in range(1, 61):
        assert transfer_count(n) == predicted_count(n), (n, transfer_count(n), predicted_count(n))
    direct_checked = 0
    for n, expected in ((3, 2397), (4, 32377)):
        direct = direct_consistency_count(n)
        assert direct == expected == transfer_count(n), (n, direct, expected)
        assert independent_inclusion_exclusion(n) == direct, (n, direct)
        direct_checked += 16**n
    assert predicted_count(3) == 2397
    # The published conjecture predicts 2337/4096 at n=3.
    assert predicted_count(3) - (predicted_count(3) - 15*2**(3-1)) == 60
    print('VERIFY_OK exhaustive_random_systems={} cycle_lengths=3,4 transfer_lengths=1..60 inclusion_exclusion_n=3,4 matrix_orbits=7 annihilator_exact=true'.format(direct_checked))


if __name__ == '__main__':
    run()
