#!/usr/bin/env python3
"""Self-contained all-support proof checker for 3-state excitable dynamics on two matched cliques.
Every occupied pair type has one of nine values; the set of types determines update.
This is an exhaustive nine-type symbolic computation, not a fixed-size graph sample.
"""
from collections import Counter, defaultdict
from math import comb

TYPES = tuple((a,b) for a in range(3) for b in range(3))


def tick(values):
    left = any(a == 1 for a,b in values)
    right = any(b == 1 for a,b in values)
    return tuple((2 if a == 1 else 0 if a == 2 else int(left or b == 1),
                  2 if b == 1 else 0 if b == 2 else int(right or a == 1))
                 for a,b in values)


def surjections(n, j):
    return sum((-1)**(j-k)*comb(j,k)*k**n for k in range(j+1))


def formulas(n):
    return (3*4**n+6*3**n-12*2**n+3,
            9**n-9*4**n+18*2**n-9,
            6*(4**n-3**n-2**n+1))


row = defaultdict(Counter)
periodic_supports = defaultdict(list)
max_entry = 0
for mask in range(1, 1<<9):
    v = tuple(TYPES[k] for k in range(9) if mask & (1<<k))
    orbit = [v]
    for _ in range(16):
        orbit.append(tick(orbit[-1]))
    assert orbit[4] == orbit[16], (mask, orbit)
    period = next((p for p in (1,3,4) if orbit[4] == orbit[4+p]), None)
    assert period is not None
    row[len(v)][period] += 1
    entry = next(t for t in range(5) if orbit[t] == orbit[t+period])
    max_entry = max(max_entry, entry)
    if orbit[0] == orbit[period]:
        periodic_supports[period].append(v)
        if period == 3:
            assert orbit[1] == tuple(((a+1)%3,(b+1)%3) for a,b in v)
assert max_entry == 4

expected_rows = ((9,0,0), (24,0,12), (18,48,18), (3,117,6),
                 (0,126,0), (0,84,0), (0,36,0), (0,9,0), (0,1,0))
assert tuple(tuple(row[j][p] for p in (1,3,4)) for j in range(1,10)) == expected_rows
assert [len(periodic_supports[p]) for p in (1,3,4)] == [1,277,4]
expected_four = {
    frozenset(((0,1),(0,2))),
    frozenset(((1,0),(2,0))),
    frozenset(((0,0),(1,2))),
    frozenset(((0,0),(2,1)))
}
assert {frozenset(v) for v in periodic_supports[4]} == expected_four
assert periodic_supports[1] == [((0,0),)]
for n in range(2,13):
    actual = tuple(sum(row[j][p]*surjections(n,j) for j in range(1,10)) for p in (1,3,4))
    assert actual == formulas(n), (n, actual, formulas(n))
    assert sum(actual) == 9**n
    # Count periodic configurations with period 3 from the explicit three-colour criterion.
    sur = 3**n - 3*2**n + 3
    three_states = sur**2 + 6*(4**n - 3*3**n + 3*2**n - 1)
    assert three_states % 3 == 0
    by_periodic_support = sum(surjections(n, len(v)) for v in periodic_supports[3])
    assert by_periodic_support == three_states
    assert 1 + 4*(2**n-2) + three_states <= 9**n
    if n in (2,3,4,5,6):
        print('n=%d basins=(%d,%d,%d) orbits=(fixed 1, three %d, four %d)' %
              (n, *actual, three_states//3, 2**n-2))
print('511 symbolic supports checked, F^16=F^4, sharp first-entry 4')
for j in range(1,10):
    print('support size %d: fixed=%d period3=%d period4=%d' %
          (j,row[j][1],row[j][3],row[j][4]))
print('periodic support classes', {p:len(periodic_supports[p]) for p in (1,3,4)})
print('ALL SYMBOLIC ASSERTIONS PASS')
