#!/usr/bin/env python3
"""Exact, finite support certificate and labelled-state cross-check for four-color CCA on K_{a,b}."""
from collections import Counter
from itertools import product
from math import comb

K = 4
NONEMPTY = tuple(range(1, 1 << K))
EXPECTED = {
    (1, 1, 1): 8,
    (1, 1, 2): 4,
    (1, 2, 1): 4,
    (1, 2, 2): 2,
    (4, 2, 2): 2,
    (4, 4, 4): 1,
    (6, 3, 3): 4,
}


def colors(mask):
    return tuple(c for c in range(K) if mask & (1 << c))


def advance(color, opposite_mask):
    nxt = (color + 1) % K
    return nxt if (opposite_mask >> nxt) & 1 else color


def mask_step(pair):
    a, b = pair
    new_a = new_b = 0
    for c in colors(a):
        new_a |= (1 << advance(c, b))
    for c in colors(b):
        new_b |= (1 << advance(c, a))
    return new_a, new_b


def cycle_data(cycle):
    """Return actual configuration period, or None if color maps merge."""
    a, b = cycle[0]
    wa, wb = {x: x for x in colors(a)}, {x: x for x in colors(b)}
    pair = (a, b)
    for state in cycle:
        assert pair == state
        s, t = pair
        wa = {x: advance(y, t) for x, y in wa.items()}
        wb = {x: advance(y, s) for x, y in wb.items()}
        pair = mask_step(pair)
    assert pair == (a, b)
    if len(set(wa.values())) < len(wa) or len(set(wb.values())) < len(wb):
        return None
    assert set(wa.values()) == set(wa) and set(wb.values()) == set(wb)
    p = len(cycle)
    ua, ub = wa.copy(), wb.copy()
    while any(ua[c] != c for c in ua) or any(ub[c] != c for c in ub):
        p += len(cycle)
        ua = {c: wa[v] for c, v in ua.items()}
        ub = {c: wb[v] for c, v in ub.items()}
    return p


def support_census():
    states = {(s, t) for s in NONEMPTY for t in NONEMPTY}
    assert len(states) == 225
    table = Counter()
    cycles = []
    unseen = set(states)
    while unseen:
        first = next(iter(unseen))
        trajectory = []
        indices = {}
        current = first
        while current not in indices and current in unseen:
            indices[current] = len(trajectory)
            trajectory.append(current)
            current = mask_step(current)
        for state in trajectory:
            unseen.discard(state)
        if current in indices:
            cycle = trajectory[indices[current]:]
            cycles.append(cycle)
            period = cycle_data(cycle)
            assert period is not None
            for a, b in cycle:
                table[period, len(colors(a)), len(colors(b))] += 1
    assert table == EXPECTED, (table, EXPECTED)
    assert sum(map(len, cycles)) == 25
    return table, cycles


def surj(n, r):
    return sum((-1)**j * comb(r, j) * (r-j)**n for j in range(r+1))


def predicted(a, b):
    s2a, s2b = surj(a,2), surj(b,2)
    return {
        1: 8 + 4*s2a + 4*s2b + 2*s2a*s2b,
        4: 2*s2a*s2b + surj(a,4)*surj(b,4),
        6: 4*surj(a,3)*surj(b,3),
    }


def state_step(state, a):
    left = set(state[:a]); right = set(state[a:])
    return tuple(advance(c, sum(1<<x for x in (right if i < a else left))) for i,c in enumerate(state))


def brute_census(a,b):
    allstates = list(product(range(K), repeat=a+b))
    # Exhaustive finite-state digraph, with memoization of known destinations.
    period_by_state = {}
    recurrent = Counter()
    for start in allstates:
        if start in period_by_state:
            continue
        path = []
        local = {}
        x = start
        while x not in local and x not in period_by_state:
            local[x] = len(path)
            path.append(x)
            x = state_step(x, a)
        if x in local:
            prefix_end = local[x]
            period = len(path) - prefix_end
            for state in path[prefix_end:]:
                period_by_state[state] = period
                recurrent[period] += 1
        else:
            period = period_by_state[x]
        for state in path:
            period_by_state[state] = period
    assert len(period_by_state)==len(allstates)
    return dict(recurrent)


def run():
    table, cycles = support_census()
    print('SUPPORT_CERTIFICATE_OK states=225 recurrent_support_states=25 recurrent_support_cycles=22')
    print('COEFFICIENTS',sorted(table.items()))
    tested = 0
    configurations = 0
    for a in range(1,5):
        for b in range(1,5):
            if a+b>8: continue
            p = {k:v for k,v in predicted(a,b).items() if v}
            q = brute_census(a,b)
            assert q == p, (a,b,p,q)
            tested += 1
            configurations += 4**(a+b)
    print(f'LABELLED_BRUTE_OK profiles={tested} configurations={configurations}')
    print('FOUR_COLOR_BICLIQUE_VERIFY_OK')

if __name__ == '__main__':
    run()
