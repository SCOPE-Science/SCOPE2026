#!/usr/bin/env python3
"""Exact polynomial transfer-matrix and direct zero-forcing checks for cycle squares."""
from collections import Counter
from math import comb

Q_EXPECTED = {(0, 0): 1, (1, 0): -1, (2, 1): -1,
              (3, 2): -1, (5, 3): -1, (7, 4): 1, (8, 5): 1}


def transition(s, new_bit):
    a, b, c, d = [(s >> j) & 1 for j in (3, 2, 1, 0)]
    if c and a + b + d + new_bit >= 3:
        return None
    return ((s << 1) & 15) | new_bit


def polynomial_trace(max_power):
    # Every path contributes a monomial: a DP counts paths by chosen-one count.
    totals = []
    for source in range(16):
        state_count = {(source, 0): 1}
        for power in range(1, max_power + 1):
            next_count = Counter()
            for (state, degree), multiplicity in state_count.items():
                for bit in (0, 1):
                    destination = transition(state, bit)
                    if destination is not None:
                        next_count[(destination, degree + bit)] += multiplicity
            state_count = next_count
            if source == 0:
                totals.append(Counter())
            for (state, degree), multiplicity in state_count.items():
                if state == source:
                    totals[power - 1][degree] += multiplicity
    return totals


def poly_add(p, q, factor=1):
    ans = Counter(p)
    for degree, count in q.items():
        ans[degree] += factor * count
    return {k: v for k, v in ans.items() if v}


def poly_times(p, q):
    result = Counter()
    for degree, count in p.items():
        for degree2, count2 in q.items():
            result[degree + degree2] += count * count2
    return {k: v for k, v in result.items() if v}


def determinant_polynomial(traces):
    # Newton identities: coefficients of det(I-uT), exact over Z[z].
    coeff = [{0: 1}]
    for j in range(1, len(traces) + 1):
        numerator = {}
        for i in range(1, j + 1):
            numerator = poly_add(numerator, poly_times(coeff[j-i], traces[i-1]), -1)
        assert all(v % j == 0 for v in numerator.values())
        coeff.append({k: v // j for k, v in numerator.items() if v})
    return {(i, j): v for i, ci in enumerate(coeff) for j, v in ci.items()}


def test_forcing(n, subset):
    black = set(subset)
    while True:
        forces = set()
        for v in black:
            white_neighbors = [w for d in (1, 2, -1, -2)
                               if (w := (v + d) % n) not in black]
            if len(white_neighbors) == 1:
                forces.add(white_neighbors[0])
        if not forces:
            break
        black |= forces
    return len(black) == n


def contains_large_degree(n, subset):
    black = set(subset)
    return any(sum(((v + d) % n in black) for d in (-2, -1, 1, 2)) >= 3
               for v in black)


def main():
    traces = polynomial_trace(16)
    actual_q = determinant_polynomial(traces)
    assert actual_q == Q_EXPECTED, (actual_q, Q_EXPECTED)
    check_subsets = 0
    for n in range(7, 15):
        counts = Counter()
        for mask in range(1 << n):
            subset = [i for i in range(n) if mask & (1 << i)]
            via_degree = contains_large_degree(n, subset)
            via_forcing = test_forcing(n, subset)
            assert via_degree == via_forcing, (n, mask)
            if not via_forcing:
                counts[len(subset)] += 1
            check_subsets += 1
        assert counts == traces[n-1], (n, counts, traces[n-1])
        assert counts.get(4, 0) == comb(n, 4) - 3*n, (n, counts)
        assert max(counts) == 2*n//3, (n, counts)
        assert sum(counts.values()) + sum(comb(n,k)-counts[k] for k in range(n+1)) == 2**n
    print('VERIFY_OK transfer_states=16 determinant_degree_u=8 traced_powers=16'
          f' cycle_orders=7..14 exhaustive_subsets={check_subsets}'
          ' coefficient_and_forcing_checks=passed')


if __name__ == '__main__':
    main()
