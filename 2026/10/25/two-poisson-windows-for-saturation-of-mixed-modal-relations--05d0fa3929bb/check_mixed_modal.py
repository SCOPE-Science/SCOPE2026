"""Independent finite checks for mixed-modal relation composition and its expansions."""
from collections import Counter
from fractions import Fraction
from itertools import product


def relations(n):
    pairs = [(i, j) for i in range(n) for j in range(n) if i != j]
    for bits in range(1 << len(pairs)):
        rows = [1 << i for i in range(n)]
        for k, (i, j) in enumerate(pairs):
            if bits >> k & 1:
                rows[i] |= 1 << j
        yield tuple(rows)


def composed_rows(x, y, n):
    result = []
    for i in range(n):
        reached = 0
        for j in range(n):
            if (x[i] >> j) & 1:
                reached |= y[j]
        result.append(reached)
    return tuple(result)


def independently_composed(x, y, n):
    return tuple(sum((1 << k) for k in range(n)
                     if any(((x[i] >> j) & 1) and ((y[j] >> k) & 1)
                            for j in range(n))) for i in range(n))


def holes(rows, n):
    return sum(n - row.bit_count() for row in rows)


def box(rows, v, n):
    return sum(1 << i for i in range(n) if rows[i] & v == rows[i])


def semantic_mix(x, y, r, n):
    full = (1 << n) - 1
    for valuation in range(1 << n):
        antecedent = box(r, valuation, n)
        rhs = box(x, box(y, valuation, n), n) & box(y, box(x, valuation, n), n)
        if antecedent & (full ^ rhs):
            return False
    return True


def main():
    for n in (1, 2, 3):
        rels = list(relations(n))
        full = (1 << n) - 1
        zdist = Counter()
        z_one_sum = 0
        count_expansions = 0
        pairs = 0
        for x, y in product(rels, repeat=2):
            ab = composed_rows(x, y, n)
            ba = composed_rows(y, x, n)
            assert ab == independently_composed(x, y, n)
            assert ba == independently_composed(y, x, n)
            u = tuple(ab[i] | ba[i] for i in range(n))
            z = holes(u, n)
            zdist[z] += 1
            z_one_sum += holes(ab, n)
            count_expansions += 1 << z
            pairs += 1
            for r in rels:
                condition = all((r[i] | u[i]) == r[i] for i in range(n))
                assert condition == semantic_mix(x, y, r, n)
        assert pairs == 2 ** (2 * n * (n - 1))
        assert count_expansions == sum(v * (1 << z) for z, v in zdist.items())
        # Exact expectation for fair off-diagonal Bernoulli entries.
        expected_z = Fraction(n*(n-1), 1) * Fraction(1, 2)**2 * Fraction(3, 4)**(2*(n-2)) if n >= 2 else Fraction(0)
        expected_single = Fraction(n*(n-1), 1) * Fraction(1, 2)**2 * Fraction(3, 4)**(n-2) if n >= 2 else Fraction(0)
        assert Fraction(sum(z * ct for z, ct in zdist.items()), pairs) == expected_z
        assert Fraction(z_one_sum, pairs) == expected_single
        print('MIXED_MODAL_EXHAUSTIVE_OK', n, pairs, count_expansions,
              dict(sorted(zdist.items())), 'Eholes=', expected_z, 'Eone=', expected_single)
    print('MIXED_MODAL_CRITICAL_WINDOW_CHECK_OK')


if __name__ == '__main__':
    main()
