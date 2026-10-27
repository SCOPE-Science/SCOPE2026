#!/usr/bin/env python3
"""Exact small-order checks for finite quadratic-residue tournaments.

Run: python3 verify_paley_tournaments.py
Only Python's standard library is required. The all-field proof uses the
quadratic character-sum bound and is given separately in RESULT.md.
"""
from collections import Counter
from itertools import combinations, permutations
from math import isqrt, sqrt


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def field27():
    # GF(3)[u]/(u^3+2u+1), irreducible because it has no root in GF(3).
    def coeff(a):
        return [a % 3, a // 3 % 3, a // 9 % 3]
    def encode(v):
        return sum((v[i] % 3) * (3 ** i) for i in range(3))
    def add(a, b):
        return encode([x + y for x, y in zip(coeff(a), coeff(b))])
    def neg(a):
        return encode([-x for x in coeff(a)])
    def mul(a, b):
        aa, bb = coeff(a), coeff(b)
        product = [0] * 5
        for i in range(3):
            for j in range(3):
                product[i + j] += aa[i] * bb[j]
        # u^3=u+2
        for d in (4, 3):
            c = product[d]
            product[d] = 0
            product[d - 3] += 2 * c
            product[d - 2] += c
        return encode(product)
    return add, neg, mul


def tournament(q):
    assert q % 4 == 3 and (prime(q) or q == 27)
    if prime(q):
        squares = {x * x % q for x in range(1, q)}
        A = [[int((y - x) % q in squares) for y in range(q)] for x in range(q)]
    else:
        add, neg, mul = field27()
        squares = {mul(x, x) for x in range(1, 27)}
        A = [[int(add(y, neg(x)) in squares) for y in range(q)] for x in range(q)]
    assert all(A[x][x] == 0 for x in range(q))
    assert all(A[x][y] + A[y][x] == 1 for x in range(q) for y in range(x))
    return A


def two_extension_holds(A):
    n = len(A)
    for a, b in combinations(range(n), 2):
        patterns = {A[a][w] + 2 * A[b][w] for w in range(n) if w not in (a, b)}
        if len(patterns) != 4:
            return False
    return True


def triple_extension_hist(A):
    n = len(A)
    hist = Counter()
    failures = []
    for a, b, c in combinations(range(n), 3):
        signs = 0
        for w in range(n):
            if w not in (a, b, c):
                signs |= 1 << (A[a][w] + 2 * A[b][w] + 4 * A[c][w])
        hist[signs.bit_count()] += 1
        if signs != 255:
            failures.append(((a, b, c), signs))
    return hist, failures


def triple_independent(A):
    # Alternative implementation: intersect in- and out-neighbor bitsets.
    n = len(A)
    incoming = [sum((A[v][a] << v) for v in range(n)) for a in range(n)]
    outgoing = [sum((A[a][v] << v) for v in range(n)) for a in range(n)]
    mask_all = (1 << n) - 1
    bad = []
    for a, b, c in combinations(range(n), 3):
        for mask in range(8):
            possible = mask_all & ~(1 << a | 1 << b | 1 << c)
            for i, v in enumerate((a, b, c)):
                possible &= outgoing[v] if ((mask >> i) & 1) else incoming[v]
            if not possible:
                bad.append(((a, b, c), mask))
    return bad


def atomic(A, t):
    return tuple((int(t[i] == t[j]), A[t[i]][t[j]]) for i in range(len(t)) for j in range(i))


def rank4_theory(A, registers):
    # Model-specific tuple sets, shared global intern dictionaries for exact comparison.
    n = len(A)
    def intern(level, key):
        table = registers[level]
        if key not in table:
            table[key] = len(table)
        return table[key]
    threes = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                t = (a, b, c)
                threes[t] = intern(3, (atomic(A, t), frozenset(atomic(A, t + (w,)) for w in range(n))))
    twos = {}
    for a in range(n):
        for b in range(n):
            t = (a, b)
            twos[t] = intern(2, (atomic(A, t), frozenset(threes[(a, b, c)] for c in range(n))))
    ones = [intern(1, ((), frozenset(twos[(a, b)] for b in range(n)))) for a in range(n)]
    return frozenset(ones)


def pattern(A, indices):
    # Canonical oriented 4-vertex graph code under all 24 permutations.
    return min(tuple(A[t[i]][t[j]] for i in range(4) for j in range(i)) for t in permutations(indices))


def has_transitive(A, size):
    # Every induced tournament is acyclic iff vertices admit a total order by arcs.
    for nodes in combinations(range(len(A)), size):
        if sorted(sum(A[x][y] for y in nodes) for x in nodes) == list(range(size)):
            return nodes
    return None


def main():
    orders = [3, 7, 11, 19, 23, 27, 31, 43]
    signatures = {}
    registers = {3: {}, 2: {}, 1: {}}
    for q in orders:
        A = tournament(q)
        hist, failures = triple_extension_hist(A)
        expected_success = q >= 19
        assert (len(failures) == 0) == expected_success, (q, failures[:1])
        if q <= 27:
            alternative = triple_independent(A)
            assert {t for t, _ in alternative} == {t for t, _ in failures}
            assert (not alternative) == expected_success
        signatures[q] = rank4_theory(A, registers)
        print('RANK4_AND_EXTENSION_OK q=%d triple_profile=%s' % (q, sorted(hist.items())))
    classes = [[3], [7], [11], [19, 23, 27, 31, 43]]
    assert len({signatures[q] for q in orders}) == 4
    assert all(len({signatures[q] for q in group}) == 1 for group in classes)
    assert len({signatures[group[0]] for group in classes}) == 4
    print('EXACT_RANK4_OK classes=4 representatives=3,7,11,19')
    assert not two_extension_holds(tournament(3))
    assert two_extension_holds(tournament(7))
    assert two_extension_holds(tournament(11))
    print('RANK3_STABILIZATION_OK classes=2 threshold_order=7 exhaustive_pair_orders=7,11')

    A3, A7, A11, A19 = (tournament(q) for q in (3, 7, 11, 19))
    assert has_transitive(A3, 3) is None
    assert has_transitive(A7, 3) == (0, 1, 2)
    assert has_transitive(A7, 4) is None
    assert has_transitive(A11, 4) == (0, 1, 3, 4)
    assert all(A11[i][j] for pos, i in enumerate((0, 3, 1, 4)) for j in (0, 3, 1, 4)[pos + 1:])
    witness = (0, 1, 3)
    assert not any(all(A11[w][v] for v in witness) for w in range(11) if w not in witness)
    assert not triple_extension_hist(A19)[1]
    print('DISTINGUISHING_FORMULAS_OK transitive3=7 transitive4=11 three_vertex_extension=19')

    codes = {}
    for q in (7, 11, 19, 23, 27):
        A = tournament(q)
        hist = Counter(pattern(A, indices) for indices in combinations(range(q), 4))
        codes[q] = hist
    assert len(set(codes[11])) == 4
    assert set(codes[11]) == set(codes[19]) == set(codes[23]) == set(codes[27])
    assert len(codes[7]) == 3
    assert sum(codes[11].values()) == 330
    print('EXISTENTIAL_FOUR_VERTEX_TYPES_OK q7=3 q11=4 q19=4 q23=4 q27=4')
    print('EXISTENTIAL_ALTERNATION_GAP_OK q11_and_q19_same_existential_rank4_distinct_full_rank4')

    # Character-sum lower bound on extension counts for every allowable q>=27.
    assert 27 - 15 - 2 * sqrt(27) > 0
    print('FIELD_UNIFORM_CHARACTER_BOUND_OK q>=27 lower_bound=(q-15-2sqrt(q))/8>0')
    print('SHARP_REPRESENTATIVE_OK vertices=19')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
