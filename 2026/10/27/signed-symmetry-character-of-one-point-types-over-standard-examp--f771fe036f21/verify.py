#!/usr/bin/env python3
"""Direct finite checks for the standard-example one-type symmetry formula.

Uses only the strict order on the original 2n points; does not implement the
symbolic one-sided/mixed classification used in the proof.
"""
from itertools import permutations
from math import factorial


def strict_order(n):
    # a_i is i, b_j is n+j.
    return {(i, n + j) for i in range(n) for j in range(n) if i != j}


def admissible_types(n):
    rel = strict_order(n)
    size = 2 * n
    down = []
    up = []
    for subset in range(1 << size):
        if all(not (subset >> y & 1) or (subset >> x & 1)
               for x, y in rel):
            down.append(subset)
        if all(not (subset >> x & 1) or (subset >> y & 1)
               for x, y in rel):
            up.append(subset)
    result = []
    for l in down:
        for u in up:
            if l & u:
                continue
            if all((x, y) in rel for x in range(size) for y in range(size)
                   if (l >> x & 1) and (u >> y & 1)):
                result.append((l, u))
    return result


def act_mask(mask, perm, n):
    out = 0
    for i, j in enumerate(perm):
        if mask >> i & 1:
            out |= 1 << j
        if mask >> (n + i) & 1:
            out |= 1 << (n + j)
    return out


def dual_mask(mask, n):
    low = mask & ((1 << n) - 1)
    high = mask >> n
    return (low << n) | high


def twisted_image(l, u, perm, n):
    # First reverse the order by exchanging a_i with b_i,
    # then permute the index labels.
    return act_mask(dual_mask(u, n), perm, n), act_mask(dual_mask(l, n), perm, n)


def stats(perm):
    n = len(perm)
    seen = set()
    cycles = 0
    for i in range(n):
        if i not in seen:
            cycles += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = perm[j]
    fixed = sum(perm[i] == i for i in range(n))
    seen = set()
    even_cycles = 0
    for i in range(n):
        if i not in seen:
            k, j = 0, i
            while j not in seen:
                seen.add(j)
                k += 1
                j = perm[j]
            even_cycles += (k % 2 == 0)
    return cycles, fixed, even_cycles


def expected(n):
    return 3 ** n + 2 ** (n + 1) + 2 * n - 2


def check():
    configurations = 0
    permutation_checks = 0
    direct_orbit_checks = 0
    twisted_checks = 0
    for n in range(2, 7):
        types = admissible_types(n)
        assert len(types) == expected(n), (n, len(types), expected(n))
        configurations += 1
        check_set = set(types)
        burnside_total = 0
        orbit_rep = set()
        twisted_total = 0
        for perm in permutations(range(n)):
            c, f, ev = stats(perm)
            expected_fixed = 3 ** c + 2 ** (c + 1) + 2 * f - 2
            fixed = sum(act_mask(l, perm, n) == l and act_mask(u, perm, n) == u
                        for l, u in types)
            assert fixed == expected_fixed, (n, perm, fixed, expected_fixed)
            burnside_total += fixed
            permutation_checks += 1
            twisted_fixed = sum(twisted_image(l, u, perm, n) == (l, u)
                                for l, u in types)
            assert twisted_fixed == 3 ** ev, (n, perm, twisted_fixed, 3 ** ev)
            twisted_total += twisted_fixed
            twisted_checks += 1
            # This also independently checks that the action preserves valid types.
            if n <= 4:
                assert all((act_mask(l, perm, n), act_mask(u, perm, n)) in check_set
                           for l, u in types)
        expected_orbits = (n + 1) * (n + 6) // 2
        assert burnside_total == factorial(n) * expected_orbits
        expected_signed_orbits = 2 * n + 2 + n * n // 4
        assert burnside_total + twisted_total == 2 * factorial(n) * expected_signed_orbits
        if n <= 4:
            unseen = set(types)
            while unseen:
                l, u = next(iter(unseen))
                orbit = {(act_mask(l, p, n), act_mask(u, p, n))
                         for p in permutations(range(n))}
                assert orbit <= check_set
                unseen -= orbit
                orbit_rep.add((l, u))
            assert len(orbit_rep) == expected_orbits
            direct_orbit_checks += 1
            signed_unseen = set(types)
            direct_signed = 0
            while signed_unseen:
                l, u = next(iter(signed_unseen))
                signed_orbit = set()
                for p in permutations(range(n)):
                    signed_orbit.add((act_mask(l, p, n), act_mask(u, p, n)))
                    signed_orbit.add(twisted_image(l, u, p, n))
                assert signed_orbit <= check_set
                signed_unseen -= signed_orbit
                direct_signed += 1
            assert direct_signed == expected_signed_orbits
        print(f'n={n} types={len(types)} order_orbits={expected_orbits} duality_orbits={expected_signed_orbits} permutations={factorial(n)}')
    print(f'finite_configs={configurations} untwisted_checks={permutation_checks} twisted_checks={twisted_checks} direct_orbit_checks={direct_orbit_checks}')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    check()
