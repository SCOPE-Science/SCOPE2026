#!/usr/bin/env python3
"""Finite checks for exact-value equalizers in the constant-free FOUR algebra.
Pure Python 3, no third-party dependencies. Every Boolean truth table at arity 4
is considered, not a formula-length-bounded sample.
"""
from collections import Counter
from itertools import combinations


def theta(v, k):
    """Involution on truth/falsity bit pairs: (t,f) -> (1-f,1-t)."""
    out = 0
    for i in range(k):
        a = (v >> (2 * i)) & 1
        b = (v >> (2 * i + 1)) & 1
        out |= (1 - b) << (2 * i)
        out |= (1 - a) << (2 * i + 1)
    return out


def monotone_nonconstant_tables(n):
    """All monotone Boolean functions in n inputs, excluding constants."""
    number = 1 << n
    out = []
    for table in range(1 << number):
        if (table & 1) or not ((table >> (number - 1)) & 1):
            continue
        if all(((table >> v) & 1) <= ((table >> (v | (1 << i))) & 1)
               for v in range(number)
               for i in range(n) if not (v & (1 << i))):
            out.append(table)
    return out


def disagreement_union(table_f, table_g, theta_indices, universe):
    d = table_f ^ table_g
    dtheta = sum(((d >> j) & 1) << i for i, j in enumerate(theta_indices))
    return (universe - 1) & ~(d | dtheta)


def allowable_equalizers(k):
    n = 2 * k
    N = 1 << n
    invol = [theta(v, k) for v in range(N)]
    result = set()
    for mask in range(1 << N):
        if not (mask & 1) or not ((mask >> (N - 1)) & 1):
            continue
        if all(((mask >> i) & 1) == ((mask >> invol[i]) & 1) for i in range(N)):
            result.add(mask)
    return result


def convex(d, interval_masks):
    return all((d & ((1 << a) | (1 << b))) != ((1 << a) | (1 << b))
               or (d & interval) == interval
               for a, b, interval in interval_masks)


def convex_equalizers(k):
    n = 2 * k
    N = 1 << n
    theta_indices = [theta(i, k) for i in range(N)]
    ranges = []
    for a in range(N):
        for b in range(N):
            if a != b and a & b == a:
                ranges.append((a, b, sum(1 << y for y in range(N)
                                          if a & y == a and y & b == y)))
    loci = set()
    # The two Boolean extrema are excluded from any nonempty disagreement set.
    for sub in range(1 << (N - 2)):
        d = sub << 1
        if not convex(d, ranges):
            continue
        td = sum(((d >> j) & 1) << i for i, j in enumerate(theta_indices))
        loci.add(((1 << N) - 1) & ~(d | td))
    return loci


def check_direct_four_semantics(tables, k):
    """Rebuild positive DNF formulas and compare independent 4-valued tables."""
    n = 2 * k
    N = 1 << n

    def eval_lit(lit, assignment):
        j, bit = divmod(lit, 2)
        t = (assignment >> (2 * j)) & 1
        f = (assignment >> (2 * j + 1)) & 1
        return (t, f) if bit == 0 else (f, t)

    def eval_dnf(terms, assignment):
        accum = None
        for minterm in terms:
            conj = None
            for lit in range(n):
                if minterm & (1 << lit):
                    q = eval_lit(lit, assignment)
                    conj = q if conj is None else (conj[0] & q[0], conj[1] | q[1])
            assert conj is not None
            accum = conj if accum is None else (accum[0] | conj[0], accum[1] & conj[1])
        assert accum is not None
        return accum

    for f in tables:
        ones = [x for x in range(1, N) if (f >> x) & 1]
        mins = [x for x in ones if not any(y != x and y & x == y for y in ones)]
        for assignment in range(N):
            actual = eval_dnf(mins, assignment)
            expected = ((f >> assignment) & 1, 1 - ((f >> theta(assignment, k)) & 1))
            assert actual == expected, (k, f, assignment, actual, expected)


def verify_small(k):
    n = 2 * k
    N = 1 << n
    tables = monotone_nonconstant_tables(n)
    indices = [theta(i, k) for i in range(N)]
    check_direct_four_semantics(tables, k)
    loci = set()
    histogram = Counter()
    for f in tables:
        for g in tables:
            e = disagreement_union(f, g, indices, 1 << N)
            loci.add(e)
            histogram[e.bit_count()] += 1
    expected = allowable_equalizers(k)
    independent = convex_equalizers(k)
    assert loci == expected == independent, (
        'equalizer enumeration mismatch', len(loci), len(expected), len(independent))
    return len(tables), len(loci), dict(sorted(histogram.items()))


def check_three_variable_obstruction():
    k = 3
    n = 2 * k
    N = 1 << n
    a = 0b000001  # bit-pair notation: (T,N,N)
    b = 0b000111  # (B,T,N)
    c = 0b011111  # (B,B,T)
    assert a & b == a and b & c == b
    U = {a, b, c, theta(a, k), theta(b, k), theta(c, k)}
    assert len(U) == 6 and {v.bit_count() for v in U} == {1, 3, 5}
    assert 0 not in U and (N - 1) not in U
    assert {theta(z, k) for z in U} == U
    mid_ab = next(z for z in range(N) if a & z == a and z & b == z
                  and a != z != b)
    mid_bc = next(z for z in range(N) if b & z == b and z & c == z
                  and b != z != c)
    assert mid_ab not in U and mid_bc not in U
    # Stronger finite certificate: no convex D subset U can cover U
    # by taking its union with theta(D).
    elements = sorted(U)
    for mask in range(1 << len(elements)):
        D = {elements[i] for i in range(len(elements)) if mask & (1 << i)}
        if any(x & z == x and any(x & y == x and y & z == y and y not in D
                                  for y in range(N)) for x in D for z in D):
            continue
        assert (D | {theta(z, k) for z in D}) != U
    return sorted(U)


def main():
    d1 = verify_small(1)
    d2 = verify_small(2)
    assert d1 == (4, 4, {2: 4, 3: 8, 4: 4}), d1
    assert d2 == (166, 512, {
        2: 238, 3: 240, 4: 644, 5: 1056, 6: 1668, 7: 2416,
        8: 3240, 9: 3808, 10: 4072, 11: 3696, 12: 2976,
        13: 1920, 14: 1016, 15: 400, 16: 166}), d2
    assert sum(d2[2].values()) == 166 ** 2
    obstructing_orbits = check_three_variable_obstruction()
    print('FOUR_EQUALIZER_VERIFY_OK')
    print('k=1 (terms, loci, multiplicities):', d1)
    print('k=2 (terms, loci, multiplicities):', d2)
    print('k=3 six-point obstruction (bit-vector integers):', obstructing_orbits)

if __name__ == '__main__':
    main()
