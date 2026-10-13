#!/usr/bin/env python3
from collections import Counter
from math import comb, factorial


def adj_crown(n, u, v):
    if u == v:
        return False
    if u < n and v >= n:
        return (v - n) != u
    if v < n and u >= n:
        return (u - n) != v
    return False


def fair_literal(n, mask, complement=False):
    N = 2 * n
    if mask == (1 << N) - 1:
        return True
    counts = []
    for v in range(N):
        if (mask >> v) & 1:
            continue
        c = 0
        for u in range(N):
            if not ((mask >> u) & 1):
                continue
            e = adj_crown(n, u, v)
            if complement:
                e = (u != v) and (not e)
            if e:
                c += 1
        counts.append(c)
    return bool(counts) and counts[0] > 0 and all(c == counts[0] for c in counts)


def criterion(n, mask):
    full = (1 << n) - 1
    I = mask & full
    J = (mask >> n) & full
    if I == full or J == full:
        return True
    p = I.bit_count()
    q = J.bit_count()
    if I == J and I != 0:
        return True
    if (I | J) == full and p == q:
        return True
    return False


def formula_coeffs(n):
    c = Counter()
    # One whole bipartition class, with arbitrary selection on the other.
    for j in range(n + 1):
        c[n + j] += 2 * comb(n, j)
    c[2 * n] -= 1
    # Equal proper index sets I=J, excluding empty and full.
    for m in range(1, n):
        c[2 * m] += comb(n, m)
    # Proper equal-size pairs with I union J = [n].
    for m in range((n + 1) // 2, n):
        c[2 * m] += comb(n, m) * comb(m, n - m)
    return c


def central_trinomial(n):
    return sum(factorial(n) // (factorial(r) ** 2 * factorial(n - 2 * r))
               for r in range(n // 2 + 1))


def main():
    subset_checks = fair_sets = classification_checks = 0
    coefficient_checks = minimum_checks = complement_checks = 0
    for n in range(3, 10):
        N = 2 * n
        observed = Counter()
        for mask in range(1 << N):
            lit = fair_literal(n, mask)
            pred = criterion(n, mask)
            subset_checks += 1
            classification_checks += 1
            if lit != pred:
                raise AssertionError(("classification", n, mask, lit, pred))
            if lit:
                fair_sets += 1
                observed[mask.bit_count()] += 1
            if n <= 8:
                # Both the crown and its complement are connected.  The
                # foundational complement theorem therefore predicts the same
                # fair sets, not only the same minimum cardinality.
                comp = fair_literal(n, mask, complement=True)
                complement_checks += 1
                if lit != comp:
                    raise AssertionError(("complement", n, mask, lit, comp))
        expected = formula_coeffs(n)
        for k in range(0, N + 1):
            coefficient_checks += 1
            if observed[k] != expected[k]:
                raise AssertionError(("coefficient", n, k, observed[k], expected[k]))
        sizes = [k for k, v in observed.items() if v]
        minimum_checks += 2
        if min(sizes) != 2 or observed[2] != n:
            raise AssertionError(("minimum", n, min(sizes), observed[2]))
        expected_total = 3 * (2 ** n) + central_trinomial(n) - 4
        minimum_checks += 1
        if sum(observed.values()) != expected_total:
            raise AssertionError(("total", n, sum(observed.values()), expected_total))
    print(
        "VERIFY_OK "
        f"n_range=3..9 subset_checks={subset_checks} fair_sets={fair_sets} "
        f"classification_checks={classification_checks} coefficient_checks={coefficient_checks} "
        f"minimum_total_checks={minimum_checks} complement_checks={complement_checks} "
        "max_order=18"
    )


if __name__ == "__main__":
    main()
