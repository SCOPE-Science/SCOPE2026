#!/usr/bin/env python3
"""Direct small-size checks for majority dynamics on path fans and wheels.

Only the Python standard library is required. These finite checks corroborate,
but do not replace, the all-size mathematical proof.
"""
from math import comb
from collections import Counter


def fan_update(n, state):
    """n path vertices (least significant bits), one hub (bit n)."""
    rim = [(state >> j) & 1 for j in range(n)]
    hub = (state >> n) & 1
    ones = sum(rim)
    if 2 * ones > n:
        next_hub = 1
    elif 2 * ones < n:
        next_hub = 0
    else:
        next_hub = hub
    output = next_hub << n
    for j in range(n):
        neighbours = [hub]
        if j > 0:
            neighbours.append(rim[j - 1])
        if j < n - 1:
            neighbours.append(rim[j + 1])
        s = sum(neighbours)
        if 2 * s > len(neighbours):
            value = 1
        elif 2 * s < len(neighbours):
            value = 0
        else:
            value = rim[j]
        output |= value << j
    return output


def wheel_update(n, state):
    rim = [(state >> j) & 1 for j in range(n)]
    hub = (state >> n) & 1
    ones = sum(rim)
    if 2 * ones > n:
        next_hub = 1
    elif 2 * ones < n:
        next_hub = 0
    else:
        next_hub = hub
    result = next_hub << n
    for j in range(n):
        value = int(hub + rim[(j - 1) % n] + rim[(j + 1) % n] >= 2)
        result |= value << j
    return result


def coefficient_table(m):
    """(a,b)-># cyclic words with no isolated ones, b consecutive 11 pairs."""
    table = {(0, 0): 1, (m, m): 1}
    for a in range(1, m):
        for r in range(1, min(a // 2, m - a) + 1):
            numerator = m * comb(a - r - 1, r - 1) * comb(m - a - 1, r - 1)
            assert numerator % r == 0
            table[a, a - r] = table.get((a, a - r), 0) + numerator // r
    return table


def fan_formula(n):
    return sum(w for (a, b), w in coefficient_table(n).items() if 2 * a > n > 2 * b)


def wheel_formula(n):
    if n % 2:
        return fan_formula(n)
    t = coefficient_table(n // 2)
    return 2 + sum(v * w for (a, b), v in t.items()
                   for (c, d), w in t.items()
                   if 2 * (a + c) > n > 2 * (b + d))


def count_direct(n, updater):
    total = 1 << (n + 1)
    fixed = 0
    genuine = 0
    for x in range(total):
        y = updater(n, x)
        if x == y:
            fixed += 1
        elif updater(n, y) == x:
            genuine += 1
            if updater is fan_update:
                assert ((x >> n) & 1) != ((y >> n) & 1), (n, x, y)
    assert genuine % 2 == 0
    return fixed, genuine // 2


def auxiliary_cycle_check(n):
    # One edge for each path site: N_0={0,1}, N_{n-1}={n-2,n-1},
    # N_i={i-1,i+1} in the interior.
    neighbourhoods = [(0, 1)] + [(i-1, i+1) for i in range(1,n-1)] + [(n-2,n-1)]
    undirected_edges = {tuple(sorted(edge)) for edge in neighbourhoods}
    assert len(undirected_edges) == n
    for i in range(n):
        assert sum(i in edge for edge in undirected_edges) == 2
    # All vertices of this 2-regular graph lie in the same component.
    seen = {0}
    todo = [0]
    while todo:
        i = todo.pop()
        for u, v in undirected_edges:
            if i == u and v not in seen:
                seen.add(v); todo.append(v)
            if i == v and u not in seen:
                seen.add(u); todo.append(u)
    assert len(seen) == n
    if n <= 14:
        for x in range(1 << n):
            edge_values = [int(bool(x & (1 << u)) and bool(x & (1 << v))) for u,v in neighbourhoods]
            opening = 0
            for j in range(n):
                if any(edge_values[k] for k,edge in enumerate(neighbourhoods) if j in edge):
                    opening |= 1 << j
            no_isolated = all(not (x & (1 << j)) or
                              any(x & (1 << k) for edge in undirected_edges if j in edge for k in edge if k != j)
                              for j in range(n))
            assert (opening == x) == no_isolated, (n, x, opening)
    return len(undirected_edges)


def main():
    n_states = 0
    n_cases = 0
    wheel_cases = 0
    for n in range(3, 17):
        auxiliary_cycle_check(n)
        fixed, twos = count_direct(n, fan_update)
        assert fixed == 2, (n, fixed)
        assert twos == fan_formula(n), (n, twos, fan_formula(n))
        n_states += 1 << (n + 1)
        n_cases += 1
        if n <= 15:
            wfixed, wtwo = count_direct(n, wheel_update)
            assert wfixed == 2
            assert wtwo == wheel_formula(n), (n, wtwo, wheel_formula(n))
            if n % 2:
                assert twos == wtwo
            wheel_cases += 1
    assert fan_formula(4) == 0 and wheel_formula(4) == 2
    assert fan_formula(12) == 243 and wheel_formula(12) == 227
    assert [fan_formula(n) for n in range(3, 14)] == [3,0,5,3,21,16,66,65,220,243,715]
    for n in range(3, 61):
        coefficient_table(n)
        if n % 2:
            assert fan_formula(n) == wheel_formula(n)
    print('VERIFY_OK')
    print('fan_cases:', n_cases, 'fan_configs:', n_states)
    print('wheel_cases:', wheel_cases)
    print('fan_orbits_n3_to_n13:', [fan_formula(n) for n in range(3, 14)])
    print('odd_n_fan_wheel_agreement: n=3..59')
    print('even_n4: fan=0 wheel=2; even_n12: fan=243 wheel=227')
    print('auxiliary_cycle_opening_checks: n=3..14, exhaustive')

if __name__ == '__main__':
    main()
