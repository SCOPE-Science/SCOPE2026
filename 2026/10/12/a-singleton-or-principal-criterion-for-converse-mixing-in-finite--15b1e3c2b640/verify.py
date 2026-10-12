"""Finite exhaustive verification of a monotone neighborhood-product theorem.

This checks all nonempty proper upward-closed local neighborhood families
on carriers of sizes 1, 2, and 3. It does not substitute for the proof.
"""
from itertools import combinations, product


def minimal_families(n):
    nonempty = list(range(1, 1 << n))
    for choice in range(1, 1 << len(nonempty)):
        family = tuple(v for k, v in enumerate(nonempty) if choice >> k & 1)
        if all(not (a & b == a or a & b == b)
               for a, b in combinations(family, 2)):
            yield family


def contains(A, minimal):
    return any(A & member == member for member in minimal)


def triple(A, n, m, M, N):
    rows = [sum(1 << j for j in range(m) if A >> (i * m + j) & 1)
            for i in range(n)]
    columns = [sum(1 << i for i in range(n) if A >> (i * m + j) & 1)
               for j in range(m)]
    forward = contains(sum(1 << i for i, row in enumerate(rows)
                           if contains(row, N)), M)
    backward = contains(sum(1 << j for j, column in enumerate(columns)
                            if contains(column, M)), N)
    rectangle = any(all((rows[i] & v) == v for i in range(n) if u >> i & 1)
                    for u in M for v in N)
    return rectangle, forward, backward


def singleton_generated(M):
    return all(member.bit_count() == 1 for member in M)


def principal(M):
    return len(M) == 1


def run():
    families = {n: list(minimal_families(n)) for n in (1, 2, 3)}
    assert {n: len(fs) for n, fs in families.items()} == {1: 1, 2: 4, 3: 18}
    total_valuations = total_family_pairs = 0
    summaries = {}
    for n, m in product((1, 2, 3), repeat=2):
        correct_one = correct_both = 0
        for F, G in product(families[n], families[m]):
            pred_fg = singleton_generated(F) or principal(G)
            pred_gf = singleton_generated(G) or principal(F)
            actual_fg = actual_gf = True
            for A in range(1 << (n * m)):
                rectangle, forward, backward = triple(A, n, m, F, G)
                assert not rectangle or (forward and backward)
                actual_fg &= (rectangle == forward)
                actual_gf &= (rectangle == backward)
                total_valuations += 1
            assert actual_fg == pred_fg, (n, m, F, G, 'first')
            assert actual_gf == pred_gf, (n, m, F, G, 'second')
            correct_one += actual_fg
            correct_both += actual_fg and actual_gf
            total_family_pairs += 1
        Tn, Tm = len(families[n]), len(families[m])
        qn, qm = (1 << n) - 1, (1 << m) - 1
        rn, rm = Tn - 2 * qn + n, Tm - 2 * qm + m
        expected_one = qn * Tm + Tn * qm - qn * qm
        expected_both = (Tn * Tm - 2 * (Tn - qn) * (Tm - qm) + rn * rm)
        assert (correct_one, correct_both) == (expected_one, expected_both)
        summaries[(n, m)] = (correct_one, correct_both)
    assert total_family_pairs == 529
    assert total_valuations == 175682
    assert summaries[(3, 3)] == (203, 131)
    print('PASS: 529 ordered local-family pairs, 175682 pair/valuation tests')
    print('PASS: one-order and two-order exact counts, including (3,3)=(203,131)')
    print('PASS: both-order failures first possible on carriers of size 3 by 3')


if __name__ == '__main__':
    run()
