"""Independent finite checks for finite-chain strict-implication persistence.

Run with Python 3 standard library: python3 verify.py.
"""
from itertools import combinations, permutations, product


def last_occurrences(rows):
    n = len(rows)
    return tuple(max((i for i in range(n) if rows[i] == p), default=-1)
                 for p in range(n))


def direct_semantic_pa(rows):
    """Evaluate (p ~> q) -> (top ~> (p ~> q)) on every valuation."""
    n = len(rows)
    for a in range(n + 1):  # p truth-set {a,...,n-1}
        for b in range(n + 1):  # q truth-set {b,...,n-1}
            bad = [i for i, t in enumerate(rows) if a <= t < b]
            k = (max(bad) + 1) if bad else 0
            # p ~> q holds exactly at worlds >= k.
            # Its box must hold there as well.
            for i in range(k, n):
                for j in range(i, n):
                    if rows[j] < k:
                        return False
    return True


def combinatorial_pa(ell):
    """Check the partial-rook exclusion condition independent of semantics."""
    rooks = sorted((i, p) for p, i in enumerate(ell) if i >= 0)
    return all(rooks[h][1] > rooks[h - 1][0]
               for h in range(1, len(rooks)))


def operation_table(rows):
    n = len(rows)
    return tuple((max([i for i, t in enumerate(rows) if a <= t < b],
                      default=-1) + 1)
                 for a in range(n + 1) for b in range(n + 1))


def formula_by_support(n):
    from math import prod
    counts = [1]
    for k in range(1, n + 1):
        total = sum((n - k + 1) * prod(n - k + h - I[h - 1]
                  for h in range(1, k))
                  for I in combinations(range(n), k))
        counts.append(total)
    return counts


def direct_rook_count(n):
    counts = [1] + [0] * n
    for k in range(1, n + 1):
        for I in combinations(range(n), k):
            for P in permutations(range(n), k):
                ell = [-1] * n
                for p, i in zip(P, I):
                    ell[p] = i
                if combinatorial_pa(tuple(ell)):
                    counts[k] += 1
    return counts


def test():
    for n in range(1, 7):
        by_ell = {}
        for rows in product(range(n + 1), repeat=n):
            ell = last_occurrences(rows)
            direct = direct_semantic_pa(rows)
            assert direct == combinatorial_pa(ell), (n, rows, ell)
            tab = operation_table(rows)
            if ell in by_ell:
                old_tab, old_direct = by_ell[ell]
                assert tab == old_tab and direct == old_direct
            else:
                by_ell[ell] = tab, direct
        # Distinct signatures give distinct operations.
        assert len(set(tab for tab, _ in by_ell.values())) == len(by_ell)
        observed = sum(valid for _, valid in by_ell.values())
        predicted = sum(formula_by_support(n))
        assert observed == predicted, (n, observed, predicted)
        print(f"n={n}: {observed} distinct persistence-valid operations")
    for n in range(1, 9):
        by_formula = formula_by_support(n)
        by_rooks = direct_rook_count(n)
        assert by_formula == by_rooks, (n, by_formula, by_rooks)
        print(f"n={n}: rook sum {sum(by_rooks)}; supports {by_rooks}")
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
